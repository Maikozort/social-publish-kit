---
name: ficha-youtube
description: Llena campo por campo el formulario de subida de YouTube Studio para videos largos y Shorts - título, descripción, miniatura, playlists, audiencia (COPPA), restricción de edad, promoción pagada, uso de IA, colaboración, capítulos, tags, idioma, licencia, remix, categoría, juego, comentarios, elementos del video y visibilidad. Úsala cuando vayan a subir un video o short a YouTube o pregunten qué poner en un campo de YouTube Studio.
---

# Ficha de YouTube y Shorts

> **Verificado:** octubre 2026 · YouTube Studio web · interfaz en inglés. Los nombres de campo van en inglés tal como aparecen; si la persona usa Studio en español, agrega el nombre en español entre paréntesis.

YouTube trata como **Short** todo video vertical o cuadrado de hasta 3 minutos. Más largo u horizontal es un video largo. La mayoría de campos son iguales; las diferencias están marcadas.

Para cada campo entrega: **valor** (texto exacto o opción a marcar) + **por qué** en una línea. Si es el valor por defecto, dilo igual ("dejar marcado").

## Paso 1: Details

### Title (required)
- Máximo **100** caracteres. Apunta a 40-60 para que no se corte en móvil.
- Palabra clave principal al inicio. Viene de la skill `copy`.
- Shorts: ya no hace falta poner `#shorts`; ponlo solo si sobran caracteres.

### Description
- Máximo **5.000** caracteres. Lo que importa son las 2 primeras líneas: es lo único visible sin expandir.
- **Largo**: hook → contexto con palabras clave → capítulos → CTA → redes → hashtags.
- **Capítulos (solo largo)**: el primero en `00:00`, mínimo 3, cada uno de al menos 10 segundos. Tiempos desde la transcripción de `analizar-video`; nunca inventados.
- **Shorts**: 1-3 líneas + hashtags.
- Hashtags: los 3 primeros aparecen sobre el título. Con más de 60, YouTube los ignora todos.
- Se puede escribir `@canal` para mencionar a otro creador.

### Thumbnail
- **Largo**: "Upload file", 1280×720, JPG o PNG. Prompt desde la skill `portada`.
- **Shorts**: "Upload file" o "Select from video". Si no hay portada diseñada, recomienda el mejor fotograma del análisis con su segundo exacto.

### Playlists
- Sugiere una playlist existente que encaje (el creador debe decir cuáles tiene) o el nombre de una nueva. Las playlists suben el tiempo de visualización por sesión.

### Audience
**Is this video made for kids? (required)**
- "Yes" solo si el video está **dirigido principalmente a niños** (personajes, juguetes, canciones infantiles, lenguaje y ritmo pensados para niños). Que lo vean niños no lo convierte en "para niños".
- Gaming, humor, tutoriales o vlogs para público general → normalmente **"No, it's not made for kids"**.
- Por qué importa: es una obligación legal (COPPA). Marcar "Yes" desactiva comentarios, notificaciones y anuncios personalizados.

**Age restriction**
- "Yes, restrict…" solo si hay violencia gráfica, contenido sexual sugerente, lenguaje muy fuerte, actividades peligrosas o drogas. Restringir limita alcance y anuncios.
- Si un juego tiene sangre o violencia fuerte en pantalla, márcalo en "Alertas" y que la persona decida.

### Paid promotion
- "Yes" si hay patrocinio, producto colocado, marca que pagó o regaló algo a cambio de mencionarlo. YouTube añade un aviso al inicio.
- Un link de afiliado propio sin acuerdo con la marca no suele contar; si hay duda, márcalo en "Alertas".

### AI use
"Yes" solo si se usó IA para algo **realista** que pueda engañar:
- Que una persona real parezca decir o hacer algo que no dijo o hizo.
- Alterar imágenes de un evento o lugar real.
- Generar una escena realista que no ocurrió.

"No" si la IA solo se usó para guion, subtítulos, ideas, color, limpiar audio, efectos claramente irreales, animación o estilo de videojuego. Si marca "Yes", YouTube agrega una etiqueta al video.

### Collaboration
- "Invite a collaborator" si el video es una colaboración real con otro canal. Muestra el video a la audiencia del otro canal. Pide el nombre exacto del canal; no lo inventes.

### Automatic chapters
- Dejar marcado "Allow automatic chapters". Si hay capítulos manuales en la descripción, YouTube usa esos.

### Featured places
- Marcado si en el video aparecen lugares públicos (restaurantes, tiendas, sitios turísticos). En gaming no aporta: da igual.

### Automatic concepts
- Dejar marcado salvo que el creador no quiera que YouTube agregue explicaciones a la descripción.

### Tags
- Máximo **500** caracteres en total, separados por coma. YouTube dice que pesan poco.
- Úsalos para: nombre del juego y variantes, errores comunes de escritura, nombre del canal. 5-10 tags bastan.

### Language and captions certification
- **Video language**: el idioma que se habla en el video. Activa subtítulos automáticos en ese idioma.
- **Caption certification**: "None" para casi todos. Solo aplica a contenido emitido en la TV de EE. UU.

### Recording date and location
- **Recording date**: opcional; útil para eventos o viajes.
- **Video location**: opcional; ayuda en búsquedas locales. Nunca pongas la dirección privada del creador.

### License
- "Standard YouTube License" por defecto. "Creative Commons" solo si el creador quiere que otros reutilicen el video.
- **Allow embedding**: marcado (permite que el video se comparta en webs).
- **Publish to subscriptions feed and notify subscribers**: marcado. Desmárcalo solo para resubidas o pruebas.

### Shorts remixing
- "Allow video and audio remixing" (por defecto) da alcance extra cuando otros hacen Shorts con tu video.
- "Allow only audio remixing" si no quieres que usen tu imagen. Si hay música con derechos, recomiéndalo.

### Category
- La que corresponda: Gaming, Entertainment, Education, People & Blogs, Howto & Style, etc.

### Game title (solo con categoría Gaming)
- Nombre exacto del juego tal como aparece en la lista de YouTube. Enlaza el video a la página del juego.

### Comments and ratings
- **Comments**: "On". Si es un tema polémico, sugiere "Hold potentially inappropriate comments for review".
- **Moderation**: "Basic" por defecto; "Strict" si el canal recibe spam o ataques.
- **Who can comment**: "Anyone" para crecer.
- **Sort by**: "Top".
- **Show how many viewers like this video**: marcado.

## Paso 2: Video elements

- **Shorts → Related video**: enlaza el video largo relacionado (la versión completa, la parte 2). Es la forma de llevar tráfico de Shorts a videos largos.
- **Largo → Subtitles**: si `analizar-video` generó un `.srt`, súbelo aquí en vez de depender de los automáticos.
- **Largo → End screen**: 1 video recomendado + botón de suscribirse en los últimos 5-20 segundos. Solo si el video tiene espacio para eso al final.
- **Largo → Cards**: 1-2 tarjetas en los momentos en que se mencione otro video.

## Paso 3: Initial check (Checks)

YouTube revisa derechos de autor y si el video es apto para anunciantes. Si aparece una advertencia:
- **Copyright**: indica qué parte. Opciones: recortar el fragmento, silenciarlo o reemplazar la música desde el editor de Studio.
- **Ad suitability**: revisa lenguaje, violencia o temas sensibles. Se puede pedir revisión manual.
Predice estos problemas en "Alertas" si el análisis detectó música comercial o contenido sensible.

## Paso 4: Visibility

- **Public** para publicar ya, o **Schedule** con fecha y hora.
- Recomienda programar en la hora de más actividad de su audiencia (YouTube Studio → Analytics → Audience). Si no la sabe, sugiere probar entre 12:00 y 18:00 de su zona horaria y medir.
- **Unlisted** solo para revisiones; **Private** para borradores.
- Largo: "Set as Premiere" si quiere un estreno con chat en vivo.

## Formato de entrega

```markdown
### YouTube Shorts

| Campo | Valor | Por qué |
|---|---|---|
| Title | … (48/100) | … |
| Description | ver abajo | … |
| Thumbnail | Select from video → 00:07 | … |
| Made for kids | No | … |
| … | … | … |

**Description (copiar):**
…

**Tags (copiar):** …

**Comentario fijado:** …
```
