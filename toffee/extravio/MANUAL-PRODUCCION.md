# Manual de producción de EXTRAVÍO (aprendido con el capítulo 1, 28-oct a 31-oct-2026)

Jay aprobó el capítulo 1 el 31-oct-2026 («está realmente muy bien»). Este manual guarda todo lo que funcionó y cada error que
costó tiempo o créditos, para que desde el capítulo 2 los prompts salgan bien a la primera.
Archivos del capítulo 1: guion y prompts `capitulos/ex01p.py` (Artifact https://claude.ai/artifact/Njyo7xQfAZUhiRoAYe2Jb1),
editor `editor/ed01p.py` + `editor/pegar.py`, video `toffee/videos-editados/EXTRAVIO-CAP01-PILOTO.mp4`, estudio de planos `ESTUDIO-PLANOS.md`.

## 1. El orden de trabajo que funciona (no cambiarlo)
1. **Guion con mundo vivo y escenas conectadas** (sección 3). Antes de mandar prompts, revisar la secuencia completa: ¿cómo llega cada personaje de un lugar al siguiente? Si no se ve, falta una toma puente.
2. **Imágenes de referencia de cada lugar nuevo** (Nano Banana Pro) ANTES de las tomas.
3. **Tomas en Flow (Omni 1.1 Flash, 16:9) con la frase dentro del prompt.** Flow dice la frase y mueve la boca; su voz NO se usa, solo da el ritmo.
4. Claude mide el ritmo de cada toma (Whisper + VAD) y manda a Jay **el texto para ElevenLabs con ese ritmo** (pausas `[short pause]`/`[long pause]`, vocales alargadas «Miii», MAYÚSCULAS en gritos, emoción en corchetes). Una voz por frase.
5. Jay hace las voces en ElevenLabs (una sola cuenta = la voz siempre igual). **La voz de Flow nunca sirve de voz final**: cambia entre cuentas y tomas, el Voice Changer y Seed-VC no la igualan (probado y rechazado).
6. Claude pega las voces a la boca (sección 5) y arma el capítulo.
7. Claude revisa TODO antes de entregar (sección 6) y solo entonces manda el video.

## 2. Reglas fijas de los prompts (cada prompt las cumple; ya están en `capitulos/base.py` y en `ex01p.py`)
- Encabezado: `Horizontal 16:9, N seconds. Photorealistic cinematic film look, normal lens (no fisheye, no vignette, no dark corners), natural colors, realistic physics. One continuous shot with no cuts, full frame from edge to edge, no black bars.`
- Cierre: `Exactly <reparto> as main characters, identical to the references; no other animals appear. The cat's whole head, nightcap and camera always in frame. The dog never speaks. No text, letters or signs with words anywhere, no phone, no selfie stick, no music; only <sonido del lugar>.`
- **Un solo personaje habla por toma** («Only Lucho speaks.») y la frase va completa entre comillas con «His mouth moves clearly in sync with every word».
- **Plano y movimiento de cámara explícitos** en cada toma (ver `ESTUDIO-PLANOS.md`), uno solo por toma. Nada de «cámara al frente y alguien hablando» todo el capítulo.
- **El mundo vivo**: cada toma de Extravío lleva algo haciendo su vida (habitantes de `refs/extravio/personajes/HABITANTES.jpg`, Cartero Caracol, objetos que caen, cometas, paraguas que vuelan).

## 3. Errores que ya pasaron y cómo se evitan (no repetirlos)
| Error | Causa | Regla |
|---|---|---|
| **Le aparecen o desaparecen quesos a Lucho** | Nombrar el queso varias veces en el prompt (Flow inventa más) y pedir objetos que caen (los vuelve queso) | Nombrar el queso **UNA sola vez**: «hugging one single chunk of yellow cheese against his chest with his left arm» + «There is only ONE piece of cheese in the whole video». No pedir que use las dos manos. Objetos que caen: solo control, llave, media |
| Lucho con el gorro/cámara de Toffee | Personajes mezclados | «Lucho wears NO hat and NO camera; only the cat wears the navy nightcap with the camera» |
| Toffee con pañoleta o placa | Mezcla con Galleta | «The cat wears NO bandana and NO tag» en tomas con los dos |
| Toffee blanco/gris de noche | Luz azul | «His fur stays warm cream-caramel, never white or gray, even in the blue night light» |
| El gancho de llaves salió con llaves | «empty» no basta | «The hook is completely EMPTY: no keys, no keychain, nothing hangs on it» |
| Letreros con texto («LUCHO'S KEY SHOP», «Merry Christmas») | Flow pone letreros | «No text, letters or signs with words anywhere» + «frames the shop door only, no sign above it». Si aparece, Claude recorta esa parte |
| Cambio de tamaño a mitad de toma (gigantes → carrito diminuto) | «Usar el último cuadro de la toma X» con otra escala | Solo usar último cuadro si la toma anterior tiene el MISMO encuadre. Si no: «Static medium-wide shot, the camera does not move or zoom, everything keeps the same size» y el objeto grande visible desde el primer cuadro |
| Personajes que salen de un lugar donde no estaban | Prompt ambiguo de entrada/salida | Decir dónde están en el primer cuadro («From the first frame, all three are OUTSIDE…») y «Nobody comes out of the shop» |
| Se ven muy pequeñitos | Plano demasiado abierto | «Medium shot… close enough that the three fill most of the frame» |
| Solo se ve la cabeza (snorricam) | Snorricam en un gancho | Para caídas y acción: «Medium-wide shot… the whole body is visible» |
| La pelota rodaba hacia atrás | POV de objeto confuso | Movimientos con dirección explícita: «always moving forward to the right… never moves backward» |
| Galleta deformado al cruzar la portezuela | Acción difícil en primer plano | Planos desde atrás para cruces de puertas; «keeps his normal shape at all times» |
| Galleta con la boca abierta mientras habla Toffee | Jadeo de perro | En tomas de diálogo: «the dog keeps his mouth closed while the cat talks» |
| Flow pone a hablar a quien no debe o inventa frases | Toma sin frase | Si nadie habla: «No one speaks». Claude silencia toda voz de Flow en la mezcla |
| Escenas sin continuidad (aparecen en otro lugar) | Faltaban tomas puente | Toda llegada a un lugar nuevo tiene su toma de camino (bajar del trineo, subir la colina, entrar por el arco, entrar al local, escalera a la azotea, meterse al carrito) |
| Lucho entra volando/saltando desde arriba (P68) | «leans into the frame from above»: Flow lo leyó como caer del cielo | Decir dónde está en el primer cuadro: «From the first frame, Lucho is already standing in front of the camera»; nunca «from above» para alguien que se asoma |
| Toffee salió sentado en vez de acostado (P69) | Posturas acostadas en primer plano: Flow las endereza | Si la postura importa, plano más abierto donde se vea el cuerpo entero acostado; si no importa, aceptar sentado |
| La amenaza aparece y desaparece | Tomas sueltas | La Polilla (o la amenaza) se ve o se siente en cada toma de la secuencia (luz, sombra, sonido) |

## 4. Voces (ElevenLabs)
- Toffee: voz «toffee» v4 (prompt de diseño en `CLAUDE.md`). Lucho: «lucho el ratón». Una frase por generación; 1–2 versiones.
- El texto con ritmo lo arma Claude midiendo la toma (`editor/ritmo.py`). Si Flow estira mucho una palabra («¡Bieeenveniiidos!»), el texto también la estira.
- Voces en off: solo cuando no se ve la boca (de espaldas, lejos, o sobre otro plano). Si se ve la cara, la frase va en una toma donde ese personaje la dice.
- Música: SOLO en el logo (Jay pidió quitar la música de fondo). Ambientes: efectos largos de ElevenLabs por lugar (si solo deja 1 minuto, un audio con 3 partes de 20 s y Claude lo corta).

## 5. Edición (`editor/ed01p.py`, la base de los próximos capítulos)
- Pegado de voz: `pegar_suave` (rubberband `--fine`, una sola pasada con mapa de tiempos). Las pausas absorben la diferencia (máx. +0,2 s por pausa); la voz solo se acelera/frena 0,8–1,25. Nunca se corta una frase por dentro. +0,08 s de retraso para que la voz no llegue antes que la boca. Ajuste fino por frase (±0,3 s) con la voz original de Flow.
- Ambiente: el sonido de cada toma sin la voz de Flow (rampas suaves), más una cama por escena (efecto de ElevenLabs o varias tomas sin voces ni gritos mezcladas; nunca una toma con gritos). El ambiente se aparta cuando hablan (≈18 dB por debajo de la voz).
- Montaje: tomas sin diálogo de 3,5–4,5 s; con diálogo, 0,9 s antes y 1,5 s después de la frase. Fundido de 0,25 s entre tomas y de 0,3–0,7 s entre lugares (sin negro). Logo con apertura circular desde el remolino. Color parejo por escena; noche con un poco más de luz en las caras.
- Volumen −14 LUFS, pico −1,5 dB. Copia < 100 MB para el repo (2 pasadas).

## 6. Revisión obligatoria antes de entregar
1. Pista de voces sola por Whisper: todas las frases, en orden, sin palabras cortadas.
2. Pista de ambiente sola por Whisper: **cero palabras** (ninguna voz de Flow escondida).
3. Ninguna frase de un personaje encima o pegada (< 0,25 s) a la de otro.
4. Golpes de sonido en el ambiente: solo los que deben estar (caída, puertas, campana).
5. Cuadros en cada toma nueva: sin texto, sin quesos de más, colores y tamaños correctos.
6. Largo de cada toma = lo planeado; video y audio del mismo largo; volumen.

## 7. Capítulos y ritmo
- 5–6 min por capítulo (el 1 quedó en 5:38). 1 diario a las 6 p. m. con 1 de reserva. Galleta nunca habla.
- Cada capítulo: gancho → logo → meta clara → mundo vivo → obstáculo con tensión → clímax → recompensa → misterio → «Sígueme para no perderte el próximo episodio» → 10 s de pantalla final.
