# Edición (cómo quedó bien la parte 1)

Editor: `toffee/extravio/editor/ed_dizzy01.py` (copiarlo como `ed_dizzy01p2.py` para la parte 2). Se corre con
`TMPED=<carpeta temporal> python3 toffee/extravio/editor/ed_dizzy01.py` (≈ 8 min). Lista de tomas en `E`.

## Estructura (estudio de Gnomo Palomo: `ESTUDIO-EDICION-GNOMO.md`)
- Gancho primero → título «EXTRAVÍO · VLOG 01» pequeño sobre la primera toma aérea, sin logo → historia → cierre en suspenso.
- Cortes secos (85 %), tomas de ≈ 2,5 s, la voz pasa en L sobre la toma siguiente, el sonido nunca se corta.
- Música solo por escena, baja bajo las voces (ducking); ambiente por lugar; efectos solo de reacción. −14 LUFS.
- Nada de grillos de chiste ni «boing». Efectos de la biblioteca nueva de Dizzy.

## Subtítulos
- Montserrat negrita blanca, borde negro, palabras clave en rojo, 1–3 palabras, **cada trozo sale cuando empieza su palabra**
  (tiempos reales de la voz ya pegada).
- **Posición final aprobada: y = 1400 de 1920** (un poco más abajo del pecho). Arriba (y = 300) NO le gustó a Jay; en
  y = 1200 tapaba las bocas.
- Las frases en inglés de Tocino van traducidas en el subtítulo (`SUBT`).

## Duración: máximo 3:00 por parte
- Si sobra tiempo: recortar transiciones y caminos, o repeticiones (la Llorona grita una vez). **Nunca tomas aéreas** y
  nunca escenas que explican algo. Si hay duda, preguntar.

## Arreglos de imagen
- Figura pequeña en un borde: zoom que la saque (`recorte2`, `recorte3`). Si es grande, se repite la toma.
- Personajes que se mueven raro al inicio: entrar a la toma después (`a=`).
- Recuerdos: tinte cálido (`tinte=1`).

## Claude Studio
- Editor web compartido: https://claude.ai/artifact/Rp5qnwNvumrHP12AFkbkkB (`toffee/extravio/studio/`). Jay prefirió
  decirle los cambios a Claude en el chat; el Studio queda para cuando lo quiera usar.

## Lo que aprendimos en la parte 2 (5-nov-2026)
- **Voz en off sobre una toma:** la toma dura lo que dure la voz (`d=None` + `cola`), nunca un tiempo fijo más corto que la voz.
- **Visiones, sueños o videos de la cámara:** se marcan con el visor de cámara (`visor=1`: esquinas blancas, punto rojo y «REC» que titila) + tinte verde + grano + el pitido de la cámara. Antes va una toma de Dizzy mirando la pantallita. Así nadie se pierde.

## Lugares animados desde fotos (aprobado por Jay, 7-nov-2026)
- Aéreas, lugares y mapas SIN personajes se hacen con la foto de Nano Banana animada (`editor/animar_lugares_demo.py`):
  cámara lenta que se acerca/baja (trabajar a 2x para que no tiemble), luces que titilan, chispas o brasas que suben,
  grano de película; en el mapa, la raya verde que viaja de Colombia a México con chispitas y destello al llegar.
- Así no se gasta Flow en eso: todos los créditos van a las tomas con personajes (Omni 1.2).
