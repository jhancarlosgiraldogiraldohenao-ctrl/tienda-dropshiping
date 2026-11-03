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
| Cruzan la puerta en un prado de día en vez de la azotea (C2-12) | La foto de referencia de la puerta tiene prado de fondo y Flow copió el fondo | Si una referencia de OBJETO trae fondo, decir «only the door from the door reference, NOT its background» y nombrar el lugar real + su foto |
| La página arrancada salió entera, con dos cachorros (C2-36) | Pedir que Galleta «pase la página» y que aparezca el dibujo: Flow inventa otra página | Que la página correcta esté abierta DESDE EL PRIMER CUADRO y una sola acción (olfatear) |
| Texto manuscrito en las páginas del libro (C2-32) | Libro antiguo = Flow escribe | Recortar en edición; para insertos de libro, usar la foto de páginas como primer cuadro |
| Texto en pantalla (letreros) | Regla fija vieja | Jay (2-nov-2026): los letreros y textos que salen de forma natural en la escena NO son error; pueden usarse como recurso. Lo que se evita es texto inventado, ilegible o que tape la acción |
| La amenaza aparece y desaparece | Tomas sueltas | La Polilla (o la amenaza) se ve o se siente en cada toma de la secuencia (luz, sombra, sonido) |

## 4. Voces (ElevenLabs)
- Toffee: voz «toffee» v4 (prompt de diseño en `CLAUDE.md`). Lucho: «lucho el ratón». Una frase por generación; 1–2 versiones.
- El texto con ritmo lo arma Claude midiendo la toma (`editor/ritmo.py`). Si Flow estira mucho una palabra («¡Bieeenveniiidos!»), el texto también la estira.
- Voces en off: solo cuando no se ve la boca (de espaldas, lejos, o sobre otro plano). Si se ve la cara, la frase va en una toma donde ese personaje la dice.
- Música (cambio de Jay, 1-nov-2026): NO de fondo todo el capítulo, sino **por momentos** (persecución, misterio, llegada/ciudad, noche, final) y bajando sola cuando alguien habla. Sin eso el capítulo suena plano. Pistas en `editor` → `sfx2/` (M_TEMA, M_PERSECUCION, M_SUSPENSO, M_MISTERIO).
- **Silencios vivos (estudio de Desencanto, Jay 1-nov-2026):** cuando nadie habla, el lugar suena con detalles propios (animales, ramas, viento, velas, papel picado, perros a lo lejos) y en los momentos tristes o tiernos entra una melodía suave. Nunca un silencio plano ni un solo viento: cada lugar tiene su ambiente de 1 minuto con capas.
- **Efectos de reacción** que despiertan: whoosh (logo, caídas), golpe de chiste en cada remate, rayón de disco antes de un estallido, «wah wah» en los fracasos de Toffee, pop, brillo mágico, alas, latido, pasos, cortina, remate final. Se ubican en el cuadro exacto (mirar la toma) y van por debajo de la voz. Ambientes: efectos largos de ElevenLabs por lugar (si solo deja 1 minuto, un audio con 3 partes de 20 s y Claude lo corta).

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

## 8. Cómo se hacen los prompts desde el capítulo 2 (optimizado el 1-nov-2026, con todo lo aprendido)
1. **Guion por escenas, no por tomas sueltas.** Cada escena: dónde están, qué quieren, qué sale mal, con qué remate termina. Antes de las tomas, revisar continuidad completa (cómo llegan, qué tienen en las manos, de día o de noche).
2. **Cada toma en una ficha de 6 líneas** (base `capitulos/base.py`): plano y movimiento · dónde está cada uno en el PRIMER cuadro · UNA acción · quién habla y la frase exacta (≤ 8 s) · qué suena (efecto o música de la librería) · si sigue a otra toma (último cuadro solo con el mismo encuadre).
3. **Sonido desde el guion**: cada toma ya dice qué efecto y qué música lleva, sacados de `recursos/EXTRAVIO-RECURSOS.zip` (LEEME.txt). Solo se le pide a Jay lo que falta, todo junto y al principio.
4. **Tomas de reacción e insertos baratos** (una cara, un objeto, 4 s) entre diálogos: dan ritmo y tapan cortes.
5. **Frases cortas y naturales**, sin vocales estiradas largas que ElevenLabs no imita («ustedeees»); si una pausa importa, escribirla en el prompt de Flow y en el de ElevenLabs.
6. **Primero 1 toma de prueba por personaje nuevo** (para ver cara y tamaño) y después el resto.
7. Al recibir tomas: «✓» en silencio, revisión completa en «listo», repetir lo que no cumpla, anotar el error nuevo en la tabla de la sección 3.

## 9. Errores del capítulo 2 (1-nov-2026, lo que encontró Jay)
| Error | Causa | Regla |
|---|---|---|
| La Catrina mueve la boca sin decir nada (1:03) | Toma sin frase grabada | Si se ve la boca, la toma lleva frase y voz; si no habla, boca cerrada en el prompt |
| La canción no calza con su boca (1:08) | Flow canta con su propia voz, no con la canción | Canción: cámara lejos y cortes a reacciones; los acercamientos son solo para frases cortas |
| «Para pasar, se paga con un recuerdo» aparece de la nada (1:41) | Falta la toma del camino y el motivo | Antes de cada pago o ritual, una toma que muestre la llegada |
| Lucho pide queso sin que se sepa por qué están ahí | Falta el contexto de quién los busca | Cada capítulo explica en una frase por qué están allí, antes del minuto 1 |
| Cartel con letras | Referencia con texto | Usar solo la foto, sin letras |
| La placa de Galleta no dice MAX | El prompt no pedía las letras | Escribir «engraved letters M-A-X» y usar PLACA-MAX como referencia |
| Ocho tomas en el mismo lugar con el mismo plano (2:19 en adelante) | Todas las tomas fijas, de frente | Cada escena: mínimo tres encuadres distintos (general, medio, a ras de piso) y una acción nueva |
| Toffee siempre de cuello para arriba | Plano medio cerrado por defecto | Toffee gesticula: patas, manos y camina en dos patas (a veces en cuatro) |
| El estilo cambia del capítulo 1 al 2 | Referencias nuevas sin estilo común | Cada toma nueva lleva también ESTILO-CAP01 como referencia |

## 10. Errores del capítulo 1 de Dizzy (4-nov-2026)
| Error | Causa | Regla |
|---|---|---|
| La canción cantó los nombres de los personajes («Gallinazo, carnecita fresca…») | Nombres entre corchetes en la letra de ElevenLabs Music | Nunca poner nombres ni etiquetas en la letra; quién canta va en el prompt de estilo. (Esta vez se dejó porque presenta a cada vendedor) |
| La segunda versión se saltó versos y estiró el coro | Letra sin etiquetas + duración larga | Si una versión ya sirve, no regenerar; poner la duración justa (≈ 35 s) |
| Flow: «No se pudo generar el audio» (G01) | Frases con palabras que el filtro de audio de Flow bloquea («me mata», groserías, drogas, sexo) | En los prompts de Flow la frase va suavizada con sílabas parecidas («me regaña», «mal portados», «polvito»); la frase real va solo en ElevenLabs. Lista en `serie/cap01_flow.py` (SUAVE) |
| Créditos gastados en efectos que Flow ya hace | Lista de efectos demasiado larga | Flow genera el sonido propio de cada toma (pasos, puertas, cascos, fuego, gente). En ElevenLabs solo los efectos de chiste, de amenaza y los que no están en la imagen |
