# Soy Toffee · El viaje · Sección 1 (vlogs 2 a 15, 26-oct a 8-nov-2026)
# Todo en Omni 1.1 Flash (Google Flow), 9:16. Este archivo genera los prompts; build.py arma el PDF.

ST = lambda s: (f"Vertical 9:16, {s} seconds. Photorealistic smartphone video, normal lens "
                "(no fisheye, no vignette, no dark corners), sharp, natural colors, realistic physics.")

T = ("the cream-caramel British Shorthair cat from the reference (chubby, very round face, big green eyes), "
     "wearing his navy knitted nightcap with a cream pompom and a small black action camera on top of the nightcap")
G = ("the scruffy golden-brown criollo dog from the reference (thin, wiry fur, bushy eyebrows, white chest and paws), "
     "wearing only his navy bandana with a gold bone tag (no backpack)")
TR = ("the red plush sleigh-shaped pet bed from the reference photo (red velvet body, thick white fluffy fur rim, "
      "red-and-white candy-cane striped runners, black boot-shaped tips at the front; no legs, no letters or words on it)")
O = ("the dark gray padded ear muff hood from the reference (a soft balaclava-style dog hood with an oval face "
     "opening that covers his ears; NOT a ring, NOT a donut, NOT headphones)")
DIS = ("the green Christmas-tree pet costume from the reference (a soft green hooded cape with ruffled layers, a "
       "shiny gold star on top of the hood, small colorful pompoms all over, and a white cord with two white pompoms "
       "tied under the chin; the dog's face shows through the hood opening)")

# Personajes nuevos (cada uno con su ficha de referencia hecha antes en Nano Banana Pro)
LE = ("Doña Lechuza, the huge old barn owl from the reference (white heart-shaped face, golden-brown speckled "
      "feathers, big round golden eyes, tiny round glasses, a small crooked black witch hat, holding a small old lantern)")
CA = ("Calabacín, the big talking jack-o'-lantern pumpkin from the reference (bright orange, carved friendly "
      "triangle eyes and a crooked smile, curly green stem on top, warm candle light glowing inside, two tiny twig arms)")
MU = ("el Conde Murciélago, the small fluffy fruit bat from the reference (brown fur, big pointy ears, big shiny "
      "dark eyes, two tiny fangs, a tiny black cape with red lining and a tiny gold medallion)")
CH = ("the little Chupacabras from the reference (a small skinny hairless gray creature like a street puppy, big sad "
      "yellow eyes, a row of soft spikes along his back, long thin tail)")
AL = ("the giant flying alebrije jaguar from the reference (its body painted with bright Mexican folk-art patterns "
      "in pink, turquoise, yellow and orange, big colorful butterfly wings)")
LL = ("Paca, the fluffy white alpaca from the reference (thick curly white wool, long neck, a colorful Andean "
      "woven tassel on each ear)")
CHI = ("El Chihuahua Enmascarado, the tiny tan chihuahua from the reference wearing a shiny gold-and-red Mexican "
       "wrestling mask and a tiny red cape")

FICHAS = [
 ("Doña Lechuza", "LECHUZA.jpg", "Guía del Valle de Octubre. Sus ojos son los que brillaban al final del vlog 1. Habla.",
  "Character reference sheet, 2x2 grid, 1:1, photorealistic, same character in all 4 views (front, 3/4 left, side, back), plain dark blue night background: a huge old barn owl with a white heart-shaped face, golden-brown speckled feathers, big round glowing golden eyes, tiny round glasses on her beak, a small crooked black witch hat, holding a small old brass lantern with a warm flame. Friendly but mysterious grandmother look. Same hat, glasses and lantern in ALL views. No text."),
 ("Calabacín", "CALABACIN.jpg", "Calabaza que le tiene miedo a la oscuridad. Habla.",
  "Character reference sheet, 2x2 grid, 1:1, photorealistic, same character in all 4 views (front, 3/4 left, side, back), plain dark night background: a big bright orange jack-o'-lantern pumpkin with a carved friendly face (triangle eyes, crooked smile), a curly green stem on top, warm candle light glowing from inside, two tiny brown twig arms. Cute and nervous expression. No text."),
 ("Conde Murciélago", "MURCIELAGO.jpg", "Murciélago vampiro que solo toma jugo de mora. Habla.",
  "Character reference sheet, 2x2 grid, 1:1, photorealistic, same character in all 4 views (front, 3/4 left, side, back), plain dark purple background: a small fluffy fruit bat with brown fur, big pointy ears, big shiny dark eyes, two tiny white fangs, wearing a tiny black cape with red lining and a tiny gold medallion on his chest. Dramatic but cute. Same cape and medallion in ALL views. No text."),
 ("Chupacabras", "CHUPACABRAS.jpg", "No es un monstruo: es un cachorrito de la calle con miedo. No habla (gemidos).",
  "Character reference sheet, 2x2 grid, 1:1, photorealistic, same character in all 4 views (front, 3/4 left, side, back), plain dark green night background: a small skinny hairless gray creature like a scared street puppy, big sad yellow eyes, a row of soft little spikes along his back, a long thin tail. Cute, shy and harmless, not scary. No text."),
 ("Alebrije", "ALEBRIJE.jpg", "Jaguar alebrije de Día de Muertos. No habla (ruge suave).",
  "Character reference sheet, 2x2 grid, 1:1, photorealistic, same character in all 4 views (front, 3/4 left, side, back), plain dark background with orange marigold petals: a giant jaguar whose body is painted with bright Mexican folk-art patterns in pink, turquoise, yellow and orange, with big colorful butterfly wings. Majestic and friendly. No text."),
 ("Paca", "PACA.jpg", "Alpaca de Machu Picchu que escupe. No habla.",
  "Character reference sheet, 2x2 grid, 1:1, photorealistic, same character in all 4 views (front, 3/4 left, side, back), plain light blue sky background: a fluffy white alpaca with thick curly white wool, long neck, a colorful Andean woven tassel hanging from each ear, cheeky expression. No text."),
 ("Chihuahua Enmascarado", "CHIHUAHUA.jpg", "Luchador de lucha libre. No habla (ladra).",
  "Character reference sheet, 2x2 grid, 1:1, photorealistic, same character in all 4 views (front, 3/4 left, side, back), plain arena-red background: a tiny tan chihuahua wearing a shiny gold-and-red Mexican wrestling mask that covers his head but shows his big eyes, and a tiny red cape. Proud and tough pose. Same mask and cape in ALL views. No text."),
]

VOCES = [
 ("Toffee", "La de siempre (Eleven v4, estabilidad 75 %, similitud 90 %, Español)."),
 ("Doña Lechuza", "En ElevenLabs › Voice Library, busca «abuela» o «old woman» en español latino: voz mayor, ronca y cálida. Guárdala como «Lechuza» y úsala SIEMPRE."),
 ("Calabacín", "Voz de hombre joven, aguda y nerviosa (busca «nervous» o «cartoon» en español). Guárdala como «Calabacín»."),
 ("Conde Murciélago", "Voz dramática, grave y teatral (busca «dramatic» o «villain» en español). Guárdala como «Murciélago»."),
]

def H(line, who="cat", voice="in a deep, slow, sleepy male voice", verb="says"):
    subj = {"cat": "The cat", "owl": "The owl", "pumpkin": "The pumpkin", "bat": "The bat"}[who]
    part = {"cat": "His lips move", "owl": "Her beak moves", "pumpkin": "His carved mouth moves", "bat": "His mouth moves"}[who]
    return f'{subj} {verb} in Latin American Spanish, {voice}: "{line}" {part} in sync with every word.'
VL = "in an old, raspy, warm grandmother voice"
VC = "in a high, shaky, nervous young male voice"
VM = "in a deep, dramatic, theatrical male voice"

def END(cast, speaker=None, amb="soft ambience"):
    s = f"Exactly {cast} for the whole video, identical to the references; no other animals appear."
    if "cat" in cast: s += " The cat's whole head, nightcap and camera always in frame."
    if "one dog" in cast and "chihuahua" not in cast: s += " The dog never speaks."
    s += f" Only {speaker} speaks, with {amb} in the background." if speaker else f" No one speaks; only {amb}."
    return s + " No phone, no selfie stick, no text, no music."

C2 = "one cat and one dog"
# Toma: (segundos, fotos, primer_cuadro, prompt, voz_toffee, voz_otro)
VLOGS = []

# ---------------- VLOG 2 ----------------
VLOGS.append(dict(n=2, fecha="Dom 26-oct", titulo="Los ojos del bosque", arriba=("¿Quién es", "LA BRUJA DEL BOSQUE?"),
 resumen="Los ojos eran de Doña Lechuza. Les cuenta que cayeron en el Valle de Octubre, donde siempre es Halloween, y que el trineo perdió sus 5 cascabeles mágicos: sin ellos no vuela. Misión de Halloween: recuperarlos.",
 fichas=["Doña Lechuza"], tomas=[
 (6,"TOFFEE + GALLETA + TRINEO","Último cuadro de la toma 9c del vlog 1",
  f"{ST(6)} Continue exactly from the first frame: same snowy forest at night, same sleigh, same cat and dog. Static camera. The cat slowly leans forward toward the dark trees, scared, ears flat; the dog hides behind the sleigh rim. A warm lantern light slowly appears between the trees. {END(C2, amb='wind')}",
  "(sin voz)", None),
 (8,"LECHUZA",None,
  f"{ST(8)} Snowy forest at night, warm lantern light. {LE} lands on a snowy branch right in front of the camera, her golden eyes glowing, and looks down at the camera. {H('¡Por fin! Llevo tres siglos esperando visitas.', 'owl', VL)} {END('one owl', 'the owl', 'wind')}",
  None, "LECHUZA: «¡Por fin! Llevo tres siglos esperando visitas.»"),
 (6,"TOFFEE",None,
  f"{ST(6)} Snowy forest at night, warm lantern light. Medium close-up at eye level: {T} sits in the snow, looking up at something above the camera with wide shocked eyes. {H('¿Es una bruja? Galleta, es una bruja.')} {END('one cat', 'the cat', 'wind')}",
  "«¿Es una bruja? Galleta, es una bruja.»", None),
 (8,"LECHUZA",None,
  f"{ST(8)} Snowy forest at night. Close-up of {LE} on a branch, rolling her golden eyes, then pointing with her wing to a valley behind her full of glowing orange jack-o'-lanterns. {H('Bruja jubilada, mijo. Bienvenidos al Valle de Octubre. Aquí siempre es Halloween.', 'owl', VL)} {END('one owl', 'the owl', 'wind')}",
  None, "LECHUZA: «Bruja jubilada, mijo. Bienvenidos al Valle de Octubre. Aquí siempre es Halloween.»"),
 (8,"TOFFEE + GALLETA + TRINEO",None,
  f"{ST(8)} Snowy forest at night. Wide shot: {TR} lies tilted in the snow. {T} pushes it with both paws, but it does not move; {G} pulls the white fur rim with his teeth. Five small golden bells are missing from the front of the sleigh: only five empty little hooks remain. {END(C2, amb='wind and crunching snow')}",
  "«El trineo no arranca. Le faltan los cascabeles.» (voz en off)", None),
 (8,"LECHUZA",None,
  f"{ST(8)} Snowy forest at night. Close-up of {LE}, holding up her lantern, very serious. Behind her, far away, five small golden lights shine in five different places of the dark valley. {H('Cinco cascabeles cayeron en el valle. Sin ellos, ese trineo no vuelve a volar.', 'owl', VL)} {END('one owl', 'the owl', 'wind')}",
  None, "LECHUZA: «Cinco cascabeles cayeron en el valle. Sin ellos, ese trineo no vuelve a volar.»"),
 (6,"TOFFEE + GALLETA",None,
  f"{ST(6)} Snowy forest at night. Medium shot at eye level: on the left, {T} stands up decided and looks into the camera; on the right, {G} shakes his head no, slowly. {H('Cinco cascabeles. Cinco monstruos. Fácil.')} {END(C2, 'the cat', 'wind')}",
  "«Cinco cascabeles. Cinco monstruos. Fácil.»", None),
 (6,"TOFFEE + GALLETA",None,
  f"{ST(6)} Night. A path of glowing orange jack-o'-lanterns leads into a dark forest of giant pumpkins. Seen from behind, {T} on the left and {G} on the right walk slowly down the path. {END(C2, amb='crickets and a distant spooky laugh')}",
  "«Díganme en los comentarios: ¿qué monstruo nos espera?» (voz en off)", None),
]))

# ---------------- VLOG 3 ----------------
VLOGS.append(dict(n=3, fecha="Lun 27-oct", titulo="La calabaza que le tiene miedo a la oscuridad", arriba=("Encontré el", "1.er CASCABEL 🔔"),
 resumen="Bosque de calabazas gigantes. El primer cascabel está DENTRO de Calabacín, una calabaza que habla y que le tiene miedo a la oscuridad: si le sacan la vela, se queda a oscuras. Toffee le cambia el cascabel por una linterna.",
 fichas=["Calabacín"], tomas=[
 (6,"TOFFEE + CALABACÍN",None,
  f"{ST(6)} Forest of giant glowing jack-o'-lanterns at night. Close-up: {T} puts his face very close to {CA}; inside the pumpkin a small golden bell shines next to the candle. The cat's eyes go wide. {END('one cat and one pumpkin', amb='crickets')}",
  "«¿Hay un cascabel… dentro de una calabaza?» (voz en off)", None),
 (8,"TOFFEE + GALLETA",None,
  f"{ST(8)} Night path between giant glowing jack-o'-lanterns taller than a house, purple fog on the ground. Medium shot at eye level: {T} walks toward the camera; behind him, {G} walks very close to him, looking around nervous. {H('Vlog tres. Estamos en el bosque de las calabazas. Huele a sopa.')} {END(C2, 'the cat', 'crickets')}",
  "«Vlog tres. Estamos en el bosque de las calabazas. Huele a sopa.»", None),
 (8,"CALABACÍN",None,
  f"{ST(8)} Forest of giant jack-o'-lanterns at night. {CA} sits on the ground. He suddenly turns toward the camera and screams, his candle light flickering. {H('¡No me miren! ¡Me da miedo que me miren!', 'pumpkin', VC)} {END('one pumpkin', 'the pumpkin', 'crickets')}",
  None, "CALABACÍN: «¡No me miren! ¡Me da miedo que me miren!»"),
 (6,"TOFFEE + GALLETA",None,
  f"{ST(6)} Forest of giant jack-o'-lanterns at night. Medium shot: {T} and {G} jump back at the same time, scared, then freeze. {END(C2, amb='crickets')}",
  "(sin voz; efecto de susto)", None),
 (8,"TOFFEE + CALABACÍN",None,
  f"{ST(8)} Forest of giant jack-o'-lanterns at night. On the left, {T} sits calmly in front of {CA} on the right, and talks to him like a therapist. {H('Tranquilo. ¿Me das ese cascabel que tienes adentro?')} {END('one cat and one pumpkin', 'the cat', 'crickets')}",
  "«Tranquilo. ¿Me das ese cascabel que tienes adentro?»", None),
 (8,"CALABACÍN",None,
  f"{ST(8)} Forest of giant jack-o'-lanterns at night. Close-up of {CA}, shaking, his candle light trembling. {H('¡No! Si me abren, se apaga mi vela. ¡Y le tengo miedo a la oscuridad!', 'pumpkin', VC)} {END('one pumpkin', 'the pumpkin', 'crickets')}",
  None, "CALABACÍN: «¡No! Si me abren, se apaga mi vela. ¡Y le tengo miedo a la oscuridad!»"),
 (6,"GALLETA + CALABACÍN",None,
  f"{ST(6)} Forest of giant jack-o'-lanterns at night. {G} walks up to {CA} carrying a small glowing yellow lantern in his mouth, and gently places it on the ground in front of the pumpkin. The pumpkin's face lights up happy. {END('one dog and one pumpkin', amb='crickets')}",
  "«Galleta tuvo una idea. Galleta nunca tiene ideas.» (voz en off)", None),
 (6,"TOFFEE",None,
  f"{ST(6)} Forest of giant jack-o'-lanterns at night. Close-up of {T}, holding up a small shiny golden bell in his paw next to his face, proud, then looking into the camera. {H('Primer cascabel. Faltan cuatro.')} {END('one cat', 'the cat', 'crickets')}",
  "«Primer cascabel. Faltan cuatro.»", None),
 (6,"TOFFEE + GALLETA",None,
  f"{ST(6)} Night. A dark stone castle on top of a cliff, with a huge full moon behind it. Hundreds of small bats fly out of the tower windows toward the camera. In the foreground, seen from behind, {T} and {G} look up at the castle. {END(C2, amb='bats squeaking and wind')}",
  "«El segundo está en ese castillo. Y no sé si quiero ir.» (voz en off)", None),
]))

# ---------------- VLOG 4 ----------------
VLOGS.append(dict(n=4, fecha="Mar 28-oct", titulo="El vampiro que solo toma jugo de mora", arriba=("Visité el castillo", "DEL VAMPIRO 🦇"),
 resumen="Castillo del Conde Murciélago. Esperan un vampiro terrible y es un murciélago frutero chiquito que solo toma jugo de mora. Hace una fiesta con 300 murciélagos chillando: Galleta se pone sus orejeras (producto, sin decir que cura nada). El conde les da el 2.º cascabel.",
 fichas=["Conde Murciélago"], tomas=[
 (6,"TOFFEE + GALLETA",None,
  f"{ST(6)} Inside a huge dark gothic castle hall lit by candles, red velvet curtains. A giant shadow of a vampire with a cape grows on the stone wall. In the foreground, {T} and {G} hug each other, terrified. {END(C2, amb='thunder and a creaking door')}",
  "«Tenemos que salir de aquí.» (voz en off)", None),
 (6,"MURCIÉLAGO",None,
  f"{ST(6)} Gothic castle hall with candles. The camera tilts down from the giant shadow on the wall to the floor and reveals that the shadow belongs to {MU}, tiny, standing in front of a candle, opening his cape dramatically. {H('¡Bienvenidos a mi castillo!', 'bat', VM)} {END('one bat', 'the bat', 'thunder')}",
  None, "CONDE: «¡Bienvenidos a mi castillo!»"),
 (6,"TOFFEE",None,
  f"{ST(6)} Gothic castle hall with candles. Medium close-up of {T}, looking down at something small, totally unimpressed, one eyebrow up. {H('¿Ese es el vampiro? Mide lo que una papa.')} {END('one cat', 'the cat', 'thunder far away')}",
  "«¿Ese es el vampiro? Mide lo que una papa.»", None),
 (8,"MURCIÉLAGO",None,
  f"{ST(8)} Gothic castle dining table with candles. {MU} sits on the table holding a tiny glass of dark purple blackberry juice with a straw, and sips it elegantly. {H('Yo no tomo sangre. Solo jugo de mora. Sin azúcar.', 'bat', VM)} {END('one bat', 'the bat', 'soft organ music in the distance')}",
  None, "CONDE: «Yo no tomo sangre. Solo jugo de mora. Sin azúcar.»"),
 (8,"MURCIÉLAGO",None,
  f"{ST(8)} Gothic castle hall. Hundreds of small bats fly in circles near the high ceiling under a big chandelier, squeaking loudly, like a party with purple disco lights. {MU} stands on the table in front, opening his cape. {END('one bat in front and many small bats far above', amb='loud bat squeaking and party noise')}",
  "«Y hoy… hizo fiesta.» (voz en off)", None),
 (8,"GALLETA + OREJERAS",None,
  f"{ST(8)} Gothic castle hall with loud bats flying far above near the ceiling. Close-up of {G}, sitting on the floor, wearing {O}. He closes his eyes calmly and lies down, relaxed, while the party continues far above. {END('one dog', amb='muffled bat squeaking')}",
  "«Galleta trajo sus orejeras. Amortiguan el ruido. Ahora el que sufre soy yo.» (voz en off)", None),
 (8,"TOFFEE + MURCIÉLAGO",None,
  f"{ST(8)} Gothic castle dining table with candles. On the left, {T} sits at the table; on the right, {MU} hangs upside down from a candle holder and gives the cat a small shiny golden bell with his tiny foot. {H('Por soportar mi fiesta, el segundo cascabel.', 'bat', VM)} {END('one cat and one bat', 'the bat', 'soft organ music')}",
  None, "CONDE: «Por soportar mi fiesta, el segundo cascabel.»"),
 (6,"TOFFEE",None,
  f"{ST(6)} Gothic castle window at night with the full moon. Close-up of {T}, holding two small golden bells, looking into the camera. {H('Dos de cinco. Mañana vamos al mercado de las brujas.')} {END('one cat', 'the cat', 'wind')}",
  "«Dos de cinco. Mañana vamos al mercado de las brujas.»", None),
]))

# ---------------- VLOG 5 ----------------
VLOGS.append(dict(n=5, fecha="Mié 29-oct", titulo="Compré una poción en el mercado de las brujas", arriba=("Probando una", "POCIÓN DE BRUJA 🧪"),
 resumen="Mercado nocturno de las brujas (puestos flotantes con faroles). Toffee cambia una de sus galletas por una «poción para volar» para no depender del trineo. Se la toma y… flota, pero no puede bajar. Caos que crece (fórmula Gnomo). Doña Lechuza lo baja y le dice dónde está el 3.er cascabel: en el concurso de disfraces de mañana.",
 fichas=[], tomas=[
 (4,"TOFFEE",None,
  f"{ST(4)} Night sky over a glowing witches' market. {T} floats in the air like a balloon, upside down, paws waving, panicked. {END('one cat', amb='wind')}",
  "«¡Bájenme!» (voz en off, gancho)", None),
 (8,"TOFFEE + GALLETA",None,
  f"{ST(8)} A magical night market of witches: wooden stalls floating a little above the ground, hundreds of hanging orange lanterns, bubbling cauldrons with green smoke, jars of glowing potions. Medium shot: {T} walks toward the camera between the stalls, excited; {G} follows him. {H('Vlog cinco. Mercado de las brujas. Todo aquí está prohibido.')} {END(C2, 'the cat', 'busy market noise and bubbling cauldrons')}",
  "«Vlog cinco. Mercado de las brujas. Todo aquí está prohibido.»", None),
 (6,"TOFFEE",None,
  f"{ST(6)} Witches' market stall with glowing potion jars. Close-up of {T} holding up a small round glass bottle with a glowing pink liquid and a cork, looking at it with greedy eyes. {H('Poción para volar. Ya no necesito trineo.')} {END('one cat', 'the cat', 'bubbling cauldrons')}",
  "«Poción para volar. Ya no necesito trineo.»", None),
 (6,"TOFFEE + GALLETA",None,
  f"{ST(6)} Witches' market at night. On the left, {T} drinks the small glowing pink potion in one gulp; on the right, {G} watches him, worried. A soft pink glow spreads over the cat's body. {END(C2, amb='bubbling cauldrons and a magic shimmer')}",
  "(sin voz)", None),
 (6,"TOFFEE",None,
  f"{ST(6)} Witches' market at night. {T} slowly lifts off the ground and floats up past the lanterns, surprised and happy at first, paws open. {END('one cat', amb='magic shimmer')}",
  "«Funciona. Funciona.» (voz en off)", None),
 (8,"TOFFEE",None,
  f"{ST(8)} Night sky above the witches' market, the market lanterns far below. {T} keeps floating higher and higher, now panicked, paws waving, his pompom flapping in the wind. {H('¿Cómo se baja? ¿Alguien sabe cómo se baja?')} {END('one cat', 'the cat', 'wind')}",
  "«¿Cómo se baja? ¿Alguien sabe cómo se baja?»", None),
 (6,"GALLETA",None,
  f"{ST(6)} Witches' market at night. {G} looks up at the sky, then runs between the stalls barking toward the sky. {END('one dog', amb='market noise')}",
  "(sin voz)", None),
 (8,"TOFFEE + LECHUZA",None,
  f"{ST(8)} Night sky above the witches' market. {LE} flies next to the floating cat and pulls him down gently by his nightcap pompom with her beak. {H('Esa poción era para globos, mijo. Mañana hay concurso de disfraces. El premio es un cascabel.', 'owl', VL)} {END('one cat and one owl', 'the owl', 'wind')}",
  None, "LECHUZA: «Esa poción era para globos, mijo. Mañana hay concurso de disfraces. El premio es un cascabel.»"),
 (6,"TOFFEE",None,
  f"{ST(6)} Witches' market at night. Close-up of {T}, back on the ground, still slightly pink, looking into the camera with a determined face. {H('¿Disfraces? Galleta… tengo el disfraz perfecto.')} {END('one cat', 'the cat', 'market noise')}",
  "«¿Disfraces? Galleta… tengo el disfraz perfecto.»", None),
]))

# ---------------- VLOG 6 ----------------
VLOGS.append(dict(n=6, fecha="Jue 30-oct", titulo="Concurso de disfraces de monstruos", arriba=("El disfraz MÁS", "ATERRADOR 🎃"),
 resumen="Concurso de disfraces del valle: zombis, momias, brujas. Galleta sale disfrazado de árbol de Navidad (producto). Los monstruos gritan de miedo: en el Valle de Octubre lo más aterrador es la Navidad. Gana el 3.er cascabel. Para TikTok: usar el sonido de moda del «costume walk» al subir.",
 fichas=[], tomas=[
 (6,"GALLETA + DISFRAZ",None,
  f"{ST(6)} A spooky costume parade at night with a purple stage, orange lights and fog. {G}, wearing {DIS}, walks proudly down the runway toward the camera like a model. {END('one dog', amb='crowd cheering')}",
  "(sin voz; gancho con el sonido de moda)", None),
 (8,"TOFFEE",None,
  f"{ST(8)} Backstage of a spooky costume contest at night, orange lights, fog. Medium close-up of {T}, looking into the camera, excited. {H('Vlog seis. Concurso de disfraces de monstruos. El premio: el tercer cascabel.')} {END('one cat', 'the cat', 'crowd noise')}",
  "«Vlog seis. Concurso de disfraces de monstruos. El premio: el tercer cascabel.»", None),
 (8,"ESCENARIO",None,
  f"{ST(8)} A spooky costume runway at night with purple and orange lights and fog. Three people in classic Halloween costumes walk one after another: a mummy wrapped in bandages, a green-faced witch with a broom, a zombie in torn clothes. No animals. No one speaks; only crowd cheering. No phone, no text, no music.",
  "«La competencia está dura.» (voz en off)", None),
 (6,"TOFFEE + GALLETA",None,
  f"{ST(6)} Backstage at night. On the left, {T} pushes {G}, who wears {DIS}, toward the stage curtain. The dog looks at the camera, embarrassed. {END(C2, amb='crowd noise')}",
  "«Confía en mí.» (voz en off)", None),
 (8,"GALLETA + DISFRAZ",None,
  f"{ST(8)} A spooky costume runway at night, purple and orange lights, fog, a crowd of shadowy monsters watching from the dark. {G}, wearing {DIS}, walks onto the stage; the colorful pompoms and the gold star shine under the lights. The crowd of monsters gasps and steps back. {END('one dog', amb='crowd gasping')}",
  "(sin voz)", None),
 (6,"LECHUZA",None,
  f"{ST(6)} Judges' table at a spooky costume contest at night. Close-up of {LE}, wearing her witch hat, dropping her lantern in shock. {H('¡Un árbol de Navidad! ¡Lo más aterrador que he visto!', 'owl', VL)} {END('one owl', 'the owl', 'crowd screaming')}",
  None, "LECHUZA: «¡Un árbol de Navidad! ¡Lo más aterrador que he visto!»"),
 (8,"TOFFEE + GALLETA",None,
  f"{ST(8)} Spooky costume stage at night, confetti in orange and purple falling. On the right, {G}, wearing {DIS}, sits proudly with a small golden bell hanging from the star on top; on the left, {T} hugs him. {H('Aquí lo que da miedo es la Navidad. Tercer cascabel.')} {END(C2, 'the cat', 'crowd cheering')}",
  "«Aquí lo que da miedo es la Navidad. Tercer cascabel.»", None),
 (6,"TOFFEE",None,
  f"{ST(6)} Night, a big glowing full moon over the valley. Close-up of {T}, looking into the camera, mysterious. {H('Mañana es treinta y uno. Y en el valle dicen que sale algo…')} {END('one cat', 'the cat', 'wind and a distant howl')}",
  "«Mañana es treinta y uno. Y en el valle dicen que sale algo…»", None),
]))

# ---------------- VLOG 7 ----------------
VLOGS.append(dict(n=7, fecha="Vie 31-oct · HALLOWEEN", titulo="La canción de la Noche del Miau", arriba=("Hicimos una", "CANCIÓN DE HALLOWEEN 🎶"),
 resumen="Noche de Halloween: todos los personajes del valle hacen una fiesta y suena la canción original «La Noche del Miau» (letra abajo; se hace en Suno). Es un videoclip: tomas de baile SIN que nadie hable. Al final, Doña Lechuza dice que el 4.º cascabel lo robó el Chupacabras.",
 fichas=[], tomas=[
 (6,"TOFFEE + GALLETA",None,
  f"{ST(6)} A huge Halloween party in a forest clearing at night: hundreds of glowing jack-o'-lanterns, purple and orange lights, fog, a big full moon. {T} and {G} dance in the middle, jumping happily. {END(C2, amb='party noise')}",
  "(canción)", None),
 (6,"CALABACÍN + MURCIÉLAGO",None,
  f"{ST(6)} Halloween party at night, orange and purple lights. {CA} wiggles his tiny twig arms dancing, holding a small lantern; next to him {MU} spins in the air with his cape open. {END('one pumpkin and one bat', amb='party noise')}",
  "(canción)", None),
 (6,"LECHUZA",None,
  f"{ST(6)} Halloween party at night. {LE} dances on a branch, swinging her lantern left and right, her witch hat bouncing. {END('one owl', amb='party noise')}",
  "(canción)", None),
 (6,"TOFFEE",None,
  f"{ST(6)} Halloween party at night, purple lights. Close-up of {T} nodding his head to the beat, eyes closed, very serious, like a DJ. {END('one cat', amb='party noise')}",
  "(canción)", None),
 (6,"GALLETA",None,
  f"{ST(6)} Halloween party at night. {G} jumps and spins in a circle chasing his tail, happy, with orange confetti falling. {END('one dog', amb='party noise')}",
  "(canción)", None),
 (8,"TODOS",None,
  f"{ST(8)} Wide shot of a Halloween party in a forest clearing at night under a big full moon, with fireworks far away in the sky. In the middle: {T}, {G}, {CA}, {MU} and {LE} together, all looking at the camera. Exactly one cat, one dog, one pumpkin, one bat and one owl, identical to the references; no other animals; the cat's whole head, nightcap and camera always in frame. No one speaks; only party noise. No phone, no text, no music.",
  "(final de la canción)", None),
 (8,"LECHUZA + TOFFEE",None,
  f"{ST(8)} End of the Halloween party at night, quiet now, fog. On the right, {LE} leans close to {T} on the left and whispers. {H('El cuarto cascabel… se lo llevó el Chupacabras.', 'owl', VL, 'whispers')} {END('one cat and one owl', 'the owl', 'wind')}",
  None, "LECHUZA (susurro): «El cuarto cascabel… se lo llevó el Chupacabras.»"),
]))

# ---------------- VLOG 8 ----------------
VLOGS.append(dict(n=8, fecha="Sáb 1-nov", titulo="Buscamos al Chupacabras", arriba=("Encontramos al", "CHUPACABRAS 😱"),
 resumen="Siguen huellas por un pantano de luciérnagas. Esperan un monstruo y el Chupacabras es un cachorrito sin pelo, flaquito y asustado, que agarró el cascabel porque nunca había tenido nada suyo. Momento de corazón: Toffee lo apunta en su lista de «animales que merecen un regalo» y él, solito, le devuelve el cascabel: el 4.º.",
 fichas=["Chupacabras"], tomas=[
 (6,"TOFFEE + GALLETA",None,
  f"{ST(6)} A dark swamp at night full of floating purple fireflies, twisted trees, mist on the water. Close-up of small strange footprints in the mud. {T} and {G} lean over the footprints, scared. {END(C2, amb='frogs and crickets')}",
  "«Huellas de Chupacabras.» (voz en off)", None),
 (8,"TOFFEE",None,
  f"{ST(8)} Swamp of purple fireflies at night. Medium close-up of {T}, whispering to the camera, eyes wide. {H('Vlog ocho. Dicen que el Chupacabras se come a los gatos. Yo soy un gato.', verb='whispers')} {END('one cat', 'the cat', 'frogs')}",
  "«Vlog ocho. Dicen que el Chupacabras se come a los gatos. Yo soy un gato.» (susurro)", None),
 (6,"CHUPACABRAS",None,
  f"{ST(6)} Swamp at night, behind a fallen tree trunk. Only a pair of big glowing yellow eyes and a row of spikes are visible in the dark behind the trunk. {END('one creature', amb='a low growl')}",
  "(sin voz)", None),
 (8,"TOFFEE + GALLETA",None,
  f"{ST(8)} Swamp at night with purple fireflies. {T} and {G} slowly peek over the fallen tree trunk, scared, ready to run. {END(C2, amb='frogs')}",
  "«A la cuenta de tres corremos. Uno…» (voz en off)", None),
 (8,"CHUPACABRAS",None,
  f"{ST(8)} Swamp at night, behind the fallen tree trunk, purple fireflies give soft light. Reveal: {CH} is curled up and shaking, hugging a small golden bell with his paws like a toy. He looks up with big sad eyes. {END('one creature', amb='soft whimpering and frogs')}",
  "«No es un monstruo… es un cachorrito.» (voz en off)", None),
 (8,"TOFFEE + CHUPACABRAS",None,
  f"{ST(8)} Swamp at night with purple fireflies. On the left, {T} sits close to {CH} on the right and gently puts his paw on the little creature's head. The creature stops shaking. {H('Nunca había tenido nada suyo. Por eso lo agarró.')} {END('one cat and one creature', 'the cat', 'frogs')}",
  "«Nunca había tenido nada suyo. Por eso lo agarró.»", None),
 (8,"TOFFEE",None,
  f"{ST(8)} Swamp at night. Close-up of {T} writing in a small old notebook with a pencil held in his paw, by the light of the fireflies. {END('one cat', amb='frogs')}",
  "«Lista de animales que merecen un regalo. Número uno: el Chupacabras.» (voz en off)", None),
 (6,"TOFFEE + GALLETA + CHUPACABRAS",None,
  f"{ST(6)} Swamp at night. Seen from behind, {T}, {G} and {CH} walk together along a path of purple fireflies toward a far orange glow. {END('one cat, one dog and one creature', amb='frogs')}",
  "«Ustedes en los comentarios: ¿qué animalito pongo de número dos?» (voz en off)", None),
]))
VLOGS[-1]['tomas'].insert(7,(6,"TOFFEE + CHUPACABRAS",None,
  f"{ST(6)} Swamp at night with purple fireflies. On the right, {CH} pushes the small golden bell with his nose into the paws of {T} on the left, then wags his thin tail. {END('one cat and one creature', amb='frogs and a soft bell ring')}",
  "«Me lo devolvió. Cuarto cascabel.» (voz en off)", None))

# ---------------- VLOG 9 ----------------
VLOGS.append(dict(n=9, fecha="Dom 2-nov · DÍA DE MUERTOS", titulo="El puente de flores del Día de Muertos", arriba=("Cruzamos el", "PUENTE DE FLORES 🌼"),
 resumen="Día de Muertos (público de México). El valle se llena de flores de cempasúchil y un puente de pétalos que brilla. Un alebrije jaguar los lleva volando hasta un altar para los animalitos que nunca tuvieron casa. Toffee deja un regalo en el altar. El alebrije les da el 5.º y último cascabel. Momento emotivo, con respeto.",
 fichas=["Alebrije"], tomas=[
 (8,"TOFFEE + GALLETA",None,
  f"{ST(8)} Night. A long glowing bridge made of orange marigold petals crosses a dark valley, with floating candles and papel picado banners in bright colors. Seen from behind, {T} on the left and {G} on the right walk onto the bridge, amazed. {END(C2, amb='soft wind and distant guitar')}",
  "«Hoy en el valle es Día de Muertos.» (voz en off)", None),
 (6,"TOFFEE",None,
  f"{ST(6)} Marigold petal bridge at night with floating candles. Medium close-up of {T}, looking around with shining eyes, a few orange petals floating around him. {H('Vlog nueve. Nunca había visto algo tan bonito.')} {END('one cat', 'the cat', 'soft wind')}",
  "«Vlog nueve. Nunca había visto algo tan bonito.»", None),
 (8,"ALEBRIJE",None,
  f"{ST(8)} Night sky over the marigold valley. {AL} flies slowly toward the camera, flapping its colorful butterfly wings, and lands on the petal bridge. {END('one alebrije', amb='wind from the wings')}",
  "(sin voz; rugido suave)", None),
 (8,"TOFFEE + GALLETA + ALEBRIJE",None,
  f"{ST(8)} Night sky. {T} and {G} ride on the back of {AL}, flying over a valley full of orange marigolds and candles. The cat holds on tight, the dog's ears fly in the wind. {END('one cat, one dog and one alebrije', amb='wind')}",
  "«Nos llevó volando.» (voz en off)", None),
 (8,"ALTAR",None,
  f"{ST(8)} Night. A big colorful altar decorated with orange marigolds, candles, papel picado and many small framed drawings of street dogs and cats. Slow camera push toward the altar. No animals. No one speaks; only soft wind and distant guitar. No phone, no text, no music.",
  "«Un altar para los animalitos que nunca tuvieron casa.» (voz en off)", None),
 (8,"TOFFEE",None,
  f"{ST(8)} In front of the marigold altar with candles at night. {T} gently places a small wrapped red gift box on the altar with his paws, then sits and looks at it quietly. {END('one cat', amb='soft wind')}",
  "«Por eso hacemos este viaje. Todos merecen un regalo.» (voz en off)", None),
 (6,"TOFFEE + ALEBRIJE",None,
  f"{ST(6)} Marigold altar at night. {AL} lowers its head next to {T} and drops a small golden bell from its mouth into the cat's paws. {END('one cat and one alebrije', amb='soft wind')}",
  "«Quinto cascabel.» (voz en off)", None),
 (6,"TOFFEE",None,
  f"{ST(6)} Marigold bridge at night. Close-up of {T}, holding four small golden bells, looking into the camera with a soft smile. {H('Cinco de cinco. ¡El trineo puede volver a volar!')} {END('one cat', 'the cat', 'soft wind')}",
  "«Cinco de cinco. ¡El trineo puede volver a volar!»", None),
]))

# ---------------- VLOG 10 ----------------
VLOGS.append(dict(n=10, fecha="Lun 3-nov", titulo="Adiós al valle y el mapa encantado", arriba=("¡EL TRINEO", "VUELVE A VOLAR! 🛷"),
 resumen="Doña Lechuza les cuenta que nadie lo había logrado y les regala un mapa encantado que brilla donde hay un animalito que necesita un regalo. Despegan y se despiden del valle (Calabacín, el Conde y el Chupacabras dicen adiós). El mapa brilla en Colombia: Valle de Cocora.",
 fichas=[], tomas=[
 (8,"TOFFEE + LECHUZA",None,
  f"{ST(8)} Snowy forest at the edge of the valley at night, lantern light. On the right, {LE} on a low branch smiles proudly; on the left, {T} looks up at her. {H('Cinco cascabeles. En trescientos años nadie lo había logrado.', 'owl', VL)} {END('one cat and one owl', 'the owl', 'wind')}",
  None, "LECHUZA: «Cinco cascabeles. En trescientos años nadie lo había logrado.»"),
 (6,"TOFFEE",None,
  f"{ST(6)} Snowy forest at night. Close-up of {T}, proud, puffing his chest, looking into the camera. {H('Nadie. Solo yo. Y Galleta… un poquito.')} {END('one cat', 'the cat', 'wind')}",
  "«Nadie. Solo yo. Y Galleta… un poquito.»", None),
 (8,"LECHUZA",None,
  f"{ST(8)} Snowy forest at night. {LE} unrolls an old paper map with her wing; small golden lights glow on the map in different places. {H('Este mapa brilla donde hay un animal que necesita un regalo. Síganlo hasta el Polo Norte.', 'owl', VL)} {END('one owl', 'the owl', 'wind')}",
  None, "LECHUZA: «Este mapa brilla donde hay un animal que necesita un regalo. Síganlo hasta el Polo Norte.»"),
 (6,"TRINEO",None,
  f"{ST(6)} Close-up of the front of {TR} in the snow at night: five small golden bells click into place one by one on five little hooks and start to glow warm gold. No animals in the shot. No one speaks; only five soft bell rings. No phone, no text, no music.",
  "(sin voz; cinco campanitas)", None),
 (8,"TOFFEE + GALLETA + TRINEO",None,
  f"{ST(8)} Snowy forest at night. {TR}, with {T} at the front and {G} behind him, glows with golden sparkles and lifts off the snow. Below, waving goodbye: {CA} holding his lantern, {MU} flying, and {CH} wagging his tail. Exactly one cat, one dog, one pumpkin, one bat and one creature; the cat's whole head, nightcap and camera always in frame. No one speaks; only bells and wind. No phone, no text, no music.",
  "«Gracias, valle. Volveremos.» (voz en off)", None),
 (8,"TOFFEE + GALLETA + TRINEO",None,
  f"{ST(8)} Sunrise sky above the clouds, golden light. {TR} flies toward the camera; {T} at the front holds the old map open with his paws, and one golden light on the map starts to shine. {G} sits behind him. {H('El mapa dice… ¡Colombia!')} {END(C2, 'the cat', 'wind and bells')}",
  "«El mapa dice… ¡Colombia!»", None),
 (8,"PAISAJE",None,
  f"{ST(8)} Drone shot at sunrise over the Cocora Valley in Colombia: very tall thin wax palm trees rising from green misty mountains, soft fog, golden light. A small red flying sleigh crosses the sky far away. No one speaks; only wind. No phone, no text, no music.",
  "«Siguiente parada: Valle de Cocora.» (voz en off)", None),
]))

# ---------------- VLOG 11 ----------------
VLOGS.append(dict(n=11, fecha="Mar 4-nov", titulo="Galleta maneja un Willys en Salento", arriba=("Galleta MANEJA", "UN WILLYS 🚙"),
 resumen="Colombia (orgullo local): Cocora y Salento. Aterrizan entre las palmas de cera. Un perro callejero viejito de Salento duerme al frío: el mapa brilla sobre él (número 2 de la lista). Para alcanzarlo bajan al pueblo… en un Willys que maneja Galleta. Caos y risa. Toffee le deja su gorrito de dormir para que no tenga frío… y se arrepiente al instante (pero no se lo quita: es su sello; se lo devuelve el perro).",
 fichas=[], tomas=[
 (6,"TOFFEE + GALLETA",None,
  f"{ST(6)} Cocora Valley, Colombia, morning: very tall wax palm trees, green mountains, fog. On the left, {T} looks up at the giant palms with his mouth open; on the right, {G} sniffs the grass. {H('Vlog once. Estas palmas miden como cincuenta Galletas.')} {END(C2, 'the cat', 'birds and wind')}",
  "«Vlog once. Estas palmas miden como cincuenta Galletas.»", None),
 (6,"TOFFEE + MAPA",None,
  f"{ST(6)} Cocora Valley morning. Close-up of {T} holding the old paper map; one golden light on it pulses brighter. {END('one cat', amb='birds')}",
  "«El mapa dice que es en el pueblo de abajo.» (voz en off)", None),
 (8,"GALLETA + WILLYS",None,
  f"{ST(8)} A colorful old Colombian Willys jeep parked on a mountain road near Salento, Colombia. {G} sits in the driver's seat with his paws on the steering wheel, looking at the camera, proud. {T} sits in the passenger seat, gripping the door, nervous. {END(C2, amb='birds')}",
  "«Galleta dice que sabe manejar. Galleta no sabe manejar.» (voz en off)", None),
 (8,"WILLYS",None,
  f"{ST(8)} Drone shot following the colorful old Willys jeep zig-zagging down a green mountain road near Salento, Colombia, too fast, leaving dust. Inside, the dog drives and the cat holds on. Exactly one cat and one dog. No one speaks; only engine noise and a happy bark. No phone, no text, no music.",
  "«¡Galleta, freno! ¡FRENO!» (voz en off)", None),
 (8,"PERRO DE SALENTO",None,
  f"{ST(8)} Colorful street in Salento, Colombia, with painted balconies, early morning, cold. An old skinny black street dog with gray whiskers sleeps curled up on a sidewalk, shivering. No other animals. No one speaks; only soft street sounds. No phone, no text, no music.",
  "«Ahí está. Número dos de la lista. Tiene frío.» (voz en off)", None),
 (8,"TOFFEE + PERRO",None,
  f"{ST(8)} Colorful street in Salento, Colombia. {T} sits next to the old black street dog and gently covers him with a small soft red blanket using his paws. The old dog stops shivering and wags his tail slowly. Exactly one cat and one dog (the old black dog); the cat's whole head, nightcap and camera always in frame. No one speaks; only street sounds. No phone, no text, no music.",
  "«Por ahora, una cobija. En Navidad vuelvo con tu regalo.» (voz en off)", None),
 (6,"TOFFEE",None,
  f"{ST(6)} Salento street, Colombia. Close-up of {T} writing in his small notebook with a pencil, then looking into the camera. {H('Número dos: el abuelo de Salento. ¿Quién sigue?')} {END('one cat', 'the cat', 'street sounds')}",
  "«Número dos: el abuelo de Salento. ¿Quién sigue?»", None),
]))

# ---------------- VLOG 12 ----------------
VLOGS.append(dict(n=12, fecha="Mié 5-nov", titulo="Una alpaca me escupió en Machu Picchu", arriba=("Me ESCUPIÓ una", "ALPACA 🦙"),
 resumen="Perú. El mapa los lleva a Machu Picchu. Paca, una alpaca, se cree la dueña del lugar y le escupe a Toffee (gag viral). Al final Paca los guía a una alpaquita bebé que se perdió de su mamá (número 3 de la lista) y ayudan a encontrarla.",
 fichas=["Paca"], tomas=[
 (8,"PAISAJE",None,
  f"{ST(8)} Drone shot of Machu Picchu, Peru, at sunrise: ancient stone ruins on a green mountain, clouds below, golden light. A small red flying sleigh lands softly on the grass terraces. No one speaks; only wind. No phone, no text, no music.",
  "«Vlog doce. Perú. Machu Picchu.» (voz en off)", None),
 (6,"TOFFEE",None,
  f"{ST(6)} Machu Picchu grass terrace at sunrise. Medium close-up of {T} posing proudly in front of the ruins, looking into the camera. {H('Foto para mi mamá. Sonrían.')} {END('one cat', 'the cat', 'wind')}",
  "«Foto para mi mamá. Sonrían.»", None),
 (6,"PACA",None,
  f"{ST(6)} Machu Picchu terrace. {LL} walks into the frame from the right, stops next to the camera and stares at it with a judging face. {END('one alpaca', amb='wind')}",
  "«¿Y esta quién es?» (voz en off)", None),
 (6,"TOFFEE + PACA",None,
  f"{ST(6)} Machu Picchu terrace. On the right, {LL} spits a small splash of water onto the face of {T} on the left. The cat freezes with wet fur on his face and closes his eyes slowly. {END('one cat and one alpaca', amb='wind and a spit sound')}",
  "(sin voz; efecto de escupida)", None),
 (6,"TOFFEE",None,
  f"{ST(6)} Machu Picchu terrace. Close-up of {T} with wet fur on his face, eyes half closed, looking into the camera, very offended. {H('Me escupió. Patrimonio de la humanidad y me escupió.')} {END('one cat', 'the cat', 'wind')}",
  "«Me escupió. Patrimonio de la humanidad y me escupió.»", None),
 (8,"PACA + GALLETA",None,
  f"{ST(8)} Machu Picchu terraces. {LL} walks ahead along a stone path, turning her head as if saying 'follow me'; {G} follows her, wagging his tail. Exactly one alpaca and one dog. No one speaks; only wind. No phone, no text, no music.",
  "«Galleta ya se hizo su amigo. Traidor.» (voz en off)", None),
 (8,"ALPAQUITA",None,
  f"{ST(8)} Behind an ancient stone wall at Machu Picchu: a tiny baby alpaca with fluffy white wool lies alone, crying softly. {LL} runs to it and rubs her head against the baby. Exactly two alpacas. No one speaks; only soft crying and wind. No phone, no text, no music.",
  "«Era su bebé. Se había perdido. Número tres de la lista.» (voz en off)", None),
 (6,"TOFFEE + PACA",None,
  f"{ST(6)} Machu Picchu at sunset. On the right, {LL} rubs her head softly against {T} on the left, like saying thank you. The cat looks at the camera, surprised and happy. {END('one cat and one alpaca', amb='wind')}",
  "«Igual me debe una lavada.» (voz en off)", None),
]))

# ---------------- VLOG 13 ----------------
VLOGS.append(dict(n=13, fecha="Jue 6-nov", titulo="Un ovni se llevó a Galleta en Atacama", arriba=("Un OVNI se llevó", "A GALLETA 🛸"),
 resumen="Chile. Desierto de Atacama de noche, el cielo más estrellado del mundo. Un ovni se lleva a Galleta con un rayo de luz. Toffee entra en pánico. Galleta vuelve… con un regalo de los extraterrestres: una pelotita que brilla. El mapa marca el siguiente: México.",
 fichas=[], tomas=[
 (8,"PAISAJE",None,
  f"{ST(8)} Atacama Desert, Chile, at night: red rocky desert, the Milky Way bright across the whole sky, millions of stars. A small red sleigh rests on the sand far away. No one speaks; only desert wind. No phone, no text, no music.",
  "«Vlog trece. Chile. Desierto de Atacama. El cielo más estrellado del mundo.» (voz en off)", None),
 (6,"TOFFEE + GALLETA",None,
  f"{ST(6)} Atacama Desert at night under the Milky Way. On the left, {T} lies on his back on the sand looking at the stars; on the right, {G} lies next to him. {H('Dicen que aquí se ven ovnis. Mentiras.')} {END(C2, 'the cat', 'desert wind')}",
  "«Dicen que aquí se ven ovnis. Mentiras.»", None),
 (8,"GALLETA + OVNI",None,
  f"{ST(8)} Atacama Desert at night. A round silver flying saucer with blue lights appears above. A soft blue beam of light shines down on {G}, who slowly floats up into the beam, surprised, paws dangling. {END('one dog', amb='a deep humming sound')}",
  "(sin voz; zumbido)", None),
 (6,"TOFFEE",None,
  f"{ST(6)} Atacama Desert at night, blue light flashing on him. Close-up of {T} running toward the camera in panic, ears back. {H('¡Galleta! ¡Devuélvanme a mi perro!')} {END('one cat', 'the cat', 'humming')}",
  "«¡Galleta! ¡Devuélvanme a mi perro!»", None),
 (6,"OVNI",None,
  f"{ST(6)} Atacama Desert at night. The silver flying saucer flies away fast across the Milky Way and disappears. No animals in the shot. No one speaks; only a fading hum. No phone, no text, no music.",
  "(sin voz)", None),
 (6,"TOFFEE",None,
  f"{ST(6)} Atacama Desert at night. {T} sits alone on the sand, looking at the empty sky, sad. {END('one cat', amb='desert wind')}",
  "«Galleta…» (voz en off)", None),
 (8,"TOFFEE + GALLETA",None,
  f"{ST(8)} Atacama Desert at night. A blue beam of light softly sets {G} back on the sand next to {T}. The dog holds a small glowing blue ball in his mouth and wags his tail. The cat hugs him. {END(C2, amb='soft hum')}",
  "«Volvió. Y con regalo de los extraterrestres.» (voz en off)", None),
 (6,"TOFFEE + MAPA",None,
  f"{ST(6)} Atacama Desert at night. Close-up of {T} holding the old map; a new golden light pulses on it. He looks into the camera. {H('Siguiente parada: México. Y dicen que allá hay lucha libre.')} {END('one cat', 'the cat', 'desert wind')}",
  "«Siguiente parada: México. Y dicen que allá hay lucha libre.»", None),
]))

# ---------------- VLOG 14 ----------------
VLOGS.append(dict(n=14, fecha="Vie 7-nov", titulo="Lucha libre contra el Chihuahua Enmascarado", arriba=("Me subí a un", "RING DE LUCHA LIBRE 🤼"),
 resumen="México. Arena de lucha libre. El Chihuahua Enmascarado desafía a Toffee. Toffee se pone una máscara de luchador encima del gorro (el gorro sigue debajo, con la cámara). Pelea cómica: Toffee gana sin hacer nada (se acuesta y el chihuahua se cansa). El chihuahua es número 4 de la lista: quiere un juguete.",
 fichas=["Chihuahua Enmascarado"], tomas=[
 (8,"ARENA",None,
  f"{ST(8)} A colorful Mexican lucha libre arena at night, bright lights, a ring with red ropes, a cheering crowd in the dark around it, papel picado hanging. Drone shot moving toward the ring. No animals in the shot. No one speaks; only a cheering crowd. No phone, no text, no music.",
  "«Vlog catorce. México. Lucha libre.» (voz en off)", None),
 (6,"CHIHUAHUA",None,
  f"{ST(6)} Inside the lucha libre ring under bright lights. {CHI} stands on the corner ropes, opens his tiny red cape and barks at the camera, very tough. {END('one dog (the chihuahua)', amb='crowd cheering')}",
  "«Y me retaron.» (voz en off)", None),
 (6,"TOFFEE",None,
  f"{ST(6)} Lucha libre locker room. Medium close-up of {T} wearing a shiny silver-and-blue lucha libre mask OVER his navy nightcap (the nightcap, pompom and action camera still visible on top), looking into the camera, serious. {H('Me llamo… el Gato Dormilón.')} {END('one cat', 'the cat', 'distant crowd')}",
  "«Me llamo… el Gato Dormilón.»", None),
 (8,"TOFFEE + CHIHUAHUA",None,
  f"{ST(8)} Inside the lucha libre ring. On the right, {CHI} runs in circles around {T} on the left, who wears the silver-and-blue mask over his nightcap and simply lies down on the ring floor and closes his eyes. {END('one cat and one dog (the chihuahua)', amb='crowd laughing')}",
  "«Mi técnica secreta: no hacer nada.» (voz en off)", None),
 (6,"CHIHUAHUA",None,
  f"{ST(6)} Inside the lucha libre ring. {CHI} stops running, out of breath, and lies down flat on his back, exhausted, tongue out. {END('one dog (the chihuahua)', amb='crowd cheering')}",
  "(sin voz)", None),
 (6,"GALLETA",None,
  f"{ST(6)} Ringside of the lucha libre arena. {G} rings a small bell with his paw three times, like a referee, wagging his tail. {END('one dog', amb='bell rings and crowd cheering')}",
  "«¡Ganó el Gato Dormilón!» (voz en off)", None),
 (8,"TOFFEE + CHIHUAHUA",None,
  f"{ST(8)} Inside the lucha libre ring, confetti falling. On the left, {T} with the mask over his nightcap and, on the right, {CHI} sit together; the chihuahua lifts his mask a little and looks at the camera with sad eyes. {END('one cat and one dog (the chihuahua)', amb='crowd')}",
  "«Me contó que nunca le han regalado un juguete. Número cuatro de la lista.» (voz en off)", None),
 (6,"TOFFEE",None,
  f"{ST(6)} Night sky above Mexico City, the sleigh flying. Close-up of {T} without the wrestling mask, in his nightcap, holding the old map, worried. {H('El mapa… se está volviendo loco.')} {END('one cat', 'the cat', 'wind')}",
  "«El mapa… se está volviendo loco.»", None),
]))

# ---------------- VLOG 15 ----------------
VLOGS.append(dict(n=15, fecha="Sáb 8-nov", titulo="Nos estrellamos en Nueva York", arriba=("Nos estrellamos en", "NUEVA YORK 🗽"),
 resumen="Llega Estados Unidos. Una tormenta los saca de ruta y aterrizan de emergencia en Times Square, entre pantallas gigantes y taxis amarillos. Toffee cree que todas las pantallas son para él (vanidad = chiste). El mapa se llena de cientos de luces: son demasiados animales, Toffee solo no puede y le pide ayuda al público. Final con suspenso: todas las pantallas se apagan y se oye un «jo, jo, jo»… ¿Santa los está vigilando?",
 fichas=[], tomas=[
 (8,"TOFFEE + GALLETA + TRINEO",None,
  f"{ST(8)} Stormy night sky with dark clouds and lightning far away. {TR} with {T} at the front and {G} behind him shakes in the strong wind and rain; the cat holds an old paper map tight. {END(C2, amb='thunder far away and rain')}",
  "«Vlog quince. Nos agarró una tormenta.» (voz en off)", None),
 (8,"TOFFEE + GALLETA + TRINEO",None,
  f"{ST(8)} Times Square, New York, at night, wet street, huge bright advertising screens all around, yellow taxis, a few blurry people far away. {TR}, with {T} at the front and {G} behind him, drops from the sky and slides to a stop in the middle of the street, splashing water. {END(C2, amb='city noise and car horns')}",
  "«Aterrizaje de emergencia.» (voz en off)", None),
 (6,"TOFFEE",None,
  f"{ST(6)} Times Square at night. Medium close-up of {T} sitting in the sleigh, looking up at the giant bright screens with shining proud eyes, the colorful lights reflecting on his face. {H('Nueva York. Todas esas pantallas… seguro son para mí.')} {END('one cat', 'the cat', 'city noise')}",
  "«Nueva York. Todas esas pantallas… seguro son para mí.»", None),
 (6,"TOFFEE + GALLETA + TAXI",None,
  f"{ST(6)} Times Square at night. A yellow taxi brakes hard right in front of the sleigh and honks. {G} jumps behind the sleigh; {T} stays still, offended, staring at the taxi. {END(C2, amb='a loud car horn and city noise')}",
  "«Aquí nadie frena por un gato.» (voz en off)", None),
 (8,"MAPA",None,
  f"{ST(8)} Close-up of an old paper map held in a cat's paw, city lights reflecting on it: hundreds of small golden lights appear one after another all over the map until it is full of lights. No faces. No one speaks; only city noise. No phone, no selfie stick, no text, no music.",
  "«Y el mapa… se llenó de luces.» (voz en off)", None),
 (6,"TOFFEE",None,
  f"{ST(6)} Times Square at night. Close-up of {T}, looking at the map, then into the camera, overwhelmed. {H('Son cientos. Yo solo no puedo con todos.')} {END('one cat', 'the cat', 'city noise')}",
  "«Son cientos. Yo solo no puedo con todos.»", None),
 (6,"TOFFEE + GALLETA",None,
  f"{ST(6)} Times Square at night. On the left, {T} looks into the camera, decided; on the right, {G} puts his paw on the map. {H('Ustedes me van a ayudar. Mañana les cuento cómo.')} {END(C2, 'the cat', 'city noise')}",
  "«Ustedes me van a ayudar. Mañana les cuento cómo.»", None),
 (6,"CLIFFHANGER",None,
  f"{ST(6)} Times Square at night, wide shot. All the giant bright screens go dark at the same time, one after another, until the whole square is dark. Only a deep, slow male laugh echoes: 'Ho, ho, ho.' No animals in the shot. No phone, no text, no music.",
  "«¿Ese… era Santa?» (voz en off, susurro)", None),
]))

CANCION = """La Noche del Miau (canción de Halloween de Toffee)
Para Suno: estilo «reggaetón infantil de Halloween, divertido, coro pegajoso, voces de grupo, 100 BPM, español latino».
(Ojo: para usarla en videos que generan dinero, Suno pide un plan de pago; con el plan gratis la canción no es tuya.)

[Intro]
¡Miau! ¡Miau! Es la noche del miau…

[Verso 1]
Se cayó mi trineo en un valle sin sol,
una lechuza bruja con lentes me habló.
Una calabaza le tiene miedo a la oscuridad,
y un vampiro chiquito solo toma jugo de mora, ¡qué maldad!

[Coro]
Es la noche del miau, miau, miau,
nadie duerme en el valle, ¡guau, guau!
Si te asustas, ponte a bailar,
que el miedo se va si te ponés a saltar.

[Verso 2]
Galleta se disfrazó de árbol de Navidad,
y los monstruos gritaron: «¡Qué cosa tan fatal!»
Cinco cascabeles para volver a volar,
todos los animales merecen un regalo… ¡y ya!

[Coro x2]

[Final]
¡Miau! (hablado, Toffee) «Feliz Halloween, humanos.»"""

GANCHO = {2:2, 3:1, 4:1, 5:1, 6:1, 7:1, 8:3, 9:1, 10:5, 11:4, 12:4, 13:3, 14:2, 15:2}
for _v in VLOGS: _v['gancho'] = GANCHO[_v['n']]
