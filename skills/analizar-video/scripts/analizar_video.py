#!/usr/bin/env python3
"""Prepara un video para que Claude lo analice: metadatos, fotogramas y transcripción.

Uso:
    python analizar_video.py VIDEO [--salida CARPETA] [--max-fotogramas 24]
                             [--modelo small] [--idioma es] [--modelo-ggml RUTA]

Requiere ffmpeg y ffprobe en el PATH. La transcripción usa, en este orden:
faster-whisper, openai-whisper o el filtro `whisper` de ffmpeg 8+ (con --modelo-ggml).
Si ninguno está disponible, se omite y se indica cómo instalarlo.
"""
import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path


def run(cmd, **kw):
    return subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", **kw)


def tiempo(seg, srt=False):
    h, rem = divmod(seg, 3600)
    m, s = divmod(rem, 60)
    if srt:
        return f"{int(h):02d}:{int(m):02d}:{int(s):02d},{int(round((s % 1) * 1000)) % 1000:03d}"
    return f"{int(h)}:{int(m):02d}:{int(s):02d}" if h else f"{int(m):02d}:{int(s):02d}"


def leer_metadatos(video):
    r = run(["ffprobe", "-v", "error", "-print_format", "json", "-show_format", "-show_streams", str(video)])
    if r.returncode:
        sys.exit(f"ffprobe no pudo leer el video: {r.stderr.strip()}")
    datos = json.loads(r.stdout)
    v = next((s for s in datos["streams"] if s["codec_type"] == "video"), None)
    if not v:
        sys.exit("El archivo no tiene pista de video.")
    ancho, alto = v["width"], v["height"]
    # Los videos de celular guardan la rotación aparte; ffmpeg la aplica al extraer.
    rot = int(v.get("tags", {}).get("rotate", 0))
    for sd in v.get("side_data_list", []):
        rot = int(sd.get("rotation", rot))
    if abs(rot) % 180 == 90:
        ancho, alto = alto, ancho
    num, _, den = v.get("avg_frame_rate", "0/1").partition("/")
    fps = round(float(num) / float(den), 2) if float(den or 0) else None
    return {
        "duracion_seg": round(float(datos["format"].get("duration", 0)), 2),
        "resolucion": f"{ancho}x{alto}",
        "orientacion": "vertical" if alto > ancho else "horizontal" if ancho > alto else "cuadrado",
        "fps": fps,
        "tiene_audio": any(s["codec_type"] == "audio" for s in datos["streams"]),
    }


def extraer_fotogramas(video, duracion, carpeta, maximo):
    carpeta.mkdir(parents=True, exist_ok=True)
    n = max(6, min(maximo, round(duracion / 3)))
    # El lado largo queda en 768 px: suficiente para leer texto y caras sin gastar de más.
    escala = "scale='if(gt(iw,ih),768,-2)':'if(gt(iw,ih),-2,768)'"
    fotogramas = []
    for i in range(n):
        seg = duracion * (i + 0.5) / n
        nombre = f"f{i + 1:02d}_{tiempo(seg).replace(':', '-')}.jpg"
        r = run(["ffmpeg", "-v", "error", "-y", "-ss", f"{seg:.2f}", "-i", str(video),
                 "-frames:v", "1", "-vf", escala, "-q:v", "3", str(carpeta / nombre)])
        if r.returncode == 0 and (carpeta / nombre).exists():
            fotogramas.append({"archivo": f"fotogramas/{nombre}", "segundo": round(seg, 2), "tiempo": tiempo(seg)})
    return fotogramas


def escribir_transcripcion(segmentos, carpeta):
    with open(carpeta / "transcripcion.srt", "w", encoding="utf-8") as srt, \
         open(carpeta / "transcripcion.txt", "w", encoding="utf-8") as txt:
        for i, (ini, fin, texto) in enumerate(segmentos, 1):
            texto = texto.strip()
            srt.write(f"{i}\n{tiempo(ini, True)} --> {tiempo(fin, True)}\n{texto}\n\n")
            txt.write(f"[{tiempo(ini)}] {texto}\n")


def audio_16k(video):
    # Decodificamos con ffmpeg en vez de dejar que Whisper use PyAV: evita choques de versiones.
    import numpy as np
    r = subprocess.run(["ffmpeg", "-v", "error", "-i", str(video), "-vn", "-ac", "1", "-ar", "16000",
                        "-f", "f32le", "-"], capture_output=True)
    if r.returncode:
        raise RuntimeError(r.stderr.decode("utf-8", "replace").strip())
    return np.frombuffer(r.stdout, np.float32)


def instalado(modulo):
    import importlib.util
    return importlib.util.find_spec(modulo) is not None


def transcribir(video, carpeta, modelo, idioma, modelo_ggml):
    if instalado("faster_whisper"):
        from faster_whisper import WhisperModel
        audio = audio_16k(video)
        try:
            m = WhisperModel(modelo, device="auto", compute_type="int8")
            segs, info = m.transcribe(audio, language=idioma)
            segs = list(segs)
        except RuntimeError:
            # GPU NVIDIA sin las librerías CUDA instaladas: usamos el procesador.
            m = WhisperModel(modelo, device="cpu", compute_type="int8")
            segs, info = m.transcribe(audio, language=idioma)
            segs = list(segs)
        escribir_transcripcion([(s.start, s.end, s.text) for s in segs], carpeta)
        return {"motor": "faster-whisper", "idioma": info.language}

    if instalado("whisper"):
        import whisper
        res = whisper.load_model(modelo).transcribe(audio_16k(video), language=idioma)
        escribir_transcripcion([(s["start"], s["end"], s["text"]) for s in res["segments"]], carpeta)
        return {"motor": "openai-whisper", "idioma": res.get("language")}

    modelo_ggml = modelo_ggml or os.environ.get("WHISPER_GGML_MODEL")
    if modelo_ggml and Path(modelo_ggml).is_file():
        # En los filtros de ffmpeg ':' separa opciones; hay que escaparlo en rutas de Windows.
        ruta = Path(modelo_ggml).resolve().as_posix().replace(":", r"\:")
        filtro = f"whisper=model='{ruta}':language={idioma or 'auto'}:queue=10:destination=transcripcion.srt:format=srt"
        r = run(["ffmpeg", "-v", "error", "-y", "-i", str(Path(video).resolve()), "-vn", "-af", filtro, "-f", "null", "-"],
                cwd=carpeta)
        srt = carpeta / "transcripcion.srt"
        if r.returncode == 0 and srt.exists():
            bloques = re.findall(r"(\d\d:\d\d:\d\d[,.]\d+) --> (\d\d:\d\d:\d\d[,.]\d+)\s*\n(.+?)(?:\n\n|\Z)",
                                 srt.read_text(encoding="utf-8"), re.S)
            a_seg = lambda t: sum(float(x) * f for x, f in zip(t.replace(",", ".").split(":"), (3600, 60, 1)))
            escribir_transcripcion([(a_seg(a), a_seg(b), t.replace("\n", " ")) for a, b, t in bloques], carpeta)
            return {"motor": "ffmpeg-whisper", "idioma": idioma or "auto"}
        return {"error": f"El filtro whisper de ffmpeg falló: {r.stderr.strip()[-300:]}"}

    return {"error": "No hay motor de transcripción. Instala uno: `pip install faster-whisper` "
                     "(recomendado) o `pip install openai-whisper`, o pasa --modelo-ggml con un modelo de whisper.cpp."}


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("video")
    p.add_argument("--salida", help="carpeta de salida (por defecto ./analisis-<nombre del video>)")
    p.add_argument("--max-fotogramas", type=int, default=24)
    p.add_argument("--modelo", default="small", help="tamaño del modelo Whisper: tiny, base, small, medium, large-v3")
    p.add_argument("--idioma", help="código de idioma (es, en, pt…). Por defecto se detecta solo")
    p.add_argument("--modelo-ggml", help="ruta a un modelo ggml de whisper.cpp para el filtro de ffmpeg")
    p.add_argument("--sin-transcripcion", action="store_true")
    a = p.parse_args()

    video = Path(a.video)
    if not video.is_file():
        sys.exit(f"No existe el archivo: {video}")
    carpeta = Path(a.salida or f"analisis-{video.stem}")
    carpeta.mkdir(parents=True, exist_ok=True)

    info = {"archivo": str(video.resolve()), **leer_metadatos(video)}
    info["fotogramas"] = extraer_fotogramas(video, info["duracion_seg"], carpeta / "fotogramas", a.max_fotogramas)

    if a.sin_transcripcion:
        info["transcripcion"] = {"error": "Omitida con --sin-transcripcion"}
    elif not info["tiene_audio"]:
        info["transcripcion"] = {"error": "El video no tiene audio"}
    else:
        try:
            info["transcripcion"] = transcribir(video, carpeta, a.modelo, a.idioma, a.modelo_ggml)
        except Exception as e:  # sin internet para bajar el modelo, memoria, etc.: los fotogramas siguen sirviendo
            info["transcripcion"] = {"error": f"La transcripción falló: {type(e).__name__}: {e}"}
        if "error" not in info["transcripcion"]:
            info["transcripcion"]["archivos"] = ["transcripcion.txt", "transcripcion.srt"]

    (carpeta / "info.json").write_text(json.dumps(info, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"carpeta": str(carpeta.resolve()), **info}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
