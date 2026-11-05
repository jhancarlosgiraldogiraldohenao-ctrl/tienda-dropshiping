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
