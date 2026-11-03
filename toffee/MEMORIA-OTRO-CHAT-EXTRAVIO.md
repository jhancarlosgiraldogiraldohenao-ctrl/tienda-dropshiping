# Memoria de trabajo · EXTRAVÍO (capítulo 1 y canal)
Sesión del 1 al 2 de noviembre de 2026. Para Jay.

---

## 1. Dónde está cada cosa

| Qué | Dónde |
|---|---|
| Video completo sin voces (4:06, 1080p) | `scratchpad/EXTRAVIO-CAP01-SIN-VOCES.mp4` |
| Video completo con voces (versión 7) | `scratchpad/EXTRAVIO-CAP01-V7-con-voces.mp4` |
| Respaldo de la versión 5 | `scratchpad/EXTRAVIO-CAP01-V5-respaldo.mp4` |
| Lista de las 37 voces por toma | `scratchpad/LISTA-VOCES-CAP01.md` |
| Voces en orden (37 archivos) | `scratchpad/VOCES-CAP01-EN-ORDEN/` |
| Eventos separados (voces, efectos, música) con su hora | `scratchpad/piloto/export/` (manifest.json) |
| Editor web de línea de tiempo | https://claude.ai/artifact/S8hQELnPfc8ZhdcQkLXGCf (versión 4) |
| Portadas del capítulo 1 | `scratchpad/portada/` (miniatura-cap01.jpg, v2, v3, v4 y v5) |
| Short vertical de prueba (44 s) | `scratchpad/short/SHORT-GNOMO-CAP01.mp4` |
| Código del editor | `toffee/extravio/editor/ed01p.py` (rama `claude/modest-bardeen-prnnui`) |

Las carpetas de `scratchpad` son temporales: si la sesión se reinicia, lo que no esté en el repositorio o en el editor web se pierde.

---

## 2. Qué se hizo con el capítulo 1

**Versiones del render:**
- **v3 y v4:** primeras versiones con música, efectos y voces.
- **v5:** correcciones de Jay: voces de Toffee en «Hola» y en «¿Me ves botas?», música más suave, quitar escenas.
- **v6:** voz de Toffee pegada en las dos tomas; «Mi humana» con otro método de pegado; canción que empieza en «Bienvenidos a la ciudad de Extravío»; quitar la toma de caminar de espaldas (P41) y la del cartero caracol (P25); «¿Siguen vivos?» cortado.
- **v7:** quitar la toma de caminar de espaldas que quedaba (P15) con su voz; música y canción más bajas.
- **v7 sin voces:** versión sin voces para que Jay ponga las suyas. Se entregó junto con la lista de voces.

**Errores del capítulo que siguen abiertos:**
- **Sincronía de las voces con la boca:** el desfase medio es de unos 0,23 s y hay tomas con 0,8 s o más (P13, P14, P23, P38). No quedó resuelto. Jay pidió que quede calzado, y no lo logré. Lo que hace falta: que Jay diga el minuto de cada frase desfasada y ajustar frase por frase.
- **«Hola, soy Tofi»:** la voz de prueba dice «Tofi», no «Toffee». Es solo de prueba; Jay pone la suya.
- **«qué lástima»:** la frase de Lucho no existe en el audio original; solo quedó «¿Siguen vivos?».
- **«Madrax»:** la voz dice «Madrax», no «Max». Si lo quiere «Max», hay que regrabar.
- **Cartero caracol:** lo identifiqué por un fotograma, no por la toma original. Si Jay ve que no era esa escena, hay que revisar.
- **Render final desde el editor web:** todavía no está hecho. El editor guarda los cambios de Jay, pero el video final con esos cambios lo tengo que armar yo leyendo los datos guardados.

---

## 3. Editor web (línea de tiempo)

Versiones publicadas: 1, 2, 3 y 4 (la 4 es la actual).

**Lo que hace:**
- Pistas separadas: Voces, Efectos, Música, Canción, Ambiente y Video.
- Volumen y silencio por pista y por clip.
- Mover, duplicar, quitar, recortar al inicio y al final.
- Dividir clips en el cursor (video y sonidos).
- Agregar videos, audios y voces (subida a la página, límite de 20 MB por archivo).
- Video con voces en vista previa (480p).
- Cambios en vivo: si cambias algo mientras suena, se oye y se ve al momento.
- Guardado compartido en la base de datos de la página (`estado/capitulo-01`).

**Lo que no está probado o no está hecho:**
- La subida de archivos propios no la probé: la prueba local no tiene cuenta.
- El guardado compartido no lo probé con datos reales. El primer cambio de Jay es la prueba.
- Render final con los cambios: pendiente.
- Video a pantalla completa de alta calidad: la vista previa es de 480p; el render final es 1080p.

---

## 4. YouTube y canal

**Video publicado (programado):**
- Título: «Me caí a otro mundo persiguiendo a mi perro | EXTRAVÍO Cap. 1».
- Descripción: la que se mandó (sin fechas ni días, con «Sígueme para no perderte el próximo episodio»).
- Miniatura: versión 4 (`miniatura-cap01-v4.jpg`).
- Estreno programado: 2 nov 2026, 6:00 p. m.

**Problemas que quedaron:**
- Al principio se marcó como «creado para niños», y eso apagó los comentarios. Hay que cambiarlo a «No es contenido creado para niños» y volver a activar los comentarios.
- El video estaba en verificación cuando se revisó. Hay que confirmar que salió al aire a las 6:00 p. m.

**Etiquetas del video:**
- Específicas: Extravío, Toffee, Galleta, Serie animada, Gatos y perros animados.
- Generales: Animación, Gatos, Perros, Serie de YouTube, Humor.

**Estrategia (la del proyecto):**
- 6:00 p. m.: capítulo largo en YouTube.
- 12:00 p. m. y 8:00 p. m.: 2 Shorts. Los mismos Shorts van a TikTok e Instagram.
- Decisión del día 30 con los números de `toffee/MEDICION-SEMANAL.csv`.
- Subtítulos de Shorts en español pegados (1 a 3 palabras); en inglés como archivo aparte.

---

## 5. Shorts

- **Short de prueba:** 44 s, vertical, con subtítulos y voces. Jay dijo que «es una porquería». Los problemas que se identificaron: los personajes salen chiquitos en el centro y el fondo difuminado domina la imagen.
- **Pendiente:** decidir si el Short se rehace con el personaje más grande o si se hace de otra forma.

---

## 6. Análisis de Gnomo Palomo

**Pendiente.** Jay quiere analizar:
- continuidad de la historia y del diálogo;
- qué hace Gnomo en momentos callados, en conversaciones y en errores;
- cuántas tomas de Google Flow tomaría un video así.

Yo no puedo abrir links de YouTube. Se necesita el video en partes (máximo 30 MB) o minutos exactos de cada momento.

---

## 7. Errores de proceso (míos) que conviene no repetir

- Afirmé que algo estaba listo o corregido sin haberlo verificado (la sincronía de las voces, por ejemplo).
- Usé tiempos de una versión vieja del video para cortar Shorts; los tiempos cambiaron al quitar escenas. Ahora se toman del manifiesto de exportación.
- Texto de voces con errores de transcripción: «Anze» en vez de «Escóndanse», «Tofi» en vez de «Toffee», «Gadeta» y otros. Ahora se usa el texto exacto de cada voz.
- Subtítulos que se encimaban: corregido con un límite de fin por línea.
- Un commit lleva el nombre del modelo en el mensaje: no debe llevarlo (regla del proyecto).
- Enlaces de YouTube: no puedo abrirlos. Debí decirlo desde el principio.

---

## 8. Reglas del proyecto que se usaron (resumen)

- Prompts para Flow: en inglés, en un solo bloque para copiar, sin texto dentro de la imagen, un solo personaje que habla por toma, sin primera persona con patas visibles.
- Cambios grandes en la tienda: vista previa antes de publicar. La tienda está cerrada: nunca mandar a soytoffee.store.
- Groserías: pocas, nunca en los primeros 10 s, título ni miniatura.
- Cierre de cada episodio: «Sígueme para no perderte el próximo episodio». Sin días ni fechas.
- Los subtítulos de capítulos largos no van pegados; los de Shorts sí.
- Todo lo que se le manda a Jay en PDF va también como link.

---

## 9. Lo que sigue (orden sugerido)

1. Jay sube el video a YouTube como está programado: revisar «creado para niños» y comentarios.
2. Confirmar que el capítulo salió a las 6:00 p. m. y revisar la verificación.
3. Jay pone sus voces en el video sin voces (y dice qué voces no le cuadran, con minutos).
4. Yo ajusto la sincronía de esas voces frase por frase.
5. Render final con los cambios del editor web.
6. Rehacer el Short con personajes más grandes, si Jay lo confirma.
7. Análisis de Gnomo Palomo cuando lleguen los videos en partes.
8. Capítulo 2: quedan pendientes la voz de la Catrina, las tomas nuevas de Flow y la risa de Lucho.
