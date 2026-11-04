# Claude Studio

Editor compartido entre Jay y Claude: https://claude.ai/artifact/Rp5qnwNvumrHP12AFkbkkB

- Página: `studio.html` (se publica con los archivos `media/` que salen del editor).
- Cómo se llena un proyecto: `EXPORTAR=1 TMPED=<carpeta> python3 toffee/extravio/editor/ed_dizzy01.py` → `<carpeta>/export/` (cama.mp3 = todo menos las voces, voces/*.mp3, proyecto.json). Video liviano: 540x960 sin audio (`media/proxy.mp4`).
- Base de datos: `proyectos/<id>` (nombre, duración, video, cama, tomas) y `proyectos/<id>/voces/<V##>` (inicio, dur, texto, personaje, url, **mueve** en segundos, **gain**, **mute**). Versiones en `…/versiones`, tareas para Claude Code en `…/mensajes` (estado «pendiente»).
- Pedazos de voz (4-nov-2026): cada doc es un pedazo: suena del segundo `desde` al `hasta` del archivo (`wav`), puesto en `inicio + mueve + desde`. Cortar crea `V##-2`, `V##-3`… con `base` = voz original. Los subtítulos (`subs`, relativos al archivo) se mueven con el pedazo; `subs_fijos` (canción, título) están en el proyecto.
- Medios del editor: `media/video2.mp4` (468x832, cuadro clave cada 0,5 s para buscar rápido), `media/cama.wav` (24 kHz), `media/vw/V##.wav` (48 kHz exactos, sin el retraso del mp3).
- **Video final = lo que se ve en el editor:** leer la base con ArtifactData (`list` de `proyectos/cap01p1/voces` y `get` de `proyectos/cap01p1` → `proyecto.json`, con `out_dir`) y correr `python3 toffee/extravio/studio/studio_render.py --datos <out_dir> --cama <export>/cama.mp3 --voces <wav de las voces> --video <video sin audio ni letras> --ass <subs.ass del editor> --out toffee/videos-editados/...mp4`. Si los archivos temporales ya no están, regenerarlos con `EXPORTAR=1 TMPED=<carpeta> python3 toffee/extravio/editor/ed_dizzy01.py`.
