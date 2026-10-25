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
- Si la idea no se cumplió, **se repite**. No hay que «arreglarlo» en la edición ni aceptarlo «porque igual funciona».
- Decirle a Jay qué falló, mejorar el prompt para que no vuelva a pasar y actualizar el plan (`toffee/plan-videos/`, `toffee/PLAN-VIDEOS-7-DIAS.pdf`).
- **Subtítulos de la voz: en español, pegados en el video** (cambio decidido el 25-oct-2026; antes eran en inglés). Estilo Gnomo Palomo: 1 a 3 palabras, centrados y sincronizados palabra por palabra. El **inglés va aparte**, como subtítulos .srt en YouTube (y la traducción automática de TikTok/Instagram).
- **Boca sincronizada:** cuando Toffee habla en cámara, la voz de ElevenLabs se ajusta palabra por palabra a la boca de la toma de Flow (o se usa el Voice Changer de ElevenLabs sobre el audio de Flow).
- **Audio de la voz: primero que suene perfecto** (pedido de Jay, 25-oct-2026). Cortar la voz SOLO en silencios reales (comprobar el nivel en cada corte); nunca dentro de una palabra; no estirar ni encoger la voz. La sincronía con la boca se logra moviendo frases enteras, sin forzar.
- **No borrar sonidos propios de la toma** (un «miau», un ladrido, un gesto a la cámara): se dejan con volumen que se oiga y sin zoom que corte la cara.

## Videos del viaje de Toffee: cómo se generan (pedido de Jay, 24-oct-2026)
- **Modelo: siempre Omni 1.1 Flash** (Google Flow). Tomas de 4, 6, 8 o 10 s según el momento; cortes cada 3–5 s como Gnomo Palomo. Si una toma sigue a otra, indicar «usar el último cuadro de la toma X como primer cuadro». Toma aprobada → mejorarla a 1080p en Flow si se puede.
- **Referencias:** `toffee/refs/TOFFEE-viajero.jpg` (gorro + cámara encima) y `toffee/refs/GALLETA-viajero.jpg` (pañoleta, mochila). Galleta es mudo. Personaje que aparece por 2.ª vez → foto propia y voz fija en ElevenLabs.
- **Voz de Toffee:** la de ElevenLabs de Jay (Eleven v4, estabilidad ~75 %, similitud 90 %, idioma Español). Si Toffee habla en cámara, el prompt lleva la frase exacta y Claude reemplaza el audio por el de ElevenLabs.
- **Reglas de prompt para evitar errores** (cada prompt debe cumplirlas):
  - Lente normal: nada de ojo de pez, viñeta ni esquinas oscuras; no se ve ningún celular ni palo de selfie.
  - Nada de vista en primera persona con patas visibles (crea un segundo gato). Toffee siempre visto desde afuera.
  - La cabeza, el gorro y la cámara de Toffee siempre completos dentro del cuadro. Un solo gato y un solo perro.
  - Pólvora solo lejos, afuera; nunca chispas ni explosiones cerca de los animales.
  - Orejeras = capucha acolchada gris tipo balaclava, NUNCA aro, dona, diadema o audífonos.
  - Una sola acción clara por toma; frases cortas; describir quién está a la izquierda o a la derecha cuando hay dos personajes.
- Prompts del vlog en `toffee/viaje/VLOG-XX.md`; estudio de referencia en `toffee/ESTUDIO-CANALES-YOUTUBE.md`.
