# EXTRAVÍO · Capítulo 2: «La Tierra de los Recordados» (1-nov-2026). Guion: GUION-CAP02.md.
# Hecho con el manual (MANUAL-PRODUCCION.md, sección 8): una acción por toma, posiciones del primer cuadro,
# un solo personaje habla, queso nombrado una vez, sin texto, sin puente (nada de Coco).
# python3 toffee/extravio/capitulos/ex02.py → web/capitulo-02.html (Artifact)
import os, sys, html
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, here)
from base import TEMP1

def S(s): return (f"Horizontal 16:9, {s} seconds. Photorealistic cinematic film look, normal lens (no fisheye, no vignette, no dark corners), "
                  "natural colors, realistic physics. One continuous shot with no cuts, full frame from edge to edge, no black bars.")
T = ("Toffee, the chubby cream-caramel British Shorthair cat from the reference (very round face, big green eyes, navy knitted nightcap "
     "with a cream pompom and a small black action camera on top of the nightcap)")
G = ("Galleta, the scruffy golden-brown criollo dog from the reference (thin wiry fur, bushy eyebrows, white chest and paws, "
     "navy bandana with a gold bone tag)")
L = ("Lucho, the skinny scruffy gray mouse from the reference standing on two legs (huge dark eye bags, big tired eyes, one crooked front tooth, "
     "torn black hoodie, small backpack full of old keys), hugging one single chunk of yellow cheese against his chest with his left arm")
CA = ("the elegant tall skeleton lady from the Catrina reference (wide black hat with orange marigolds and white ostrich feathers, painted ivory skull "
      "with floral patterns, deep purple lace dress, turquoise shawl, small brass bell in her right hand)")
XO = ("the hairless gray xolo guardian dog from the xolo reference (smooth slate-gray skin, tall upright ears, amber eyes, collar of orange marigold "
      "flowers with a round turquoise stone pendant), calm and serious, mouth closed")
BALL = "a small round rubber ball that glows soft turquoise from inside"
Q1 = "There is only ONE piece of cheese in the whole video; no other food appears near Lucho."
VT = "with a light, soft and sweet young adult male voice (a 20-year-old light tenor: warm, lazy, smug; clearly a young man, not a child)"
VL = "with a hoarse, raspy, quiet adult male voice, slightly short of breath, with a faint wheezy whistle"
VC = "with a warm, deep, velvety mature female voice, slow, elegant and a little mysterious"
def TT(line, tone="calmly"):
    return f'Toffee speaks in Latin American Spanish {tone}, {VT}: "{line}" His mouth moves clearly in sync with every word. Only Toffee speaks.'
def LL(line, tone="secretively"):
    return f'Lucho speaks in Latin American Spanish {tone}, {VL}: "{line}" His mouth moves clearly in sync with every word. Only Lucho speaks.'
def CC(line, tone="calmly"):
    return f'The skeleton lady speaks in Latin American Spanish {tone}, {VC}: "{line}" Her jaw moves clearly in sync with every word. Only she speaks.'
def END(cast, amb, cat=True, dog=False, extra=""):
    s = f"Exactly {cast} as main characters, identical to the references; {extra or 'no other animals appear.'}"
    if cat: s += " The cat's whole head, nightcap and camera always in frame. The cat wears NO bandana and NO tag."
    if dog: s += " The dog never speaks and keeps his normal shape."
    return s + f" No text, letters or signs with words anywhere, no phone, no selfie stick, no music; only {amb}."
NOWORDS = "The pages show only hand-drawn pictures, absolutely no writing, no letters, no words."

ROOF = ("On the flat roof of Lucho's shop in the city of lost things (like the rooftop reference), early morning: soft pink-gold sunrise light, "
        "chimneys made of old teapots, a clothesline of single socks, lost objects slowly falling from the sky like snow.")
STREET = ("The main cobblestone street of a magical Mexican Day of the Dead village at night (like the street reference): colorful adobe houses with "
          "glowing windows, papel picado banners overhead, candles and orange marigolds along the sidewalks, a tall arch of lit candles and marigolds "
          "at the end of the street, petals floating slowly; no bridge.")
TOWN = ("A magical Mexican Day of the Dead village on hills at night (like the village reference): colorful adobe houses with glowing windows, "
        "papel picado banners, thousands of candles, a calm river with small floating candles, a small white church tower; no bridge.")
ALTAR = ("In front of a giant Day of the Dead ofrenda altar at night (like the altar reference): seven wide stone steps covered with orange marigolds, "
         "hundreds of lit candles, sugar skulls and pan de muerto, papel picado above, and on the top step an enormous ancient open book on a carved "
         "wooden stand glowing soft turquoise.")
EXTRAS = ("friendly skeleton villagers in festive clothes (only skeletons, no other animals)")

REF = dict(T="TOFFEE-viajero.jpg", G="GALLETA-viajero.jpg", L="LUCHO.jpg", N="CATRINA.jpg", J="XOLO.jpg", Z="AZOTEA-LUCHO.jpg", D="PUERTA-PORTAL.jpg",
           V="CALLE-RECORDADOS.jpg", W="TIERRA-RECORDADOS.jpg", A="ALTAR-DEL-LIBRO.jpg", B="LIBRO-PAGINAS.jpg", O="RECUERDO.jpg", P="POLILLA.jpg")
ESC, N_ = [], [0]
def esc(t, f): ESC.append(dict(t=t, f=f, tomas=[]))
def tk(s, fotos, plano, p, quien, sonido, cont=None, nota=None):
    N_[0] += 1
    ESC[-1]['tomas'].append(dict(id=f"C2-{N_[0]:02d}", s=s, fotos=[REF[x] for x in fotos], plano=plano, p=p, quien=quien, sonido=sonido, cont=cont, nota=nota))

esc("0 · Gancho", "Lo más loco primero: Toffee con su primer «público»")
tk(6, "TV", "Contrapicado medio", f"{S(6)} {STREET} Low-angle medium shot: in the middle of the street {T} stands proud and happy, looking around; behind him three small friendly skeleton musicians in charro outfits (one with a guitar, one with a violin, one with a trumpet) stop playing and stare at him curiously. {TT('¡Por fin tengo público!', 'excitedly, opening his paws')} {END('one cat and three skeleton musicians', 'a soft festive night ambience', extra='no other animals appear.')}",
   "TOFFEE: «¡Por fin tengo público!»", "música de muertos de fondo")
tk(4, "TV", "Primer plano", f"{S(4)} {STREET} Close-up of {T}, the candlelit street softly out of focus behind him; he stops smiling, looks straight at the camera with a deadpan face. {TT('Mis primeros fans están muertos… Literalmente.', 'flatly, deadpan')} {END('one cat', 'a soft festive night ambience')}",
   "TOFFEE: «Mis primeros fans están muertos… Literalmente.»", "golpe de chiste → logo")

esc("1 · Azotea, amanece", "INICIO · sigue justo después del capítulo 1; la meta: saber si su humana lo busca")
tk(6, "TGZ", "Plano general fijo", f"{S(6)} {ROOF} Static wide shot, the whole bodies visible: on the left {G} sleeps curled up hugging {BALL}; on the right {T} sits awake on the roof edge, looking at the sunrise. The ball glows softly. No one speaks. {END('one cat and one dog', 'a quiet morning breeze and distant birds', dog=True)}",
   "(sin voz: amanece)", "tema de Extravío, suave")
tk(6, "TZ", "Plano medio frontal", f"{S(6)} {ROOF} Medium shot from the front: {T} sits on the roof and talks proudly straight to the camera, holding up one paw like counting. {TT('Buenos días, mis desgraciados. Ya tenemos… trece seguidores.', 'proudly, slowly')} {END('one cat', 'a quiet morning breeze')}",
   "TOFFEE: «Buenos días, mis desgraciados. Ya tenemos… trece seguidores.»", "")
tk(4, "TZ", "Primer plano", f"{S(4)} {ROOF} Close-up of {T}: his proud face drops, his ears go down, he sighs and looks at the camera, disappointed. {TT('Ah, no. Es un bot.', 'flatly, disappointed')} {END('one cat', 'a quiet morning breeze')}",
   "TOFFEE: «Ah, no. Es un bot.»", "wah wah triste")
tk(5, "GZ", "Inserto, primer plano", f"{S(5)} {ROOF} Close-up of {G} lying on the roof hugging {BALL} between his front paws; he opens his eyes, sniffs the ball and his tail starts to wag. His fur stays warm golden. No one speaks. {END('one dog', 'a quiet morning breeze', cat=False, dog=True)}",
   "(sin voz: Galleta y su pelota)", "", nota="Guiño de producto: la pelota que brilla.")
tk(8, "LZ", "Plano medio, Lucho llega", f"{S(8)} {ROOF} Medium shot: from the first frame {L} is already on the roof, walking toward the camera from the wooden stairs at the back, holding up an old iron key that glows warm orange in his right paw; a few orange marigold petals float around the key. He stops and speaks. {Q1} {LL('Esta llave abre la Tierra de los Recordados.', 'secretively, proud')} {END('one mouse', 'a quiet morning breeze', cat=False)}",
   "LUCHO: «Esta llave abre la Tierra de los Recordados.»", "brillo mágico")
tk(8, "TLZ", "Plano de dos", f"{S(8)} {ROOF} Two-shot: on the left {T} listens, on the right {L} talks, gesturing only with his right paw that holds the glowing orange key. {Q1} {LL('Allá está el Libro de los Buscados. Si alguien te busca… tu nombre aparece.', 'mysteriously')} {END('one cat and one mouse', 'a quiet morning breeze')}",
   "LUCHO: «Allá está el Libro de los Buscados. Si alguien te busca… tu nombre aparece.»", "comedia bajo el diálogo")
tk(6, "TZ", "Primer plano", f"{S(6)} {ROOF} Close-up of {T}: he lifts his chin, proud and smug, and waves a paw as if it were obvious. {TT('Obvio que me busca. Soy irremplazable.', 'smugly')} {END('one cat', 'a quiet morning breeze')}",
   "TOFFEE: «Obvio que me busca. Soy irremplazable.»", "")
tk(5, "TZ", "Primer plano, duda", f"{S(5)} {ROOF} Close-up of {T}: after a short silence his smug face softens, he looks away a little worried, then back. {TT('…Vamos. Por si acaso.', 'quietly, a little worried')} {END('one cat', 'a quiet morning breeze')}",
   "TOFFEE: «…Vamos. Por si acaso.»", "")

esc("2 · La puerta", "Toma puente: de la azotea al otro mundo")
tk(6, "TGLDZ", "Plano general", f"{S(6)} {ROOF} Static wide shot: in the middle of the roof stands an old wooden door alone, with no wall around it (like the door reference). From the first frame {L} stands in front of it, and {T} and {G} wait on the left. Lucho puts the glowing orange key into the keyhole with his right paw and turns it; the door swings open and warm orange light and marigold petals burst out. {Q1} No one speaks. {END('one cat, one dog and one mouse', 'a creaking door and a magical whoosh', dog=True)}",
   "(sin voz: se abre la puerta)", "puerta mágica")
tk(6, "TGLD", "De espaldas", f"{S(6)} Seen from behind: {T}, {G} and {L} walk slowly through the open old wooden door (like the door reference) into a wall of warm orange light full of floating marigold petals, and disappear into the light. {Q1} No one speaks. {END('one cat, one dog and one mouse', 'a warm magical whoosh', dog=True)}",
   "(sin voz: cruzan)", "whoosh")

esc("3 · La canción de bienvenida", "Los recibe la Catrina cantando (canción «Tierra del Recuerdo»)")
tk(8, "TGLNV", "Plano general desde atrás", f"{S(8)} {STREET} Static wide shot from behind and slightly above the three, seen from the back, whole bodies visible, standing in the middle of the street: on the left {T}, in the middle {G}, on the right {L}. At the far end of the street, under the arch of candles, {CA} slowly opens her arms in welcome and starts to sing. The three stay still, amazed. {Q1} {END('one cat, one dog, one mouse and one skeleton lady', 'a soft festive night ambience and her singing', dog=True)}",
   "(ella canta a lo lejos)", "canción: intro")
tk(10, "NV", "Plano medio, la cámara se acerca", f"{S(10)} {STREET} Medium shot, the camera slowly pushes in: {CA} stands under the arch of candles and sings tenderly straight to the camera like a slow bolero, gently opening her left hand toward the viewer, the bell still in her right hand. She sings in Latin American Spanish, very slowly, {VC}: \"Bienvenidos, forasteros, a la Tierra del Recuerdo.\" Her jaw moves clearly in sync with every word. Only she sings. {END('one skeleton lady', 'a soft festive night ambience and her voice', cat=False, extra='no animals appear.')}",
   "CATRINA canta: «Bienvenidos, forasteros, a la Tierra del Recuerdo»", "canción, estrofa 1")
tk(6, "TGV", "Reacción de dos", f"{S(6)} {STREET} Medium two-shot from the front, slightly low, warm candlelight on their faces: on the left {T} looks up amazed with his eyes wide and his mouth closed; on the right {G} tilts his head and slowly wags his tail, mouth closed. The cat stays cream-caramel and the dog warm golden. No one speaks. {END('one cat and one dog', 'a soft festive night ambience', dog=True)}",
   "(sin voz: asombrados)", "canción sigue")
tk(10, "NV", "Primer plano de la Catrina", f"{S(10)} {STREET} Close-up of {CA}, candles and papel picado softly out of focus behind her; she sings very slowly with tenderness, tilting her head, and at the end smiles. She sings in Latin American Spanish, {VC}: \"Aquí vive quien te piensa, solo el olvido está muerto.\" Her jaw moves clearly in sync with every word. Only she sings. {END('one skeleton lady', 'a soft festive night ambience and her voice', cat=False, extra='no animals appear.')}",
   "CATRINA canta: «Aquí vive quien te piensa, solo el olvido está muerto»", "canción, estrofa 2")
tk(8, "W", "Plano general aéreo lento", f"{S(8)} {TOWN} Slow aerial push forward over the village: the candles on the river drift slowly, papel picado moves in the breeze, tiny {EXTRAS} dance in a small square. No characters in close view. No one speaks. {END('only small skeleton villagers far away', 'a festive night ambience', cat=False, extra='no animals appear.')}",
   "(sin voz: el pueblo)", "canción: final")
tk(6, "TGLV", "Travelling lateral", f"{S(6)} {STREET} Side tracking shot: {T}, {G} and {L} walk side by side down the street, whole bodies visible, looking around amazed; a skeleton couple dances behind them and a small skeleton boy crosses in front of them carrying a tray of pan de muerto. {Q1} No one speaks. {END('one cat, one dog and one mouse', 'a festive night ambience and footsteps', dog=True, extra='the only other characters are ' + EXTRAS + '.')}",
   "(sin voz: el mundo vivo)", "pasitos")
tk(4, "TV", "Primer plano", f"{S(4)} {STREET} Close-up of {T} walking, the camera on his hat pointing forward, his eyes shining with ambition. {TT('Esto sí es contenido.', 'whispering, excited')} {END('one cat', 'a festive night ambience')}",
   "TOFFEE: «Esto sí es contenido.»", "")

esc("4 · El precio", "OBSTÁCULO 1 · para pasar hay que pagar con un recuerdo")
tk(6, "NV", "Plano medio", f"{S(6)} {STREET} Medium shot: {CA} stands in front of the arch of candles, rings her small brass bell once with her right hand and speaks to someone below the camera. {CC('Para pasar… se paga con un recuerdo.', 'calmly, with authority')} {END('one skeleton lady', 'a soft festive night ambience and a small bell', cat=False, extra='no animals appear.')}",
   "CATRINA: «Para pasar… se paga con un recuerdo.»", "campanita")
tk(5, "LV", "Plano medio", f"{S(5)} {STREET} Medium shot of {L}, looking up hopefully at someone tall in front of him and leaning forward with a hopeful smile, as if offering a deal. {Q1} {LL('¿Acepta queso?', 'hopefully')} {END('one mouse', 'a soft festive night ambience', cat=False)}",
   "LUCHO: «¿Acepta queso?»", "")
tk(3, "NV", "Primer plano", f"{S(3)} {STREET} Close-up of {CA}, looking down. {CC('No.', 'flatly')} {END('one skeleton lady', 'a soft festive night ambience', cat=False, extra='no animals appear.')}",
   "CATRINA: «No.»", "golpe de chiste")
tk(6, "TV", "Primer plano", f"{S(6)} {STREET} Close-up of {T}: he closes his eyes, takes a deep breath, embarrassed. {TT('El día que me caí del sofá en vivo. Lléveselo, por favor.', 'embarrassed, quickly')} {END('one cat', 'a soft festive night ambience')}",
   "TOFFEE: «El día que me caí del sofá en vivo. Lléveselo, por favor.»", "")
tk(6, "TNOV", "Plano de dos", f"{S(6)} {STREET} Two-shot: on the left {T} with his eyes closed; a small glowing turquoise sphere (like the memory reference) slowly floats out of his forehead and drifts to the right into the open bony hand of {CA}, who closes her hand around it. No one speaks. {END('one cat and one skeleton lady', 'a soft magical shimmer')}",
   "(sin voz: el recuerdo sale)", "brillo mágico")

esc("5 · Galleta y el xolo", "Momento tierno · el guardián del libro")
tk(6, "GJA", "Plano general", f"{S(6)} {ALTAR} Static wide shot: at the bottom of the steps sits {XO}, guarding. From the left {G} walks toward him carrying {BALL} in his mouth. No one speaks. {END('one dog and one xolo dog', 'a soft festive night ambience', cat=False, dog=True, extra='no other animals appear.')}",
   "(sin voz: Galleta se acerca)", "música tierna")
tk(8, "GJA", "Plano medio a ras de piso", f"{S(8)} {ALTAR} Low medium shot at floor level: {G} drops {BALL} and rolls it with his nose to {XO}; the xolo looks at the ball, then gently pushes it back with his nose. Both tails start to wag. No one speaks. {END('one dog and one xolo dog', 'a soft festive night ambience', cat=False, dog=True, extra='no other animals appear.')}",
   "(sin voz: se hacen amigos)", "", nota="Guiño de producto: la pelota que brilla.")

esc("6 · El guardián", "OBSTÁCULO 2 · el xolo no deja subir")
tk(6, "TJA", "Plano medio", f"{S(6)} {ALTAR} Medium shot: {T} walks confidently to the first step; {XO} stands up and blocks his way, staring at him and growling softly with his mouth closed. No one speaks. {END('one cat and one xolo dog', 'a low soft growl', extra='no other animals appear.')}",
   "(sin voz: el xolo le cierra el paso)", "gruñido")
tk(4, "TA", "Primer plano", f"{S(4)} {ALTAR} Close-up of {T}, chin up, very smug. {TT('¿Sabes quién soy?', 'smugly')} {END('one cat', 'a soft festive night ambience')}",
   "TOFFEE: «¿Sabes quién soy?»", "")
tk(4, "JA", "Primer plano", f"{S(4)} {ALTAR} Close-up of {XO}: his ears go forward and he growls a little louder, mouth closed, not aggressive. No one speaks. {END('one xolo dog', 'a low growl', cat=False, extra='no other animals appear.')}",
   "(sin voz: gruñe más)", "gruñido + golpe")
tk(6, "GJA", "Plano medio", f"{S(6)} {ALTAR} Medium shot: {G} walks in, puts {BALL} down in front of the paws of {XO} and sits; the xolo looks at the ball, then at Galleta, and slowly steps aside, leaving the steps free. No one speaks. {END('one dog and one xolo dog', 'a soft festive night ambience', cat=False, dog=True, extra='no other animals appear.')}",
   "(sin voz: el xolo los deja pasar)", "música tierna", nota="Guiño de producto: la pelota que brilla.")

esc("7 · El libro", "RECOMPENSA · su humana sí lo busca")
tk(6, "TGLA", "Desde atrás, abajo", f"{S(6)} {ALTAR} Low shot from behind: {T}, {G} and {L} climb the candlelit steps toward the glowing book, seen from the back. {Q1} No one speaks. {END('one cat, one dog and one mouse', 'soft footsteps and crackling candles', dog=True)}",
   "(sin voz: suben)", "")
tk(6, "AB", "Inserto del libro", f"{S(6)} Close shot of the enormous ancient book on its carved wooden stand on top of the altar (like the altar reference): it opens by itself and its pages flip fast in a soft turquoise glow, then stop. {NOWORDS} No characters. No one speaks. No text, letters or words anywhere; only a heavy book thud and fluttering pages.",
   "(sin voz: el libro se abre)", "libro gigante")
tk(5, "B", "Inserto de la página", f"{S(5)} Close-up of an open page of the ancient book (like the pages reference): a hand-drawn picture of a young woman holding up a paper poster with a photo of a chubby cream cat wearing a navy nightcap; the drawing glows softly turquoise; the camera pushes in slowly. {NOWORDS} No characters. No one speaks. No text, letters or words anywhere, the poster has only the photo; only a soft magical hum.",
   "(sin voz: la página de Toffee)", "música tierna")
tk(6, "TA", "Primer plano", f"{S(6)} {ALTAR} Close-up of {T}, the turquoise glow of the book on his face; his eyes become shiny with tears. {TT('Me está buscando…', 'softly, voice breaking')} {END('one cat', 'a soft magical hum')}",
   "TOFFEE: «Me está buscando…»", "")
tk(4, "TA", "Primer plano", f"{S(4)} {ALTAR} Close-up of {T}: he quickly turns his head away and rubs one eye with his paw, pretending. {TT('Tengo polvo en el ojo.', 'quickly, pretending to be fine')} {END('one cat', 'a soft magical hum')}",
   "TOFFEE: «Tengo polvo en el ojo.»", "")

esc("8 · El misterio de Max", "CONTINUACIÓN · la página arrancada")
tk(6, "GBA", "Plano medio", f"{S(6)} {ALTAR} Medium shot: {G} sniffs the pages of the enormous glowing book and turns one with his nose; it shows a drawing of a golden puppy with a navy bandana and a gold bone tag, half torn away with bite marks, covered in glowing silver moth-wing dust (like the pages reference). {NOWORDS} No one speaks. {END('one dog', 'paper rustling and a soft magical hum', cat=False, dog=True)}",
   "(sin voz: la página de Max)", "página que se rasga · suspenso")
tk(4, "GB", "Inserto", f"{S(4)} Extreme close-up: the gold bone-shaped tag on the navy bandana of {G} in the foreground, and right behind it, on the book page, the drawing of the same gold bone tag. The camera racks focus from the real tag to the drawing. {NOWORDS} No one speaks. No text, letters or words anywhere, the tags are blank; only a soft magical hum.",
   "(sin voz: la misma placa)", "", nota="Guiño de producto: la placa.")
tk(6, "LPA", "Primer plano", f"{S(6)} {ALTAR} Close-up of {L}, terrified, looking up at the night sky; far above, the huge dark shadow of moth wings glides over the candles and makes them flicker. {Q1} {LL('Eso… fue ella.', 'whispering, terrified')} {END('one mouse', 'distant heavy wings and flickering candles', cat=False)}",
   "LUCHO: «Eso… fue ella.»", "alas · suspenso")

esc("9 · Cierre", "Pregunta al público + escena tranquila para las pantallas finales")
tk(8, "TA", "Primer plano a cámara", f"{S(8)} {ALTAR} Close-up of {T} talking straight to the camera, serious and curious, the glowing book behind him. {TT('¿Quién busca a Max? ¿Y por qué la Polilla se comió su página?… Los leo.', 'seriously, then curious')} {END('one cat', 'a soft festive night ambience')}",
   "TOFFEE: «¿Quién busca a Max? ¿Y por qué la Polilla se comió su página?… Los leo.»", "misterio")
tk(5, "TA", "Primer plano a cámara", f"{S(5)} {ALTAR} Close-up of {T}, he winks at the camera. {TT('Sígueme para no perderte el próximo episodio.', 'warmly, smug')} {END('one cat', 'a soft festive night ambience')}",
   "TOFFEE: «Sígueme para no perderte el próximo episodio.»", "remate final")
tk(10, "GJA", "Plano general, la cámara se aleja", f"{S(10)} {ALTAR} Wide shot, the camera slowly pulls back: at the foot of the altar {G} and {XO} lie side by side among the candles, calm and sleepy, {BALL} glowing between their paws; petals float slowly. No one speaks. {END('one dog and one xolo dog', 'a soft festive night ambience', cat=False, dog=True, extra='no other animals appear.')}",
   "(sin voz: final tranquilo, pantallas finales)", "música tierna", nota="Guiño de producto: la pelota que brilla.")

TOMAS = [t for e in ESC for t in e['tomas']]
def page():
    e_ = html.escape; tot = sum(t['s'] for t in TOMAS)
    h = ['<h1>Extravío · Capítulo 2: La Tierra de los Recordados</h1>',
         f'<p class="sub">{len(TOMAS)} tomas ({tot // 60}:{tot % 60:02d} sin recortar) · Omni 1.1 Flash · 16:9 · duración final ≈ 4:30</p>',
         '<h2>Cómo se hace</h2><ol><li>Primero las 2 tomas de prueba: <b>C2-14</b> (la Catrina canta) y <b>C2-26</b> (Galleta y el xolo). Si salen bien, el resto.</li>'
         '<li>Fotos de cada toma: las que dice debajo del título (carpeta de recursos).</li>'
         '<li>Me mandas las tomas (respondo «✓» hasta «listo») → te mando el texto de cada voz con el ritmo medido → haces las voces → armo el capítulo.</li></ol>']
    for es in ESC:
        h.append(f'<h3>{e_(es["t"])}</h3><p class="sub">{e_(es["f"])}</p>')
        for t in es['tomas']:
            chips = ''.join(f'<span class="chip">{e_(f)}</span>' for f in t['fotos']) or '<span class="chip">sin fotos</span>'
            h.append(f'<div class="toma"><div class="meta">{t["id"]} · {t["s"]} s · {e_(t["plano"])}</div>{chips}')
            if t['cont']: h.append(f'<div class="cont">{e_(t["cont"])}</div>')
            h.append(f'<div class="voz"><b>{e_(t["quien"])}</b>' + (f' · sonido: {e_(t["sonido"])}' if t['sonido'] else '') + '</div>')
            if t['nota']: h.append(f'<div class="sub">{e_(t["nota"])}</div>')
            h.append(f'<pre>{e_(t["p"])}</pre></div>')
    return "\n".join(h)

if __name__ == '__main__':
    src = open(os.path.join(TEMP1, 'build_web.py')).read()
    head = src[src.index("head = '''") + 10: src.index("'''", src.index("head = '''") + 10)].replace('<title>El viaje de Toffee</title>', '<title>Extravío · Capítulo 2</title>')
    script = src[src.index("<script>"): src.index("</script>") + 9]
    open(os.path.join(here, 'web', 'capitulo-02.html'), 'w').write(head + '<main>' + page() + '</main>\n' + script)
    if len(sys.argv) > 1:   # imprime las tomas para el chat
        for es in ESC:
            print(f"\n### {es['t']}")
            for t in es['tomas']:
                print(f"\n**{t['id']} · {t['s']} s · {t['plano']}** · Fotos: {', '.join(f.replace('.jpg','') for f in t['fotos'])}" + (f" · _{t['nota']}_" if t['nota'] else ''))
                print('```\n' + t['p'] + '\n```')
    print('tomas:', len(TOMAS), 'segundos:', sum(t['s'] for t in TOMAS))
