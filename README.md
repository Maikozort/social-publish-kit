# Social Publish Kit

Plugin de skills para Claude que prepara la publicación de un video en **YouTube (largo y Shorts), TikTok, Instagram Reels y Facebook Reels**.

Le das tu video (o le cuentas de qué trata) y te devuelve una **ficha de publicación**: cada campo del formulario de la plataforma, en su orden, listo para copiar y pegar. Incluye título, descripción con SEO, CTAs, hashtags, tus redes, las respuestas correctas a los campos legales (para niños, promoción pagada, etiqueta de IA) y el prompt para generar la portada en vertical y horizontal.

*English summary below.*

## Skills incluidas

| Skill | Qué hace | Úsala sola cuando… |
|---|---|---|
| `publicar` | Flujo completo: entrevista, análisis, copy, fichas y portada | Vas a subir un video |
| `analizar-video` | Saca fotogramas y transcripción del video y reporta qué tiene, qué falta y qué recomienda | Quieres una revisión del video antes de subirlo |
| `copy` | Títulos, descripciones, hooks, CTAs, hashtags y comentario fijado | Solo necesitas los textos |
| `portada` | Prompts de portada 16:9 y 9:16 para cualquier generador de imágenes | Solo necesitas la miniatura |
| `ficha-youtube` | Todos los campos de YouTube y Shorts | Ya tienes el copy y quieres llenar YouTube |
| `ficha-tiktok` | Todos los campos de TikTok | Ídem para TikTok |
| `ficha-instagram` | Todos los campos de Instagram Reels | Ídem para Instagram |
| `ficha-facebook` | Todos los campos de Facebook Reels | Ídem para Facebook |

## Instalación

### Claude Code

```bash
/plugin marketplace add Maikozort/social-publish-kit
/plugin install social-publish-kit@social-publish-kit
```

Para probarlo en local sin GitHub:

```bash
claude --plugin-dir ./social-publish-kit
```

### Claude.ai (web o app)

Comprime en un `.zip` la carpeta de cada skill que quieras (por ejemplo `skills/publicar`) y súbela en **Configuración → Capacidades → Skills**.

## Requisitos para analizar videos (opcional)

Sin esto la skill funciona igual: te pide un resumen del video en lugar de analizarlo.

- **ffmpeg** (fotogramas y metadatos): https://ffmpeg.org/download.html
- **Python 3.9+**
- **Transcripción** (una de estas):
  - `pip install faster-whisper` (recomendado)
  - `pip install openai-whisper`
  - ffmpeg 8 o superior trae el filtro `whisper`; solo hay que descargar un modelo `ggml` de whisper.cpp y pasarlo con `--modelo-ggml`.

Todo corre en tu computador. El video no se sube a ningún servidor.

## Uso

Dile a Claude algo como:

> Voy a subir este short a YouTube y TikTok: `C:\videos\clip-final.mp4`. Es una jugada de Valorant.

La skill te pide los datos que falten (tus redes, idiomas, si hay patrocinio…), analiza el video y te entrega un archivo `ficha-<video>-<fecha>.md` con todo.

**Tip:** crea un archivo `creador.md` en tu carpeta de trabajo con tus datos (usa [la plantilla](skills/publicar/creador-plantilla.md)) y la skill no te los volverá a preguntar.

## Las plataformas cambian

Cada skill de plataforma indica la fecha en que se verificaron sus campos. Si ves un campo nuevo, renombrado o que ya no existe, abre un issue o un PR con una captura. Lee [CONTRIBUTING.md](CONTRIBUTING.md).

---

## English summary

Social Publish Kit is a Claude plugin that prepares a video for upload to YouTube (long-form and Shorts), TikTok, Instagram Reels and Facebook Reels. It analyzes the video locally (ffmpeg frames + Whisper transcript), asks for anything missing, and produces a copy-paste "publishing sheet" with every platform field in order: SEO titles and descriptions, CTAs, hashtags, the creator's social links, correct answers for legal fields (made for kids, paid promotion, AI disclosure), and image-generation prompts for 16:9 and 9:16 thumbnails. Skills are written in Spanish and generate output in any language you ask for. Contributions in any language are welcome.

## Créditos

**Creado por [Maikozort](https://github.com/Maikozort)**: idea, diseño del flujo y pruebas con videos reales.
Desarrollado junto con **Claude (Anthropic)**.

¿Te sirvió? Dale una ⭐ al repo y compártelo con otros creadores.

## Licencia

MIT © 2026 Maikozort
