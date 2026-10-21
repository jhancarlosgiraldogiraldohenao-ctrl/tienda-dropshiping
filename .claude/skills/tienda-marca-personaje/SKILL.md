---
name: tienda-marca-personaje
description: Diseña, audita y mejora tiendas online de MARCA CON PERSONAJE (una mascota, un gato, un perro, un muñeco o un influencer de IA que es la cara de la tienda), con los patrones comprobados de las 10 mejores tiendas del mundo (Chewy, Petco, The Farmer's Dog, BARK, Zesty Paws, Duolingo Store, Sanrio, Pusheen, Love Nala, Meowingtons). Úsala SIEMPRE que el usuario quiera crear, rediseñar, revisar o "volver una de las mejores" su tienda de marca o de personaje, armar el inicio, la ficha de producto, el carrito, la confianza, las reseñas, las temporadas, la causa social, los combos o la voz del personaje en la tienda, o pregunte "qué le falta a mi tienda", aunque no diga "personaje" ni "skill". Caso principal Soy Toffee (soytoffee.store, el gato Toffee y el perro Galleta). Se encarga de la estrategia, la estructura y los textos; para instalar, editar el tema y publicar en Shopify, combínala con la skill tienda-shopify-v2.
---

# Tienda de marca con personaje

Esta skill convierte lo que aprendimos estudiando 10 de las mejores tiendas del mundo en decisiones concretas para
una tienda cuyo corazón es un personaje. Sirve para tres cosas: **auditar** una tienda que ya existe, **planear**
qué cambiar en orden de impacto y **construir o reescribir** cada página con los patrones que funcionan.

La idea central del estudio: las mejores tiendas no ganan por la página, ganan por lo que pasa antes (el personaje,
la comunidad, el servicio) y la página solo no estorba. Las tiendas de mascotas ganan con **confianza** (garantía
con nombre, reseñas con foto, fechas honestas) y las de personaje ganan con un **universo** (fichas de personajes,
temporadas, voz con humor, lanzamientos). Las de personaje famosas se saltan las reseñas porque todo el mundo ya
las conoce; una marca nueva no puede: necesita el universo de las de personaje **más** la confianza de las de mascotas.

## Antes de empezar

1. **Lee el caso de la marca.** Si es Soy Toffee, lee `references/caso-toffee.md`: reglas del dueño (anónimo, sin
   WhatsApp, sin Facebook, sin anuncios), productos, precios, mercados, fechas de entrega y lo que ya está bien. Si es
   otra marca, llena primero la ficha del personaje y la ficha del negocio de `references/plantillas.md`; sin eso las
   recomendaciones salen genéricas.
2. **Mira la tienda real en el celular**, no solo el código. El tráfico de estas marcas llega de TikTok, Reels y
   Shorts, o sea desde un teléfono. Usa Playwright con el Chromium preinstalado
   (`require('/opt/node-tools/node_modules/playwright')`, viewport 390x844, `isMobile: true`) y saca capturas del
   primer pantallazo, la ficha, el carrito y el pie. Si hay código local del tema, comprueba que esté al día con el
   tema publicado antes de editar nada: trabajar sobre una versión vieja borra cambios que ya están en vivo.
3. **Para Shopify** (bajar el tema, editar secciones, publicar), usa la skill `tienda-shopify-v2` si está disponible.
   Esta skill decide qué hacer y qué decir; aquella sabe cómo hacerlo técnicamente.

## Flujo de trabajo

### 1. Auditar
Recorre la tienda con `references/checklist.md` (secciones A a J) y anota cada punto como ✅ bien, ⚠️ a medias o
❌ falta, con la evidencia (URL o captura). Empieza por lo que ya está bien: el dueño necesita saber qué no tocar.

### 2. Priorizar
Ordena lo que falta en tres niveles, como hizo el estudio: **ya** (esta semana, poco esfuerzo, mucho impacto),
**este mes** (lo que mueve la meta de ventas) y **largo plazo** (lo que construye la marca). Para cada punto di
qué hacer, de qué tienda de referencia viene (`references/tiendas-referencia.md`), qué impacto esperas y cuánto
esfuerzo cuesta. El impacto es cualitativo (alto, medio, bajo) y explicado: no prometas cifras que no tienes.

### 3. Construir
Página por página, con los patrones de abajo y de `references/patrones.md`. Escribe los textos con la voz del
personaje (guía en `references/plantillas.md`) y deja el botón de compra siempre claro.

### 4. Verificar
Antes de publicar, pasa la sección J del checklist: celular real, fechas y cifras iguales en todas las páginas,
nada de contenido viejo, nada de plantilla olvidada.

## Las 20 reglas

Cada regla viene de algo que vimos funcionar (o fallar) en las 10 tiendas. Entender el porqué te deja adaptarla a
casos que la regla no prevé.

**El personaje**
1. **Ficha del personaje** con nombre, especie, cumpleaños, mejor rasgo, frase, 3 rasgos de personalidad, colores
   fijos y, si es IA, aviso de transparencia. Pusheen, Sanrio y Love Nala venden desde la biografía del personaje:
   la gente compra lo que quiere el personaje que ya quiere.
2. **Elenco de al menos dos personajes opuestos** (uno serio, uno sensible) con un papel en la tienda. El contraste
   da historias y BARK demuestra que una "empresa dirigida por perros" hace memorable hasta la página legal.
3. **Set de 8 a 10 poses** reutilizables (portada, popup, contacto, rastreo, 404, carrito vacío, causa, envío).
   Pusheen y Love Nala ponen al personaje en cada rincón, también en las páginas aburridas.
4. **Voz con humor en cada texto**, incluso en el FAQ y el carrito vacío, pero el botón de compra siempre dice lo que
   hace ("Agregar al carrito"). El chiste va al lado del botón, nunca en lugar de él: Duolingo es divertida y aun así
   nadie duda dónde pagar.
5. **La opinión del personaje no es una reseña.** Toda calificación o "prueba" del personaje se rotula como opinión
   del personaje (y de IA si lo es); nunca estrellas que parezcan de clientes, nunca "probado por" un personaje sin
   aclararlo, nunca reseñas, cifras ni escasez inventadas. Es la diferencia entre una marca simpática y publicidad
   engañosa (en Colombia, Ley 1480 y la SIC).

**Las páginas**
6. **Primer pantallazo en celular** = personaje + producto + problema de la temporada + un solo botón. Quien llega
   desde un video tiene que reconocer en un segundo lo que vio. Compruébalo a 390 px de ancho.
7. **Ficha de producto en este orden:** frase del personaje → precio → talla o variante → botón → fecha de entrega →
   garantía → causa. Galería: foto 1 el producto en uso, foto 2 infografía de usos, foto 3 guía de tallas (Petco MX,
   Zesty, Love Nala). Botón fijo abajo en el celular (Farmer's Dog; casi ninguna otra lo tiene) y FAQ propia.
8. **Temporadas reales por país**, en tres lugares a la vez: menú, portada y contenido (Chewy, Petco, Zesty). Cada
   campaña con fecha de cierre: el contenido viejo es el error que más se repite en las tiendas que van peor.
9. **Fechas de entrega honestas** calculadas con la promesa real del proveedor y por país, desde una sola fuente de
   verdad. Si una fecha ya no alcanza, se quita ese día. Con dropshipping nunca se promete entrega el mismo día.
10. **Una sola oferta, conectada a la palabra del video** ("Comenta CALMA" → código o beneficio CALMA en la tienda).
    Las top nunca mezclan varias ofertas; quien llega del video debe encontrar su palabra.
11. **La causa con una sola cifra**, con fecha, comprobante y aliado real, igual en todas las páginas. Chewy y Petco
    la hacen parte de la marca; el error repetido es que las cifras no cuadran entre páginas.

**La confianza y la venta**
12. **Captura de correo con regalo del personaje** (fondos de pantalla, certificado), casilla de autorización sin
    marcar, y nunca un popup a pantalla completa en el celular ni nada que tape el carrito (Petco MX, Love Nala y
    Meowingtons lo hacen mal).
13. **Correos con la voz del personaje:** confirmación con el nombre de la mascota, envío, "así se usa", pedido de
    reseña y carrito abandonado. Si la marca no usa WhatsApp, el correo es el único canal de vuelta.
14. **Prueba social real:** app de reseñas con foto (Judge.me tiene plan gratis), respuestas firmadas por el personaje
    (BARK responde todas), galería de clientes. Las estrellas en las tarjetas solo cuando ya hay reseñas: cero
    estrellas se ve peor que nada.
15. **Las redes dentro de la tienda:** bloque "Sigue a…" y videos con el producto enlazado. La tienda es la
    consecuencia del contenido; quien no compra hoy, que al menos siga al personaje.
16. **Subir el pedido sin trucos:** combos con el ahorro escrito y visible en la ficha (Zesty "Better Together"),
    el complemento lógico del producto estrella y un regalo con la compra (Sanrio, Duolingo).
17. **Productos que son el personaje** como meta de largo plazo (el gorro, la pañoleta, peluches): Duolingo, Sanrio
    y Pusheen venden al personaje mismo, muchas veces hecho por terceros (licencia o impresión bajo pedido).

**Lo legal y el cierre**
18. **Legal LATAM:** derecho de retracto por país (5 días hábiles en Colombia, 10 en Chile), PQR y enlace a la SIC
    (Colombia), Libro de Reclamaciones (Perú), aviso de impuestos de importación (México, Chile), autorización de
    datos (Ley 1581) y aviso de IA si el personaje lo es. Ver `references/plantillas.md`.
19. **Errores prohibidos:** contenido viejo, cifras que no cuadran, popups que tapan, casillas marcadas, texto de
    plantilla olvidado, productos agotados en el inicio, errores de escritura, reseñas o urgencia inventadas,
    promesas de salud con números.
20. **Checklist antes de publicar** (sección J de `references/checklist.md`): celular real, fechas y cifras iguales
    en todas partes, código local al día con el tema publicado.

## Lo que no se copia todavía

Algunas cosas de las top no sirven para una marca pequeña con dropshipping, y conviene decirlo en voz alta para no
perder tiempo: suscripción o Autoship (solo con productos que se gastan), quiz largo antes de comprar (con pocos
productos sobra), descuentos grandes (el margen del dropshipping no los aguanta), entrega el mismo día, y saltarse
las reseñas (solo lo pueden hacer personajes ya famosos).

## Cómo entregar

- Escribe para el dueño de la marca: si no es técnico, en palabras simples, y explica cada término en la misma frase.
- Auditoría o plan: tabla con qué hacer, de qué tienda viene, impacto y esfuerzo; primero lo que ya está bien.
- Textos para la tienda: listos para pegar, con la voz del personaje, señalando dónde va cada uno.
- Marca como **(sin confirmar)** lo que no comprobaste y nunca inventes datos de la tienda o del proveedor:
  pregúntalos o márcalos como pendiente (por ejemplo, días reales de entrega por país).
