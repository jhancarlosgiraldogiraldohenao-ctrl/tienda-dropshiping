# Prompt maestro para la skill de tienda · Soy Toffee (v1, 18-oct-2026)

**Cómo usarlo:** copia todo lo que está entre `=== INICIO DEL PROMPT ===` y `=== FIN DEL PROMPT ===` y pégalo en la
skill de creación de tiendas (por ejemplo `tienda-shopify-v2`), como instrucciones o como primer mensaje.
Antes, llena los datos que están entre [CORCHETES] en la sección 0 (si no los llenas, la skill te los va a pedir).

Está basado en el análisis de `toffee/ANALISIS-WEBS-TOP-MASCOTAS.md` (41 marcas top de mascotas y de personajes,
leyes de Colombia, México, Chile y Perú, y comercio con agentes de IA en 2026).

=== INICIO DEL PROMPT ===

# Misión

Vas a rediseñar y completar mi tienda Shopify **Soy Toffee** (soytoffee.store), del nicho de mascotas (gatos y
perros pequeños). La "dueña" de la tienda es un personaje de IA que yo creé: **Toffee, un gato**. Quiero que quede a
la altura de las mejores marcas de mascotas del mundo (The Farmer's Dog, Ollie, Smalls, Tuft + Paw, Paw.com, Wild One,
BARK) y de las mejores marcas-personaje (Pusheen, Jellycat, Meowingtons, Love Nala), pero hecha para Latinoamérica
y cumpliendo la ley de cada país donde vendo.

Hazlo todo tú: lee la tienda y los productos, construye, sube y muéstrame la vista previa. Yo no soy técnico:
explícame en palabras simples qué hiciste y qué necesito hacer yo en el panel.

---

## 0. Datos que necesitas (pídemelos si faltan; NUNCA los inventes)

- Nombre legal del vendedor: [NOMBRE COMPLETO O RAZÓN SOCIAL]
- Cédula o NIT: [NÚMERO]
- Dirección de notificación: [DIRECCIÓN, CIUDAD, COLOMBIA]
- Correo de atención: [CORREO]
- WhatsApp de atención: [NÚMERO CON +57]
- Redes: TikTok e Instagram @toffee.elgato (confírmame si ya están creadas)
- Variante de diseño: **A "Noche acogedora"** (recomendada) o **B "Futurista suave"** (ver sección 2). Si no te
  digo nada, usa la A.

---

## 1. Contexto de la marca (no lo cambies)

**Toffee:** gato British Shorthair adulto de IA (realista, no caricatura), color crema-caramelo de un solo tono, muy
gordito y redondo, cara redondísima con cachetes, ojos verdes grandes con pupilas muy dilatadas. Siempre lleva un
**gorro de dormir tejido azul marino con pompón crema**. Personalidad: tierno, dramático, glotón, dormilón y se cree
un empresario serio. Fórmula: "se ve como un peluche, actúa como un drama".

**Historia:** Toffee probó todas las camitas, cobijas y juguetes de la casa y todos le parecieron horribles. Cansado
de que a los michis y perritos les vendan cosas incómodas, abrió su propia tienda. **Su regla: "Si no pasa mi
prueba, lo tiro de la mesa." 😾** Es el jefe más tierno y más flojo del mundo: se duerme en las reuniones, se come
las galletas del inventario y le tiene pánico a los lunes y a la aspiradora.

**Galleta:** perro criollo de unos 12 kg, flaco y patilargo, color galleta con pecho y patitas blancas, pelo de
alambre despeinado, orejas caídas, barbita, ojos cafés nerviosos, pañoleta azul marino con placa dorada en forma de
hueso. Toffee lo rescató de la calle y ahora es su empleado. Miedoso, torpe, leal y comelón; le tiene pánico a la
pólvora, a la aspiradora y al cartero.

**Propuesta de valor:** "Todo en mi tienda está probado y aprobado por Toffee." Sello oficial: **"Aprobado por
Toffee 💤"**. Fans: **Toffeelovers**. Palabra para comentar en redes: **TOFFEE**.

**El marrano de Toffee:** el 3 % de cada venta va a un marrano (alcancía) para ayudar a peludos de la calle. La
sección `tf-marrano` lee el metacampo de tienda `custom.marrano` (lo actualiza Shopify Flow con cada pedido pagado).
Cuando se llena, se dona y se publica el comprobante. **No lo rompas.**

**Operación:** dropshipping con TeemDrop, sin muestras. Envío gratis con rastreo de **10 a 25 días hábiles**. Países:
**Colombia, México, Chile y Perú**. Se cobra en **COP** con dLocal Go (tarjetas Visa, Mastercard, Amex, Discover) y el
tema muestra "≈ $X MXN/CLP/PEN · se cobra en COP" (snippet `tf-precio-local`). **No cambies precios, productos,
envíos ni pagos sin preguntarme.**

**Tema actual:** el código está en la carpeta `tienda-holly/` del repositorio (secciones `hl-*` y `tf-*`). El tema
en vivo es "Toffee (vista previa)" #189551870241. Lee `tienda-holly/ESTADO.md` y `toffee/TOFFEE-BIBLIA.md` antes de
empezar.

---

## 2. Sistema de marca

### 2.1 Por qué cambia el color

Analicé 41 marcas top: **ninguna marca de mascotas usa fondo oscuro con neón como base**. La fórmula ganadora es
**fondo crema + un color ancla profundo + un color vivo solo para el botón**, y el ancla más repetida es el **azul
marino**. Toffee ya tiene esa paleta en su cuerpo: pompón crema, gorro marino, pelaje caramelo y ojos verdes.

### 2.2 Paleta A "Noche acogedora" (recomendada)

Créala como variables CSS en `:root` y úsalas en TODAS las secciones (nada de colores sueltos en el código):

```css
:root {
  --tf-crema: #FBF6EE;          /* fondo principal (pompón) */
  --tf-crema-2: #F3E9D8;        /* secciones alternas y fondo de fotos de estudio */
  --tf-marino: #16213E;         /* ancla: cabecera, portada, pie, titulares (gorro) */
  --tf-marino-noche: #0F1830;   /* degradados de noche */
  --tf-caramelo: #E0954F;       /* BOTÓN PRINCIPAL, siempre con texto marino (6,5:1) */
  --tf-caramelo-hover: #C8834A;
  --tf-caramelo-hondo: #8F5527; /* enlaces y acentos de texto sobre crema (5,6:1) */
  --tf-verde: #4F6E43;          /* sello "Aprobado", checks ✓ (ojos) */
  --tf-verde-suave: #E3EBDC;    /* fondo de chips de "aprobado" */
  --tf-rosa: #F2B8B0;           /* marrano y detalles tiernos */
  --tf-dorado: #FFD27A;         /* estrellas y destacados sobre marino (12:1) */
  --tf-texto: #2B2118;          /* texto principal (cacao) */
  --tf-texto-suave: #6E5F56;    /* texto secundario (5,7:1 sobre crema) */
  --tf-linea: rgba(22, 33, 62, 0.12);
  --tf-sombra: 0 14px 40px -18px rgba(22, 33, 62, 0.35);
}
```

Reglas de uso:
- Proporción: **60 % crema · 25 % marino · 10 % caramelo · 5 % verde/rosa/dorado**.
- **El caramelo es solo para la acción principal** (comprar, agregar al carrito, ver producto). Los botones
  secundarios van con borde marino y fondo transparente.
- Portada (hero), cabecera, sección "Toffee HQ" y pie: fondo **marino** con texto crema (ambiente de noche y siesta).
- Contenido, catálogo, producto, FAQ y legales: fondo **crema** con texto cacao.
- Nunca texto gris claro sobre azul oscuro ni texto caramelo claro sobre crema. Todo debe pasar contraste WCAG AA
  (4,5:1 en texto normal).

### 2.3 Paleta B "Futurista suave" (solo si yo la elijo)

Mantiene la noche del tema actual pero con orden de marca top: fondo `#0F1830`, tarjetas `#16213E`, texto
`#FBF6EE`, texto secundario `#C9CEE3` (no `#9AA3C8`), botón principal sólido `#E0954F` con texto `#0F1830` (sin
degradado arcoíris). El neón (rosa `#FF5FA2`, cian `#4FE3FF`) solo como brillo decorativo en la portada y en "Toffee
HQ", nunca en botones ni textos. Las fichas de producto y las legales igual van sobre crema `#FBF6EE` para que el
producto se vea real.

### 2.4 Tipografía

- Titulares: **Fraunces** (Google Fonts) peso 600-800, con eje SOFT alto: seria pero tierna, como Toffee.
- Texto y precios: **DM Sans** 400 / 500 / 700 (números tabulares en precios).
- Notas de Toffee (opcional): **Caveat** 600, solo en frases cortas tipo "Nota de Toffee".
- Sube las fuentes como archivos woff2 al tema (solo caracteres latinos) con `font-display: swap`. Máximo 2
  familias cargadas en la primera pantalla.
- Tamaños en celular: titular de portada 40-44 px, H2 28-32 px, texto 16-17 px, botones 17 px en negrita.

### 2.5 Formas, íconos y detalles

- Botones tipo píldora (`border-radius: 999px`), alto mínimo 52 px en celular, ancho completo en móvil.
- Tarjetas y fotos con bordes de 20-24 px y la sombra `--tf-sombra`.
- Íconos de línea redondeada (grosor 1,75 px): patita, zZz, caja, escudo, camión, corazón.
- **Sello "Aprobado por Toffee 💤"** en SVG (sin texto quemado en imagen: texto en HTML sobre el SVG): círculo
  marino, centro caramelo, carita de Toffee con gorro y "zZz". Va en tarjetas de producto, página de producto y
  correos. Existe también un sello "Rechazado 😾" solo para la comparativa y el contenido de humor.
- Un detalle de marca repetido: la **punta caída del gorro con pompón** como separador o como esquina de tarjetas.

### 2.6 Fotografía: dos mundos que no se mezclan

1. **Producto real** (manda en la galería): fondo liso crema `#F3E9D8`, luz suave de estudio, producto al ~70 % del
   cuadro, formato 4:5. **La primera foto de cada producto siempre es el producto real y fiel** (forma, color,
   bordados, tallas).
2. **Escenas de Toffee y Galleta** (IA realista en un hogar latino, luz cálida): van en la galería después de las
   fotos reales y en las secciones. Cada escena lleva un chip pequeño en HTML: **"Escena creada con IA"**.
- Nada de neón ni 3D en fotos de producto.
- Nunca texto quemado dentro de las fotos: todo texto va en HTML encima o al lado.
- Si necesitas fotos nuevas, escríbeme los prompts para Google Flow con la descripción oficial de Toffee (en inglés):
  `the chubby round cream-caramel British Shorthair cat from the reference (solid color, no stripes), big round green eyes with very dilated pupils, wearing a navy blue knitted nightcap with a drooping tip and a cream pompom`
  y dime qué foto de referencia subir (`toffee/TOFFEE-ficha.jpg`, `toffee/refs/GALLETA-oficial.jpg`, fotos de
  `toffee/refs/productos/`).

### 2.7 Voz y tono

- Español neutro latino, tuteo ("tú"). Palabras que entienden en los 4 países: "peludos", "michis", "perritos".
- **Toffee habla en primera persona** en: portada, sello, "Notas de Toffee", comparativa, carrito vacío, 404,
  agotado, ventanas de correo, correos y página de gracias.
- **La información importante va en voz clara y neutra, sin chistes que confundan:** precio, tallas, envío, plazos,
  pagos, garantía, devoluciones y legales.
- Humor de Toffee: drama exagerado + flojera + "empresario serio". Nunca burlarse del cliente ni de otras marcas
  por su nombre.
- Léxico de marca: Toffeelovers · Aprobado por Toffee · la prueba de Toffee · la siesta-prueba · el marrano ·
  "humano" (así llama Toffee a los clientes) · "lo tiro de la mesa" · michi-aprobado · miau-ravilloso.

Microcopy listo para usar (ajústalo si hace falta):
- Carrito vacío: "Tu carrito está más vacío que mi plato a las 6 a. m. 😾" + botón "Ver lo que aprobé".
- 404: "Esta página me la comí. Perdón, humano." + botón "Volver a la tienda".
- Agotado: "Se acabó. Galleta está empacando más (lento, pero con amor)."
- Gracias por tu compra: "¡Pedido recibido! Ya le avisé a Galleta para que lo cuide hasta que llegue. Y un 3 % ya
  cayó en mi marrano 🐷."
- Error de correo: "Ese correo no me cuadra, humano. ¿Lo revisas?"
- Ventana de correo: "Humano, déjame tu correo y te mando un regalo (no, no es una bola de pelos)."
- Botón principal en producto: "Agregar al carrito · $79.900" (claro primero, chiste después).

---

## 3. Arquitectura del sitio

**Menú principal (máximo 5):** Tienda (catálogo "Aprobado por Toffee") · Test de Toffee · El marrano · Conoce a
Toffee · Ayuda (FAQ + contacto).

**Páginas que deben existir:**
1. Portada.
2. Páginas de producto (una plantilla por producto, como hoy: `product.trineo`, `product.disfraz`,
   `product.orejeras`).
3. Catálogo "Aprobado por Toffee".
4. **La historia de Toffee** (Quiénes somos).
5. **Test de Toffee** (quiz).
6. El marrano de Toffee (ya existe: `page.marrano`).
7. Ayuda: preguntas frecuentes + contacto (WhatsApp, correo, formulario).
8. **Rastrea tu pedido** (enlace a la página de pedidos de Shopify o app de rastreo; textos con voz de Galleta).
9. Legales (sección 9).
10. **Contenido con IA** (transparencia, sección 10).

---

## 4. Portada (orden, contenido y objetivo de cada sección)

Cada sección debe ser editable desde el editor de temas (textos, fotos, colores, botones y ocultar/mostrar).

1. **Barra de anuncio rotativa:** "🎄 Pide antes del [fecha real] y llega antes de Navidad" · "🐷 El 3 % de cada
   venta va al marrano" · "🚚 Envío gratis con rastreo a Colombia, México, Chile y Perú". La fecha de Navidad
   tiene que salir de los días reales de envío (ya existe la lógica: no la cambies).
2. **Cabecera** marina: logo Soy Toffee (avatar de Toffee + palabra), menú, carrito. En celular: menú hamburguesa y
   carrito visibles.
3. **Portada (hero)** fondo marino: Toffee grande (foto de noche acogedora), chip "Tienda para gatos y perros 🐾",
   titular **"Si no pasa mi prueba, lo tiro de la mesa."** (con "lo tiro de la mesa" en caramelo), subtítulo
   "Soy Toffee: gato, jefe y probador oficial. Todo lo que llega a mi tienda pasa primero por mis patitas.", botón
   caramelo "Ver lo que aprobé" y botón secundario "Conoce a Toffee". Debajo: banderas de los 4 países, sello
   "Aprobado por Toffee" y un chip pequeño "Toffee es un personaje de IA · sus siestas son reales".
4. **Cinta de confianza** (marquesina lenta, crema-2): Envío gratis con rastreo · Pago seguro con tarjeta · Si no te
   llega, te devolvemos tu dinero · 3 % para peludos de la calle · Aprobado por Toffee 💤.
5. **"Aprobado por Toffee"** (catálogo, fondo crema): tarjetas de los productos con foto (escena de Toffee/Galleta
   con el producto), etiqueta ("Favorito de Toffee", "El más viral", "Para la pólvora"), nombre, frase corta del
   veredicto de Toffee, **calificación de Toffee** (Comodidad, Siesta-prueba, ¿Lo tiró de la mesa? No), precio +
   aproximado en moneda local, botón "Comprar ahora".
6. **"La prueba de Toffee"** (3 pasos, como el "How your plan works" de The Farmer's Dog): 1) Lo huelo y lo
   inspecciono. 2) Le hago la siesta-prueba (mínimo 3 horas). 3) Si me gusta, lo apruebo. Si no… lo tiro de la mesa.
   Cierra con: "Por eso en mi tienda hay poquitas cosas: solo las que aprobé."
7. **Temporada (hoy: Navidad y pólvora):** bloque emocional con Galleta y las orejeras: "Galleta le tenía pánico a la
   pólvora. Este diciembre lo pasa tranquilo." + botón al producto. Debe poder cambiarse fácil a otra temporada.
8. **Test de Toffee** (entrada al quiz): "¿Qué aprobaría Toffee para tu peludo? Responde 4 preguntas y te digo qué y
   en qué talla." + botón.
9. **El marrano de Toffee** (`tf-marrano`, ya existe): barra de progreso, mensaje de Toffee e historial con
   comprobantes. Usa la paleta nueva (rosa marrano + marino).
10. **Conoce al jefe** (`tf-toffee`) y **Y yo soy Galleta** (segunda instancia): foto, historia corta, regla de
    Toffee, enlace a "La historia de Toffee".
11. **Toffee en redes:** carrusel de videos o portadas de TikTok/Reels (enlaces o insertados ligeros que carguen solo
    al tocar). Cifras de seguidores o vistas **solo si son reales**; si no hay, "Sígueme en @toffee.elgato".
12. **Reseñas reales** (se oculta sola si no hay reseñas). Nunca inventar, copiar ni generar reseñas.
13. **Comparativa:** "Aprobado por Toffee vs. lo que venden en cualquier lado" (tela, acabados, tallas, envío con
    rastreo, garantía, 3 % al marrano). Sin nombrar marcas.
14. **Compra tranquilo** (`hl-seguro`): pago seguro, envío con rastreo, retracto y garantía, contacto humano por
    WhatsApp.
15. **Preguntas frecuentes** (`hl-faq`): envíos por país y plazos, impuestos de importación, tallas, pagos, cambios
    y devoluciones, "¿Toffee es real?", el marrano.
16. **Club Toffeelovers** (captura de correo): "Únete a los Toffeelovers y te mando mi regalo: fondos de pantalla y
    stickers de Toffee y Galleta." Casilla de autorización de datos **sin marcar** con enlace a la política.
17. **Cierre** (`hl-cierre`): Toffee dormido + "Este año, que también sea su Navidad" + botón.
18. **Pie de página** marino (sección 9.2).

---

## 5. Página de producto (la que más vende: aquí llegan los anuncios)

Arriba del todo (lo primero que se ve en el celular):
1. Galería: **foto 1 = producto real**, luego la escena de Toffee/Galleta que coincide con el video del anuncio,
   detalles, guía de tallas (en HTML si se puede, no solo imagen), escena de uso. Deslizable en celular.
2. Sello "Aprobado por Toffee" + nombre claro con beneficio (ej.: "Orejeras anti ruido para perros · versión
   engrosada").
3. Frase de Toffee de una línea ("Galleta las usó en Año Nuevo y durmió como yo un domingo.").
4. Precio en COP + aproximado en moneda local (`tf-precio-local`) + precio tachado **solo si es real**.
5. Selector de talla/color en botones grandes (píldoras) + "¿No sabes tu talla?" que abre la guía o el test.
6. Botón caramelo "Agregar al carrito · $precio" + "Comprar ahora" (directo al pago).
7. Fecha estimada de entrega real (ya existe) + cuenta regresiva a la fecha límite de Navidad (ya existe).
8. Logos de tarjetas y "Pago 100 % seguro con tarjeta".
9. Tres garantías cortas: Envío gratis con rastreo · Pago seguro · Si no te llega, te devolvemos tu dinero.

Más abajo:
10. **"El veredicto de Toffee"**: tarjeta con la calificación (Comodidad ★★★★★, Siesta-prueba ✓, Resistencia a
    Galleta ✓) y una "Nota de Toffee".
11. Problema → solución (por qué existe este producto) con 3 beneficios con ícono.
12. Cómo se usa (3 pasos con fotos).
13. Guía de tallas con peso de la mascota y medidas (tabla HTML).
14. Comparativa corta contra lo genérico.
15. Reseñas reales (se oculta si no hay).
16. Preguntas frecuentes del producto (incluye lavado, tallas, para gatos y perros, seguridad).
17. Avisos de seguridad cuando aplique (disfraces: "supervisa a tu mascota mientras lo usa"; orejeras: "ayudan a
    reducir el ruido, no son un tratamiento médico").
18. Marrano compacto ("Con esta compra, $X van al marrano").
19. "También aprobado por Toffee" (venta cruzada).
20. **Barra fija abajo en celular** con nombre, precio y botón cuando el botón principal sale de la pantalla.

Reglas: ninguna promesa médica ("cura la ansiedad"), ninguna urgencia falsa (contadores que se reinician, "quedan 3"
inventado), ningún precio tachado inventado.

---

## 6. La historia de Toffee (Quiénes somos)

Estructura (como el "Our Story" de las marcas top y como Love, Nala cuenta a Nala):
1. Titular: "Soy Toffee. Probé todas las camas de la casa. Todas eran horribles."
2. El origen: la historia de Toffee y por qué abrió la tienda.
3. Su regla y su sello.
4. El equipo: Toffee (jefe, dormilón) y Galleta (empleado, rescatado de la calle).
5. El marrano: qué es, cómo se calcula (3 % del subtotal) y dónde se publican los comprobantes.
6. **Transparencia:** "Toffee y Galleta son personajes creados con inteligencia artificial. Los productos, los
   envíos, la atención y las donaciones son 100 % reales. Detrás de Toffee hay una persona: [NOMBRE], desde
   [CIUDAD], Colombia." Con los datos del vendedor (sección 0).
7. Botón a la tienda y a las redes.

---

## 7. Test de Toffee (quiz, sin apps pagas)

Sección propia del tema con HTML + JS liviano, editable desde el editor:
1. ¿Tu peludo es gato o perro?
2. ¿Cuánto pesa? (rangos según las guías de tallas reales de los productos)
3. ¿Qué le pasa? (le asustan la pólvora y los ruidos / quiero que esté calientito y cómodo / quiero fotos de Navidad
   divertidas)
4. ¿Cómo se llama? (opcional, para personalizar el resultado: "Toffee aprobó esto para Luna")

Resultado: producto + **talla recomendada** + frase de Toffee + botón que abre el producto con esa variante ya
seleccionada (`?variant=ID`). Opcional: "¿Te mando el resultado y mi regalo al correo?" con formulario de cliente de
Shopify, etiqueta `test-toffee` y casilla de autorización sin marcar. Las preguntas, rangos y productos deben poder
editarse con bloques.

---

## 8. Carrito, correos y WhatsApp

- **Cajón del carrito:** "Completa el kit" (venta cruzada, ya existe), nota de confianza bajo el botón, monto que va
  al marrano, aproximado en moneda local, botón caramelo "Finalizar compra →".
- **No crees descuentos, combos ni cupones nuevos sin mi aprobación.** Si propones uno, déjalo listo pero oculto.
- **Regalo digital de Toffee** (cuesta $0): fondos de pantalla y stickers de Toffee y Galleta en un enlace de
  Archivos de Shopify, entregado en el correo de bienvenida.
- **Correos con Shopify Email / automatizaciones de marketing** (escribe los textos con la voz de Toffee y déjalos
  listos para que yo los active): bienvenida + regalo · carrito abandonado ("Dejaste esto en el carrito y no he
  podido dormir 😾") · confirmación y envío ("Galleta está cuidando tu pedido") · pedido de reseña real con foto
  (después de la entrega) · recuperación a los 60 días.
- WhatsApp o SMS solo a quien dio autorización, por el canal autorizado y en horario prudente (lunes a viernes 7 a. m.
  a 7 p. m., sábados 8 a. m. a 3 p. m., nunca domingos ni festivos), según la Ley 2300 de 2023 de Colombia.
- **Nada de ruletas, rasca y gana ni sorteos** (en Colombia necesitan permiso de Coljuegos). Mejor regalo fijo.

---

## 9. Legales (obligatorio, sin inventar datos)

Crea o actualiza las políticas en **Configuración → Políticas** (para que Shopify las use también en el pago y en las
respuestas de los agentes de IA) y enlázalas en el pie. Escribe en español claro. Al final de tu entrega dime:
"Estos textos son una base; revísalos con un abogado".

### 9.1 Páginas

1. **Información de contacto / Datos del vendedor** (Ley 1480, art. 50 de Colombia): nombre o razón social, cédula o
   NIT, dirección de notificación judicial, teléfono/WhatsApp, correo.
2. **Términos y condiciones:** quién vende, ley colombiana, países donde se vende, precios en COP con aproximado
   local, pagos con dLocal, proceso de compra (resumen antes de pagar y confirmación por correo), propiedad
   intelectual de Toffee y Galleta, **cláusula de IA** (personajes y escenas creados con IA; productos y fotos de
   producto reales), uso del sitio.
3. **Envíos:** gratis con rastreo, 10 a 25 días hábiles, por país; qué pasa si no llega; **impuestos de
   importación**: Chile cobra IVA 19 % a compras en tiendas extranjeras desde el 25-oct-2025 (Ley 21.713); México
   subió aranceles a productos de países sin tratado como China desde el 1-ene-2026; Perú: verificar. Dime qué
   decisión tomar (¿los asume la tienda o el cliente?) antes de publicarlo y avísame que confirme las cifras.
4. **Devoluciones, retracto y garantía, por país:**
   - Colombia: retracto de 5 días hábiles desde la entrega (Ley 1480, art. 47); reembolso en máximo **15 días
     calendario** (Ley 2439 de 2024); reversión del pago (art. 51); garantía legal; excepciones (productos de uso
     personal o higiene solo si aplica de verdad).
   - Chile: retracto de **10 días desde que recibe el producto** (Ley 19.496, art. 3 bis); enviar confirmación
     escrita de las condiciones después de cada compra.
   - México: derechos ante PROFECO (verificar plazo de revocación vigente).
   - Perú: derechos ante Indecopi + Libro de Reclamaciones.
   - Cómo pedirlo: WhatsApp/correo/formulario, quién paga el envío de vuelta y en cuánto tiempo se devuelve el dinero.
5. **Privacidad y tratamiento de datos:** Colombia (Ley 1581 de 2012 y Decreto 1377 de 2013: responsable,
   finalidades, derechos, cómo ejercerlos, autorización previa), México (aviso de privacidad y derechos ARCO), Chile y
   Perú (sus leyes de datos). En todo formulario: casilla de autorización **sin marcar** con enlace a esta política.
6. **PQR (peticiones, quejas y reclamos):** formulario que, al enviarse, muestra y envía un **número de radicado
   único** (fecha + código) para seguimiento (Ley 2439 de 2024). Puede ser el formulario de contacto de Shopify con
   un campo oculto que genera el código.
7. **Libro de Reclamaciones (Perú):** página con formulario (identificación del consumidor, producto, detalle del
   reclamo o queja, fecha; **sin casillas obligatorias ni datos extra**) que entrega código y fecha; respuesta en
   máximo 15 días hábiles. Enlace **visible desde la portada y el pie** (Ley 32495 de 2025). Alternativa: la
   herramienta gratis "Tu Libro de Reclamaciones" de Indecopi.
8. **Política del marrano:** cómo se calcula el 3 %, a quién se dona, cada cuánto y dónde están los comprobantes.
9. **Contenido con IA** (sección 10).
10. Cookies: aviso con la API de privacidad de clientes de Shopify (recomendado).

### 9.2 Pie de página

Marino, con: logo y frase de Toffee · menú de tienda · Ayuda (FAQ, rastrear pedido, contacto por WhatsApp y correo) ·
Legales (Términos, Envíos, Devoluciones y garantía, Privacidad, Datos del vendedor, PQR, Política del marrano,
Contenido con IA) · **"Libro de Reclamaciones" con su ícono** · **enlace visible a la Superintendencia de Industria y
Comercio (sic.gov.co)** · redes @toffee.elgato · logos de tarjetas · línea final: "© 2026 Soy Toffee. Toffee y Galleta
son personajes creados con IA. Los productos y la atención son reales."

---

## 10. Transparencia de IA (hacerlo bien es parte de la marca)

- Página **"Contenido con IA"**: qué es IA (Toffee, Galleta, escenas), qué es real (productos, fotos de producto,
  envíos, atención, donaciones), y cómo se hacen las imágenes.
- Chip "Escena creada con IA" en cada escena de Toffee/Galleta dentro de la web.
- Si agregas un asistente de chat ("Pregúntale a Toffee"): debe decir que es una IA en el primer mensaje, responder
  solo con datos de la tienda (envíos, tallas, políticas), no inventar plazos ni promesas y pasar a una persona por
  WhatsApp o correo cuando no sepa. Si no hay una app confiable, usa Shopify Inbox sin IA.
- Nada de hacer pasar a Toffee por un humano ni por un gato real.

---

## 11. Listo para agentes de IA (ChatGPT, Copilot, Google AI Mode)

En 2026 Shopify manda los productos a ChatGPT, Microsoft Copilot y Google AI Mode (Shopify Catalog + Agentic
Storefronts). Hoy solo vende a compradores de EE. UU., pero quiero la tienda lista para cuando se abra en LATAM:
1. Títulos claros con tipo de producto + beneficio + variante (sin mayúsculas sostenidas ni emojis).
2. Descripciones con datos concretos que respondan preguntas reales: medidas, peso de la mascota por talla,
   materiales, cuidado y lavado, para qué sirve y para qué no, envío por país.
3. Categoría estándar de producto de Shopify, tipo de producto, etiquetas y **metacampos de producto**: especie
   (perro/gato), talla, peso mínimo y máximo de la mascota, material, medidas, temporada.
4. Variantes con SKU, precio e inventario correctos.
5. Texto alternativo descriptivo en todas las imágenes.
6. Datos estructurados: en la plantilla de producto `<script type="application/ld+json">{{ product | structured_data }}</script>`
   y en el layout un `Organization` con logo y redes (`sameAs`). **Nunca** poner calificaciones (`AggregateRating`)
   sin reseñas reales.
7. No bloquear a los buscadores de IA en `robots.txt` (dejar el de Shopify por defecto).
8. Políticas completas en Configuración → Políticas.
9. Dime cómo instalar la app gratis **Shopify Knowledge Base** y escríbeme 15 preguntas frecuentes con respuestas
   para cargarla.
10. Dime dónde revisar **Configuración → Canales de venta → Agentic Storefronts** y la herramienta de Shopify para
    revisar si la tienda está lista para agentes.

---

## 12. Velocidad, SEO y accesibilidad

- Mucha gente entra con internet lento: imágenes WebP/AVIF con `srcset`, foto de portada ≤ 150 KB con precarga, carga
  diferida debajo de la primera pantalla, máximo 2 fuentes, JS mínimo, sin videos pesados en reproducción automática.
  Meta: Lighthouse móvil ≥ 80 en rendimiento y ≥ 95 en accesibilidad.
- SEO: título y descripción de portada y de cada producto en español, un solo H1 por página, URLs limpias, imagen
  para compartir (1200×630) con Toffee en la paleta nueva.
- Accesibilidad: contraste AA, foco visible al navegar con teclado, áreas táctiles de 44 px, `alt` en todo, no
  depender solo del color para dar información.

---

## 13. Medición

Revisa que estén conectados (con las apps oficiales de Shopify, respetando el permiso de cookies): píxel de Meta con
API de conversiones, píxel de TikTok y Google Analytics 4. Eventos: ver producto, agregar al carrito, iniciar pago,
compra y "test completado". Enlaces de la bio con UTM.

---

## 14. Cómo trabajar (reglas del dueño)

1. **Antes de tocar nada, duplica el tema en vivo como respaldo.** Trabaja en una copia sin publicar y mándame el
   enlace de vista previa. **Publica solo cuando yo diga "publica".**
2. Todo texto en HTML, nunca quemado en imágenes. Todo editable desde el editor de temas.
3. Composición trabajada, nada de plantilla genérica: que se vea de marca top.
4. No borres secciones que funcionan (`tf-marrano`, `tf-precio-local`, fecha de entrega, cuenta regresiva, venta
   cruzada): adáptalas a la paleta nueva.
5. No inventes reseñas, cifras, veterinarios, premios, "envío en 3 días", stock ni descuentos.
6. Cuando termines, actualiza `tienda-holly/ESTADO.md` con lo que cambiaste.

## 15. Revisión final antes de mostrarme (marca cada punto)

- [ ] Se ve bien en celular (390 px) y en computador; sin desbordes ni textos cortados.
- [ ] Todos los colores salen de las variables `--tf-*`; contraste AA comprobado.
- [ ] Primera foto de cada producto = producto real; escenas con chip "Escena creada con IA".
- [ ] Botón principal caramelo con texto marino en portada, catálogo, producto, carrito y barra fija.
- [ ] Agregar al carrito y Comprar ahora funcionan en cada variante; el test abre la variante correcta.
- [ ] Precio aproximado en moneda local, fecha de entrega y cuenta regresiva funcionando.
- [ ] Marrano lee `custom.marrano` y se ve bien.
- [ ] Pie con todos los legales, Libro de Reclamaciones, enlace a la SIC, contacto y redes.
- [ ] Formularios con casilla de autorización sin marcar; PQR y Libro de Reclamaciones dan número de radicado.
- [ ] 404, carrito vacío, agotado y gracias con la voz de Toffee.
- [ ] Datos estructurados de producto presentes y sin calificaciones falsas.
- [ ] Lighthouse móvil: rendimiento ≥ 80, accesibilidad ≥ 95.
- [ ] Entrégame: enlace de vista previa, capturas de celular de portada y producto, lista de cambios en palabras
      simples, lo que yo debo hacer en el panel y los prompts de fotos que falten.

=== FIN DEL PROMPT ===

---

## Prompts de fotos para la paleta "Noche acogedora" (Google Flow)

Sube `toffee/TOFFEE-ficha.jpg` como referencia (y `toffee/refs/GALLETA-oficial.jpg` cuando salga Galleta).

**P1 · Portada horizontal (16:9)**
```
Wide 16:9 shot. Toffee (the chubby round cream-caramel British Shorthair cat from the reference (solid color, no stripes), big round green eyes with very dilated pupils, wearing a navy blue knitted nightcap with a drooping tip and a cream pompom) sits like a serious but sleepy CEO on a wooden desk in a cozy home office at night. Warm caramel desk lamp light, deep navy blue walls and shadows, a cream knitted blanket, a small stack of cardboard shipping boxes, a cup of warm milk, a laptop seen from behind. Toffee is on the RIGHT third of the image; the LEFT 55% is calm dark navy space for text. He looks at the camera, unimpressed, one paw on a small gift box. Cinematic but cozy, photorealistic, real fur texture, soft film grain, warm caramel and deep navy color palette, NOT neon, NOT 3D render, NOT illustration. No text, no letters, no logos, no watermark.
```

**P2 · Portada vertical (9:16)**
```
Vertical 9:16 phone composition. Same scene: Toffee (the chubby round cream-caramel British Shorthair cat from the reference (solid color, no stripes), big round green eyes with very dilated pupils, wearing a navy blue knitted nightcap with a drooping tip and a cream pompom) as a sleepy CEO on a wooden desk in a cozy home office at night, warm caramel lamp light, deep navy walls, cardboard boxes, cream blanket. Toffee in the BOTTOM 45% of the image, centered; the TOP 50% is calm dark navy space for text. Cinematic but cozy, photorealistic, warm caramel and deep navy palette, NOT neon, NOT 3D render. No text, no letters, no logos, no watermark.
```

**P3 · La historia de Toffee: el equipo (4:5)**
```
Vertical 4:5. Toffee (the chubby round cream-caramel British Shorthair cat from the reference (solid color, no stripes), big round green eyes with very dilated pupils, wearing a navy blue knitted nightcap with a drooping tip and a cream pompom) sits on top of a cardboard box like a boss, and next to him Galleta (the exact same dog from the second reference photo: scruffy wiry golden-brown Latin American criollo mutt, floppy ears, bushy eyebrows and beard, white chest and paws, navy blue bandana with a golden bone tag) holds a small roll of packing tape in his mouth, nervous and proud. Cozy Latin American living room in the afternoon, warm natural window light, cream and navy tones. Real candid photograph taken with an iPhone, real fur textures, slight phone-camera grain. NOT 3D, NOT render, NOT illustration, no neon. No text, no letters, no logos, no watermark.
```

**P4 · Página 404 (1:1)**
```
Square 1:1. Toffee (the chubby round cream-caramel British Shorthair cat from the reference (solid color, no stripes), big round green eyes with very dilated pupils, wearing a navy blue knitted nightcap with a drooping tip and a cream pompom) sitting on a cream rug with a torn piece of blank paper in his mouth and small paper scraps around him, guilty innocent face, looking at the camera. Plain warm cream background (#F3E9D8), soft studio light. Real photograph, real fur texture. NOT 3D, NOT illustration. No text, no letters, no logos, no watermark.
```

**P5 · Carrito vacío (1:1)**
```
Square 1:1. Toffee (the chubby round cream-caramel British Shorthair cat from the reference (solid color, no stripes), big round green eyes with very dilated pupils, wearing a navy blue knitted nightcap with a drooping tip and a cream pompom) lying dramatically next to an empty ceramic food bowl on a kitchen floor, looking at the camera with an offended, starving drama face. Warm morning light, cream and navy tones. Real candid photograph taken with an iPhone, real fur texture, slight grain. NOT 3D, NOT illustration. No text, no letters, no logos, no watermark.
```
