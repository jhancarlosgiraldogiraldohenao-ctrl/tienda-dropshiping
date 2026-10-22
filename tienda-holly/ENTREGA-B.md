# Entrega · Diseño B «La tienda de Toffee» (21 y 22-oct-2026)

Hecho con la skill **tienda-marca-personaje**: lo que funciona en las mejores tiendas (Chewy, Farmer's Dog, BARK,
Zesty Paws, Pusheen, Love Nala…) aplicado a Soy Toffee. Se parte del tema en vivo v4
(«Toffee A - Noche acogedora (18-oct v4)», #189657645345), que es el mismo código de este repositorio.

> El tema nuevo **todavía no está en Shopify**. Para subirlo hay que iniciar sesión en Shopify desde esta sesión
> (te pido el enlace de permiso). Se sube como **copia sin publicar**, la revisas en vista previa y se publica solo
> cuando digas «publica».

---

## 0. Cambio del 22-oct: Toffee primero, la tienda después, la temporada como invitada

Por pedido de Jay, la portada deja de ser la página de un solo producto y pasa a ser **la tienda de Toffee**:

1. **Portada con Toffee** (personaje principal): «Si no pasa mi prueba, lo tiro de la mesa», botón «Entrar a la
   tienda» y debajo un enlace pequeño a la temporada (foto de Galleta + «Temporada de pólvora: orejeras para tu
   perro» + la próxima fecha límite).
2. **¿Para quién es?**: círculos Gatos · Perros · Para dormir · Navidad · Pólvora. Cada uno abre la tienda filtrada
   (salen solos de las etiquetas de los productos).
3. **La tiendita de Toffee**: todos los productos en cuadrícula (2 por fila en el celular) con filtros. **Crece sola**:
   cada producto nuevo aparece sin tocar el diseño. Nombre corto, etiqueta, frase y opinión de Toffee de cada uno se
   escriben en *Configuración del tema → Toffee – Fichas de producto* (un producto por línea).
4. **Temporada de pólvora** (Galleta + orejeras) como sección destacada en la mitad de la portada.
5. El equipo · Test de Toffee · Sigue a Toffee · Marrano · Preguntas · Club.
6. **Catálogo (/collections/all)** con el mismo diseño: «Todo lo que aprobé», filtros y tarjetas (antes era la lista
   genérica de Shopify con precios «$79.900,00»).

**Por qué así y no un solo producto de primero:** quien llega de un video sobre las orejeras debe caer **directo en
la ficha de las orejeras** (el enlace que Toffee responde a «Comenta CALMA» va a la ficha, no a la portada). La
portada la ven los que quieren conocer la marca: a ellos se les muestra Toffee y la tienda, y la temporada sigue a
un toque. Así cada temporada nueva solo cambia el enlace pequeño y la sección destacada.

**Pendiente en el panel:** en *Tienda online → Navegación → menú de la cabecera*, cambia el enlace «Tienda» de
`/#aprobado` a `/collections/all`. (Mientras tanto `/#aprobado` lleva a la tiendita de la portada, no se rompe.)

## Fotos que necesito (en orden de importancia)

Mismo estilo de siempre: foto real de iPhone, hogar latino acogedor, nada de 3D ni neón, **sin texto en la imagen**.
Sube como referencia `TOFFEE-ficha.jpg` (y `GALLETA-oficial.jpg` cuando sale Galleta).

**T01 · Portada vertical (celular) · 9:16 (768 × 1376)** — reemplaza la portada actual. *Referencias:* TOFFEE-ficha +
GALLETA-oficial + fotos reales de la cama trineo roja, el disfraz verde y las orejeras.
```
Vertical 9:16. Toffee (an adult British Shorthair cat, solid cream-caramel color in one single tone, very chubby and round, round face with big cheeks, large green eyes with very dilated pupils, wearing a knitted navy blue sleeping cap with a drooping tip and a cream pompom, exactly like the reference image) sits like a serious little shop owner on a small wooden counter of a tiny cozy pet shop at night. Behind him, simple wooden shelves show the products from the references: the RED Christmas sleigh pet bed, the GREEN Christmas-tree cape costume on a tiny hanger, and the DARK GRAY padded dog ear muffs (exact copies). Galleta (the exact dog from the reference: scruffy golden-brown criollo mutt, bushy eyebrows and beard, white chest, navy bandana with golden bone tag) peeks from behind the counter. Warm lamp light, deep navy blue wall. The top 40% of the image is calm empty navy wall (space for text); Toffee and the counter are in the lower half. Real candid photograph taken with an iPhone, natural light, real fur and fabric textures, slight phone-camera grain. NOT 3D, NOT render, NOT CGI, NOT illustration, NOT futuristic, no neon. No text, no letters, no logos, no watermark.
```

**T02 · Portada horizontal (computador) · 16:9 (2000 × 1124)** — la misma escena, con Toffee y el mostrador **a la
derecha** y la mitad izquierda libre (pared azul marino) para el texto. Usa el mismo prompt cambiando la primera
línea por «Horizontal 16:9» y la del espacio por «The left half of the image is calm empty navy wall (space for
text); Toffee, Galleta and the counter are on the right half.»

**T03 · Carrito vacío · cuadrada 1:1** — Toffee sentado junto a un plato vacío, mirando a la cámara ofendido.
```
Square 1:1. Toffee (same description as above, with his navy sleeping cap) sits next to a completely empty ceramic food bowl on a kitchen floor, staring at the camera, deeply offended. Real candid iPhone photo, cozy Latin American home, natural light. NOT 3D, NOT render, NOT illustration, no neon. No text, no letters, no logos, no watermark.
```

**T04 · Página no encontrada (404) · cuadrada 1:1** — Toffee con un pedazo de papel arrugado en la boca, cara de
«yo no fui».
```
Square 1:1. Toffee (same description as above, with his navy sleeping cap) on a desk with a crumpled torn piece of paper in his mouth, looking at the camera with a guilty "it wasn't me" face, scattered paper pieces around. Real candid iPhone photo, cozy home, warm lamp light. NOT 3D, NOT render, NOT illustration, no neon. No text, no letters, no logos, no watermark.
```

**Por cada producto nuevo que entre a la tienda:** 1) foto real del producto sobre fondo crema `#F3E9D8` (de la
tienda del proveedor), 2) una escena con Toffee o Galleta usándolo (4:5 vertical), 3) la guía de tallas si tiene
tallas. Con eso la tarjeta y la ficha salen completas.

Las fotos de las categorías (Gatos, Perros, Para dormir, Navidad, Pólvora) ya están: uso las que tenemos.


---

## 1. Qué cambió el 21-oct (simple)

### Portada: ahora abre con el problema de la temporada
- **Primer pantallazo en el celular:** Galleta con las orejeras y la pólvora en la ventana, el título
  «Que la pólvora no le arruine diciembre *a tu perro*», **un solo botón** «Ver las orejeras · $79.900» y la fecha
  límite justo debajo. Antes abría con el lema y la cama trineo arriba.
- **Tarjetas por problema** (patrón Farmer's Dog/Petco): «Le teme a la pólvora» → orejeras, «Quiere su foto
  navideña» → disfraz, «Duerme en cualquier lado» → cama trineo. Las orejeras van primero.
- **Nueva sección «Las fechas límite de diciembre»**: una fila por noche (velitas, Navidad, Año Nuevo). La fecha que
  ya no alcanza desaparece sola ese mismo día.
- **«Sigue a Toffee»** activado, con TikTok, Instagram y YouTube (@toffee.elgato). Los íconos también salen en el pie.
- Quitadas de la portada (siguen guardadas, desactivadas): la portada vieja, el bloque de temporada (ya es la portada)
  y «La prueba de Toffee». Quedan 11 secciones, igual que en la v4.

### Una sola fuente para las fechas
- Todo sale de **Configuración del tema → Toffee – Fechas y garantía**: días de entrega (10 a 25 hábiles), las fechas
  límite y los festivos. La barra de anuncios, la ficha, las preguntas, la página de Ayuda y el envío de cada producto
  leen de ahí. Se acabó «13 de noviembre» en un lado y «24 días» en otro.
- Fechas puestas (peor caso de 25 días hábiles, festivos de Colombia y 3 días hábiles de margen):

  | Noche | Pide hasta el | Último día posible sin margen |
  |---|---|---|
  | Velitas (7 dic, Colombia) | 26 de octubre | 29 de octubre |
  | Navidad (24 dic) | 13 de noviembre (la de siempre) | 18 de noviembre |
  | Año Nuevo (31 dic) | 20 de noviembre | 24 de noviembre |

  **(sin confirmar)** Son con la promesa actual de «10 a 25 días hábiles». Confirma con TeemDrop los días reales por
  país y, si cambian, solo editas esa lista.
- **La barra de anuncios tiene un solo mensaje** (antes rotaban dos): la próxima fecha límite + envío gratis, con
  enlace a las orejeras. Cambia sola: hoy dice velitas; desde el 27 de octubre dirá Navidad; desde el 14 de noviembre,
  Año Nuevo.
- Las preguntas pueden escribir `[fecha-limite]` (la próxima fecha) o `[fechas]` (todas) y se llenan solas.

### La opinión de Toffee ya no parece una reseña (regla 5, Ley 1480 / SIC)
- Se quitaron **todas las estrellas** (★★★★★) del veredicto en la portada y en las 3 fichas.
- «Probado por Galleta», «Siesta-prueba 14 h» y «Toffee la probó por 14 horas» se cambiaron por notas como
  «Aprobada 💤» y «¿Lo tiré de la mesa? No».
- El bloque ahora se llama **«La opinión de Toffee»** y dice: «Toffee es un personaje creado con IA: esto es su opinión
  de personaje, no una reseña de clientes.» En las tarjetas: «Opinión de Toffee, personaje de IA · no es una reseña
  de clientes».
- La frase de la ficha se firma «— Toffee, personaje de IA».

### Ficha de producto
- Orden: frase de Toffee → **precio** (antes solo estaba dentro del botón) → talla → botón → fecha de entrega → fecha
  límite → garantía → marrano.
- **Garantía con nombre: «Palabra de Toffee»**: si no llega o llega dañado, otro o tu dinero. Va junto al botón, en el
  envío, en las preguntas y en el carrito.

### Carrito
- Bajo el botón de pago: «🛡️ Palabra de Toffee…», «🐷 Con este pedido, $X van al marrano de Toffee» (3 % del
  subtotal, la misma cuenta que hace Flow) y «Pago seguro · Envío gratis».
- Carrito vacío: el botón lleva a las orejeras («Ver las orejeras de Galleta»).

---

## 2. Lo que tienes que hacer tú en el panel (en orden de impacto)

1. **Guía de tallas como foto 3** de las orejeras y del disfraz (*Productos → la foto de la guía → arrástrala al 3.er
   lugar*). Hoy es la última (7.ª) y casi nadie llega hasta ahí.
2. **Reseñas reales con foto:** instala **Judge.me** (plan gratis). Con la primera entrega, pide la reseña por correo.
   Nunca reseñas inventadas; las estrellas aparecen cuando ya haya reseñas.
3. **Correo de carrito abandonado** (*Marketing → Automatizaciones → Carrito abandonado*). Texto en la sección 3.
4. **Oferta CALMA** (la palabra de los videos): crea un código o beneficio llamado **CALMA** en *Descuentos* (por
   ejemplo, envío prioritario o un regalo digital; el margen de 48 % no aguanta descuentos grandes). Cuando exista, lo
   ponemos en la barra y en la ficha. **No lo puse en la tienda** porque un código que no funciona es peor que nada.
5. **Combo orejeras x2** con el ahorro escrito (patrón Zesty «Better Together»): necesita una variante o un descuento
   automático «2 por $X». Dime el precio y lo armo en la ficha.
6. **Placa de identificación** como complemento de las orejeras (la noche de pólvora es cuando más perros se
   pierden). Buscar en TeemDrop y pedir fotos reales al agente antes de venderla.
7. **Revisa que @toffee.elgato exista en TikTok e Instagram** (YouTube sí está). Si alguno no existe todavía, borra el
   enlace en *Configuración del tema → Redes sociales* y en la sección «Sigue a Toffee».
8. **Métodos de pago locales** con dLocal (PSE, Nequi, OXXO) **(sin confirmar)**: pregúntale a dLocal cuáles puedes
   activar. Solo se muestran los que estén activos.

---

## 3. Correos con la voz de Toffee (listos para pegar)

**Carrito abandonado** — *Asunto:* Me quedé dormido encima de tu carrito 😴
> Humano:
> Fui a revisar y tu carrito seguía ahí, tibiecito. Me eché una siesta encima para cuidártelo.
> Tus cosas siguen apartadas: {{ productos }}.
> Ojo con las fechas: {{ la próxima fecha límite }}.
> [Volver a mi carrito]
> — Toffee (personaje de IA). Galleta dice que no hay afán, pero que la pólvora no espera.

**Pedido enviado** — *Asunto:* Galleta ya empacó tu pedido 📦
> ¡Salió! Este es tu número de rastreo: {{ rastreo }}. Llega en 10 a 25 días hábiles.
> Mientras tanto, si compraste las orejeras: empieza a presentárselas apenas lleguen, con premios, unos minutos al
> día. Así la noche de pólvora ya son su cosa favorita.
> — Toffee

**Después de la entrega (7 días)** — *Asunto:* ¿Pasó la prueba de tu peludo?
> Humano, ya llevas unos días con tu pedido. Cuéntame: ¿cómo le fue a {{ nombre de tu mascota }}?
> Si nos mandas una foto y tu reseña (buena o mala, las dos sirven), la respondo yo mismo.
> [Dejar mi reseña]
> — Toffee. Reviso todas, entre siesta y siesta.

---

## 4. Auditoría (checklist de la skill)

| Área | Punto | Antes (v4) | Ahora (B) |
|---|---|---|---|
| A. Primer pantallazo | Personaje + producto estrella + problema + un botón | ⚠️ lema y 2 botones, sin producto | ✅ Galleta + orejeras + pólvora + 1 botón |
| A | Barra con un solo mensaje vigente | ❌ dos mensajes rotando | ✅ uno, con la fecha que sigue |
| B. Inicio | Empieza por el producto que resuelve el problema | ❌ trineo primero | ✅ orejeras primero |
| B | Tarjetas por problema | ❌ | ✅ |
| B | Bloque «Sigue a…» | ❌ desactivado | ✅ (enlaces a confirmar) |
| B | Causa con una sola cifra | ✅ | ✅ |
| B | Club por correo con regalo, casilla sin marcar | ✅ | ✅ |
| C. Ficha | Orden frase → precio → talla → botón → entrega → garantía → causa | ⚠️ sin precio antes de la talla | ✅ |
| C | Galería: 1 en uso, 2 usos, 3 tallas | ⚠️ guía de tallas en el 7.º lugar | ⚠️ pendiente en el panel (punto 1) |
| C | Botón fijo abajo en el celular | ✅ | ✅ |
| C | Opinión del personaje rotulada, sin estrellas | ❌ estrellas y «Probado por Galleta» | ✅ |
| C | Combo con ahorro escrito | ❌ | ❌ pendiente (punto 5) |
| C | Reseñas reales con foto | ❌ (sin ventas aún) | ❌ pendiente (punto 2) |
| D. Carrito | Garantía con nombre junto al botón | ⚠️ sin nombre | ✅ «Palabra de Toffee» |
| D | Cuánto va a la causa con esta compra | ⚠️ solo «3 %» | ✅ en pesos |
| D | Carrito vacío con voz y enlace al producto estrella | ⚠️ enlazaba a la portada | ✅ |
| E. Confianza | Fechas iguales en barra, ficha, FAQ | ❌ 13-nov vs «24 días» | ✅ una sola fuente |
| G. Correos | Carrito abandonado / post-entrega | ❌ | ⚠️ textos listos, falta pegarlos |
| H. Oferta | La palabra del video existe en la tienda | ❌ | ❌ pendiente (punto 4) |
| I. Legal | Retracto, PQR/SIC, Libro, impuestos, datos, IA | ✅ | ✅ |

## 5. Para el técnico
- Secciones nuevas: `tf-portada` (portada de temporada). Snippets nuevos: `tf-corte` (fecha límite / lista),
  `tf-fechas-datos` (JSON para `hl-scripts.js`), `tf-carrito-extra`.
- Ajustes globales nuevos: `tf_dias_min`, `tf_dias_max`, `tf_cortes`, `tf_corte_vencido`, `tf_festivos`,
  `tf_garantia_nombre`, `tf_garantia_texto`. `hl-producto` ya no tiene `dias_min`, `dias_max` ni `fecha_navidad`.
- `hl-scripts.js` → `initFechas`: recalcula en el navegador la próxima fecha y la entrega estimada (con festivos) por
  si la página quedó en caché.
- Tokens `[fecha-limite]` y `[fechas]` en `hl-faq` (respuestas), `tf-bloque` (texto), `hl-producto` (envío) y la barra
  de anuncios.
- `theme check`: sin errores nuevos frente a la v4.
