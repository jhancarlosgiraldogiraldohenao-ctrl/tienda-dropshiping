# Soy Toffee · reglas fijas para Claude

## Al empezar CADA conversación (pedido de Jay, 22-oct-2026)
Antes de responder cualquier otra cosa, a cualquier hora (mañana, mediodía o noche), empieza el primer mensaje con este recordatorio, tal cual y corto:

> 🔔 **Antes de seguir, revisa tus redes:**
> - [ ] **YouTube** (Studio): comentarios nuevos, sobre todo «CALMA»
> - [ ] **Instagram**: comentarios y mensajes
> - [ ] **TikTok**: comentarios y mensajes
>
> Responde hoy mismo cada palabra clave como Toffee, con «soytoffee.store» (el enlace está en el perfil).

Después del recordatorio, sigue con lo que Jay pidió. No lo repitas en los demás mensajes de la misma conversación.

## Cambios grandes en la web: primero vista previa, después publicar (pedido de Jay, 23-oct-2026)
- **Cambio grande** = rediseño o sección nueva, cambios en varias secciones o páginas, muchos textos a la vez, o cualquier cosa que cambie cómo se ve la tienda.
  1. Subirlo a una **copia sin publicar** del tema en vivo (nunca directo al tema en vivo).
  2. Mandarle a Jay el **enlace de vista previa** y **capturas en celular**, con un resumen corto de qué cambia.
  3. Publicar **solo cuando Jay diga «publica»**.
- **Cambio pequeño** (un texto puntual, un error, un dato) se puede hacer directo en vivo, diciéndole qué se cambió.
- Si hay duda de si es grande o pequeño, tratarlo como grande.

## Dónde está todo
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
- **Antes de hablar de la serie, leer `toffee/extravio/`:** `BIBLIA.md` (mundo, reglas, personajes, mundos, temporada, tono), `DECISIONES.md` (canal y negocio) y `CONVERSACION-28-29-OCT.md` (la conversación completa en texto). Mandan sobre los planes viejos del viaje al Polo Norte.
- Fichas de todo lo que Jay genera (personajes, objetos, mundos, logo, voces, sonidos): `toffee/EXTRAVIO-1-IMAGENES.pdf` y `toffee/EXTRAVIO-2-AUDIO.pdf` (`python3 toffee/extravio/fichas.py`; también como páginas web en `toffee/extravio/web/`: imágenes https://claude.ai/artifact/QKJpZJ4GfaMeoj999nXQ2U · audio https://claude.ai/artifact/EuNDN73dwzMmLU8fPCJ5EQ). Imágenes aprobadas en `toffee/refs/extravio/{personajes,objetos,mundos,marca}/`.
- **Ritmo: 1 capítulo diario a las 6 p. m. (Colombia) con 1 de reserva terminado; 2 shorts diarios (12 p. m. y 8 p. m.) del capítulo, los mismos en YouTube Shorts, TikTok e Instagram.**
- **Edición de los capítulos como una serie de TV (pedido de Jay, 29-oct-2026):** sin subtítulos pegados ni títulos encima, sin texto en pantalla. Gancho → logo corto de EXTRAVÍO con su firma sonora (2–3 s) → capítulo con música y efectos → cierre con la invitación a seguir dicha por Toffee (no escrita) → 15–20 s finales de escena tranquila para las pantallas finales de YouTube. Subtítulos solo como archivos .srt en YouTube (español e inglés). Los **shorts sí van con estilo Gnomo Palomo** (subtítulos de 1–3 palabras, título arriba).
- **Tono de Extravío (29-oct-2026, manda sobre la regla vieja de «una grosería por episodio»):** groserías sí, pocas fuertes y nunca en los primeros 10 s, título ni miniatura; parodias y referencias a lo olvidado con dominio público o guiños sin nombre ni diseño idéntico; nada de caras o voces de personas reales ni copias de personajes con dueño (ver `toffee/extravio/BIBLIA.md`).
- La serie no tiene final escrito. Lucho (ratón adicto al queso) reemplaza a Don Turbio. No más tiempo en la web por ahora.

## Entregas en link (pedido de Jay, 29-oct-2026)
- Todo PDF que se le mande a Jay va **también como link** (Artifact) que pueda abrir directo en el navegador, con botones de Copiar en los prompts. El PDF se puede adjuntar además, pero el link es obligatorio.
