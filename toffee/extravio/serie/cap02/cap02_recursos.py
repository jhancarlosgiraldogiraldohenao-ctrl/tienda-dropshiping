# Capítulo 2 (México, Día de Muertos): prompts de personajes, lugares, música, sonidos y voces.
# python3 toffee/extravio/serie/cap02/cap02_recursos.py  ->  CAP02-RECURSOS.md y web/cap02-recursos.html
import html, os
AQUI = os.path.dirname(os.path.abspath(__file__))
FIN_P = " Photorealistic 3D animated film style, expressive face, soft natural light, no text, no letters, no logos."
FIN_L = (" Photorealistic 3D animated film style, cinematic light, rich colors, no characters, no people, no animals,"
         " no text, no letters, no writing on signs, empty space in the center for small characters. Vertical 9:16.")

SECC = [
 ("1 · Personajes nuevos (Nano Banana Pro)", "Se guardan en refs/extravio/personajes/ con el nombre que dice cada uno.", [
  ("CATRINA", "La Catrina: gata esqueleto elegante. Confunde a Dizzy con un alma perdida y se lo quiere llevar al panteón. Tocino se enamora de ella.",
   "Character reference sheet of an original cartoon elegant lady cat skeleton for a Mexican Day of the Dead story, four views (front, three-quarter, side, back) on a plain light gray background: a tall, slim, graceful female cat made of smooth ivory-white bones, her skull face painted like a colorful sugar skull with blue, pink and orange flower patterns, big dark eye sockets with warm glowing orange pupils and long black eyelashes, a red painted smile, pointy bone cat ears, a long thin bone tail; she wears a huge wide-brimmed black hat covered in orange marigold flowers, purple ribbons and two feathers, a long elegant purple and black ruffled lace dress, a necklace of marigold flowers, long black lace gloves and a small folding fan in one hand; proud, theatrical, flirty posture. She looks friendly-spooky and funny, never scary." + FIN_P),
  ("CHUY", "Chuy, el ajolote trabado (reemplaza al Xolo). Lento, risueño, con los ojos rojos; sabe el secreto para volver.",
   "Character reference sheet of an original cartoon Mexican axolotl, four views (front, three-quarter, side, back) on a plain light gray background: a chubby pink axolotl standing on two short legs, soft shiny pink skin with tiny dark freckles, six fluffy frilly gills like pink feathers on the sides of his wide head, a lazy goofy smile, heavy-lidded half-closed eyes that are very red and watery, relaxed droopy eyebrows, totally sleepy and slow; he wears a faded striped Mexican sarape poncho and a small tilted straw sombrero with a frayed edge; in one hand he holds a thick crooked hand-rolled herbal cigarette with a glowing tip, a soft cloud of gray smoke floating around his head; slouching posture, belly forward, very chill." + FIN_P),
  ("LUPE", "Lupe, la chihuahua mariachi: brava y coqueta. Tocino le da serenata y ella le rompe el violín en la cabeza.",
   "Character reference sheet of an original cartoon female chihuahua mariachi musician, four views (front, three-quarter, side, back) on a plain light gray background: a small tan chihuahua with huge pointed ears, big shiny dark eyes with long eyelashes, a sassy confident look with one eyebrow raised, a pink bow on one ear; she wears a fitted black charro mariachi suit with silver buttons and silver embroidery, a red bow tie, and a giant black and silver embroidered sombrero much wider than her body; she holds a small violin and its bow; hand on hip posture, tiny but fierce." + FIN_P),
 ]),
 ("2 · Lugares y tomas aéreas (Nano Banana Pro, vertical 9:16)", "Se guardan en refs/extravio/lugares/. Así se explica el viaje: finca → pueblo → alcantarilla → caída → viaje bajo la tierra → Ciudad de México.", [
  ("AEREA-PUEBLO-NOCHE", "Aérea del pueblo de la finca a medianoche (después de AEREA-FINCA-NOCHE, que ya está).",
   "Vertical aerial drone shot at midnight of a small colorful colonial village on a steep Colombian coffee mountain: white houses with clay tile roofs and colorful doors around a little plaza with a white church, warm yellow street lamps, empty cobblestone streets, a full moon (only one moon) in a dark blue sky with stars, misty green mountains around, quiet and magical." + FIN_L),
  ("PUEBLO-ALCANTARILLA-NOCHE", "La alcantarilla del pueblo que a medianoche brilla verde (la puerta al mundo).",
   "Vertical shot at ground level of a narrow cobblestone street in a small Colombian colonial village at midnight: a round old iron manhole cover in the lower center of the frame with a soft magical green glow coming out of its holes and edges, thin green mist rising from it, colorful closed doors and windows of colonial houses on both sides, one warm street lamp, a dark blue night sky with stars at the top, mysterious and magical, not scary." + FIN_L),
  ("TUNEL-VERDE", "Dentro de la alcantarilla: el túnel mágico por donde caen.",
   "Vertical shot looking straight down inside a deep round old brick sewer shaft that turns into a magical tunnel: wet old bricks and a rusty iron ladder at the top, and further down the walls dissolve into a swirling spiral of glowing green light with tiny golden sparkles, like a magic portal, water drops falling, strong depth, dizzying and wonderful." + FIN_L),
  ("AEREA-VIAJE-MAPA", "El viaje: de Colombia a México por debajo de la tierra (una raya verde que cruza el mar).",
   "Vertical very high aerial shot at night from above the clouds over the Caribbean sea and the coast of Central America, the land dark with tiny city lights, the ocean shining under the moon, and a thin bright glowing green line of magic light traveling fast under the land and the sea from the bottom of the frame (south) to the top of the frame (north), leaving a trail of green sparkles, epic and magical." + FIN_L),
  ("AEREA-CDMX-NOCHE", "Llegada: Ciudad de México en Día de Muertos, de noche.",
   "Vertical aerial drone shot at night of a huge old Mexican city during the Day of the Dead: a big colonial plaza with a cathedral with two bell towers, streets lit with thousands of candles and orange marigold flower paths, strings of colorful papel picado over the streets, small fireworks far away in the sky, the silhouette of two volcanoes on the horizon under a full moon (only one moon), warm orange and purple light, festive and magical." + FIN_L),
  ("MX-CALLE-ALTAR", "La calle del altar (donde aparece Dizzy y lo ve la Catrina). Foto 1.",
   "Vertical shot at eye level of a narrow colonial street in Mexico on the Night of the Dead: brightly painted houses in pink, blue and yellow, strings of colorful cut paper flags (papel picado, blank shapes, no letters) crossing overhead, a big home altar on the right side with many candles, orange marigolds, sugar skulls, bread and empty wooden picture frames, a path of orange marigold petals on the cobblestones in the lower center, warm candle light and purple night sky." + FIN_L),
  ("MX-CALLE-ALTAR-2", "La misma calle desde abajo, otro ángulo. Foto 2.",
   "Vertical low shot from the ground of the same colonial Mexican street on the Night of the Dead, looking up the street: candles lined along both sidewalks, orange marigold petals on the cobblestones in front, a small stone fountain with flowers in the middle distance, strings of colorful cut paper flags (blank shapes) overhead, painted houses with iron balconies full of flowers, warm glow and a purple sky." + FIN_L),
  ("MX-MERCADO", "El mercado de noche (la huida). Foto 1.",
   "Vertical shot at eye level of a busy-looking but empty Mexican night market on the Day of the Dead: colorful stalls with tables full of sugar skulls, sweet bread, clay pots, paper mache skeletons and colorful fantasy animal figures, piñatas and strings of lights hanging, orange and purple fabric roofs, a narrow aisle in the center between the stalls, warm festive light." + FIN_L),
  ("MX-MERCADO-2", "El mercado a ras del piso, entre ollas y cajas (persecución). Foto 2.",
   "Vertical shot very close to the floor inside a Mexican night market: big clay pots, wooden crates of chili peppers and corn, a taco stand with a steaming pot on the left, colorful tablecloths hanging to the floor, marigold petals scattered on the tiles, a long aisle running into the distance in the center, warm light and soft steam." + FIN_L),
  ("MX-PANTEON", "El panteón lleno de velas (donde la Catrina se los quiere llevar). Foto 1.",
   "Vertical shot at eye level of a small old Mexican cemetery on the Night of the Dead: old stone graves covered with orange marigolds and hundreds of lit candles, crosses made of flowers, low mist on the ground, an old church dome in the background under the full moon, warm candle glow against a dark blue night, beautiful and festive, not scary." + FIN_L),
  ("MX-PANTEON-2", "La reja de entrada del panteón. Foto 2.",
   "Vertical shot from the ground of the tall old black iron gate of a Mexican cemetery on the Night of the Dead, the gate half open in the center, an arch of orange marigold flowers over it, candles and flower petals on the path that goes through the gate, graves with candles glowing behind, mist and moonlight." + FIN_L),
  ("AEREA-XOCHIMILCO-NOCHE", "Aérea de los canales con trajineras (adonde los lleva Chuy).",
   "Vertical aerial drone shot at night of long calm canals surrounded by trees and floating gardens, many long colorful wooden boats (trajineras) with painted arches lit by paper lanterns floating on the dark water, orange marigold flowers floating on the canals, reflections of the lights in the water, full moon (only one moon), magical and festive." + FIN_L),
  ("MX-CANAL-TRAJINERAS", "Los canales a ras del agua. Foto 1.",
   "Vertical shot at water level of a calm canal at night with colorful wooden boats (trajineras) tied along both sides, their painted arches covered only with orange marigolds, flower patterns and painted swirls (no names, no letters, no words), paper lanterns glowing, orange marigold flowers floating on the water in the lower center, trees and reeds behind, soft warm reflections." + FIN_L),
  ("ARREGLO · MX-CANAL-TRAJINERAS", "Sobre la imagen que salió con letras en los arcos: edición en Nano Banana, no una nueva.",
   "Edit this image: remove every letter and word from the arches of all the boats and replace them with colorful flower patterns and painted swirls in the same style and colors. Keep everything else exactly the same: the canal, the water, the reflections, the lanterns, the willow trees, the floating marigolds, the night sky and the framing. No text, no letters, no names anywhere. Vertical 9:16."),
  ("MX-TRAJINERA-CHUY", "Dentro de la trajinera de Chuy. Foto 2.",
   "Vertical shot on board a small colorful wooden trajinera boat at night: a long wooden deck in the center, a small table with clay cups and a bowl of fruit, a tiny hammock tied between two posts, flowers and paper lanterns hanging from the arch, which is covered only with flower patterns (no names, no letters), the dark canal and other lit boats far behind, relaxed and cozy." + FIN_L),
  ("MX-ALCANTARILLA-NOCHE", "Por donde sale Dizzy al llegar a México (el gancho), de noche.",
   "Vertical shot at ground level of a narrow colonial street in Mexico on the Night of the Dead: a round old iron manhole cover in the lower center of the frame, slightly lifted, with bright magical green light and green mist bursting out from under it, orange marigold petals scattered around it on the cobblestones, a home altar with candles and marigolds on the right side, strings of colorful cut paper flags (blank shapes) overhead, painted houses, purple night sky." + FIN_L),
  ("MX-TRAJINERA-MARIACHI", "La trajinera de Lupe y los mariachis (la serenata de Tocino). Foto 4 de los canales.",
   "Vertical shot at eye level of a colorful wooden trajinera boat at night tied at the edge of a calm canal, its painted arch covered only with orange marigolds, flower patterns and painted swirls (no names, no letters, no words), a small empty wooden stage on board with three empty chairs, a big guitar and a guitarrón resting on the chairs, paper lanterns and string lights glowing, the dark canal with floating marigolds in front, willow trees behind." + FIN_L),
  ("MX-ALCANTARILLA-AMANECER", "La alcantarilla de regreso, justo antes del amanecer (la carrera final).",
   "Vertical shot at ground level of a narrow Mexican colonial alley at blue dawn: a round old iron manhole cover in the lower center glowing a faint magical green from its holes, burnt-out candles and marigold petals on the cobblestones, painted houses, the sky at the top turning from dark blue to pink as the sun is about to rise, urgent feeling." + FIN_L),
 ]),
 ("3 · Música nueva (ElevenLabs Music, instrumental)", "Se guardan en sonidos/musica/. Lo demás se reusa: M6 coqueteo, M8 la abuela, M10 la cámara, M11 tema.", [
  ("M12-mariachi-muertos (1:00)", "Llegada a México y la calle del altar.",
   "Instrumental festive Mexican mariachi for the Day of the Dead, trumpets, violins, vihuela and guitarrón, medium tempo, joyful but a little mysterious, like a magical night with candles, perfect as background for a comedy cartoon, no vocals, 60 seconds."),
  ("M13-persecucion-cumbia (0:45)", "Huida por el mercado y carrera a la alcantarilla.",
   "Instrumental fast Mexican cumbia sonidera chase music, accordion, güiro, bass and timbales, energetic and funny, comedy cartoon chase, builds tension, no vocals, 45 seconds."),
  ("M14-bolero-tocino (0:30)", "Serenata de Tocino a Lupe (y a la Catrina).",
   "Instrumental cheesy romantic Mexican bolero, requinto guitar and soft maracas, slow and exaggerated, over-the-top romantic for a funny cartoon serenade, no vocals, 30 seconds."),
  ("M16-vals-catrina (0:30)", "Cada vez que aparece la Catrina: vals elegante y de miedito.",
   "Instrumental elegant spooky Mexican waltz for a funny skeleton lady, soft violins, music box, marimba and light castanets, slow 3/4 time, theatrical and a little creepy but charming, comedy cartoon, no vocals, 30 seconds."),
  ("M15-tema-chuy (0:40)", "Cada vez que habla Chuy: cumbia lenta y mareada.",
   "Instrumental very slow lazy psychedelic cumbia, slowed down and wobbly, soft accordion, deep bass, echo and reverb, dreamy and sleepy, funny relaxed mood for a stoned cartoon character, no vocals, 40 seconds."),
 ]),
 ("4 · Ambientes y efectos que faltan (ElevenLabs Sound Effects)", "Se guardan en sonidos/ambientes/ y sonidos/efectos/. El resto (whoosh, golpe de chiste, chanclazo, cachetada, brillo mágico) ya está.", [
  ("E25-ambiente-muertos-noche (0:30)", "Fondo de la calle y el mercado.",
   "Ambience of a Mexican town square on the Night of the Dead: distant mariachi music far away, distant small fireworks popping, a church bell far away, soft crowd murmur in the distance, gentle night wind, 30 seconds."),
  ("E26-ambiente-alcantarilla (0:20)", "Dentro de la alcantarilla.",
   "Ambience inside an old brick sewer tunnel: slow water drips with long echo, a soft low hum of magic, distant running water, 20 seconds."),
  ("E27-ambiente-canal (0:30)", "Los canales de noche.",
   "Ambience of calm canals at night: soft water lapping against wooden boats, wooden boat creaks, frogs and crickets, very distant marimba music, 30 seconds."),
  ("E28-calada-tos-chuy (0:05)", "Chuy le da una calada larga y tose.",
   "A long slow inhale through a hand-rolled cigarette with soft paper crackle, a pause, then a funny deep cough and a sleepy giggle, cartoon style, 5 seconds."),
  ("E29-huesos-catrina (0:03)", "La Catrina se mueve: huesitos que suenan.",
   "Light rattling of small bones like wooden castanets, playful and elegant, cartoon skeleton moving, 3 seconds."),
  ("E30-violin-roto (0:03)", "Lupe le rompe el violín en la cabeza a Tocino.",
   "A small violin smashed on a head: wood crack, strings snapping with a twang, then a soft cartoon thud, 3 seconds."),
  ("E32-campanas-amanecer (0:06)", "Aviso de que va a salir el sol (la cuenta para volver).",
   "Old church bells ringing far away at dawn, three slow deep tolls with long echo, a rooster crowing in the distance after the last bell, 6 seconds."),
  ("E31-grito-ajua (0:03)", "El grito mexicano para los remates.",
   "A joyful Mexican mariachi shout 'ajúa' with a high trill, festive, short, 3 seconds."),
 ]),
 ("5 · Voces nuevas (ElevenLabs Voice Design)", "Una voz fija por personaje (estabilidad 50 %, similitud 75 %). Frase de prueba en cada una.", [
  ("VOZ-CATRINA", "Prueba: «Ay, mi alma perdida… ven conmigo al panteón, chiquito.»",
   "Elegant Mexican woman in her forties, warm, theatrical and seductive, slow and dramatic like an old telenovela star, soft spooky echo-like breathiness, rolls the r, laughs elegantly 'jo jo jo', speaks with a strong Mexico City accent, friendly-spooky, never scary."),
  ("VOZ-CHUY", "Prueba: «Qué onda, carnal… ¿neta vienes de Colombia?… no manches… está bien loco.»",
   "Young Mexican man in his twenties, very slow and sleepy, raspy deep voice, slurred relaxed words, long lazy pauses, giggles to himself, sounds totally stoned and happy, strong Mexico City slang accent ('qué onda, carnal', 'no manches'), funny and warm."),
  ("VOZ-LUPE", "Prueba: «¿Y tú qué me ves, cochino? ¡Órale, a volar!»",
   "Small fierce Mexican woman in her twenties, high-pitched, fast and sassy, very confident and bossy, strong northern Mexican accent, quick tongue, sharp attitude, funny and loud when angry."),
 ]),

 ("6 · Modo película: más ángulos (Nano Banana Pro, vertical 9:16)",
  "Adjunta SIEMPRE la foto que dice cada uno: así el lugar es el mismo visto desde otro lado (contraplanos, detalles, horas). Primero los 2 arreglos.", [
  ("AEREA-AMERICA-NOCHE", '(Reemplazado) Nano Banana no editó la foto: se hace un mapa nuevo sin raya, AEREA-AMERICA-NOCHE. La raya la animo yo.',
   'Vertical very high aerial shot at night from above the clouds, looking down at the Caribbean sea: Colombia and the north of South America with tiny warm city lights at the bottom right of the frame, the thin land of Central America curving through the middle, the Yucatán peninsula and Mexico with glowing city lights on the left side, Cuba and the Caribbean islands on the upper right, the ocean shining under the moonlight, soft clouds at the bottom and top edges, epic and calm. No lines, no light beams, no lasers, no glowing paths, no arrows. Photorealistic 3D animated film style, cinematic light, rich colors, no characters, no people, no animals, no text, no letters, no writing on signs. Vertical 9:16.'),
  ("PUEBLO-CALLE-NOCHE", 'Sube PUEBLO-ALCANTARILLA-NOCHE en el mismo mensaje. Sin alcantarilla y con la entrada del callejón a la derecha.',
   'Using the uploaded photo as the exact same Colombian village street (same houses with clay tile roofs, the same blue, red and yellow wooden doors, the same carved window bars, the same street lamp and the same starry night sky), remove the round manhole cover and the green light completely so the cobblestone street is continuous, and on the right side of the street add the dark narrow entrance of an alley between two houses, with tangled electric cables hanging above it and two black trash bags at its corner. Photorealistic 3D animated film style, cinematic light, rich colors, no characters, no people, no animals, no text, no letters. Vertical 9:16.'),
  ("CALLEJON-ALCANTARILLA-CONTRA", "Adjunta CALLEJON-ALCANTARILLA (el de la visión). Contraplano: desde adentro, mirando hacia el pueblo.",
   "Using the attached image as the exact same place (the same narrow dark alley with old brick walls, peeling plaster, tangled electric cables, black trash bags, wet cobblestones with puddles, the round sewer hole glowing green and the same night light), show it from the opposite direction: the camera stands deep inside the alley, behind the sewer hole, looking back toward the alley entrance, where the warm-lit cobblestone street of a small Colombian colonial village with colorful doors is visible at the far end. The glowing green sewer hole is in the lower center of the frame." + FIN_L),
  ("CALLEJON-ALCANTARILLA-PISO", 'Sube CALLEJON-ALCANTARILLA en el mismo mensaje. La MISMA tapa (huequitos), sin escaleras de incendio.',
   'Using the uploaded photo as the exact same alley and the exact same sewer cover (the same round iron cover with the same pattern of small holes glowing green, the same wet cobblestones and puddles, the same old brick walls with peeling plaster, tangled electric cables and black trash bags), show a very low shot at ground level right next to the cover: the cover fills the lower part of the frame, green light coming out of its holes and thin green mist rising, a puddle reflecting the green light, the alley walls rising softly out of focus behind. No fire escapes, no tall apartment buildings. Photorealistic 3D animated film style, cinematic light, rich colors, no characters, no people, no animals, no text, no letters. Vertical 9:16.'),
  ("AEREA-BARRIO-MX-NOCHE", 'Una sola foto aérea (la primera salió en 3 franjas pegadas). El barrio de México: la calle del altar, el mercado y el panteón juntos.',
   'One single continuous vertical aerial drone photo, not a collage, not split into panels, no borders: a low drone view at night looking down over one colorful colonial neighborhood in Mexico on the Night of the Dead. In the lower part of the frame a narrow cobblestone street with a big home altar and a long path of orange marigold petals; that street leads up to a small square in the middle of the frame filled with the colorful fabric roofs and paper lanterns of a night market; right behind the market, in the upper part of the frame, an old cemetery glowing with hundreds of candles next to a church with a dome. Strings of cut paper flags cross the streets, full moon (only one moon), warm orange and purple light. Photorealistic 3D animated film style, cinematic light, rich colors, no characters, no people, no animals, no text, no letters, no writing on signs. Vertical 9:16.'),
  ("MX-CALLE-ALTAR-CONTRA", "Adjunta MX-CALLE-ALTAR. Contraplano: el altar queda a la izquierda y al fondo se ve el mercado.",
   "Using the attached image as the exact same street (same painted houses, same strings of cut paper flags, same marigold petal path and the same big home altar with candles), show it from the opposite direction: the camera looks back up the street, so the big altar is now on the left side of the frame, the path of orange marigold petals runs from the lower center into the distance, and at the far end of the street the warm glow of a night market with lanterns is visible." + FIN_L),
  ("MX-ALTAR-CERCA", "Adjunta MX-CALLE-ALTAR. El altar a la altura de una rata: donde cae Dizzy en el gancho.",
   "Using the attached image as the exact same altar, show a close shot at the height of a small rat, in front of the lowest tier of the altar: big sugar skulls, round sweet breads, candles, orange marigolds and empty wooden picture frames tower above the camera, a soft pile of marigold petals on the lowest step in the center, warm candle light." + FIN_L),
  ("MX-MERCADO-CONTRA", "Adjunta MX-MERCADO. Contraplano: mirando hacia la entrada, se ve la calle del altar.",
   "Using the attached image as the exact same night market (same stalls, orange and purple fabric roofs, paper lanterns, cut paper flags, sugar skulls, piñatas and clay pots), show it from the opposite direction: the camera looks back down the aisle toward the market entrance, where the colorful street with the altar and the marigold petal path is visible beyond the last stalls." + FIN_L),
  ("MX-MERCADO-ESCONDITE", "Adjunta MX-MERCADO. El escondite de Chuy debajo de un puesto.",
   "Using the attached image as the same night market, show a hidden low corner under a stall: a tight cozy hideout under a table covered by a long colorful tablecloth, piñatas and colorful fantasy animal figures hanging above, a few crates, a small woven mat and a clay cup on the floor in the center, soft warm light coming through the tablecloth, a gentle haze of smoke." + FIN_L),
  ("MX-PANTEON-TUMBA", "Adjunta MX-PANTEON. La tumba de la Catrina (con su abanico encima).",
   "Using the attached image as the exact same cemetery (same stone graves, marigold crosses, candles, mist, church tower and full moon, only one moon), show a close low shot of one big old ornate stone grave in the center that is the most decorated of all: a large cross made of orange marigolds, an arch of purple flowers, dozens of candles, a small altar with sweet bread and a folded black lace fan resting on the stone." + FIN_L),
  ("MX-TRAJINERA-CHUY-CONTRA", "Adjunta MX-TRAJINERA-CHUY. Contraplano: desde la punta del bote hacia la hamaca.",
   "Using the attached image as the exact same boat (same painted arch with flowers, paper lanterns, string lights, the hammock, the small table with fruit and clay cups and the colorful wooden benches), show it from the opposite direction: the camera stands at the front tip of the boat looking back along the deck toward the hammock and the table, with the dark canal and other lit boats behind." + FIN_L),
  ("MX-CANAL-PUENTE", "Adjunta MX-CANAL-TRAJINERAS. Un puentecito sobre el canal (la Catrina los espera arriba).",
   "Using the attached image as the same canals (same colorful trajineras with arches covered only with marigolds and painted swirls, no names, no letters, paper lanterns, willow trees and floating marigolds), show a small old arched wooden footbridge crossing over the canal in the middle of the frame, decorated with marigolds and paper lanterns, the boats passing under it, reflections on the water." + FIN_L),
  ("AEREA-CDMX-AMANECER", "Adjunta AEREA-CDMX-NOCHE. La misma ciudad al amanecer (se acaba el tiempo).",
   "Using the attached image as the exact same city and framing (same colonial plaza, cathedral with two bell towers, streets and the two volcanoes on the horizon), show it at dawn: the sky turning from deep blue to pink and orange behind the volcanoes, the sun just about to rise, the candles almost burned out, soft blue morning light, no moon, no fireworks." + FIN_L),
  ("HABITANTES-MEXICO", "Los extras: para que el fondo esté vivo (se mueven atrás en las tomas). Se guarda en personajes/.",
   "Character reference sheet of a group of original cartoon animal background characters for a Mexican Day of the Dead night, all standing in one row on a plain light gray background, front view: three small male chihuahua mariachi musicians in black charro suits with silver buttons and big sombreros (one with a trumpet, one with a guitarrón, one with a vihuela), an old turtle vendor in an apron holding a tray of sugar skulls, a plump iguana lady with her face painted like a sugar skull holding a candle, a goat wearing a straw sombrero and a sarape carrying baskets of orange marigolds, and a green parrot selling sweet bread." + FIN_P),
 ]),
]

def md():
    o = ["# Capítulo 2 · «Salí por una alcantarilla y aparecí en México» — recursos (6-nov-2026)\n",
         "Historia v1 (falta el aval de Jay): ver el chat del 6-nov-2026. Nunca escribir «marijuana», «joint» ni «weed» en los prompts: «herbal cigarette» / «yerbita».\n",
         "Reusados: AEREA-FINCA-NOCHE, ZARZO-NOCHE, AEREA-FINCA (amanecer), G99 (caída), G103; música M6, M8, M10, M11.\n"]
    for t, sub, its in SECC:
        o.append(f"\n## {t}\n{sub}\n")
        for n, d, p in its:
            o.append(f"\n### {n}\n{d}\n```\n{p}\n```\n")
    return "".join(o)

def web():
    e = html.escape
    b = []
    for t, sub, its in SECC:
        b.append(f"<h2>{e(t)}</h2><p class=sub>{e(sub)}</p>")
        for n, d, p in its:
            b.append(f"<div class=card><div class=hd><b>{e(n)}</b><button onclick=\"cp(this)\">Copiar</button></div>"
                     f"<p>{e(d)}</p><pre>{e(p)}</pre></div>")
    return ("<!doctype html><html lang=es><head><meta charset=utf-8><meta name=viewport content='width=device-width,initial-scale=1'>"
     "<title>Capítulo 2 México</title><style>:root{--bg:#fbf6ef;--fg:#2a2118;--card:#fff;--ac:#e8590c;--mut:#6b5d50;--bd:#eadfce}"
     "@media (prefers-color-scheme:dark){:root:not([data-theme=light]){--bg:#17120d;--fg:#f3ebe1;--card:#221a13;--ac:#ff8a3d;--mut:#b6a796;--bd:#3a2e22}}"
     ":root[data-theme=dark]{--bg:#17120d;--fg:#f3ebe1;--card:#221a13;--ac:#ff8a3d;--mut:#b6a796;--bd:#3a2e22}"
     "body{background:var(--bg);color:var(--fg);font:16px/1.5 system-ui,sans-serif;margin:0;padding:16px;max-width:820px;margin:auto}"
     "h1{font-size:1.5rem;margin:.4em 0}h2{color:var(--ac);font-size:1.15rem;margin-top:1.6em}.sub{color:var(--mut);margin-top:-.4em}"
     ".card{background:var(--card);border:1px solid var(--bd);border-radius:12px;padding:12px;margin:10px 0}"
     ".hd{display:flex;justify-content:space-between;align-items:center;gap:8px}.card p{margin:.3em 0;color:var(--mut)}"
     "pre{white-space:pre-wrap;word-break:break-word;font-size:.85rem;background:var(--bg);padding:10px;border-radius:8px;margin:6px 0 0}"
     "button{background:var(--ac);color:#fff;border:0;border-radius:8px;padding:6px 14px;font-weight:600;cursor:pointer}</style></head><body>"
     "<h1>Extravío · Capítulo 2 · México 💀🌼</h1><p class=sub>Personajes, lugares, música, sonidos y voces. Toca «Copiar» y pégalo.</p>"
     + "".join(b) +
     "<script>function cp(x){const t=x.closest('.card').querySelector('pre').innerText;navigator.clipboard.writeText(t).then(()=>{x.textContent='¡Copiado!';setTimeout(()=>x.textContent='Copiar',1500)})}</script></body></html>")

if __name__ == "__main__":
    open(os.path.join(AQUI, "CAP02-RECURSOS.md"), "w").write(md())
    os.makedirs(os.path.join(AQUI, "web"), exist_ok=True)
    open(os.path.join(AQUI, "web", "cap02-recursos.html"), "w").write(web())
    print("ok", sum(len(s[2]) for s in SECC), "prompts")
