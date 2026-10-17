---
name: analizar-video
description: Analiza un archivo de video (short, reel, tiktok o video largo) para saber qué se ve, qué se dice, de qué trata, cuál es el mejor momento para el hook y la portada, qué capítulos tiene y qué problemas o faltantes hay antes de publicarlo. Extrae fotogramas y transcripción en local con ffmpeg y Whisper. Úsala cuando alguien comparta la ruta de un video y pida revisarlo, resumirlo o prepararlo para publicar, o como paso de análisis dentro de la skill publicar.
---

# Analizar un video

No puedes ver un video directamente. Este script lo convierte en lo que sí puedes revisar: **fotogramas** (imágenes con su segundo exacto) y **transcripción** con tiempos. Todo se procesa en el computador del usuario.

## 1. Ejecutar el script

Desde la carpeta de esta skill:

```bash
python scripts/analizar_video.py "RUTA/AL/VIDEO.mp4" --salida "analisis-<nombre>"
```

Opciones útiles:
- `--idioma es` si sabes el idioma (más rápido y preciso que la detección automática).
- `--modelo base` en equipos lentos; `--modelo medium` si el audio es difícil.
- `--max-fotogramas 40` para videos largos.
- `--sin-transcripcion` si solo necesitas lo visual.

Si falla:
- **ffmpeg no encontrado** → pide instalarlo (https://ffmpeg.org/download.html) o trabaja con el resumen del usuario.
- **Sin motor de transcripción** → el script lo dice en `info.json`. Sigue con los fotogramas y pide al usuario un resumen de lo que se dice, o sugiere `pip install faster-whisper`.
- **Transcribir tarda** (la primera vez descarga el modelo) → ejecútalo en segundo plano si tu entorno lo permite.

## 2. Revisar la salida

- `info.json`: duración, resolución, orientación, audio, lista de fotogramas y estado de la transcripción.
- `fotogramas/*.jpg`: **míralos todos**, en orden. El nombre lleva el tiempo (`f03_00-12.jpg` = segundo 12).
- `transcripcion.txt`: lo que se dice, con tiempos. `transcripcion.srt`: listo para subir como subtítulos.

Si un tramo importante queda sin fotograma (un cambio brusco entre dos), extrae uno extra:

```bash
ffmpeg -v error -ss 00:00:15 -i "VIDEO.mp4" -frames:v 1 extra_00-15.jpg
```

## 3. Reporte

Entrega este reporte, corto y concreto:

```markdown
## Análisis del video

**Ficha técnica:** 0:42 · vertical 1080x1920 · 60 fps · con audio · idioma: español

**De qué trata:** <2-3 líneas>

**Qué se ve, por tramos**
- 00:00-00:05: …
- 00:05-00:18: …

**Qué se dice:** <resumen; citas textuales cortas de las frases clave>

**Tema / juego detectado:** <nombre> (seguro / probable / no identificado; por qué)

**Mejor momento para el hook:** <segundo y por qué>. ¿El video arranca con él? Si no, sugiere recortar.

**Fotograma recomendado para portada:** <archivo y segundo>

**Capítulos sugeridos** (solo videos largos, mínimo 3, cada uno ≥10 s):
00:00 …

**Palabras clave detectadas:** <dichas o vistas en pantalla>

**Alertas**
- Música comercial o audio de terceros → riesgo de Content ID o silenciado
- Marcas o productos visibles → ¿patrocinio?
- Contenido sensible (violencia gráfica, lenguaje fuerte) → restricción de edad
- Personas o escenas que parezcan alteradas con IA → etiqueta de IA
- Texto o elementos importantes en zonas que tapa la interfaz (vertical: arriba, abajo, lado derecho)
- Subtítulos ya quemados en el video → no activar subtítulos automáticos que se superpongan (Facebook)
- Rótulos o textos en pantalla que prometen algo que el video no cumple
- Cortes, pantallas negras o pérdida de captura
- Calidad: audio bajo o saturado, imagen borrosa, inicio lento

**Lo que no queda claro para el espectador:** <contexto que falta; qué explicar en el copy>

**Recomendaciones:** <2-4 acciones concretas>
```

## Reglas

- Describe lo que **ves y oyes**, no lo que supones. Si algo es incierto, dilo ("parece ser…").
- Si el usuario dio un resumen, compáralo con lo que encontraste. Si se contradicen, pregunta.
- Whisper escribe mal nombres propios (clases, personajes, jerga). Corrígelos con lo que se ve en pantalla y no los copies mal al copy.
- Identificar el juego: fíjate en la interfaz (HUD), menús, logos y nombres en pantalla. Si no estás seguro, pregunta.
- No identifiques a personas reales por su cara. Usa solo nombres que aparezcan en pantalla, en el audio o que dé el usuario.
- La carpeta de análisis queda en el equipo del usuario. Al terminar, dile dónde está y que puede borrarla.
