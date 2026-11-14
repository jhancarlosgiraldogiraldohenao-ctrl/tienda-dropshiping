# Continuidad: el método fijo (Jay, 13 y 14-nov-2026 — «la continuidad es lo más importante, brother»)

## Lo que salió mal en el capítulo 2 (parte 2) y no se repite
- **Tomas cortas de 4–6 s con varios personajes:** Flow dibuja cada vez una barca, un puente o un lugar un poco distinto → parece
  otro sitio en cada corte (la trajinera, el puente que «desaparece»).
- **Faltaban las tomas puente:** se pasaba de A a C sin B (aparecían a bordo sin subirse; corriendo en el puente sin bajarse;
  Lupe aparecía en otro barco y luego detrás de ellos; la vaca corría para un lado y luego para el otro).
- **Lo que llega no se veía llegar** (el barco de los mariachis, la Catrina).
- **Se descubrían las escenas que faltaban DESPUÉS de gastar créditos.** Unas 20 generaciones de más.
- Fallos técnicos de Flow: dos ratas, Tocino que no sale con 6 fotos, Tocino que se pasa de barco, voces de Flow que se cuelan.

## Cómo se trabaja desde el capítulo 3
1. **Escaleta antes de cualquier prompt.** Claude escribe el vlog como película, toma por toma, y lo revisa con estas preguntas
   antes de mandarlo a Jay: ¿de dónde viene cada personaje? ¿cómo llega al siguiente lugar? ¿lo que aparece se vio llegar?
   ¿la dirección de movimiento sigue igual? ¿el vehículo/lugar es el mismo? Jay da el aval de la escaleta completa.
2. **Tomas largas alternadas: 10 s, 6 s, 10 s, 6 s…** (5 de 10 + 5 de 6 por día = 80 s, lo que dan las 5 cuentas de 16 s).
   - **10 s** = la escena principal de un lugar, con la cámara moviéndose de cara en cara (varios hablan por turnos; modo
     «vídeos silenciosos»; ventanas de tiempo).
   - **6 s** = el puente o el detalle que une con la siguiente (llegar, salir, subir, una reacción, un inserto).
3. **Encadenar con el último cuadro:** Claude saca el ÚLTIMO CUADRO de la toma aprobada y se lo manda a Jay; Jay lo sube como
   primera foto de la toma siguiente y el prompt empieza con «Continue exactly from the reference frame: same place, same
   characters in the same positions». Por eso **las tomas se generan EN ORDEN**, una a la vez.
4. **Misma foto del lugar o vehículo en todas las tomas de esa escena**, posiciones fijas escritas («the pig on the left…»),
   «nobody changes boats/places». Máximo 5 fotos por toma.
5. **Una acción principal por bloque de tiempo**; quien no actúa, quieto y descrito donde está; decir dónde TERMINA cada uno.
6. **Lo que llega se ve llegar:** primero lejos (silueta, sombra, sonido), después cerca.
7. **Armado sin voces** apenas estén todas las tomas (regla del 13-nov) → Jay revisa → voces.
8. **Voces:** el audio de Flow va en CERO en toda toma con voz nuestra y en las tomas largas; las bocas se miden con Whisper
   y con los murmullos de Flow (que también marcan cuándo mueve la boca cada uno).

## Cada vlog se entiende solo (estrategia Gnomo, Jay 14-nov)
- Segundo 0–2: Dizzy con el palo de selfie, la cara pegada al lente, la meta del vlog en una frase.
- En los primeros 10 s, quién es y dónde está («Me quedé atrapado en México…»), sin necesitar el vlog anterior.
- Meta → problema → escalada → remate → «Sígueme pa' no perderte el próximo vlog, mi llave».
- Personajes conocidos (leyendas, dominio público) con un giro de problema de adultos de hoy.
