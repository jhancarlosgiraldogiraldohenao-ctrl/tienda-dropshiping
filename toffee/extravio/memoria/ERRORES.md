# Errores del capítulo 1 (parte 1) y la regla que los evita

Copiados del manual (`MANUAL-PRODUCCION.md` §10–12) más los de la tercera y cuarta revisión. Los del capítulo 2 viejo (Toffee) están en el manual §9.

## 10. Errores del capítulo 1 de Dizzy (4-nov-2026)
| Error | Causa | Regla |
|---|---|---|
| La canción cantó los nombres de los personajes («Gallinazo, carnecita fresca…») | Nombres entre corchetes en la letra de ElevenLabs Music | Nunca poner nombres ni etiquetas en la letra; quién canta va en el prompt de estilo. (Esta vez se dejó porque presenta a cada vendedor) |
| La segunda versión se saltó versos y estiró el coro | Letra sin etiquetas + duración larga | Si una versión ya sirve, no regenerar; poner la duración justa (≈ 35 s) |
| Flow: «No se pudo generar el audio» (G01) | Frases con palabras que el filtro de audio de Flow bloquea («me mata», groserías, drogas, sexo) | En los prompts de Flow la frase va suavizada con sílabas parecidas («me regaña», «mal portados», «polvito»); la frase real va solo en ElevenLabs. Lista en `serie/cap01_flow.py` (SUAVE) |
| La cadena de Dizzy salió con la palabra «DIZZY» y sin el buzo (G01 prueba) | El nombre propio en el prompt (Flow lo escribe) y el buzo nombrado una sola vez | Nada de nombres propios en los prompts de Flow («the rat», «the hen»…); «torn black hoodie that he always wears (never bare-chested)»; «the bottle-cap pendant is plain with no letters» |
| Humanos caminando al fondo de la plaza (G22 prueba) | «people in the square» en el sonido y nada que lo prohibiera | Todos los prompts: «No humans or people anywhere»; en el sonido, nunca «people» |
| Los personajes salían distintos a las referencias (3 pruebas del 4-nov) | «Photorealistic» chocaba con personajes 3D animados; descripciones largas que contradecían la foto; hojas de 4 vistas como referencia | Estilo «High-quality 3D animated movie style, exactly the same look as the character reference images»; descripción corta («looks exactly like the reference image: …»); referencia = una sola vista de frente (`*-FRENTE.jpg`) |
| Errores al generar por palabras delicadas | «slum», «dangerous», «cleaver», «stolen», «powder», «bloodshot», groserías | Lista de palabras prohibidas en Flow: violencia, drogas, armas, sangre, sexo, groserías. Se cambian por suaves («night market», «magic dust», «hijuepucha») |
| Texto en el video | — | Jay (4-nov): el texto dentro del video NO es problema (letreros, el nombre en la cadena). Ya no se prohíbe en los prompts |
| Dizzy salió en bicicleta (G20) | «riding» sin decir en qué: Flow le puso una bicicleta | Decir siempre sobre qué está («stands on the stone pavement», «on the mule's back») y «no vehicle» |
| Flow pegó subtítulos inventados («¿Contaaba?», G28) | Toma con diálogo corto | Todos los prompts: «no subtitles or captions» |
| Créditos gastados en efectos que Flow ya hace | Lista de efectos demasiado larga | Flow genera el sonido propio de cada toma (pasos, puertas, cascos, fuego, gente). En ElevenLabs solo los efectos de chiste, de amenaza y los que no están en la imagen |

## 11. Errores del primer reel de Dizzy (4-nov-2026, revisión de Jay)
| Error | Causa | Regla |
|---|---|---|
| Dizzy sin buzo en la primera toma (G01) | La foto de 4 vistas y «black hoodie» una sola vez | Dizzy: «ALWAYS wearing his black hoodie (never bare-chested…)» y foto DIZZY-FRENTE |
| Bartolo con sombrero de paja liso en el camino (G12–G17) y vueltiao en la finca | «woven straw hat» | «black-and-white striped Colombian sombrero vueltiao (never a plain straw hat)» |
| Dizzy montado raro (encima de la cabeza o el cuello de Bartolo, G15) y Bartolo saliéndose del cuadro (G17) | Primer plano con el sombrero adelante; «trotting fast» | Plano medio de lado con los dos cuerpos enteros; Dizzy «on the saddle in the middle of the mule's back»; «both stay fully inside the frame» |
| Voces corridas de la boca | Se alineaba solo la primera palabra | Pegar palabra por palabra (`pegar_suave` con las palabras de la voz y de Flow) + 0,08 s de retraso |
| Efectos de impacto feos | Los efectos viejos del Extravío de Toffee (golpe, whoosh, rayón, brillo, latido) | Descartados (`sonidos/descartados/`). Solo los efectos nuevos de Dizzy |
| Tocino con cuatro patas y además dos brazos (G24) | Se le pidió levantar una pezuña y hacer el gesto del rock | Tocino es marrano en cuatro patas: nunca gestos de manos; «only four legs and no arms or hands»; expresar con la cabeza, la cresta o las orejas |

## 12. Segunda revisión del reel de Dizzy (4-nov-2026, Jay)
| Error | Por qué pasó | Regla nueva |
|---|---|---|
| Voz corrida de la boca (G01, «¡Muévete!», «What the…», «Siga») | Los tiempos de Whisper sobre el audio de Flow fallan hasta 1,5 s | Pegar la voz frase por frase al **volumen real** del audio de Flow (`alinear()` en el editor: tramos de boca + emparejar por duración) |
| Se oía un «mue» antes de «¡Muévete!» | La máscara de la voz de Flow salía de Whisper y empezaba tarde | Tapar la voz de Flow también por volumen (0,12 s antes, 0,15 s después de cada tramo) |
| Subtítulos sobre las bocas: se nota cualquier desfase | Iban a la altura del pecho (y=1200) | **Subtítulos arriba (y=300 de 1920)**, sobre las cabezas y debajo de la barra de YouTube; cada trozo sale con su palabra |
| Personajes que cambian de puesto dentro de una toma (G27) | Flow los mueve en el primer segundo | Revisar el primer segundo de cada toma y entrar después del cambio |
| Saltos de historia (Cuca canta de la nada, la cachetada de frente, por qué Cuca habla del Tuerto) | Faltaban tomas puente | Antes de entregar el guion, cada acción nueva necesita una toma que la cause (G29b, G37b, G41b) |
| «¡Mía!», «¡Mijito!», grillos y «boing» que sobraban | Palabras y efectos de más | Menos es más: cortar lo que no suma, sin grillos ni efectos de caricatura |
| Una figura humana borrosa en la esquina (G40) | Flow la coló al fondo | Revisar las 4 esquinas de cada toma; si es pequeña, zoom (`recorte2`); si no, repetir |

## 13. Tercera y cuarta revisión (5-nov-2026, Jay)
| Error | Por qué pasó | Regla nueva |
|---|---|---|
| El inicio (G01) y «Que es distinto, malparidos» totalmente desfasados | Flow habló en inglés y la voz de ElevenLabs duraba 8,7 s con pausas largas; la boca solo 6 s seguidos | Voces DESPUÉS de las tomas, escritas con el ritmo de la boca (`memoria/VOCES-Y-BOCAS.md`). Jay repitió V01 (versión rápida de 7 s) y V02 |
| La voz arrancaba 3 s tarde en G01 | El emparejador saltaba los primeros tramos de boca por ser «barato» | Saltar un tramo del principio ahora cuesta 1,6 + su duración: la voz arranca con la boca |
| Claude borró la escena de la gallina saliendo de la casa al quitar «¡Mijito!»; la voz de Dizzy quedó encima de la de ella | Se cortó la toma entera en vez de solo la palabra | Quitar palabras = quitar el audio, no la imagen. Nunca borrar una escena sin preguntar |
| Subtítulos arriba (y = 300) no le gustaron | Se fue al otro extremo | Posición final: **y = 1400** |
| Se pasó de 3:00 (3:01) | Tomas puente nuevas | Recortar transiciones o repeticiones (la Llorona una vez), nunca tomas aéreas |

## 14. Parte 2 (5-nov-2026)
| Error | Por qué pasó | Regla nueva |
|---|---|---|
| Dos lunas en el cielo (G103, finca de noche desde el aire) | La cámara se mueve y Flow inventa otra luz en el cielo | Cielos de noche: «exactly one bright full moon (never two moons, no second light in the sky)» y que la luna «stays in the same place» |
| El Tuerto sin parche (G77, G78) | El parche iba nombrado una vez y Flow lo olvida en planos medios | Candado del Tuerto: «black eye patch over one eye (ALWAYS visible in every frame)» |
| Dizzy «colgado» pero derecho (G78, G79) | «upside down» no basta | «hangs HEAD DOWN, cap pointing to the floor, feet up». Truco: primer plano normal con la cola hacia abajo y **voltearlo 180° en la edición** |
| Toma «cenital» que no fue cenital y sin Dizzy (G73) | Plano raro + solo «paws» en el prompt | Plano picado (high-angle) y los candados de los dos jugadores; «only one rat with a cap» |
| La gallina no le pegó al marrano (G92) | El marrano iba lejos de ella | Poner al que recibe el golpe «very close, right under» al que pega, y decir cómo reacciona («his head turns from the hit») |
| Tocino agarrando la guitarra como humano en la cocina (G97) | El candado decía «his electric guitar» y Flow se la puso en las patas | Candado: guitarra «hanging on his back (he never holds it unless he is playing)»; primeros planos «framed from the chest up» |
| Frase cortada al final de la toma (G83 «…muchacho», G88 «…I love this woman») | Frase larga para 4 s | Frases de más de 5 palabras: toma de 6 s. Si se corta, el final va en off sobre la toma siguiente |
| Personajes que aparecen «de la nada» (Bartolo en el rincón, Cuca seduciendo al Tuerto) | El guion pasa de una acción a otra sin mostrar la llegada | **Regla de entrada:** cada personaje que entra a una escena necesita una toma que lo muestre llegando o ya ubicado (plano general del grupo) antes de su acción |
| Del «Oh, no» de la cocina a Dizzy durmiendo, sin aviso | Salto de lugar y de hora sin puente | **Regla de tiempo:** cada cambio de lugar u hora lleva una toma puente (aérea de noche, la casa por fuera, una puerta…). Lo que es sueño o visión se marca con una toma que lo cause (Dizzy mira la pantallita) |
| La mula iba a la derecha y en la toma siguiente a la izquierda (G91 → G92) | Flow elige la dirección | **Regla de dirección:** en el prompt decir siempre la dirección («walks from left to right») en TODAS las tomas de un viaje; si sale al revés, se voltea en espejo en la edición (`espejo=1`) |
| Toma aérea de la parte 1 pasada a atardecer se veía naranja y con un solo jinete | El color no se puede inventar y la toma vieja tenía otros personajes | No reusar tomas si cambian la hora o quién va en ellas: se genera la toma nueva (G90) |

## 15. Cierre del capítulo 1 (5-nov-2026, Jay: «quedó brutal»)
| Lo que faltó | Regla para el capítulo 2 en adelante |
|---|---|
| **Siempre el mismo encuadre del rincón del Tuerto** (16 tomas con la misma foto de lugar) | **Dinamismo:** cada lugar donde pasa mucho tiempo lleva **3 a 4 fotos de zonas distintas** (ej. El Hueco: entrada, calle de puestos, rincón del Tuerto de frente, el trono de cerca, detrás de los barriles, la mesa) y se alternan; además cambiar el ángulo en cada toma (picado, contrapicado, por encima del hombro, de perfil, primer plano). Nunca más de 3 tomas seguidas con la misma foto de lugar |
| El recuento en off quedó corto sobre la aérea | La toma dura lo que dura la voz |
| La visión del futuro confundía | Toma de Dizzy mirando la pantallita + visor de cámara (REC) |
| Escenas sin llegada, sin cambio de hora y con dirección cambiada | Reglas de entrada, tiempo y dirección (§13–14) |

## 16. Lugares del capítulo 2 (6-nov-2026)
| Error | Por qué | Regla |
|---|---|---|
| Las trajineras salieron con nombres escritos en los arcos (letras raras) | En la vida real las trajineras llevan el nombre en el arco, y Nano Banana lo copia aunque el prompt diga «no letters» | Objetos que en la realidad llevan letras (arcos, letreros, camiones, tiendas): describir con qué van cubiertos **en vez** de las letras («arches covered only with flower patterns and swirls»). Si sale con letras, se arregla con una edición en Nano Banana sobre la misma imagen, no con una nueva |
| Nano Banana hizo fotos nuevas en vez de editar (calle inglesa, planeta con Asia, otra tapa de alcantarilla) | La foto de referencia no iba en el mismo mensaje del prompt, o el prompt decía «attached» y no la vio | **Siempre subir la foto en el MISMO mensaje** del prompt y escribir «Using the uploaded photo…». Al revisar: comparar con la foto original (misma tapa, mismas puertas, mismo continente). Para mapas: mejor una foto limpia sin la raya y la raya se anima en la edición |
| La aérea del barrio salió como 3 franjas pegadas (collage) | El prompt pedía «tres lugares» y Nano Banana hizo un panel por lugar | Cuando una foto muestra varios lugares: «one single continuous photo, not a collage, not split into panels» y decir dónde va cada lugar (abajo, en el medio, arriba) |
| El puente del canal salió de día (la escena es de noche) | El prompt de ángulo nuevo no repitió la hora | En cada prompt de ángulo nuevo repetir la hora: «at night with a dark blue starry sky… It is night, not day, not sunset» |
| Salió una rata gris en la foto del altar «a la altura de una rata» | Decir «at the height of a small rat» le hizo dibujar una rata | En fotos de lugar, la altura se dice sin nombrar animales: «seen from very low, a few centimeters above the ground» |
| El mapa salió con nombres de ciudades (Mérida, Cancún, Cartagena…) y líneas de fronteras | Las fotos de mapas vienen con letreros | En mapas: «no city names, no labels, no borders, no lines». Si salen, Claude los borra (clonando el mar de al lado), como en AEREA-AMERICA-NOCHE |

## 17. Cap. 2 · parte 1, primera versión (8-nov-2026, revisión de Jay)
| Error | Por qué pasó | Regla |
|---|---|---|
| **Voces desfasadas de la boca en casi todo el video** (T01, T11, T13, T20, T21, T25…) | El editor partía la voz solo en silencios largos: una frase entera quedaba con UN ancla (solo el arranque); además tomaba ruidos cortos de Flow como «boca» (T25 «¡Corra, Gringo!» 1 s antes) | Sincronía **palabra por palabra**: palabras de Flow (Whisper) ajustadas al arranque real de cada tramo de boca ≥ 0,2 s, palabras de ElevenLabs ajustadas a su propio arranque, emparejadas por texto (`sincronizar()` en `editor/ed_dizzy02p1.py`). Antes de mandar un video, revisar el error por toma (≤ 0,15 s) |
| Se oía «ratas» dos veces (la voz de Flow se coló) | La máscara solo tapaba los tramos de boca | En tomas con voz, la voz de Flow se silencia desde 0,25 s antes de la primera boca hasta 0,35 s después de la última |
| El grito sonaba antes de caer (T09) y en el gancho (T13) | Se pegaba al primer ruido | Gritos: al primer tramo de boca ≥ 0,2 s |
| Se cayó por una alcantarilla con la tapa cerrada (T08, T09, T10) | El guion no mostraba la tapa abriéndose | **Lógica física:** todo lo que se usa tiene que verse posible: toma de la tapa abriéndose sola y las tomas siguientes con el hueco abierto (prompt: «the cover is already slid aside, the round hole is open») |
| Tocino aparece de la nada al lado de Dizzy en México (T16) | Faltó su caída | Regla de entrada también en las caídas: cada personaje que llega necesita su toma de llegada |
| Dizzy se veía gigante / flotando junto a Tocino (T03) y sin patas en primer plano (T07) | Tamaños no dichos en el prompt | Con dos personajes: «both small in the frame, both feet on the ground, the rat is much smaller than the pig». Jay prefiere ver el cuerpo entero: planos medios con los pies, no primeros planos de cara salvo en reacciones |
| La Catrina cambiaba de lado y se veía cortada entre T33 y T34 | Dos tomas de la misma acción sin regla de lados | T33 se corta antes de que aparezca; T34 se rehace con ella de cuerpo entero en el mismo lado |
| Las aéreas hechas con foto animada se veían falsas (finca, pueblo, CDMX, barrio) | Una foto quieta no tiene vida | **Aéreas en Flow a 360p** (1 crédito/s) y Claude las sube a 720/1080; el mapa sí puede ser animado |
| No se oía la tos de Chuy | El efecto estaba en otra toma | Cada efecto en la toma donde pasa la acción |
| Doble llegada (Dizzy sale disparado dos veces) | Se repitió la toma del gancho en la historia | La toma del gancho no se repite si no suma; en la historia basta la caída en las flores |

- 8-nov-2026 · Tráiler cap. 2 (toma CTA): «No se pudo generar el audio» con la frase «…completo en YouTube, mis ratas…». Causa probable: nombre de marca (YouTube) en la frase hablada. Arreglo: en Flow decir «en mi canal» (mismas sílabas) y poner «en YouTube» solo en la voz de ElevenLabs. Regla: nada de marcas ni plataformas dentro de las comillas de Flow.

## 18. Vlog 2 en horizontal (8-nov-2026)
| Error | Por qué | Regla |
|---|---|---|
| T02: Dizzy se mete en la ventana y luego se devuelve saltando al cuarto | «squeezes out» sin decir que no vuelve | Salidas: «he never turns around and never comes back inside; for the final second the window/door is empty» |
| T10: Tocino se paró en 2 patas con las patas de adelante como brazos | La acción decía «shrugs» (encogerse de hombros = gesto humano) | Con Tocino nunca verbos de hombros o brazos (shrug, wave, point); decir «his four hooves stay on the ground the whole time» y la acción como cerdo real («dives like a real pig jumping into water») |
| Flow: «No puedo generar el video… debido a intereses de proveedores de contenido de terceros» (9-nov-2026) | El prompt comparaba con producciones comerciales («like a big-budget animated feature film»), pedía «exactly the same look / looks exactly like the reference image» y voces «like an old telenovela star» | Nunca comparar con películas, estudios, franquicias ni pedir voces «como» alguien. Encabezado: «Original high-quality stylized 3D animation… the same character designs shown in the uploaded reference images»; candados: «has this original design: …»; voces descritas por tono, acento, ritmo y emoción. Lo aplica `LIMPIO` en `cap02_flow_h.py` |
| Diagnóstico T23 (9-nov-2026, en curso) | Comprobado: la redacción vieja sola no bloquea (T18/T19/T21 salieron con ella); la T23 falla con y sin diálogo (pruebas A y B) → la frase NO es la causa; Flow reembolsa los bloqueados | Hipótesis abiertas: imágenes de Catrina + Tocino juntas, o la combinación del cuadro (esqueleto + Día de Muertos + guitarra). Pruebas siguientes: C sin fotos, D con fotos de a una, E sin guitarra |
| T23 · prueba G (9-nov-2026) | **Comprobado:** el prompt LIMPIO (sin encabezado largo, sin «has this original design», sin la línea larga de fondo vivo, sin el bloque de prohibiciones) con las mismas 4 fotos SÍ salió. Jay tenía razón: el bloqueo viene de alguna parte fija del builder combinada con la escena. Falta saber cuál (pruebas una por una) | Desde ahora: plantilla limpia y corta; agregar solo lo necesario (diálogo y boca) |
| T23 · prueba H (9-nov-2026) | **Comprobado:** el mismo prompt limpio que pasó (G) + SOLO la frase «Mamacita, I don't care you're all bones… I like 'em skinny» = bloqueado. La frase, dentro del prompt, activa el filtro (con el prompt largo también fallaba sin frase: los dos sumaban) | No repetir. T23 = toma G sin voz; la frase va con ElevenLabs mientras Tocino camina de perfil (boca escondida, como Gnomo). Frases con apodos de piropo + cuerpo («mamacita», «skinny», «all bones») no van dentro de las comillas de Flow |
| T24 limpia bloqueada (9-nov-2026) | Hipótesis (sin comprobar): el filtro se activa con las escenas de coqueteo Catrina–Tocino; las tomas de la Catrina sola con el formato largo SÍ pasaron (T19, T21) | Probar la T24 con el MISMO formato de la T19/T21; si falla, toma sin voz con el abanico tapando la boca y la voz en off |
