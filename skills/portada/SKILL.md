---
name: portada
description: Crea prompts detallados para generar la portada o miniatura de un video (YouTube 16:9, Shorts, TikTok, Reels 9:16) con cualquier generador de imágenes - ChatGPT, Gemini, Midjourney, Firefly, Ideogram u otros - con hook de texto, composición, colores y zonas seguras. Úsala cuando pidan portada, miniatura, thumbnail o cover de un video, o como paso de portada dentro de la skill publicar.
---

# Portada de video

Una portada tiene un solo trabajo: que alguien que hace scroll rápido entienda **qué pasa** y sienta **ganas de verlo** en menos de un segundo, en tamaño pequeño.

## 1. Lo que necesitas saber

- De qué trata el video y cuál es su momento más fuerte (sale del análisis o del resumen).
- **Orientaciones**: 16:9 (YouTube largo) y/o 9:16 (Shorts, TikTok, Reels).
- **Texto del hook** para la portada (no es el título; lo complementa).
- Si aparece la cara del creador y qué emoción transmite.
- Juego o tema y su estética. Colores de marca si tiene.
- Generador que va a usar, si lo sabe.

Si falta lo esencial (tema u orientación), pregunta. Lo demás, propónlo tú.

## 2. Reglas de una buena portada

- **Un solo foco**: una cara, un personaje o un objeto protagonista. Si hay de todo, no se ve nada.
- **Emoción clara**: sorpresa, risa, tensión, triunfo. Una cara expresiva casi siempre gana.
- **Texto de 2 a 4 palabras**, grande y grueso. Que no repita el título: que lo complete. Título "Gané con 1 HP" → portada "NO PUEDE SER".
- **Contraste alto**: sujeto claro sobre fondo oscuro o al revés, con borde o sombra para separarlo.
- **2-3 colores dominantes**, saturados. Amarillo, rojo y cian destacan en el feed.
- **Legible pequeña**: imagínala del tamaño de una estampilla. Si no se entiende, simplifica.
- **Honesta**: lo que muestra la portada tiene que pasar en el video.

## 3. Medidas y zonas seguras

| Uso | Tamaño | Zona a evitar |
|---|---|---|
| YouTube largo | 1280×720 (16:9) | Esquina inferior derecha: ahí va la duración |
| Shorts, TikTok, Reels | 1080×1920 (9:16) | ~15% superior, ~25% inferior y ~15% del lado derecho: los tapan la interfaz y los botones |
| Cuadrícula de perfil Instagram | recorte central vertical | Deja lo importante en el centro; los bordes de arriba y abajo se cortan |

En 9:16 pon el texto en el **tercio central**. En 16:9, el texto a la izquierda o arriba y el sujeto al otro lado.

## 4. Texto: dentro o fuera de la imagen

Los generadores a veces escriben mal el texto. Ofrece siempre dos caminos:

- **A. Con texto en el prompt**: rápido. Va entre comillas y en mayúsculas. Revisa la ortografía en el resultado.
- **B. Sin texto (recomendado)**: genera la imagen con espacio libre y pon el texto después en Canva, Photoshop, CapCut o Express. Más control y cero errores.

## 5. Plantilla del prompt

Entrega un prompt por orientación, en inglés (los generadores rinden mejor) y con una línea en el idioma del usuario que explique qué pide.

```
[FORMATO] Vertical 9:16 video cover, 1080x1920 / Horizontal 16:9 YouTube thumbnail, 1280x720.
[SUJETO] <quién o qué, pose, expresión exagerada y concreta>
[ACCIÓN / MOMENTO] <lo que está pasando, el instante más fuerte del video>
[ESCENARIO] <fondo, simplificado, desenfocado o con profundidad>
[ESTILO] <hiperrealista, 3D render, estilo del juego, cómic…>, high contrast, vibrant saturated colors, dramatic rim light
[COLORES] <2-3 colores dominantes>
[COMPOSICIÓN] subject on the <left/right/center>, clean empty space <top/left> for text, keep the <bottom 25% and right 15%> free of important elements
[TEXTO] bold title text "NO PUEDE SER" in thick white sans-serif with black outline   ← solo en el camino A
[EVITAR] clutter, small details, extra text, watermarks, logos, blurry face
```

Adaptaciones por generador:
- **Midjourney**: todo en una línea y al final `--ar 16:9` o `--ar 9:16` y `--style raw` si lo quieres más realista.
- **ChatGPT / GPT Image, Gemini, Firefly, Ideogram**: frases completas; pide el tamaño explícito. Si el creador sube una foto suya, dile al generador que la use como referencia de la cara.

## 6. Juegos y marcas

- Describe el **estilo visual** del juego ("dark fantasy armor, Souls-like atmosphere") en vez de pedir una copia exacta de arte oficial o logos: los generadores suelen rechazarlo y puede traer problemas de derechos.
- Mejor opción para gaming: usar un **fotograma real del video** (la skill `analizar-video` sugiere el mejor) como fondo o referencia y agregarle cara, texto y efectos encima.

## 7. Entrega

Por cada orientación:
1. Concepto en una línea (qué se ve y por qué funciona).
2. Texto de la portada (2-3 opciones).
3. Prompt camino A y prompt camino B.
4. Si hay análisis del video: el fotograma recomendado como base, con su segundo exacto.
