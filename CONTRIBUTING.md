# Cómo contribuir

Gracias por ayudar. Lo que más valor aporta es mantener las plataformas al día, porque sus formularios cambian seguido.

## Actualizar una plataforma

1. Sube un video de prueba (en privado o borrador) y saca capturas de **todas** las pantallas y opciones desplegadas.
2. Edita solo la skill de esa plataforma, por ejemplo `skills/ficha-tiktok/SKILL.md`.
3. Respeta el orden en que aparecen los campos en la app. Así la ficha se puede llenar de arriba a abajo.
4. Actualiza la línea `Verificado:` con la fecha, el dispositivo (web, iOS, Android) y el idioma de la interfaz.
5. En el PR adjunta las capturas y explica qué cambió.

Los límites de caracteres y las reglas de políticas (IA, niños, promoción pagada) deben venir de la documentación oficial. Pon el enlace en el PR.

## Agregar una plataforma nueva

Copia una skill `ficha-*` existente como base, cambia el `name` y la `description` del encabezado, y agrega la plataforma a la tabla del README y al paso 4 de `skills/publicar/SKILL.md`.

## Reglas de estilo

- Las skills se escriben en español neutro. La salida puede ser en cualquier idioma.
- Instrucciones cortas y accionables. Explica el *por qué* cuando una regla no es obvia.
- Nada de datos inventados: si un límite no está confirmado, dilo.
- Una skill por responsabilidad. Si algo crece mucho, sepáralo.

## Probar tus cambios

```bash
claude --plugin-dir ./social-publish-kit
```

Pide una ficha completa con un video real y revisa que cada campo coincida con lo que ves en la app.
