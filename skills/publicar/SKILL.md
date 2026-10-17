---
name: publicar
description: Prepara todo lo necesario para subir un video a YouTube, YouTube Shorts, TikTok, Instagram Reels o Facebook Reels. Entrevista al creador, analiza el video, escribe el copy con SEO y CTAs, llena cada campo de cada plataforma y crea el prompt de la portada. Úsala cuando alguien diga que va a subir o publicar un video, short, reel o tiktok, o pida título, descripción, hashtags, miniatura o "qué le pongo" a un video. También en inglés ("upload this video", "post this short").
---

# Publicar un video

Tu trabajo es dejar a la persona con una **ficha de publicación** que pueda llenar de arriba a abajo sin pensar: cada campo de cada plataforma, en el orden en que aparece en la app, con el texto exacto o la opción a marcar y una línea de por qué.

Esta skill orquesta a las demás del plugin. Úsalas en este orden: `analizar-video` → `copy` → `ficha-*` → `portada`.

## Paso 1. Datos del creador

Si existe un archivo `creador.md` en la carpeta de trabajo, léelo y no preguntes lo que ya dice. Si no, pide estos datos **una sola vez por conversación**, todos en un mismo mensaje:

- Nombre del canal o marca
- Nicho y tipo de contenido (por ejemplo: gaming de shooters, recetas rápidas, vlogs de viaje)
- Links o usuarios de sus redes sociales
- Tono (divertido, técnico, motivador, irreverente…) y frases o muletillas propias
- Hashtags fijos y CTA preferido (seguir, suscribirse, comentar, ir a un link)

Si la persona quiere no repetirlos, ofrécele guardar un `creador.md` con [la plantilla](creador-plantilla.md).

## Paso 2. Datos del video

Pregunta en **un solo mensaje** solo lo que todavía no sepas:

1. **Plataformas** donde se publica y **formato**: vertical (Short/Reel/TikTok) u horizontal (video largo).
2. **Idioma o idiomas** del copy. Si son varios, cada idioma se escribe de forma nativa, no traducido palabra por palabra.
3. **El video**: ruta del archivo, y además un **resumen corto** con sus palabras (de qué trata, qué juego o tema, qué pasa, qué quiere lograr con él).
4. **Gaming**: nombre exacto del juego, modo, personaje o mapa, temporada o parche si importa.
5. **Campos legales** (no adivines, pregunta si no es obvio):
   - ¿Hay patrocinio, producto regalado, afiliado o marca pagada?
   - ¿Usó IA para crear o alterar algo que **parezca real** (voz o cara de una persona real, un hecho que no pasó)?
   - ¿El video está **dirigido** a niños?
   - ¿Tiene música comercial o clips de terceros?
6. **Opcional**: colaboradores a etiquetar, ubicación, fecha de grabación, playlist, link a promocionar.

## Paso 3. Entender el video

- Si hay archivo de video, usa la skill `analizar-video`.
- Cruza el análisis con el resumen de la persona. Si se contradicen (por ejemplo, dice que es Fortnite y los fotogramas muestran Warzone), **pregunta** antes de seguir.
- Si no hay archivo ni forma de analizarlo, trabaja con el resumen y dilo en la ficha.

No escribas nada del copy hasta entender bien el video. Un copy genérico es justo lo que esta skill debe evitar.

## Paso 4. Generar

1. **Copy base** con la skill `copy`: un hook, palabras clave, variantes de título, descripción y CTAs.
2. **Una ficha por plataforma**, adaptando el copy a cada red (no pegues el mismo texto en todas):
   - YouTube largo o Shorts → `ficha-youtube`
   - TikTok → `ficha-tiktok`
   - Instagram Reels → `ficha-instagram`
   - Facebook Reels → `ficha-facebook`
3. **Portada** con la skill `portada`, en la orientación de cada plataforma (16:9 para YouTube largo, 9:16 para las verticales).

## Paso 5. Entregar

Escribe un archivo `ficha-<nombre-del-video>-<AAAA-MM-DD>.md` en la carpeta de trabajo con esta estructura:

```markdown
# Ficha de publicación: <título corto>

## Resumen del video
<2-3 líneas: de qué trata, hook, público>

## Alertas antes de publicar
<derechos de música, campos legales dudosos, problemas del video. Si no hay, "Ninguna">

## YouTube / Shorts
<ficha-youtube>

## TikTok
<ficha-tiktok>

## Instagram Reels
<ficha-instagram>

## Facebook Reels
<ficha-facebook>

## Portada
<prompts>

## Checklist final
- [ ] Título y descripción revisados en voz alta
- [ ] Campos legales confirmados
- [ ] Portada legible en tamaño pequeño
- [ ] Comentario fijado listo para publicar apenas salga el video
```

Incluye solo las plataformas pedidas. En el chat, da un resumen corto y el enlace al archivo; no repitas toda la ficha.

## Reglas

- **No inventes datos**: redes, ubicaciones, nombres de colaboradores, patrocinadores. Si falta algo, deja `[COMPLETAR: …]`.
- **Campos legales**: responde según los hechos que dio la persona y explica la regla en una línea. Si hay duda, márcalo en "Alertas".
- **Respeta los límites de caracteres** de cada plataforma (están en cada skill `ficha-*`). Cuenta antes de entregar.
- **Para cada campo, di qué marcar aunque sea el valor por defecto**, así la persona no tiene que adivinar si debe tocarlo.
- Si la persona pide solo una parte ("solo el título", "solo la portada"), usa directamente la skill que corresponde.
