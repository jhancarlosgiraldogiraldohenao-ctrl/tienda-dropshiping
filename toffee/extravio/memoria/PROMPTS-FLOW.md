# Prompts de Google Flow (Omni 1.1 Flash, vertical 9:16)

El generador es `toffee/extravio/serie/cap01_flow.py` (`prompt()`): **siempre** se arman los prompts con él, para que salgan
todos con la misma plantilla. Cada prompt nuevo va en el chat en su propio bloque y también en el link.

## Plantilla fija (en este orden)
1. `Vertical 9:16, N seconds. High-quality 3D animated movie style, exactly the same look as the character reference images, cinematic lighting, normal lens (no fisheye, no vignette, no dark corners). One continuous shot with no cuts, full vertical frame from edge to edge, no black bars.`
2. Lugar y luz (LUZ) → plano y cámara → «From the first frame…» (cómo arranca) → UNA acción clara.
3. Candado de cada personaje (LOCK): «looks exactly like the reference image: …» corto.
4. Si habla: `The rat speaks in … voice: "frase suavizada" His mouth moves clearly in sync with every word. Only the rat speaks; everybody else keeps their mouth closed.` Si no: `No one speaks; all mouths stay closed.`
5. `Only these characters appear; no other animals. No humans or people anywhere, no subtitles or captions, no phone, no selfie stick, no bicycle, no music; only <sonidos del lugar>.`

## Reglas (cada una costó créditos)
- **Sin nombres propios** fuera de las comillas: «the rat», «the hen», «the mule», «the pig», «the cockroach», «the cat». Flow los escribe como texto.
- **Referencias:** solo la foto `*-FRENTE.jpg` de cada personaje + la foto del lugar. Nunca hojas de 4 vistas.
- **Groserías y palabras delicadas suavizadas** solo en Flow (lista SUAVE): hijueputa→hijuepucha, malparido→mal portado, pirobo→bobo, me mata→me regaña, perico→polvito, cuca→cara, fuck→heck, shit→cow. Nada de violencia, drogas, armas, sangre, sexo. La frase real va en ElevenLabs.
- **Si Flow dice «No se pudo generar el audio»:** suavizar más la frase, o usar el modo de videos silenciados.
- **Idioma:** la frase entre comillas en el idioma en que la dirá ElevenLabs (español; inglés solo para Tocino). Si Flow
  habla en otro idioma, la boca no calza: se repite la toma o se rehace la voz con el ritmo de esa boca.
- **Dizzy:** «ALWAYS wearing his black hoodie (never bare-chested…)».
- **Bartolo:** «black-and-white striped Colombian sombrero vueltiao (never a plain straw hat)».
- **Tocino:** marrano en cuatro patas, «no arms or hands»; nunca gestos de manos (expresa con la cabeza, las orejas, la cresta). Si toca guitarra: con la pezuña, «pig hooves, no human hands».
- **Quién monta a Bartolo:** «sits on the saddle in the middle of the mule's back», plano medio de lado, los dos cuerpos enteros, «both stay fully inside the frame».
- **Decir sobre qué está parado** («stands on the stone pavement») y «no vehicle» (salió una bicicleta).
- **Dos personajes:** decir quién está a la izquierda y quién a la derecha; uno solo habla.
- **Una sola acción por toma.** Si hay dos acciones (hablar y pegar), son dos tomas.
- **Planos variados:** cada escena con general, medio y primer plano o inserto. Las caras de frente son para las frases.
- **Duración:** la toma dura al menos la frase + 1 s. Tomas de 4, 6, 8 o 10 s.
- **Palo selfie, celulares, pantallas con letreros:** prohibidos. La cámara de Dizzy es la de la gorra.
- **Toma puente:** toda acción nueva necesita una toma que la cause (por qué canta, por qué pega, por qué habla del Tuerto).
- **Revisar las 4 esquinas** y el primer segundo de cada toma (figuras humanas, personajes que cambian de puesto).

## HORIZONTAL 16:9 desde el 8-nov-2026 (decisión de Jay)
- Prueba aprobada: Dizzy y Tocino caminando por la calle de México, 10 s, travelling hacia atrás, fondo vivo (mariachis, vecinos, papel picado, pólvora lejos). Guardada en `serie/tomas-cap02/horizontal/H-PRUEBA.mp4 (las tomas horizontales van en esa carpeta)`.
- Encabezado: «Horizontal 16:9 … like a big-budget animated feature film … shallow depth of field …». Línea de fondo vivo reforzada por lugar (`VIVO` en `cap02_flow_h.py`), extras desenfocados que nunca miran a cámara.
- Composición de cine: personaje en un tercio del cuadro y el lugar al otro lado; con dos personajes, izquierda/derecha y cuerpos enteros.
- Planos abiertos y de acción a 360p (Claude los sube); caras y frases a 720p.
- El video largo de YouTube va en 16:9; los reels se suben en horizontal (franjas negras) y YouTube Shorts solo con tomas de un personaje recortadas o shorts aparte.
