---
name: ficha-facebook
description: Llena campo por campo la pantalla "Crear reel" de Facebook - descripción, personas, ubicación, sentimiento, portada, audio, subtítulos (.srt), audiodescripciones, transcripciones, destinatarios, remixes, etiqueta de IA, grupos, historia, lista de reproducción y promoción. Úsala cuando vayan a subir un reel o video a Facebook o pregunten qué poner en un campo de Facebook.
---

# Ficha de Facebook Reels

> **Verificado:** octubre 2026 · Facebook web · interfaz en español.

Facebook publica los videos nuevos como reels. El flujo tiene dos pasos: **Editar** y **Configuración**.

Para cada campo entrega: **valor** + **por qué** en una línea. Si es el valor por defecto, dilo igual.

## Paso 1: Editar

### Personas
- Etiqueta a quien aparece en el video o colaboró. Nombres exactos: no los inventes.

### Ubicación
- Opcional. Útil para contenido local. Nunca la casa del creador.

### Sentimiento/actividad
- Opcional. Casi siempre se deja vacío; úsalo solo si suma al tono ("jugando a…").

### Describe tu reel…
- En Facebook funciona un tono más conversacional. Una pregunta al final genera comentarios.
- Estructura: hook → 1-2 líneas de contexto → pregunta o CTA → 1-3 hashtags.
- Aquí los links sí son clicables, pero un link externo puede bajar el alcance: mejor en el primer comentario.

### Portada
- Elige el mejor fotograma (el análisis da el segundo) o sube la portada 9:16.

### Audio
- Música de la biblioteca de Facebook si el video no tiene audio propio o tiene música con derechos que conviene reemplazar.

### Recortar
- Solo si el análisis detectó un inicio lento: sugiere desde qué segundo empezar.

### Subtítulos
- **Subir subtítulos**: si `analizar-video` generó `transcripcion.srt`, renómbralo con el código de idioma que pide Facebook, por ejemplo `subtitulos.es_LA.srt` (español latino), `subtitulos.es_ES.srt` (España) o `subtitulos.en_US.srt`, y súbelo. Son más precisos que los automáticos.
- **Agregar subtítulos automáticamente**: actívalo si no hay `.srt`, porque muchos ven reels sin sonido. **Desactívalo si el video ya tiene subtítulos quemados**: se verían dos veces.

### Audiodescripciones
- Opcional. Accesibilidad para personas con discapacidad visual. Actívalo si está disponible y el video depende mucho de lo visual.

### Transcripciones de texto
- Opcional. Si hay transcripción del análisis, puede usarse aquí.

## Paso 2: Configuración

### Destinatarios de la publicación
- **Público** para crecer.

### Remixes y uso del audio original
- Permitir (por defecto) para alcance. Desactívalo si hay música con derechos o el creador no quiere remixes.

### Agregar etiqueta de IA
- Activar si hay contenido **realista** creado o alterado con IA. No hace falta para subtítulos, filtros comunes o efectos claramente irreales.

### Compartir en grupos
- Sugiere compartir en 1-3 grupos **donde el tema encaje y las reglas lo permitan** (grupos del juego, de la comunidad). No en grupos al azar: se marca como spam.

### Compartir en historia
- Activar: es alcance extra gratis entre sus seguidores.

### Agregar a lista de reproducción
- Si la página tiene listas por tema o juego, elige la que corresponda.

### Promocionar publicación
- **Desactivado** salvo que el creador quiera pagar publicidad. Si lo activa, Facebook pide presupuesto después de publicar. Nunca lo actives por tu cuenta.

## Formato de entrega

```markdown
### Facebook Reels

| Campo | Valor | Por qué |
|---|---|---|
| Describe tu reel | ver abajo | … |
| Subtítulos | Subir subtitulos.es_LA.srt | … |
| Destinatarios | Público | … |
| Compartir en historia | Activar | … |
| … | … | … |

**Descripción (copiar):**
…

**Primer comentario:** …
```
