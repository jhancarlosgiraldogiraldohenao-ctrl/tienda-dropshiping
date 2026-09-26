# ESTADO de la tienda

- Tienda: sqfyqn-qn.myshopify.com (panel: https://admin.shopify.com/store/vuronix)
  - OJO: el dominio interno es `sqfyqn-qn.myshopify.com`; "vuronix" es solo el
    nombre del panel. Usar siempre `--store sqfyqn-qn.myshopify.com`.
- Proyecto: este repositorio (tema base Dawn, sin modificar todavía)
- Tema activo actual: "Build Your Store Theme" (#154842661043) — no tocar
- Fases completadas: 0 (entorno), 1 (conexión + sondeo), 2 (tema base)
- Notas de entorno (nube): ejecutar el programa de Shopify con
  `NODE_USE_ENV_PROXY=1`; el permiso de datos se completa pegando la URL
  `http://127.0.0.1:13387/auth/callback?...` que devuelve el navegador.

## Producto principal
- id: gid://shopify/Product/8709568856243
- handle: compresor-inflador-portatil
- título: AirGo/Vuronix" Compresor Inflador Portatil
- precio: 109.900 COP, sin precio de comparación. Stock 405. SKU CI-01
- tipo de producto (a corregir): "papelería"
- descripción: inflador portátil inalámbrico para moto, carro y bici; 150 PSI,
  ±1 PSI, 2x2000 mAh, USB-C, 480 g, luz LED, 4 modos + manual, apagado
  automático; pago contraentrega en toda Colombia. Público: motociclistas en Colombia.
- fotos (fotos-producto/): 1 y 5 de proveedor en baja resolución; 2 = ambiente
  junto a rueda de carro (buena); 3 = infografía con textos; 4 = detalles (buena).
  Producto negro mate con aro metálico y pantalla digital "32.0".

## Otros productos en la tienda (importados, en inglés, plantilla general_template)
- Mini Retro White Noise Bluetooth Speaker, D5 Starry Moon Lamp,
  Smart Fingerprint Padlock, Metal Expansion Phone Stand

## Brief confirmado (2026-09-26)
- Estilo "herramienta pro de carretera": asfalto #0E0F11, grafito #17191C,
  amarillo señal #FFC400, estudio claro #EEF0F2. Titulares Barlow Condensed
  (Google Fonts) + Inter. Radios 8/14px. Tema global: barlow_n7 / inter_n4.
- Requisitos del usuario: texto SIEMPRE en bloques HTML (nunca quemado en la
  imagen); sinergia fotos-bloques; composición muy trabajada, nada de plantilla;
  usar SUS fotos (las mejores). Sin fotos IA.
- Marca: Vuronix (producto: AirGo). Otros 4 productos: sin tocar (el usuario
  no respondió; la web se centra en el inflador).

## Fotos usadas (recortes de producto-2/3/4, en assets/)
- vx-escena-rueda (hero, paso 1, cierre), vx-estudio-frente (anatomía),
  vx-recorte-tres-cuartos.png (modos, sin fondo), vx-paso-controles, vx-detalle-*
  (pantalla, botones, válvula, usbc, boquillas, linterna), vx-estudio-gris.
- Descartadas: producto-1 (500px, iconos) y producto-5 (320px): baja calidad.

## Tema de trabajo
- "Vuronix AirGo" id 155009319091 (NO publicado). Tema activo sigue siendo #154842661043.
- Preview: https://sqfyqn-qn.myshopify.com?preview_theme_id=155009319091

## Secciones (prefijo vx-)
- vx-hero: apertura, foto con parallax + pantalla animada HTML que "infla" 18→32 PSI
- vx-cifras: banda de 4 cifras con contador
- vx-anatomia: foto de estudio con puntos numerados + tarjetas (bloques con x/y)
- vx-modos: selector interactivo moto/carro/bici/balón con lectura digital
- vx-garantias: marquesina amarilla
- vx-pasos: escena sticky, la foto cambia con cada paso (ancla #como-funciona)
- vx-comparativa: AirGo vs gasolinera
- vx-detalles: bento de detalles + "qué incluye"
- vx-faq, vx-cierre
- vx-producto: página de producto (galería del catálogo, variantes, cantidad,
  product-form de Dawn -> cajón del carrito, confianza, desplegables, barra móvil)
- header.liquid: wordmark "Vuronix" + logo opcional por sección
- footer.liquid: reescrito (VX – Pie de página)
- snippets/vx-icono.liquid, assets/vx-styles.css, assets/vx-scripts.js, vx-favicon.png
- templates/index.json y templates/product.vx.json

## Catálogo (hecho por API)
- Producto: título "Inflador Portátil Inalámbrico AirGo – Vuronix", tipo
  "Infladores portátiles", vendor Vuronix, descripción reescrita, SEO,
  templateSuffix "vx" asignado, fotos reordenadas (escena, detalles, infografía,
  proveedor 500px, proveedor 320px) y textos alternativos corregidos.

## Cambios ronda 2 (2026-09-26)
- Menú: "Catálogo" (/collections/all) oculto con el ajuste del header "ocultar_enlaces".
- Producto: galería en modo "dos" (vx-producto-frente.jpg + vx-producto-incluye.jpg,
  compuestas sin texto); modo "catalogo" sigue disponible desde el editor.
- Batería: 2000 mAh (7,4 V, 2 celdas en serie; la infografía del proveedor indica 7,4 V).
  Cambiado en cifras, especificaciones y descripción del catálogo.
- Pedidas al usuario fotos profesionales para "Detalles" (subidas en Contenido → Archivos).

## Cambios ronda 3 (2026-09-26)
- Producto: opción "Presentación": "1 unidad" (46092267061427, 109.900, stock 405)
  y "Pack dúo (2 unidades)" (46094051573939, 199.900, tachado 219.800, SKU CI-02,
  inventoryPolicy CONTINUE porque no tenemos permiso de inventario).
- vx-producto: tarjetas de opciones (radio) con foto, nota, precio y ahorro; al elegir
  el pack cambia la foto principal a vx-pack-duo.jpg (provisional, compuesta).
- Nueva sección vx-packs en portada (tras comparativa), tarjeta 2 destacada "Mejor precio".
- Modos: foto nueva vx-recorte-frente.png (alta resolución, sin reflejo blanco ni fondo en el asa).
- Fotos de producto sobre fondo grafito (vx-producto-frente/incluye, vx-pack-duo).
- Detalles: quitadas "Rosca firme" y "Cabe en todo"; quedan 3 tarjetas iguales.
- Fotos del usuario (detalles + pack dúo): AÚN NO recibidas en Contenido → Archivos.

## Cambios ronda 4 (2026-09-26)
- Fotos profesionales del usuario (recibidas por chat): pack dúo (recortado a fondo
  grafito -> assets/vx-pack-duo.jpg y subida al producto como foto del pack,
  MediaImage 33551302131891 asignada a la variante), USB-C cargando (recortada a la
  derecha y tapado el recuadro "Cargando..." -> vx-detalle-usbc-pro.jpg), linterna
  (vx-detalle-linterna-pro.jpg), boquillas (recorte sobre grafito -> vx-detalle-boquillas-pro.jpg).
- Detalles: fondo de fotos #101114, altura mínima 280px.
- Pack dúo: precio 189.900 (tachado 219.800, ahorro 29.900).

## Ronda 5 (2026-09-26)
- Contraseña de la tienda: datsea (auto-revisión con theme dev --store-password).
- Precios sin ",00" (money_without_trailing_zeros + JS), hero/cierre usan la variante 1.
- HUD del hero arriba (no tapa el aparato); cierre con degradado más opaco; wordmark móvil 20px.
- Pasos: paso 2 = vx-paso-ajusta.jpg (recorte de la foto linterna), paso 3 = vx-producto-frente.jpg.
- Pack: foto sin base blanca, re-subida al producto (MediaImage 33551420981427), la vieja borrada.
- PROBLEMA ABIERTO: la variante "1 unidad" (46092267061427) sale AGOTADA en la tienda
  (cart/add.js 422) aunque el admin dice availableForSale=true, tracked=false, policy CONTINUE.
  Causa: el inventario de "1 unidad" vive SOLO en la ubicación de Dropi (FulfillmentDropi,
  Location 85472051379, servicio de preparación, 405 uds) y la tienda online no la cuenta como
  vendible (probable: esa ubicación no está en el perfil de envío / mercado de Colombia).
  Probé tracked=true -> sigue agotada; lo dejé como estaba (tracked=false).
  El pack (46094051573939) está en la ubicación propia "calle 20c no 28b-08 pereira" -> se vende,
  pero sus pedidos NO van a Dropi automáticamente. Pendiente del usuario: revisar Envío y entrega / app Dropi.
  RESUELTO: la ubicación FulfillmentDropi estaba "sin asignar" en el Perfil general de envío.
  Añadida al grupo de ubicaciones (DeliveryLocationGroup 105616933043) -> "1 unidad" disponible.
  Permisos actuales: products, files, inventory, locations, shipping.

## Ronda 6 (2026-09-26)
- Título del producto: "AirGo · Compresor Inteligente Inalámbrico" (+ SEO).
- Precios tachados (pedido del usuario): 1 unidad 109.900 (antes 129.900), pack 189.900 (antes 239.800).
- Portada: sección de packs justo después de la apertura (id #packs); "Pídelo hoy" baja a #packs.
- Producto: botón "Comprar ahora" (enlace /cart/ID:CANT -> checkout directo), "Agregar al carrito"
  pasa a secundario; % de ahorro se actualiza al cambiar de opción.

## Ronda 7 (2026-09-26)
- Envío: borrada la tarifa "Estándar" (14.951 COP, gratis desde 162.600) y creada "Envío gratis" (0 COP)
  en la zona Domestic (CO). Internacional sin tocar (60.000).
- Textos "Envío gratis" (barra superior, hero, packs, garantías, producto, pie) + cláusula del flete
  (FAQ "¿El envío tiene costo?", "¿Cómo pago?", producto "Envío y pago", pie).
- Pago contraentrega activado por el usuario (con textos de flete); PayPal desactivado.
- Nueva sección vx-resenas (solo reseñas reales, se oculta sin reseñas) en portada (antes de FAQ)
  y producto (tras garantías) + plantilla templates/page.resenas.json para una página de reseñas.

## Ronda 8 (2026-09-26)
- Carrito: botón "Finalizar compra →" (locales/es.json "checkout"), grande y de marca; nota
  "Envío gratis a toda Colombia · Pagas en efectivo al recibir" (textos tax-note en es.json);
  cajón con altura 100dvh y pie fijo para que el botón se vea en móvil.

## Ronda 9 (2026-09-26)
- Cabecera: sin lupa ni cuenta (ajustes mostrar_busqueda / mostrar_cuenta = false); "Contacto" oculto
  del menú (ocultar_enlaces "/collections/all, /pages/contact"); icono de carrito de compras nuevo
  (assets/icon-cart*.svg). Pie sin enlace a Contacto; FAQ sin botón "Escríbenos".
- Producto: tarjeta "Asesoría" -> "Fácil de usar · Listo en minutos"; aviso stock "Disponible · envío gratis".

## Ronda 10 (2026-09-26)
- Galería producto: foto 1 "AirGo" (vx-producto-frente), foto 2 "Accesorios incluidos"
  (vx-producto-accesorios.jpg: boquillas pro + cable USB-C recortado de producto-1). Al elegir el pack
  la foto 1 pasa a vx-pack-duo con el texto "AirGo Dúo" (ajuste oferta_2_foto_texto).
- Frase de introducción del producto: "El compresor inteligente para moto, carro y bici...".

## Ronda 11 (2026-09-26)
- "Pídelo hoy" (hero) ahora va a la página del producto (sin btn1_url -> product.url). Scroll suave para anclas.

## PUBLICADO (2026-09-26)
- Tema "Vuronix AirGo" #155009319091 es ahora el tema ACTIVO (live). El anterior #154842661043 queda sin publicar.
- A partir de ahora los push necesitan --allow-live (cambios visibles al instante).
- Usuario ya tiene plan Basic. Pack dúo en Dropi: lo gestiona él a mano.

## Políticas (2026-09-26)
- Creadas por API (permiso legal_policies): envíos, reembolsos (retracto 5 días hábiles, Ley 1480,
  garantía legal), términos del servicio. Privacidad: la plantilla de Shopify ya existente (en español).
- Correo usado en las políticas: el de la tienda. Tiempo de entrega indicado: 2 a 7 días hábiles (confirmar con Dropi).
- El nombre de la tienda sigue siendo "Mi tienda" -> el usuario debe cambiarlo a "Vuronix"
  (Configuración → Detalles de la tienda); no se puede por API.

## TIENDA ABIERTA (2026-09-26) — verificación final OK
- Sin contraseña; título "Vuronix AirGo"; tema live #155009319091; producto y las 2 opciones disponibles
  (se añaden al carrito); 4 políticas responden 200; pago contraentrega en checkout.

## Precios (2026-09-26, decididos con el usuario; costo Dropi 59.000/ud)
- 1 unidad 139.900 SIN tachado. Pack dúo 239.900, tachado 279.800 (= 2 sueltas, descuento real, ahorro 39.900).

## Ronda 12 (2026-09-26, en vivo con --allow-live)
- Nueva sección vx-porque "¿Por qué comprar en Vuronix?" (envío desde Colombia 2-7 días, contraentrega,
  garantía legal + retracto 5 días, especificaciones claras + franja "Pagas solo cuando el AirGo está en tus manos").
  En portada tras packs y en producto tras la ficha. Motivo: el mismo producto aparece más barato en Mercado Libre.

- vx-porque tarjeta 3 -> "Compra protegida" (solo garantía legal). El retracto de 5 días se mantiene SOLO en la
  política de reembolsos (obligatorio por Ley 1480 art. 47); decisión consensuada con el usuario.

## Vista previa al compartir (2026-09-26)
- La portada no tenía og:image -> WhatsApp mostraba tarjeta vacía/antigua. Añadido assets/vx-compartir.jpg (1200x630)
  como og:image por defecto y descripción por defecto en snippets/meta-tags.liquid.
- Comprobado: todos los visitantes (sin sesión) ven el tema nuevo #155009319091.

## Pendiente
