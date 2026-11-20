# Estado del proyecto — Zero Club

- Tienda: am4qyv-vq.myshopify.com (correo zeroclub.store@gmail.com) · moneda COP
- Carpeta: tienda-zeroclub/ (base: tema Horizon descargado de la tienda; GitHub bloqueado para bajar Dawn)
- Tema de trabajo: "Zero Club" id 196250927474 (NO publicado). Tema activo: Horizon 196250337650.
- Entorno: Shopify CLI 5.0.2 con NODE_USE_ENV_PROXY=1. Permiso de datos: pegar URL 127.0.0.1:13387/auth/callback?... (curl --noproxy '*').

## Producto
- Body Zero Sweat 24/7 – Spray Antisudoral · gid://shopify/Product/15353919046002 · handle body-zero-sweat · plantilla product.zc
- Variantes (Oferta), inventario sin seguimiento:
  - 1 frasco 63029753676146 · 74.900 (antes 119.900) · costo Dropi 19.000
  - 2 frascos 63029754462578 · 119.900 (antes 199.900) · costo 38.000
  - 3 frascos + mini de viaje 63029754495346 · 149.800 (antes 279.900) · costo 57.000
- Proveedor Dropi: Inversiones Milab, bodega Medellín. INVIMA confirmado por el proveedor (NO se muestra en la página, decisión del usuario).
- No prometer: "sin efectos secundarios", "dura 4 meses", "cura hiperhidrosis".

## Diseño
- Verde menta #2fae8c / oscuro #0f3d33 / menta claro #8ff0d2. Archivo Black + Inter (Google Fonts en layout/theme.liquid).
- assets/zc.css, assets/zc.js. Secciones: zc-cinta, zc-producto (ofertas + casilla de compromiso obligatoria + compra directa a /checkout + barra fija móvil), zc-problema, zc-beneficios, zc-comparativa, zc-pasos, zc-faq, zc-cierre.
- index.json = página de venta (zc-producto con producto body-zero-sweat). product.zc.json igual.

## Pendiente
- Contraseña de la tienda (para revisar) y fotos del producto.
- Header/footer con logo, páginas legales, favicon, pago contra entrega (método manual), integración Dropi, píxel Meta, publicar.
