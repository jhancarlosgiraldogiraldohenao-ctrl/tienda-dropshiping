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
  Probable nivel de inventario/ubicación. Pedido permiso read/write_inventory + read_locations.

## Pendiente
- Auto-revisión visual: la tienda tiene contraseña -> pedirla al usuario.
- Publicar el tema como activo solo con OK explícito.
- Políticas legales (panel → Configuración → Políticas).
