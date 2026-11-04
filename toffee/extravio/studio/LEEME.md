# Claude Studio

Editor compartido entre Jay y Claude: https://claude.ai/artifact/Rp5qnwNvumrHP12AFkbkkB

- Página: `studio.html` (se publica con los archivos `media/` que salen del editor).
- Cómo se llena un proyecto: `EXPORTAR=1 TMPED=<carpeta> python3 toffee/extravio/editor/ed_dizzy01.py` → `<carpeta>/export/` (cama.mp3 = todo menos las voces, voces/*.mp3, proyecto.json). Video liviano: 540x960 sin audio (`media/proxy.mp4`).
- Base de datos: `proyectos/<id>` (nombre, duración, video, cama, tomas) y `proyectos/<id>/voces/<V##>` (inicio, dur, texto, personaje, url, **mueve** en segundos, **gain**, **mute**). Versiones en `…/versiones`, tareas para Claude Code en `…/mensajes` (estado «pendiente»).
- Render final: Claude lee las voces de la base, escribe `editor/datos-dizzy01/ajustes.json` ({V##: {mueve, gain, mute}}) y corre `ed_dizzy01.py` (sin EXPORTAR). Los ajustes se suman a la sincronía automática; no se pierde nada (edición no destructiva).
