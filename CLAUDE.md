# Soy Toffee · reglas fijas para Claude

## Al empezar CADA conversación (pedido de Jay, 22-oct-2026)
Antes de responder cualquier otra cosa, a cualquier hora (mañana, mediodía o noche), empieza el primer mensaje con este recordatorio, tal cual y corto:

> 🔔 **Antes de seguir, revisa tus redes:**
> - [ ] **YouTube** (Studio): comentarios nuevos, sobre todo «CALMA»
> - [ ] **Instagram**: comentarios y mensajes
> - [ ] **TikTok**: comentarios y mensajes
>
> Responde hoy mismo cada palabra clave como Toffee (la tienda está cerrada por ahora: no mandar a nadie a soytoffee.store).

Después del recordatorio, sigue con lo que Jay pidió. No lo repitas en los demás mensajes de la misma conversación.

## Cambios grandes en la web: primero vista previa, después publicar (pedido de Jay, 23-oct-2026)
- **Cambio grande** = rediseño o sección nueva, cambios en varias secciones o páginas, muchos textos a la vez, o cualquier cosa que cambie cómo se ve la tienda.
  1. Subirlo a una **copia sin publicar** del tema en vivo (nunca directo al tema en vivo).
  2. Mandarle a Jay el **enlace de vista previa** y **capturas en celular**, con un resumen corto de qué cambia.
  3. Publicar **solo cuando Jay diga «publica»**.
- **Cambio pequeño** (un texto puntual, un error, un dato) se puede hacer directo en vivo, diciéndole qué se cambió.
- Si hay duda de si es grande o pequeño, tratarlo como grande.

## Dónde está todo
- **Tienda cerrada desde el 31-oct-2026; plan nuevo de Jay (1-nov-2026): los capítulos hacen GUIÑOS de productos para mascotas** (aparecen en la serie sin decir «compra»; enlace solo en la descripción). Lista elegida del catálogo de TeemDrop: `toffee/extravio/web/productos-guinos.html` (Artifact) y catálogo completo en `toffee/extravio/TEEMDROP-MASCOTAS.csv`. Antes de montar un producto: Jay revisa el envío a Colombia en TeemDrop y Claude calcula el precio. Ideas digitales guardadas: guía «Diciembre sin miedo» y retrato «Tu mascota en Extravío».
- Tienda: soytoffee.store (Shopify `a1fcei-t6.myshopify.com`). Tema en `tienda-holly/`; estado y decisiones en `tienda-holly/ESTADO.md`.
- Colores: `toffee/COLORIMETRIA.md`. Entregas y pendientes del panel: `tienda-holly/ENTREGA-B.md`.
- Jay no es técnico: explicar en palabras simples, en español, paso a paso.

## Videos de Toffee: si no salió como el prompt, se repite (pedido de Jay, 23-oct-2026)
- Al revisar cada clip que manda Jay, compararlo con la idea del prompt (encuadre, acción, personajes, gorro, producto).
- **Cuando Jay manda videos para revisar (regla para siempre, 27-oct-2026):** no comentar nada mientras los manda; solo analizarlos en silencio (respuesta mínima, p. ej. «✓»). Cuando Jay diga **«listo»**, dar la revisión completa de todos: qué está bien y qué hay que corregir o repetir.
- Si la idea no se cumplió, **se repite**. No hay que «arreglarlo» en la edición ni aceptarlo «porque igual funciona».
- Decirle a Jay qué falló, mejorar el prompt para que no vuelva a pasar y actualizar el plan (`toffee/plan-videos/`, `toffee/PLAN-VIDEOS-7-DIAS.pdf`).
- **Subtítulos de la voz (en los shorts; los capítulos de Extravío van sin texto): en español, pegados en el video** (cambio decidido el 25-oct-2026; antes eran en inglés). Estilo Gnomo Palomo: 1 a 3 palabras, centrados y sincronizados palabra por palabra. El **inglés va aparte**, como subtítulos .srt en YouTube (y la traducción automática de TikTok/Instagram).
- **Boca sincronizada:** cuando Toffee habla en cámara, la voz de ElevenLabs se ajusta palabra por palabra a la boca de la toma de Flow (o se usa el Voice Changer de ElevenLabs sobre el audio de Flow).
- **Audio de la voz: primero que suene perfecto** (pedido de Jay, 25-oct-2026). Cortar la voz SOLO en silencios reales (comprobar el nivel en cada corte); nunca dentro de una palabra; no estirar ni encoger la voz. La sincronía con la boca se logra moviendo frases enteras, sin forzar.
- **No borrar sonidos propios de la toma** (un «miau», un ladrido, un gesto a la cámara): se dejan con volumen que se oiga y sin zoom que corte la cara.

## Videos del viaje de Toffee: cómo se generan (pedido de Jay, 24-oct-2026)
- **Modelo: siempre Omni 1.1 Flash** (Google Flow). Tomas de 4, 6, 8 o 10 s según el momento; cortes cada 3–5 s como Gnomo Palomo. Si una toma sigue a otra, indicar «usar el último cuadro de la toma X como primer cuadro». Toma aprobada → mejorarla a 1080p en Flow si se puede.
- **Referencias:** `toffee/refs/TOFFEE-viajero.jpg` (gorro + cámara encima) y `toffee/refs/GALLETA-viajero.jpg` (pañoleta, mochila). Galleta es mudo. Personaje que aparece por 2.ª vez → foto propia y voz fija en ElevenLabs.
- **Voz de Toffee:** la de ElevenLabs de Jay (Eleven v4, estabilidad 35–45 %, similitud 85 %, idioma Español). Texto con actuación entre corchetes en inglés ([shouting], [whispers], [sighs], [nervous laugh]…) para que suba, baje, grite y respire como Gnomo; generar 2–3 versiones. Primero la voz, después la toma de Flow con la duración de esa voz. Volumen final del video: −14 LUFS. Revisar cada frase transcrita (ElevenLabs puede cambiar palabras: «Yo NO tenía» en vez de «Yo LO tenía»). Si Toffee habla en cámara, el prompt lleva la frase exacta y Claude reemplaza el audio por el de ElevenLabs.
- **Reglas de prompt para evitar errores** (cada prompt debe cumplirlas):
  - Lente normal: nada de ojo de pez, viñeta ni esquinas oscuras; no se ve ningún celular ni palo de selfie.
  - Nada de vista en primera persona con patas visibles (crea un segundo gato). Toffee siempre visto desde afuera.
  - La cabeza, el gorro y la cámara de Toffee siempre completos dentro del cuadro. Un solo gato y un solo perro.
  - Pólvora solo lejos, afuera; nunca chispas ni explosiones cerca de los animales.
  - Orejeras = capucha acolchada gris tipo balaclava, NUNCA aro, dona, diadema o audífonos.
  - Una sola acción clara por toma; frases cortas; describir quién está a la izquierda o a la derecha cuando hay dos personajes.
- Prompts del vlog 1 en `toffee/viaje/VLOG-01.md`; vlogs 2–15 (sección 1) en `toffee/viaje/temporada1/datos.py` → PDF `toffee/VIAJE-ESTUDIO-Y-SECCION-1.pdf` (`python3 toffee/viaje/temporada1/build.py`). Estudio: `toffee/ESTUDIO-GNOMO-Y-LOCO-BLANCO.md` y `toffee/ESTUDIO-CANALES-YOUTUBE.md`.
- **Final de cada episodio (pedido de Jay, 27-oct-2026):** nunca poner días ni fechas («episodio 3 el miércoles», no). Cierre estilo Gnomo: «Sígueme para no perderte el próximo episodio».
- **Continuidad de diálogos:** cada frase tiene que responder a algo que ya se dijo o se vio (si Toffee dice «¿Monstruos?», alguien tiene que haber nombrado monstruos antes). Revisar el guion completo de cada episodio antes de entregar prompts.
- Cada vlog trae una toma GANCHO que va primero en la edición. Nada de personajes famosos con dueño (Disney, Warner…): usar dominio público, leyendas latinas o guiños sin nombre.
- **Sección 1 versión 2 (27-oct-2026, vigente):** `toffee/viaje/temporada1/datos_v2.py` → `toffee/VIAJE-SECCION-1-v2.pdf` (`python3 toffee/viaje/temporada1/build_v2.py`). Versión 2.1: un episodio día de por medio y un video de viralización (formato B) en cada día intermedio; comerciales (C) y fotos como segunda publicación opcional. Calendario día por día en `DIAS`. Cada episodio: conflicto + recompensa; cada toma con una función (inicio, desarrollo, obstáculo, recompensa, continuación).
- **Plan vigente desde el 28-oct-2026: YouTube primero** (capítulos largos de 3–5 min + 2 Shorts diarios; los mismos shorts van a TikTok e Instagram hasta decidir el día 30). Biblia de la serie, formatos, calendario de capítulos y medición en `toffee/PLAN-CANAL-YOUTUBE.md`. Toffee además quiere hacerse famoso en secreto; el Diario de Galleta es serie fija.
- **Capítulos largos de YouTube:** uno por archivo en `toffee/viaje/capitulos/capNN.py` → `web/capitulo-NN.html` (Artifact) y `CAPITULO-NN.md` (`python3 toffee/viaje/capitulos/cap01.py`). El capítulo 1 (escrito desde cero el 28-oct-2026) presenta a Don Turbio como tercer personaje fijo (el provocador). **Formato (29-oct-2026):** los capítulos se generan en **16:9 horizontal** (personaje principal cerca del centro); los shorts en 9:16 se recortan de las tomas de un personaje y las tomas con dos personajes o planos abiertos se generan también en 9:16. El editor exporta el capítulo a 1920×1080.
- **Personalidades:** Toffee = antihéroe orgulloso y sarcástico con buen corazón (saludo «A ver, mis desgraciados…»); Galleta = mudo, impulsivo, curioso, a veces el más listo, con 7 expresiones fijas. Humor irreverente sí; humillar personas o grupos, o burlarse del sufrimiento animal, no. Máximo una grosería por episodio, en voz en off.
- **Comerciales:** producto real al final, #publicidad, sin promesas no comprobables (orejeras: nunca «protegen la audición» ni «eliminan el ruido»). Medición semanal en `toffee/MEDICION-SEMANAL.csv`.

## Extravío: la serie de YouTube (decidido por Jay el 29-oct-2026)
- **Cambio del 3-nov-2026 (versión 3): el protagonista es Dizzy (antes Lucho; se descartaron Rocco, Brayan y Toffee), una rata ñera «de Colombia» (gorra plana con la cámara encima, cadena con una tapa de dije, medias con chanclas; saludo «¿Quiubo pues, mis ratas?», cierre «…mi llave»), y Extravío es una Colombia mágica con todos sus paisajes; hay viajes por Colombia y por el mundo.** Antes de hablar de la serie, leer `toffee/extravio/BIBLIA-EXTRAVIO.md` (mundo, reglas, mapa, viajes, personajes, formatos, voces, primeros vlogs) y `toffee/extravio/PROTAGONISTA-DIZZY.html` (ficha de Dizzy); estudio base: `toffee/ESTUDIO-GNOMO-PALOMO.html`; estudio de Yvan The Creator («Yván y Lolo»): `toffee/ESTUDIO-YVAN-Y-LOLO.md`. Fijos: Doña Gertrudis (abuela gallina finquera, segunda protagonista), Bartolo (mula terca) y Tocino (marrano rockero, mejor amigo). La plata son tapas de gaseosa; la magia es «perico» (polvo de café mágico, guiño de doble sentido; Jay pidió cocaína y se le explicó el riesgo en YouTube). Prompts de imagen y voz de los personajes: `toffee/extravio/PROMPTS-PERSONAJES.md` (link https://claude.ai/artifact/4y4iD1cfR2MUD5NpHME65N); Tocino es gringo y le dicen «el Pinche Gringo». Links: biblia https://claude.ai/artifact/XfNwaZPaaLBFkwyez7iG9M · ficha https://claude.ai/artifact/DHBUCyAuPhChT941x9P4FM. Lo que digan las reglas de abajo sobre Lucho, Rocco, Brayan, Toffee, la temporada de la llave, La Gran Polilla y el formato horizontal queda reemplazado por la biblia nueva. `BIBLIA.md` quedó archivada; `DECISIONES.md` y `CONVERSACION-28-29-OCT.md` son historia.
- Fichas de todo lo que Jay genera (personajes, objetos, mundos, logo, voces, sonidos): `toffee/EXTRAVIO-1-IMAGENES.pdf` y `toffee/EXTRAVIO-2-AUDIO.pdf` (`python3 toffee/extravio/fichas.py`; también como páginas web en `toffee/extravio/web/`: imágenes https://claude.ai/artifact/QKJpZJ4GfaMeoj999nXQ2U · audio https://claude.ai/artifact/EuNDN73dwzMmLU8fPCJ5EQ). Imágenes aprobadas en `toffee/refs/extravio/{personajes,objetos,mundos,marca}/`.
- **Ritmo: 1 capítulo diario a las 6 p. m. (Colombia) con 1 de reserva terminado; 2 shorts diarios (12 p. m. y 8 p. m.) del capítulo, los mismos en YouTube Shorts, TikTok e Instagram.**
- **Edición de los capítulos como una serie de TV (pedido de Jay, 29-oct-2026; lo de «sin subtítulos ni texto» quedó reemplazado el 3-nov-2026: ahora van subtítulos estilo Gnomo en todo, ver «Formato YouTube»):** sin títulos encima. Gancho → **título como Gnomo, sin logo ni banner (decisión de Jay, 4-nov-2026): «EXTRAVÍO · VLOG 01» en letras pequeñas sobre la primera toma aérea del mundo** (el logo viejo con llaves ya no se usa) → capítulo con música y efectos → cierre con la invitación a seguir dicha por Toffee (no escrita) → 15–20 s finales de escena tranquila para las pantallas finales de YouTube. Subtítulos solo como archivos .srt en YouTube (español e inglés). Los **shorts sí van con estilo Gnomo Palomo** (subtítulos de 1–3 palabras, título arriba).
- **Tono de Extravío (29-oct-2026, manda sobre la regla vieja de «una grosería por episodio»):** groserías sí, pocas fuertes y nunca en los primeros 10 s, título ni miniatura; parodias y referencias a lo olvidado con dominio público o guiños sin nombre ni diseño idéntico; nada de caras o voces de personas reales ni copias de personajes con dueño (ver `toffee/extravio/BIBLIA.md`).
- **Capítulos de Extravío:** `toffee/extravio/capitulos/exNN.py` (base común en `base.py`) → `web/capitulo-NN.html` (Artifact). Los viejos de `toffee/viaje/capitulos/` (Don Turbio, Polo Norte) quedan descartados.
- La serie no tiene final escrito. Lucho (ratón adicto al queso) reemplaza a Don Turbio. No más tiempo en la web por ahora.
- **Capítulo 1 aprobado por Jay el 31-oct-2026 (5:38). ANTES de escribir prompts o editar cualquier capítulo nuevo, leer `toffee/extravio/MANUAL-PRODUCCION.md`** (orden de trabajo, reglas fijas de prompts, tabla de errores ya cometidos, voces, edición y revisión obligatoria) , `toffee/extravio/ESTUDIO-PLANOS.md` y `toffee/extravio/ESTUDIO-EDICION-GNOMO.md` (cortes, cómo esconder la boca, letras; 4-nov-2026). Pedido de Jay: prompts optimizados y sin errores técnicos a la primera, para no gastar créditos ni tiempo; aprender de cada capítulo y anotar los errores nuevos en el manual.
- **Lo que manda desde el capítulo 1 (reemplaza reglas viejas de arriba):** voz final SIEMPRE de ElevenLabs (Flow solo da la boca y el ritmo; Claude manda el texto con ritmo medido y pega la voz con `toffee/extravio/editor/pegar.py`); música solo por momentos y efectos de reacción en chistes y acciones (cambio de Jay, 1-nov-2026; ver el manual); ambiente por escena bajo las voces; fundidos cortos entre tomas; tomas puente entre lugares; un solo personaje habla por toma; el queso de Lucho se nombra UNA vez; nada de texto en pantalla ni en letreros. Editor base: `toffee/extravio/editor/ed01p.py`.

## Extravío: orden de trabajo por partes (pedido de Jay, 3-nov-2026)
Se trabaja una parte a la vez. **Jay avisa «parte N lista»** antes de seguir con la siguiente; no adelantar partes.
1. **Imágenes de los personajes** de los primeros capítulos (prompts en `toffee/extravio/PROMPTS-PERSONAJES.md`). ✅ Lista el 3-nov-2026: DIZZY, GERTRUDIS, BARTOLO, TOCINO, CUCA y TUERTO en `toffee/refs/extravio/personajes/`.
2. ✅ Aprobada el 3-nov-2026 (v3). **La historia del capítulo 1** (de qué trata; propuesta en `toffee/extravio/serie/CAP01-HISTORIA.md`, link https://claude.ai/artifact/ASdqUEhnZVok6NvuSw2XRP), copiando la estrategia y la forma de contar de Gnomo Palomo (`toffee/ESTUDIO-GNOMO-PALOMO.html`). Jay da el aval.
3. **Imágenes de los lugares** que pide esa historia (prompts del cap. 1 en `toffee/extravio/serie/CAP01-LUGARES.md`). ✅ Lista el 4-nov-2026 (lugares en `toffee/refs/extravio/lugares/`, vertical; horizontales en `horizontal/`).
4. ✅ Aprobado el 4-nov-2026. **El guion y la estructura del video** (tomas, diálogos, tiempos; todavía no los prompts de video). Cap. 1: `toffee/extravio/serie/cap01_guion.py` → `CAP01-GUION.md`.
5. **Voces, efectos de sonido y música** que pida el guion (Jay los genera). Voces del cap. 1: `toffee/extravio/serie/CAP01-VOCES.md`. **Sonidos: biblioteca fija `toffee/extravio/sonidos/` (LEEME.md); reusar siempre, pedir solo lo que falte.** ✅ Lista el 4-nov-2026.
6. **Los prompts de video** (Flow), toma por toma.

**Formato YouTube (pedido de Jay, 3-nov-2026):** el objetivo es el canal de YouTube. Cada capítulo es una historia partida en dos reels (parte 1 de 1:30–2:00 el día 1, termina en suspenso; parte 2 el día 2, arranca con la respuesta; cada una ≤ 3 min para Shorts) que se pegan en el video largo de YouTube (3–10 min) el día 2, como la Fábrica de Santa de Gnomo. Usar canciones propias y efectos (Jay tiene con qué generarlos). **Subtítulos (decisión de Jay, 3-nov-2026, reemplaza «sin texto en pantalla»): se copia a Gnomo Palomo; subtítulos pegados en TODO (shorts y video largo de YouTube): letras blancas en negrita con borde negro, pequeñas, centradas, pocas palabras, palabras clave en color.** Las frases en inglés de Tocino van con su traducción en el subtítulo. **Formato de las tomas (decisión de Jay, 4-nov-2026): TODO en vertical 9:16, como Gnomo** (shorts y video largo de YouTube iguales; nada de generar en 16:9 y recortar, porque el recorte queda borroso). Las imágenes de lugares en 16:9 sirven como referencia.

## Memoria de Extravío (pedido de Jay, 5-nov-2026)
- **ANTES de cualquier prompt, voz o edición, leer toda la carpeta `toffee/extravio/memoria/`** (orden de trabajo, prompts de Flow, voces y bocas, edición, errores, revisión). Cada error nuevo se anota ahí el mismo día. Objetivo: no gastar créditos de más.
- **Secciones de dos partes:** cada capítulo son 2 partes (máx. 3:00 cada una); Jay hace las dos y al día siguiente sube. De cada sección salen 4 shorts/reels/TikToks. Al terminar, Claude ayuda con YouTube, Instagram y TikTok.
- **Orden nuevo:** prompts de Flow → tomas → Claude mide la boca → textos de voz con ese ritmo → voces → edición. Nunca voces antes que las tomas.
- Parte 2 del capítulo 1: prompts en `toffee/extravio/serie/CAP01-FLOW-P2.md` (47 generaciones, `P2` en `cap01_flow.py`), link https://claude.ai/artifact/6xqFZ4eWWYVSe8zwgRcVPa. Reusadas: 81=G37, 90=G12 con atardecer; 103 = G103 nueva (AEREA-FINCA-NOCHE) + inicio de G98.
- Parte 2 del capítulo 1 armada el 5-nov-2026 (v4: recuento completo sobre la aérea y visor de cámara en la visión: 2:57): editor `toffee/extravio/editor/ed_dizzy01p2.py` → `toffee/videos-editados/EXTRAVIO-DIZZY-CAP01-P2.mp4`; voces en `serie/voces-cap01/p2/` (ELEGIDAS.json), textos en `serie/cap01_voces_p2.py`, bocas medidas en `serie/cap01_bocas_p2.json`.
- **Capítulo 1 TERMINADO (5-nov-2026):** parte 2 aprobada → `toffee/videos-editados/EXTRAVIO-DIZZY-CAP01-P2-FINAL.mp4` (2:57, etiqueta `cap01-parte2-final`). Recursos para reusar: `toffee/extravio/reusables/LEEME.md`. Próximo capítulo: más dinamismo (3–4 fotos por lugar, ángulos variados).
- Parte 1 del capítulo 1 aprobada el 5-nov-2026: `toffee/videos-editados/EXTRAVIO-DIZZY-CAP01-P1-FINAL.mp4` (2:55, etiqueta `cap01-parte1-final`). Subtítulos en y = 1400.

## Claude Studio (editor de Jay, 4-nov-2026)
- Link: https://claude.ai/artifact/Rp5qnwNvumrHP12AFkbkkB · cómo funciona: `toffee/extravio/studio/LEEME.md`. Jay mueve voces, volumen y silencios; cuando dice «finalizar» (o hay tareas «pendiente» en `mensajes`), Claude lee la base, escribe `ajustes.json` y renderiza.

## Entregas en link (pedido de Jay, 29-oct-2026)
- **Prompts nuevos o cambiados: SIEMPRE en el chat, cada uno en su bloque para copiar y pegar** (pedido de Jay, 29-oct-2026). No basta con decir «está en el link».
- Todo PDF que se le mande a Jay va **también como link** (Artifact) que pueda abrir directo en el navegador, con botones de Copiar en los prompts. El PDF se puede adjuntar además, pero el link es obligatorio.
