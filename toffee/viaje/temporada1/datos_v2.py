# Soy Toffee · El viaje · Sección 1, versión 2 (27-oct-2026)
# Cambios pedidos por Jay: gancho en los primeros segundos, historias simples con una función por toma
# (inicio, desarrollo, obstáculo, recompensa, continuación), personalidades definidas, conflicto + recompensa
# en cada episodio, productos integrados con transparencia, medición con datos, propósito social verificable.
# 4 episodios por semana (lun, mié, vie, dom). Todo en Omni 1.1 Flash, 9:16.

from datos import ST, T, G, TR, O, DIS, LE, CA, MU, CH, AL, LL, CHI, END, VL, VC, VM, FICHAS as FICHAS_V1, VOCES as VOCES_V1

# ---- Personajes nuevos de la versión 2 ----
TU = ("Don Turbio, the raccoon from the reference (gray fur, black eye mask, striped tail), wearing an old beige trench coat "
      "with the collar up and a small brown hat, with shifty eyes")
RA = ("Ratoncio, the small gray street mouse from the reference, wearing an old shiny black tuxedo that is a bit too big, "
      "dark round sunglasses and a fake plastic gold star pinned on his chest (no gloves, no shorts)")
VT_ = "in a raspy, fast, whispering salesman voice"
VR = "in a squeaky, theatrical, fake-glamorous voice"

FICHAS_NUEVAS = [
 ("Don Turbio (el vendedor sospechoso)", "TURBIO.jpg", "Mapache que aparece en los lugares más raros vendiendo soluciones absurdas. Personaje fijo del universo (como el vendedor de Gnomo, pero nuestro). Habla.",
  "Character reference sheet, 2x2 grid, 1:1, photorealistic, same character in all 4 views (front, 3/4 left, side, back), plain dark city-alley background: a raccoon standing on two legs, gray fur, black eye mask, striped tail, wearing an old beige trench coat with the collar up and a small brown hat, shifty suspicious eyes, holding the coat slightly open showing small strange gadgets hanging inside. Same coat and hat in ALL views. No text."),
 ("Ratoncio (el ratón famoso venido a menos)", "RATONCIO.jpg", "Ratón callejero que se cree celebridad de Hollywood. Original nuestro: SIN orejas negras redondas, SIN guantes blancos, SIN pantaloncito rojo. Habla.",
  "Character reference sheet, 2x2 grid, 1:1, photorealistic, same character in all 4 views (front, 3/4 left, side, back), plain red-carpet background: a small gray street mouse standing on two legs, wearing an old shiny black tuxedo that is a bit too big, dark round sunglasses and a fake plastic gold star pinned on his chest. Proud but a little sad. No gloves, no shorts. Same tuxedo, sunglasses and star in ALL views. No text."),
]
VOCES_NUEVAS = [
 ("Don Turbio", "Voice Design: «A middle-aged Latin American man, raspy and fast-talking street salesman, whispering like he is sharing a secret, sly and funny, Latin American Spanish, close to the microphone.» Prueba: «Psst… gato. ¿Necesitas un mapa? Tengo de todo. Original. Casi.» Guardar como «Turbio»."),
 ("Ratoncio", "Voice Design: «A small man with a squeaky but theatrical voice pretending to be a glamorous movie star, over-the-top, a bit sad underneath, Latin American Spanish.» Prueba: «Son veinte dólares la foto, gato. Soy una estrella… bueno, lo fui.» Guardar como «Ratoncio»."),
]

# ---- Expresiones fijas de Galleta (no habla: actúa con la cara) ----
GX = {
 "inocente": "slowly turns his head away and puts on an innocent face: big round eyes, head slightly tilted, sweet little smile",
 "desastre": "a slow mischievous smile spreads on his face, eyebrows raised, eyes fixed on the forbidden thing",
 "camara": "looks straight into the camera with a knowing, complicit look",
 "escondite": "hides behind the cat, only his head peeking out, ears back",
 "suplica": "makes huge shiny puppy eyes, ears low, looking up, begging",
 "celebra": "jumps and wiggles his whole body, celebrating happily",
 "abrazo": "gently leans his head against the cat's body, like a hug",
}

def HX(line, who, voice, verb="says"):
    subj = {"raccoon": "The raccoon", "mouse": "The mouse"}[who]
    return f'{subj} {verb} in Latin American Spanish, {voice}: "{line}" His mouth moves in sync with every word.'
def HT(line, verb="says"):
    return f'The cat {verb} in Latin American Spanish, in a deep, slow, sleepy male voice: "{line}" His lips move in sync with every word.'
def HO(line, who, voice, verb="says"):
    subj = {"owl": "The owl", "pumpkin": "The pumpkin", "bat": "The bat"}[who]
    part = {"owl": "Her beak moves", "pumpkin": "His carved mouth moves", "bat": "His mouth moves"}[who]
    return f'{subj} {verb} in Latin American Spanish, {voice}: "{line}" {part} in sync with every word.'

C2 = "one cat and one dog"
F_INI, F_DES, F_OBS, F_REC, F_CON = "INICIO", "DESARROLLO", "OBSTÁCULO", "RECOMPENSA", "CONTINUACIÓN"
def tk(f, s, fotos, p, toffee=None, otro=None, cont=None, gancho=False):
    return dict(f=f, s=s, fotos=fotos, p=p, toffee=toffee, otro=otro, cont=cont, gancho=gancho)

EP = []

# =============== EPISODIO 2 ===============
EP.append(dict(n=2, fecha="Lun 27-oct", titulo="La bruja del bosque", arriba=("Nos encontró una", "BRUJA EN EL BOSQUE 🦉"),
 conflicto="El trineo no vuela y están perdidos en un bosque de noche.", recompensa="Galleta, sin querer, encuentra el camino (y Toffee se lleva el mérito).",
 pregunta="¿Qué monstruo creen que nos espera en el valle?",
 resumen="Los ojos eran de Doña Lechuza, una bruja jubilada. El trineo no vuela: le faltan sus tres cascabeles, que cayeron en el Valle de Octubre, donde siempre es Halloween. Galleta tumba el farol de la lechuza y, sin querer, enciende el camino de calabazas.",
 tomas=[
 tk(F_INI, 6, "LECHUZA", f"{ST(6)} Dark snowy forest at night. Right in front of the camera, {LE} lands on a snowy branch out of the darkness, her golden eyes glowing, and stares down at the camera. {HO('¡Por fin! Llevo tres siglos esperando visitas.', 'owl', VL)} {END('one owl', 'the owl', 'wind')}",
    otro="LECHUZA: «¡Por fin! Llevo tres siglos esperando visitas.»", gancho=True),
 tk(F_INI, 6, "TOFFEE", f"{ST(6)} Snowy forest at night, warm lantern light. Medium close-up at eye level: {T} sits in the snow next to the crashed sleigh, unimpressed, looking into the camera. {HT('A ver, mis desgraciados… nos estrellamos. Y nos encontró una bruja.')} {END('one cat', 'the cat', 'wind')}",
    toffee="«A ver, mis desgraciados… nos estrellamos. Y nos encontró una bruja.»"),
 tk(F_DES, 8, "TOFFEE + GALLETA + TRINEO", f"{ST(8)} Snowy forest at night, static camera. Wide shot: {TR} lies tilted on its side, half buried in deep snow. {T} sits inside at the front and pushes against the front rim with both front paws, straining, but the sleigh does not move at all. On the right, outside the sleigh, {G} bites the white fur rim and pulls backward, his paws sliding in the snow. Both stay in the same place for the whole shot. {END(C2, amb='wind and crunching snow')}",
    toffee="«Plan A: despegar. Plan B: culpar a Galleta.» (voz en off)"),
 tk(F_OBS, 8, "LECHUZA", f"{ST(8)} Snowy forest at night. Close-up of Doña Lechuza, the barn owl from the reference with her small crooked witch hat and tiny round glasses, perched on a snowy branch with her wings folded like a real owl, very serious; her old brass lantern stands on the branch next to her feet (she does not hold anything). Behind her, far away in a dark valley, exactly three small round golden lights glow, clearly separated from each other. {HO('Sin sus tres cascabeles, ese trineo no vuela. Cayeron en el Valle de Octubre.', 'owl', VL)} {END('one owl', 'the owl', 'wind')}",
    otro="LECHUZA: «Sin sus tres cascabeles, ese trineo no vuela. Cayeron en el Valle de Octubre.»"),
 tk(F_OBS, 6, "TOFFEE + GALLETA", f"{ST(6)} Snowy forest at night. Medium shot at eye level: On the left, {T} stands with his chest out, trying to look brave. On the right, a little behind him, {G} lies flat on his belly in the snow, covering his eyes with both front paws, ears flat back, trembling with fear. {HT('¿Monstruos? Yo no tengo miedo. Estoy evaluando la situación.')} {END(C2, 'the cat', 'wind')}",
    toffee="«¿Monstruos? Yo no tengo miedo. Estoy evaluando la situación.»"),
 tk(F_REC, 8, "GALLETA + LECHUZA", f"{ST(8)} Snowy forest at night. Doña Lechuza, the barn owl from the reference with her small witch hat and tiny glasses, stands on the snow and has put her old brass lantern down next to her. {G} sniffs the lantern and knocks it over with his nose. The flame rolls out and, one after another, a long path of orange jack-o'-lanterns lights up into the dark valley. Then the dog {GX['inocente']}. {END('one dog and one owl', amb='wind and a soft magical whoosh')}",
    toffee="«Galleta encontró el camino. Fue suerte. Yo lo tenía calculado.» (voz en off)"),
 tk(F_CON, 6, "TOFFEE + GALLETA", f"{ST(6)} Night. A path of glowing orange jack-o'-lanterns leads into a dark forest of giant pumpkins. Seen from behind, {T} on the left and {G} on the right walk slowly down the path. Far away, a scream comes from the pumpkins. {END(C2, amb='crickets and a distant scream')}",
    toffee="«¿Qué monstruo creen que nos espera? Los leo.» (voz en off)"),
]))

# =============== EPISODIO 3 ===============
EP.append(dict(n=3, fecha="Mié 29-oct", titulo="La calabaza que le tiene miedo a la oscuridad", arriba=("El cascabel estaba", "DENTRO DE UNA CALABAZA 🎃"),
 conflicto="El primer cascabel está dentro de una calabaza que no se deja abrir porque le tiene miedo a la oscuridad.", recompensa="Galleta le regala una linterna, la calabaza deja de tener miedo y entrega el cascabel.",
 pregunta=None,
 resumen="Toffee intenta convencer a Calabacín con un «plan de doce pasos». No funciona. Galleta le pone una linterna al lado y listo. Toffee dice que era su plan.",
 tomas=[
 tk(F_INI, 6, "TOFFEE + CALABACÍN", f"{ST(6)} Forest of giant glowing jack-o'-lanterns at night. Extreme close-up: {T} presses his face against the carved eye of {CA}; inside the pumpkin a small golden bell shines next to the candle. Suddenly the pumpkin screams and the cat jumps back. {END('one cat and one pumpkin', amb='a scream and crickets')}",
    toffee="(sin voz: grito de la calabaza)", gancho=True),
 tk(F_DES, 8, "CALABACÍN", f"{ST(8)} Forest of giant jack-o'-lanterns at night. {CA} sits on the ground, shaking, his candle light flickering, and shouts toward the camera. {HO('¡No me miren! ¡Me da miedo que me miren!', 'pumpkin', VC)} {END('one pumpkin', 'the pumpkin', 'crickets')}",
    otro="CALABACÍN: «¡No me miren! ¡Me da miedo que me miren!»"),
 tk(F_DES, 8, "TOFFEE + CALABACÍN", f"{ST(8)} Forest of giant jack-o'-lanterns at night. On the left, {T} sits calmly in front of {CA} on the right, like a serious therapist. {HT('Tranquilo. Tengo un plan de doce pasos. Paso uno: me das el cascabel.')} {END('one cat and one pumpkin', 'the cat', 'crickets')}",
    toffee="«Tranquilo. Tengo un plan de doce pasos. Paso uno: me das el cascabel.»"),
 tk(F_OBS, 8, "CALABACÍN", f"{ST(8)} Forest of giant jack-o'-lanterns at night. Close-up of {CA}, shaking, his candle light trembling. {HO('¡No! Si me abren, se apaga mi vela. ¡Y le tengo miedo a la oscuridad!', 'pumpkin', VC)} {END('one pumpkin', 'the pumpkin', 'crickets')}",
    otro="CALABACÍN: «¡No! Si me abren, se apaga mi vela. ¡Y le tengo miedo a la oscuridad!»"),
 tk(F_OBS, 6, "TOFFEE", f"{ST(6)} Forest of giant jack-o'-lanterns at night. Close-up of {T}, slowly turning to look into the camera with a flat, tired, deadpan face. {HT('Una calabaza de Halloween… con miedo a la oscuridad. Excelente.')} {END('one cat', 'the cat', 'crickets')}",
    toffee="«Una calabaza de Halloween… con miedo a la oscuridad. Excelente.»"),
 tk(F_REC, 8, "GALLETA + CALABACÍN", f"{ST(8)} Forest of giant jack-o'-lanterns at night. {G} walks up to {CA} carrying a small glowing yellow lantern in his mouth and gently puts it on the ground next to the pumpkin. The pumpkin's face lights up happy, his lid lifts by itself and a small golden bell rolls out onto the grass. {END('one dog and one pumpkin', amb='crickets and a soft bell ring')}",
    toffee="«Galleta tuvo una idea. Galleta nunca tiene ideas.» (voz en off)"),
 tk(F_REC, 6, "TOFFEE + GALLETA", f"{ST(6)} Forest of glowing jack-o'-lanterns at night. On the left, {T} holds up a small golden bell, proud, looking into the camera; on the right, {G} {GX['camara']}. {HT('Primer cascabel. Mi plan funcionó.')} {END(C2, 'the cat', 'crickets')}",
    toffee="«Primer cascabel. Mi plan funcionó.»"),
 tk(F_CON, 6, "TOFFEE + GALLETA", f"{ST(6)} Night. A dark stone castle on top of a cliff with a huge full moon behind it; hundreds of small bats fly out of the tower windows. In the foreground, seen from behind, {T} and {G} look up at the castle. {END(C2, amb='bats squeaking and wind')}",
    toffee="«El segundo lo tiene un vampiro. Y mañana es Halloween.» (voz en off)"),
]))

# =============== EPISODIO 4 ===============
EP.append(dict(n=4, fecha="Vie 31-oct · HALLOWEEN", titulo="El disfraz más aterrador", arriba=("El disfraz MÁS", "ATERRADOR 🎃"),
 conflicto="El vampiro solo entrega el segundo cascabel al disfraz más aterrador de su fiesta, y Toffee no tiene disfraz.", recompensa="Galleta gana disfrazado de árbol de Navidad: en el Valle de Octubre lo más aterrador es la Navidad. Fiesta con la canción «La Noche del Miau».",
 pregunta=None,
 resumen="El vampiro resulta ser un murciélago diminuto. Toffee se presenta «disfrazado de gato guapo un lunes» y nadie se asusta. Galleta sale con el disfraz de árbol de Navidad (producto) y los monstruos gritan. Ganan el cascabel y hay fiesta.",
 producto="Disfraz Árbol de Navidad: aparece porque tiene sentido (el concurso). No se dice nada de venta dentro del episodio; la venta va en el formato C.",
 tomas=[
 tk(F_REC, 6, "GALLETA + DISFRAZ", f"{ST(6)} A spooky costume runway at night with purple and orange lights and fog. {G}, wearing {DIS}, walks proudly toward the camera like a model while a crowd of shadowy monsters in the dark screams and steps back. {END('one dog', amb='monsters screaming')}",
    toffee="(sin voz)", gancho=True),
 tk(F_INI, 6, "MURCIÉLAGO", f"{ST(6)} Gothic castle hall with candles, Halloween decorations. The camera tilts down from a giant vampire shadow on the wall to the floor and reveals that it belongs to {MU}, tiny, standing in front of a candle, opening his cape. {HO('¡Bienvenidos a mi fiesta de Halloween!', 'bat', VM)} {END('one bat', 'the bat', 'thunder')}",
    otro="CONDE: «¡Bienvenidos a mi fiesta de Halloween!»"),
 tk(F_DES, 6, "TOFFEE", f"{ST(6)} Gothic castle hall with candles. Medium close-up of {T} looking down at something small, totally unimpressed, one eyebrow up. {HT('¿Ese es el vampiro? Mide lo que una papa.')} {END('one cat', 'the cat', 'thunder far away')}",
    toffee="«¿Ese es el vampiro? Mide lo que una papa.»"),
 tk(F_OBS, 8, "MURCIÉLAGO", f"{ST(8)} Gothic castle hall. {MU} stands on a table next to a small golden bell on a velvet cushion and points at it dramatically. {HO('El cascabel es para el disfraz más aterrador. Sin disfraz, no hay cascabel.', 'bat', VM)} {END('one bat', 'the bat', 'organ music far away')}",
    otro="CONDE: «El cascabel es para el disfraz más aterrador. Sin disfraz, no hay cascabel.»"),
 tk(F_DES, 6, "TOFFEE + LECHUZA", f"{ST(6)} Spooky costume stage at night, purple lights. {T}, without any costume, stands proudly in the middle of the stage. At the judges' table on the right, {LE} yawns, bored. {END('one cat and one owl', amb='a few crickets and one cough')}",
    toffee="«Mi disfraz: un gato guapo un lunes. Aterrador.» (voz en off)"),
 tk(F_OBS, 6, "LECHUZA", f"{ST(6)} Judges' table at a spooky costume contest at night. Close-up of {LE}, wearing her witch hat, staring at the stage in shock and dropping her lantern. {HO('¡Un árbol de Navidad! ¡Lo más aterrador que he visto!', 'owl', VL)} {END('one owl', 'the owl', 'monsters screaming')}",
    otro="LECHUZA: «¡Un árbol de Navidad! ¡Lo más aterrador que he visto!»"),
 tk(F_REC, 8, "TOFFEE + GALLETA + DISFRAZ", f"{ST(8)} Spooky costume stage at night, orange and purple confetti falling. On the right, {G}, wearing {DIS}, {GX['celebra']}, a small golden bell hanging from the star; on the left, {T} looks into the camera. {HT('Aquí lo que da miedo es la Navidad. El disfraz lo escogí yo.')} {END(C2, 'the cat', 'crowd cheering')}",
    toffee="«Aquí lo que da miedo es la Navidad. El disfraz lo escogí yo.»"),
 tk(F_REC, 6, "TODOS", f"{ST(6)} Halloween party in the castle courtyard at night under a full moon, glowing jack-o'-lanterns, purple lights. {T}, {G}, {CA}, {MU} and {LE} dance together. Exactly one cat, one dog, one pumpkin, one bat and one owl; the cat's whole head, nightcap and camera always in frame. No one speaks; only party noise. No phone, no text, no music.",
    toffee="(canción «La Noche del Miau», coro)"),
 tk(F_CON, 6, "LECHUZA + TOFFEE", f"{ST(6)} End of the Halloween party at night, quiet now, fog. On the right, {LE} leans close to {T} on the left and whispers. {HO('El tercer cascabel… lo tiene el Chupacabras.', 'owl', VL, 'whispers')} {END('one cat and one owl', 'the owl', 'wind')}",
    otro="LECHUZA (susurro): «El tercer cascabel… lo tiene el Chupacabras.»"),
]))

# =============== EPISODIO 5 ===============
EP.append(dict(n=5, fecha="Dom 2-nov · DÍA DE MUERTOS", titulo="El Chupacabras", arriba=("Encontramos al", "CHUPACABRAS 😱"),
 conflicto="El tercer cascabel lo tiene el Chupacabras, y dicen que se come a los gatos.", recompensa="El «monstruo» es un cachorro de la calle con miedo. Devuelve el cascabel, Toffee lo pone en su lista y el trineo vuelve a volar.",
 pregunta="¿Qué animalito de la calle pongo de número dos en mi lista?",
 resumen="Toffee manda a Galleta adelante («confío plenamente en ti»). Galleta va, valiente. El Chupacabras es un cachorrito temblando abrazado al cascabel. Toffee lo ayuda «porque le estorbaba el camino». En el altar de Día de Muertos de los animales de la calle, Toffee deja un regalo. Con los tres cascabeles, el trineo despega escoltado por el alebrije.",
 tomas=[
 tk(F_INI, 6, "CHUPACABRAS", f"{ST(6)} A dark swamp at night lit by orange marigold flowers and floating candles. Behind a fallen tree trunk, only a pair of big glowing yellow eyes and a row of spikes are visible in the dark. {END('one creature', amb='a low growl and frogs')}",
    toffee="(sin voz)", gancho=True),
 tk(F_INI, 8, "TOFFEE + GALLETA", f"{ST(8)} Swamp at night with marigold petals and floating candles. On the left, {T} whispers to the camera, eyes wide; on the right, {G} listens. {HT('Dicen que se come a los gatos. Galleta, ve tú primero. Confío plenamente en ti.', 'whispers')} {END(C2, 'the cat', 'frogs')}",
    toffee="«Dicen que se come a los gatos. Galleta, ve tú primero. Confío plenamente en ti.» (susurro)"),
 tk(F_DES, 8, "TOFFEE + GALLETA", f"{ST(8)} Swamp at night. {G} walks bravely ahead toward a fallen tree trunk; {T} follows far behind, step by step, hiding behind small plants. {END(C2, amb='frogs and a low growl')}",
    toffee="«Yo cubro la retaguardia.» (voz en off)"),
 tk(F_OBS, 8, "CHUPACABRAS", f"{ST(8)} Swamp at night, behind the fallen tree trunk, lit by marigolds and fireflies. Reveal: {CH} is curled up and shaking, hugging a small golden bell like a toy. He looks up with big sad eyes. {END('one creature', amb='soft whimpering')}",
    toffee="«No es un monstruo… es un cachorro.» (voz en off)"),
 tk(F_REC, 8, "TOFFEE + CHUPACABRAS", f"{ST(8)} Swamp at night. On the left, {T} sits next to {CH} on the right, looks away as if he doesn't care, and gently puts his paw on the little creature's head. The creature stops shaking. {HT('No lo hago por él. Me estaba estorbando el camino.')} {END('one cat and one creature', 'the cat', 'frogs')}",
    toffee="«No lo hago por él. Me estaba estorbando el camino.»"),
 tk(F_REC, 6, "TOFFEE + CHUPACABRAS", f"{ST(6)} Swamp at night. On the right, {CH} pushes the small golden bell with his nose into the paws of {T} on the left and wags his thin tail. The cat freezes, speechless, mouth slightly open. {END('one cat and one creature', amb='a soft bell ring')}",
    toffee="«Lista de animales que merecen un regalo. Número uno: el Chupacabras.» (voz en off)"),
 tk(F_REC, 8, "TOFFEE + GALLETA", f"{ST(8)} Night. A colorful Day of the Dead altar decorated with orange marigolds, candles and papel picado, with small framed drawings of street dogs and cats. On the left, {T} places a small wrapped red gift box on the altar; on the right, {G} {GX['abrazo']}. {END(C2, amb='soft wind and distant guitar')}",
    toffee="«Hoy es Día de Muertos. Y este es para los que nunca tuvieron casa.» (voz en off)"),
 tk(F_CON, 8, "TOFFEE + GALLETA + TRINEO + ALEBRIJE", f"{ST(8)} Night sky over a valley full of orange marigolds and candles. {TR}, with three small golden bells glowing at the front, flies with {T} at the front and {G} behind him; next to them flies {AL}, flapping its colorful wings. Exactly one cat, one dog and one alebrije; the cat's whole head, nightcap and camera always in frame. No one speaks; only wind and bells. No phone, no text, no music.",
    toffee="«¡El trineo vuelve a volar! Ahora… ¿para dónde es el Polo Norte?» (voz en off)"),
]))

# =============== EPISODIO 6 ===============
EP.append(dict(n=6, fecha="Mar 4-nov", titulo="Perdidos en las nubes", arriba=("Nos PERDIMOS", "EN LAS NUBES ☁️"),
 conflicto="Vuelan, pero no saben a dónde ir, y Toffee no quiere admitir que está perdido.", recompensa="Doña Lechuza les da un mapa que brilla donde hay un animal que necesita un regalo… y marca justo donde Galleta señalaba.",
 pregunta="¿Adivinan en qué país es la primera luz?",
 resumen="Toffee dice que «reconoce el terreno». Galleta olfatea el viento y señala una dirección; Toffee lo ignora. Llega la lechuza con un mapa encantado. La primera luz está justo donde señaló Galleta.",
 tomas=[
 tk(F_INI, 6, "TOFFEE + GALLETA + TRINEO", f"{ST(6)} Inside thick white clouds, daylight. {TR} spins slowly in circles; {T} at the front looks around confused; behind him {G} looks dizzy, tongue out. {END(C2, amb='wind')}",
    toffee="«Llevamos tres horas dando vueltas.» (voz en off)", gancho=True),
 tk(F_DES, 6, "TOFFEE", f"{ST(6)} Inside white clouds. Close-up of {T} sitting at the front of the flying sleigh, chin up, pretending to be confident. {HT('No estamos perdidos. Estoy reconociendo el terreno.')} {END('one cat', 'the cat', 'wind')}",
    toffee="«No estamos perdidos. Estoy reconociendo el terreno.»"),
 tk(F_DES, 6, "TOFFEE + GALLETA", f"{ST(6)} Inside the flying sleigh among clouds. {G} sticks his head out, sniffs the wind and points firmly with his paw to the left; {T} doesn't even look and points to the right. {END(C2, amb='wind')}",
    toffee="«Galleta dice que es por allá. Galleta no sabe de navegación.» (voz en off)"),
 tk(F_OBS, 6, "LECHUZA + TRINEO", f"{ST(6)} Among clouds. {LE} flies right in front of the sleigh, wings open, and stops it. {HO('Sabía que se iban a perder, mijo.', 'owl', VL)} {END('one owl', 'the owl', 'wind')}",
    otro="LECHUZA: «Sabía que se iban a perder, mijo.»"),
 tk(F_REC, 8, "LECHUZA", f"{ST(8)} Among clouds, golden light. Close-up of {LE} unrolling an old paper map with her wing; small golden lights glow on it. {HO('Este mapa brilla donde hay un animal que necesita un regalo.', 'owl', VL)} {END('one owl', 'the owl', 'wind')}",
    otro="LECHUZA: «Este mapa brilla donde hay un animal que necesita un regalo.»"),
 tk(F_REC, 6, "TOFFEE + GALLETA", f"{ST(6)} Inside the flying sleigh. Close-up: {T} holds the old map; one golden light shines exactly to the left, where the dog pointed. The cat slowly looks at {G}, who {GX['camara']}. {HT('…Eso lo sabía yo.')} {END(C2, 'the cat', 'wind')}",
    toffee="«…Eso lo sabía yo.»"),
 tk(F_CON, 8, "PAISAJE", f"{ST(8)} Drone shot at sunrise over the Cocora Valley in Colombia: very tall thin wax palm trees rising from green misty mountains, soft fog, golden light. A small red flying sleigh crosses the sky far away. No one speaks; only wind. No phone, no text, no music.",
    toffee="«Primera luz del mapa: Colombia. ¿Adivinan quién nos espera?» (voz en off)"),
]))

# =============== EPISODIO 7 ===============
EP.append(dict(n=7, fecha="Jue 6-nov", titulo="Galleta maneja un Willys", arriba=("Galleta MANEJA", "UN WILLYS 🚙"),
 conflicto="El animal del mapa está en el pueblo de abajo y Toffee no quiere caminar.", recompensa="Llegan (de milagro) y le dan una cobija a un perrito abuelo que tiene frío. Toffee se queda sin palabras cuando el perro le agradece.",
 pregunta="¿Qué animalito de la calle conocen que merezca estar en la lista? Escriban su nombre.",
 resumen="Valle de Cocora. Toffee: «caminar es para los pobres». Galleta ya está al volante de un Willys con la sonrisa del desastre. Bajan en zigzag (Cumbia del Willys). En Salento encuentran al abuelo que tiembla de frío; Toffee le da la cobija «porque le estorbaba».",
 tomas=[
 tk(F_OBS, 8, "WILLYS", f"{ST(8)} Drone shot following a colorful old Colombian Willys jeep zig-zagging down a green mountain road near Salento, Colombia, too fast, leaving dust. Inside, the dog drives and the cat holds on. Exactly one cat and one dog. No one speaks; only engine noise and a happy bark. No phone, no text, no music.",
    toffee="«¡Galleta, freno! ¡FRENO!» (voz en off)", gancho=True),
 tk(F_INI, 6, "TOFFEE + GALLETA", f"{ST(6)} Cocora Valley, Colombia, morning: very tall wax palm trees, green mountains, fog. On the left, {T} looks into the camera; on the right, {G} sniffs the grass. {HT('A ver, mis desgraciados: Valle de Cocora. El mapa dice que es en el pueblo.')} {END(C2, 'the cat', 'birds and wind')}",
    toffee="«A ver, mis desgraciados: Valle de Cocora. El mapa dice que es en el pueblo.»"),
 tk(F_DES, 6, "TOFFEE", f"{ST(6)} Cocora Valley, a long steep road going down far away. Close-up of {T} looking at the long road, disgusted. {HT('Caminar es para los que no tienen categoría.')} {END('one cat', 'the cat', 'birds')}",
    toffee="«Caminar es para los que no tienen categoría.»"),
 tk(F_OBS, 8, "GALLETA + WILLYS", f"{ST(8)} A colorful old Colombian Willys jeep parked on a mountain road. {G} already sits in the driver's seat with his paws on the steering wheel; {GX['desastre']}. {T} sits in the passenger seat, gripping the door, eyes wide. {END(C2, amb='birds and an engine starting')}",
    toffee="«Galleta no sabe manejar. Galleta no sabía que no sabía.» (voz en off)"),
 tk(F_REC, 8, "PERRO DE SALENTO", f"{ST(8)} Colorful street in Salento, Colombia, with painted balconies, early morning, cold. An old skinny black street dog with gray whiskers sleeps curled up on a sidewalk, shivering. No other animals. No one speaks; only soft street sounds. No phone, no text, no music.",
    toffee="«Ahí está. Tiene frío.» (voz en off)"),
 tk(F_REC, 8, "TOFFEE + PERRO", f"{ST(8)} Colorful street in Salento, Colombia. {T} looks away as if he doesn't care and quickly covers the old black street dog with a small soft red blanket using his paws. The old dog stops shivering. Exactly one cat and one dog (the old black dog); the cat's whole head, nightcap and camera always in frame. No one speaks; only street sounds. No phone, no text, no music.",
    toffee="«No lo hice por él. La cobija me estorbaba.» (voz en off)"),
 tk(F_REC, 6, "TOFFEE + PERRO", f"{ST(6)} Salento street. The old black dog licks the cheek of {T}; the cat freezes, speechless, then looks into the camera. Exactly one cat and one dog (the old black dog); the cat's whole head, nightcap and camera always in frame. No one speaks; only street sounds. No phone, no text, no music.",
    toffee="«…No le cuenten a nadie.» (voz en off)"),
 tk(F_CON, 6, "TOFFEE", f"{ST(6)} Salento street, Colombia. Close-up of {T} writing in a small old notebook with a pencil in his paw, then looking into the camera. {HT('Número dos: el abuelo de Salento. ¿Quién más merece estar aquí?')} {END('one cat', 'the cat', 'street sounds')}",
    toffee="«Número dos: el abuelo de Salento. ¿Quién más merece estar aquí?»"),
]))

# =============== EPISODIO 8 ===============
EP.append(dict(n=8, fecha="Sáb 8-nov", titulo="Una alpaca me escupió en Machu Picchu", arriba=("Me ESCUPIÓ", "UNA ALPACA 🦙"),
 conflicto="Toffee quiere su foto perfecta en Machu Picchu y una alpaca no lo deja.", recompensa="La alpaca estaba nerviosa porque perdió a su bebé; Galleta la sigue y lo encuentran.",
 pregunta=None,
 resumen="Toffee posa como estrella. Paca lo mira mal y le escupe. Galleta, curioso, la sigue; encuentran a la alpaquita perdida. Paca le agradece a Toffee con un cabezazo cariñoso. Número tres de la lista.",
 tomas=[
 tk(F_OBS, 6, "TOFFEE + PACA", f"{ST(6)} Machu Picchu grass terrace at sunrise. On the right, {LL} spits a small splash of water onto the face of {T} on the left. The cat freezes with wet fur on his face and closes his eyes slowly. {END('one cat and one alpaca', amb='wind and a spit sound')}",
    toffee="(sin voz: efecto de escupida)", gancho=True),
 tk(F_INI, 6, "TOFFEE", f"{ST(6)} Machu Picchu terrace at sunrise, ruins and mountains behind. Medium close-up of {T} posing proudly, chin up, looking into the camera. {HT('Machu Picchu. Foto oficial del protagonista.')} {END('one cat', 'the cat', 'wind')}",
    toffee="«Machu Picchu. Foto oficial del protagonista.»"),
 tk(F_DES, 6, "PACA", f"{ST(6)} Machu Picchu terrace. {LL} walks into the frame from the right, stops right next to the camera and stares at it with a judging face. {END('one alpaca', amb='wind')}",
    toffee="«¿Y esta quién es? No tiene cita.» (voz en off)"),
 tk(F_OBS, 6, "TOFFEE", f"{ST(6)} Machu Picchu terrace. Close-up of {T} with wet fur on his face, eyes half closed, looking into the camera, deeply offended. {HT('Me escupió. Patrimonio de la humanidad y me escupió.')} {END('one cat', 'the cat', 'wind')}",
    toffee="«Me escupió. Patrimonio de la humanidad y me escupió.»"),
 tk(F_DES, 8, "PACA + GALLETA", f"{ST(8)} Machu Picchu terraces. {LL} walks nervously along a stone path, looking back; {G} follows her, curious, wagging his tail. Exactly one alpaca and one dog. No one speaks; only wind. No phone, no text, no music.",
    toffee="«Galleta ya se hizo su amigo. Traidor.» (voz en off)"),
 tk(F_REC, 8, "ALPAQUITA", f"{ST(8)} Behind an ancient stone wall at Machu Picchu: a tiny baby alpaca with fluffy white wool lies alone, crying softly. {LL} runs to it and rubs her head against the baby. Exactly two alpacas. No one speaks; only soft crying and wind. No phone, no text, no music.",
    toffee="«Era su bebé. Por eso estaba de mal genio. Número tres de la lista.» (voz en off)"),
 tk(F_REC, 6, "TOFFEE + PACA", f"{ST(6)} Machu Picchu at sunset. On the right, {LL} gently rubs her head against {T} on the left. The cat looks at the camera, surprised. {END('one cat and one alpaca', amb='wind')}",
    toffee="«Igual me debes una lavada.» (voz en off)"),
 tk(F_CON, 6, "TOFFEE + MAPA", f"{ST(6)} Machu Picchu at night. Close-up of {T} holding the old map; a new golden light pulses on it. {END('one cat', amb='wind')}",
    toffee="«Siguiente: Chile. Dicen que allá el cielo es otra cosa.» (voz en off)"),
]))

# =============== EPISODIO 9 ===============
EP.append(dict(n=9, fecha="Lun 10-nov", titulo="Un ovni se llevó a Galleta", arriba=("Un OVNI se llevó", "A GALLETA 🛸"),
 conflicto="Un ovni se lleva a Galleta en el desierto de Atacama.", recompensa="Toffee, que «no pensaba buscarlo», corre como loco; Galleta vuelve con un regalo de los extraterrestres y se abrazan.",
 pregunta=None,
 resumen="Toffee dice que los ovnis son «mentiras de turistas». Un rayo azul se lleva a Galleta. «No pienso perder el tiempo buscándolo», dice Toffee… y corre por todo el desierto. Galleta regresa con una pelotita que brilla. «No lloré. Era arena.»",
 tomas=[
 tk(F_OBS, 8, "GALLETA + OVNI", f"{ST(8)} Atacama Desert, Chile, at night under the Milky Way. A round silver flying saucer with blue lights appears above. A soft blue beam shines down on {G}, who slowly floats up into the beam, surprised, paws dangling. {END('one dog', amb='a deep humming sound')}",
    toffee="(sin voz)", gancho=True),
 tk(F_INI, 6, "TOFFEE + GALLETA", f"{ST(6)} Atacama Desert at night, the Milky Way across the whole sky. On the left, {T} lies on his back on the sand; on the right, {G} lies next to him. {HT('Dicen que aquí se ven ovnis. Mentiras de turistas.')} {END(C2, 'the cat', 'desert wind')}",
    toffee="«Dicen que aquí se ven ovnis. Mentiras de turistas.»"),
 tk(F_DES, 6, "TOFFEE", f"{ST(6)} Atacama Desert at night, blue light fading in the sky. {T} stands with his back straight, pretending to be calm, looking into the camera. {HT('No pienso perder el tiempo buscándolo.')} {END('one cat', 'the cat', 'desert wind')}",
    toffee="«No pienso perder el tiempo buscándolo.»"),
 tk(F_DES, 6, "TOFFEE", f"{ST(6)} Atacama Desert at night. Wide shot: {T} runs at full speed across the sand toward a tiny blue light far away in the sky, ears back. {END('one cat', amb='desert wind and fast steps')}",
    toffee="«¡GALLETA!» (voz en off)"),
 tk(F_OBS, 6, "TOFFEE", f"{ST(6)} Atacama Desert at night, empty sky. {T} sits alone on the sand, looking up at the stars, sad and quiet. {END('one cat', amb='desert wind')}",
    toffee="(silencio)"),
 tk(F_REC, 8, "TOFFEE + GALLETA", f"{ST(8)} Atacama Desert at night. A soft blue beam sets {G} back on the sand next to {T}. The dog holds a small glowing blue ball in his mouth, drops it in front of the cat and {GX['abrazo']}. {END(C2, amb='soft hum')}",
    toffee="«No lloré. Era arena.» (voz en off)"),
 tk(F_CON, 6, "TOFFEE + MAPA", f"{ST(6)} Atacama Desert at night. Close-up of {T} holding the old map; a new golden light pulses on it. {HT('Siguiente: México. Y dicen que allá hay lucha libre.')} {END('one cat', 'the cat', 'desert wind')}",
    toffee="«Siguiente: México. Y dicen que allá hay lucha libre.»"),
]))

# =============== EPISODIO 10 ===============
EP.append(dict(n=10, fecha="Mié 12-nov", titulo="Lucha libre contra el Chihuahua Enmascarado", arriba=("Me retó un", "LUCHADOR 🤼"),
 conflicto="Un chihuahua luchador reta a Toffee y no lo deja pasar.", recompensa="Toffee gana sin hacer nada (se acuesta). El chihuahua solo quería que alguien le regalara un juguete.",
 pregunta=None,
 resumen="El Chihuahua Enmascarado reta a Toffee. Toffee se pone una máscara encima del gorro: «el Gato Dormilón». Su técnica: acostarse. El chihuahua se cansa solo. Galleta toca la campana. Número cuatro de la lista.",
 tomas=[
 tk(F_INI, 6, "CHIHUAHUA", f"{ST(6)} Inside a colorful Mexican lucha libre ring under bright lights. {CHI} stands on the corner ropes, opens his tiny red cape and barks at the camera, very tough. {END('one chihuahua', amb='crowd cheering')}",
    toffee="«Y este me retó.» (voz en off)", gancho=True),
 tk(F_INI, 6, "ARENA", f"{ST(6)} A colorful Mexican lucha libre arena at night, bright lights, a ring with red ropes, a cheering crowd in the dark, papel picado hanging. Drone shot moving toward the ring. No animals in the shot. No one speaks; only a cheering crowd. No phone, no text, no music.",
    toffee="«México. El mapa nos trajo a una arena de lucha libre.» (voz en off)"),
 tk(F_DES, 6, "TOFFEE", f"{ST(6)} Lucha libre locker room. Medium close-up of {T} wearing a shiny silver-and-blue lucha libre mask OVER his navy nightcap (the nightcap, pompom and action camera still visible on top), looking into the camera, serious. {HT('Me llamo… el Gato Dormilón.')} {END('one cat', 'the cat', 'distant crowd')}",
    toffee="«Me llamo… el Gato Dormilón.»"),
 tk(F_OBS, 8, "TOFFEE + CHIHUAHUA", f"{ST(8)} Inside the lucha libre ring. On the right, {CHI} runs in fast circles around {T} on the left, who wears the silver-and-blue mask over his nightcap and simply lies down on the ring floor and closes his eyes. {END('one cat and one chihuahua', amb='crowd laughing')}",
    toffee="«No es cobardía. Es estrategia.» (voz en off)"),
 tk(F_REC, 6, "CHIHUAHUA", f"{ST(6)} Inside the lucha libre ring. {CHI} stops running, out of breath, and lies flat on his back, exhausted, tongue out. {END('one chihuahua', amb='crowd cheering')}",
    toffee="(sin voz)"),
 tk(F_REC, 6, "GALLETA", f"{ST(6)} Ringside of the lucha libre arena. {G} rings a small bell with his paw three times like a referee and {GX['celebra']}. {END('one dog', amb='bell rings and crowd cheering')}",
    toffee="«¡Ganó el Gato Dormilón! La humildad es para los que no tienen talento.» (voz en off)"),
 tk(F_REC, 8, "TOFFEE + CHIHUAHUA", f"{ST(8)} Inside the lucha libre ring, confetti falling. On the left, {T} with the mask over his nightcap and, on the right, {CHI} sit together; the chihuahua lifts his mask a little and looks at the camera with sad eyes. {END('one cat and one chihuahua', amb='crowd')}",
    toffee="«Me contó que nunca le han regalado un juguete. Número cuatro de la lista.» (voz en off)"),
 tk(F_CON, 6, "TOFFEE + MAPA", f"{ST(6)} Night sky above Mexico City, the sleigh flying, lightning far away. Close-up of {T} in his nightcap, holding the old map, worried; the map's lights flicker. {HT('El mapa… se está volviendo loco.')} {END('one cat', 'the cat', 'wind and thunder far away')}",
    toffee="«El mapa… se está volviendo loco.»"),
]))

# =============== EPISODIO 11 ===============
EP.append(dict(n=11, fecha="Vie 14-nov", titulo="Nos estrellamos en Nueva York", arriba=("Nos estrellamos en", "NUEVA YORK 🗽"),
 conflicto="Una tormenta los tira en Times Square y el mapa se moja y se apaga.", recompensa="Aparece un vendedor muy sospechoso que dice tener la solución (y Toffee, obviamente, le va a comprar).",
 pregunta="¿Le compramos a este señor? Sí o no.",
 resumen="Aterrizaje de emergencia en Times Square. Toffee cree que las pantallas son para él. Un taxi les pita. El mapa mojado se apaga. En un callejón, Don Turbio abre su gabardina: «¿Necesitas un mapa? Tengo de todo».",
 fichas=["Don Turbio (el vendedor sospechoso)"],
 tomas=[
 tk(F_INI, 8, "TOFFEE + GALLETA + TRINEO", f"{ST(8)} Times Square, New York, at night, wet street, huge bright advertising screens all around, yellow taxis, a few blurry people far away. {TR}, with {T} at the front and {G} behind him, drops from the sky and slides to a stop in the middle of the street, splashing water. {END(C2, amb='city noise and car horns')}",
    toffee="«Aterrizaje de emergencia.» (voz en off)", gancho=True),
 tk(F_DES, 6, "TOFFEE", f"{ST(6)} Times Square at night. Medium close-up of {T} sitting in the sleigh, looking up at the giant bright screens with shining proud eyes, the colorful lights reflecting on his face. {HT('Nueva York. Todas esas pantallas… seguro son para mí.')} {END('one cat', 'the cat', 'city noise')}",
    toffee="«Nueva York. Todas esas pantallas… seguro son para mí.»"),
 tk(F_OBS, 6, "TOFFEE + GALLETA + TAXI", f"{ST(6)} Times Square at night. A yellow taxi brakes hard right in front of the sleigh and honks. {G} jumps behind the sleigh; {T} stays still, offended, staring at the taxi. {END(C2, amb='a loud car horn and city noise')}",
    toffee="«Aquí nadie respeta a un gato famoso.» (voz en off)"),
 tk(F_OBS, 6, "TOFFEE + MAPA", f"{ST(6)} Times Square at night, light rain. Close-up of {T} holding the old paper map, soaking wet; its golden lights flicker and go out one by one. {END('one cat', amb='rain and city noise')}",
    toffee="«Y el mapa se mojó. Excelente. Otra desgracia.» (voz en off)"),
 tk(F_REC, 8, "TURBIO", f"{ST(8)} A dark wet New York alley at night, steam coming from the ground. {TU} steps out of the shadows and opens his coat, showing many small strange gadgets hanging inside. {HX('Psst… gato. ¿Necesitas un mapa? Tengo de todo.', 'raccoon', VT_, 'whispers')} {END('one raccoon', 'the raccoon', 'city noise far away')}",
    otro="TURBIO (susurro): «Psst… gato. ¿Necesitas un mapa? Tengo de todo.»"),
 tk(F_CON, 6, "TOFFEE + GALLETA", f"{ST(6)} Dark New York alley at night. On the left, {T} looks into the camera with a tired, knowing face; on the right, {G} {GX['suplica']} toward the gadgets. {HT('Esto va a salir mal. Igual voy a comprar.')} {END(C2, 'the cat', 'city noise')}",
    toffee="«Esto va a salir mal. Igual voy a comprar.»"),
]))

# =============== EPISODIO 12 ===============
EP.append(dict(n=12, fecha="Dom 16-nov", titulo="El vendedor sospechoso", arriba=("Le compré a un", "VENDEDOR SOSPECHOSO 🦝"),
 conflicto="Toffee le compra a Don Turbio un «secador de mapas turbo»… y le explota en la cara.", recompensa="El calor del secador despierta el mapa, que se llena de cientos de luces. Funciona… demasiado.",
 pregunta=None,
 resumen="Don Turbio vende un «secador de mapas turbo. Original. Casi». Toffee paga con las galletas de Galleta (Galleta pone cara de súplica). El secador le despeina toda la cara. El mapa caliente se enciende con cientos de luces.",
 tomas=[
 tk(F_OBS, 6, "TOFFEE", f"{ST(6)} Dark New York alley at night. A small strange hair dryer held in front of {T} blasts a huge gust of air and glitter into his face; his cheeks and fur flap wildly, his nightcap stays on. {END('one cat', amb='a loud blowing sound')}",
    toffee="(sin voz)", gancho=True),
 tk(F_INI, 8, "TURBIO", f"{ST(8)} Dark New York alley at night. {TU} holds up a small weird metal hair dryer with blinking lights, like a precious object. {HX('Secador de mapas turbo. Original. Casi.', 'raccoon', VT_)} {END('one raccoon', 'the raccoon', 'city noise far away')}",
    otro="TURBIO: «Secador de mapas turbo. Original. Casi.»"),
 tk(F_DES, 6, "TOFFEE + GALLETA", f"{ST(6)} Dark New York alley. On the left, {T} hands over a small bag of dog cookies; on the right, {G} {GX['suplica']} as his cookies are taken away. {END(C2, amb='city noise')}",
    toffee="«Lo pagué con las galletas de Galleta. Es una inversión.» (voz en off)"),
 tk(F_OBS, 6, "TOFFEE", f"{ST(6)} Dark New York alley. Close-up of {T} after the blast, his fur all messed up and full of glitter, staring into the camera in silence. {END('one cat', amb='silence and a small cough')}",
    toffee="«Esto no estaba en mis planes.» (voz en off)"),
 tk(F_REC, 8, "MAPA", f"{ST(8)} Close-up of an old paper map lying on the wet ground of an alley, warm from the air; hundreds of small golden lights appear one after another all over it until it is full of lights. No faces. No one speaks; only a magical shimmer. No phone, no text, no music.",
    toffee="«Y el mapa… se llenó de luces.» (voz en off)"),
 tk(F_REC, 6, "TURBIO", f"{ST(6)} Dark New York alley. {TU} quickly closes his coat and walks backward into the shadows. {HX('Sin devoluciones.', 'raccoon', VT_)} {END('one raccoon', 'the raccoon', 'city noise')}",
    otro="TURBIO: «Sin devoluciones.»"),
 tk(F_CON, 6, "TOFFEE + GALLETA", f"{ST(6)} Dark New York alley. On the left, {T} holds the glowing map, overwhelmed; on the right, {G} {GX['camara']}. {HT('Son cientos. Y el más cercano… está en Hollywood.')} {END(C2, 'the cat', 'city noise')}",
    toffee="«Son cientos. Y el más cercano… está en Hollywood.»"),
]))

# =============== EPISODIO 13 ===============
EP.append(dict(n=13, fecha="Mar 18-nov", titulo="La foto con el ratón más famoso", arriba=("Hice 3 horas de fila", "PARA ESTA FOTO 📸"),
 conflicto="Toffee hace tres horas de fila para la foto con «el ratón más famoso del mundo»… y es un ratón callejero disfrazado que cobra la foto.", recompensa="Ratoncio confiesa que nadie quiere fotos con un ratón de la calle. Toffee se la paga y se la toman los tres.",
 pregunta="¿Qué nombre le ponen al próximo personaje que encontremos?",
 resumen="Los Ángeles. Toffee viene a que lo «descubran». Fila larguísima. El famoso es Ratoncio, un ratón callejero con esmoquin viejo y estrella de plástico. Toffee, estafado, termina pagándole la foto. Número cinco de la lista.",
 fichas=["Ratoncio (el ratón famoso venido a menos)"],
 tomas=[
 tk(F_OBS, 6, "RATONCIO", f"{ST(6)} A glamorous boulevard in Los Angeles at sunset with palm trees and a red carpet. Close-up of {RA}, looking up at the camera, holding out his tiny paw for money. {HX('Son veinte dólares la foto, gato.', 'mouse', VR)} {END('one mouse', 'the mouse', 'street noise')}",
    otro="RATONCIO: «Son veinte dólares la foto, gato.»", gancho=True),
 tk(F_INI, 6, "TOFFEE", f"{ST(6)} A glamorous boulevard in Los Angeles at sunset, palm trees, red carpet. Medium close-up of {T} with sunglasses pushed up on his nightcap, chin up, looking into the camera. {HT('Los Ángeles. Aquí me van a descubrir. Obviamente.')} {END('one cat', 'the cat', 'street noise')}",
    toffee="«Los Ángeles. Aquí me van a descubrir. Obviamente.»"),
 tk(F_DES, 8, "TOFFEE + GALLETA", f"{ST(8)} Los Angeles boulevard, afternoon. {T} and {G} wait at the end of a very long line of tourists' legs on a red carpet, under a palm tree; the cat looks bored, the dog falls asleep standing. Only one cat and one dog are animals in the shot. No one speaks; only street noise. No phone, no text, no music.",
    toffee="«Tres horas de fila para la foto con el ratón más famoso del mundo.» (voz en off)"),
 tk(F_OBS, 6, "TOFFEE", f"{ST(6)} Los Angeles boulevard at sunset. Close-up of {T} staring down at something small, deadpan, one eye twitching. {HT('Me estafaron. En la ciudad de los sueños.')} {END('one cat', 'the cat', 'street noise')}",
    toffee="«Me estafaron. En la ciudad de los sueños.»"),
 tk(F_REC, 8, "RATONCIO", f"{ST(8)} Los Angeles boulevard at dusk. {RA} slowly takes off his sunglasses and looks down, sad, his fake star a little crooked. {HX('Nadie quiere fotos con un ratón de la calle.', 'mouse', VR)} {END('one mouse', 'the mouse', 'quiet street')}",
    otro="RATONCIO: «Nadie quiere fotos con un ratón de la calle.»"),
 tk(F_REC, 6, "TOFFEE + GALLETA + RATONCIO", f"{ST(6)} Los Angeles boulevard at dusk, red carpet. {T}, {G} and {RA} pose together for a photo, a flash goes off; the dog {GX['abrazo']}. Exactly one cat, one dog and one mouse; the cat's whole head, nightcap and camera always in frame. No one speaks; only a camera click. No phone, no text, no music.",
    toffee="«La foto la pagué yo. Número cinco de la lista. Que nadie se entere.» (voz en off)"),
 tk(F_CON, 6, "TOFFEE + MAPA", f"{ST(6)} Night above Los Angeles. Close-up of {T} looking at the map full of hundreds of golden lights, tired. {HT('Son demasiados…')} {END('one cat', 'the cat', 'wind')}",
    toffee="«Son demasiados…»"),
]))

# =============== EPISODIO 14 ===============
EP.append(dict(n=14, fecha="Jue 20-nov", titulo="El día que Toffee se quiso rendir", arriba=("Toffee se", "QUIERE RENDIR 💔"),
 conflicto="El mapa tiene cientos de luces y Toffee cree que la misión es imposible.", recompensa="Galleta se sienta a su lado sin decir nada. Toffee entiende que no está solo… y le pide ayuda a la gente.",
 pregunta="Escriban el nombre de un animalito de la calle que conozcan: va para la lista de Toffee.",
 resumen="Episodio emotivo y corto (la escena 3 que propusiste). Gran Cañón al atardecer. Toffee se rinde. Galleta intenta animarlo con la pelotita del ovni; nada. Entonces solo se sienta a su lado y apoya la cabeza. «No le vayas contando a nadie que tengo sentimientos.» Toffee le pide al público los nombres para la lista.",
 tomas=[
 tk(F_INI, 6, "TOFFEE", f"{ST(6)} Grand Canyon at sunset, huge red cliffs. {T} sits alone at the edge with his back to the camera, then drops the old map next to him. {END('one cat', amb='wind')}",
    toffee="«Me rindo.» (voz en off)", gancho=True),
 tk(F_INI, 8, "TOFFEE", f"{ST(8)} Grand Canyon at sunset. Close-up of {T} looking at the map full of golden lights, tired and sad. {HT('Son cientos. Un gato y un perro no pueden con todos.')} {END('one cat', 'the cat', 'wind')}",
    toffee="«Son cientos. Un gato y un perro no pueden con todos.»"),
 tk(F_DES, 6, "TOFFEE + GALLETA", f"{ST(6)} Grand Canyon at sunset. On the right, {G} drops a small glowing blue ball in front of {T} on the left and waits, wagging his tail; the cat doesn't even look at it. {END(C2, amb='wind')}",
    toffee="(silencio)"),
 tk(F_OBS, 6, "TOFFEE", f"{ST(6)} Grand Canyon at sunset. Close-up of {T}, eyes low. {HT('La misión era una tontería. Nos vamos a casa.')} {END('one cat', 'the cat', 'wind')}",
    toffee="«La misión era una tontería. Nos vamos a casa.»"),
 tk(F_REC, 8, "TOFFEE + GALLETA", f"{ST(8)} Grand Canyon at sunset, golden light. {G} quietly sits next to {T} and {GX['abrazo']}. The cat sighs, looks at him and gently pats his head with one paw. {END(C2, amb='wind')}",
    toffee="(silencio)"),
 tk(F_REC, 6, "TOFFEE + GALLETA", f"{ST(6)} Grand Canyon at sunset. Close-up of {T} with {G} leaning on him. {HT('No le vayas contando a nadie que tengo sentimientos.')} {END(C2, 'the cat', 'wind')}",
    toffee="«No le vayas contando a nadie que tengo sentimientos.»"),
 tk(F_CON, 8, "TOFFEE", f"{ST(8)} Grand Canyon at dusk. {T} stands up, picks up the map and looks into the camera, decided. {HT('Solo no puedo. Pero ustedes son muchos. ¿Me ayudan?')} {END('one cat', 'the cat', 'wind')}",
    toffee="«Solo no puedo. Pero ustedes son muchos. ¿Me ayudan?»"),
]))

# =============== EPISODIO 15 ===============
EP.append(dict(n=15, fecha="Sáb 22-nov", titulo="El barco de hielo", arriba=("¿Qué es ESO", "EN LAS NUBES? ⚡"),
 conflicto="Con la lista llena de nombres (los del público), una tormenta los sorprende y aparece algo gigante entre las nubes.", recompensa="La lista ya tiene más de cien nombres gracias a la gente (en la edición pongo nombres reales de los comentarios). Final con suspenso: «jo, jo, jo».",
 pregunta="¿Ese era Santa? ¿Qué creen que va a pasar?",
 resumen="Cierre de la sección 1. Toffee lee los nombres que mandó la gente. Tormenta. Un rayo muestra un barco de hielo gigante en las nubes. Galleta se esconde; Toffee «evalúa la situación». Un reflector los ilumina y se oye «jo, jo, jo».",
 tomas=[
 tk(F_OBS, 6, "CLIFFHANGER", f"{ST(6)} Stormy night sky. A huge flash of lightning lights up the clouds and reveals, for a second, the giant silhouette of a flying ship made of ice among the clouds. Then darkness. No animals in the shot. No one speaks; only thunder. No phone, no text, no music.",
    toffee="(sin voz)", gancho=True),
 tk(F_INI, 8, "TOFFEE + GALLETA + TRINEO", f"{ST(8)} Night sky above the clouds, calm, stars. {TR} flies with {T} at the front holding a long paper list that unrolls down past the sleigh, and {G} behind him. {END(C2, amb='wind')}",
    toffee="«Leí sus comentarios. La lista ya tiene más de cien nombres.» (voz en off) · EN PANTALLA: nombres reales de los comentarios"),
 tk(F_DES, 6, "TOFFEE", f"{ST(6)} Night sky. Close-up of {T} holding the long list proudly, looking into the camera. {HT('Con esta lista, Santa no se puede negar.')} {END('one cat', 'the cat', 'wind')}",
    toffee="«Con esta lista, Santa no se puede negar.»"),
 tk(F_OBS, 8, "TOFFEE + GALLETA + TRINEO", f"{ST(8)} Stormy night sky with dark clouds and lightning far away. {TR} with {T} at the front and {G} behind him shakes in the strong wind and rain; the cat holds the list tight. {END(C2, amb='thunder far away and rain')}",
    toffee="«Y ahí fue cuando nos agarró la tormenta.» (voz en off)"),
 tk(F_OBS, 6, "TOFFEE + GALLETA", f"{ST(6)} Inside the flying sleigh at night, rain. {G} {GX['escondite']}; {T} sits very straight, pretending to be calm. {HT('Yo no tengo miedo. Estoy evaluando la situación.')} {END(C2, 'the cat', 'rain')}",
    toffee="«Yo no tengo miedo. Estoy evaluando la situación.»"),
 tk(F_CON, 6, "TOFFEE + GALLETA + TRINEO", f"{ST(6)} Stormy night sky. A huge bright searchlight beam from above lands on the small flying sleigh with {T} and {G}, lighting them up. A deep, slow male laugh echoes: 'Ho, ho, ho.' {END(C2, amb='thunder')}",
    toffee="«¿Ese… era Santa?» (voz en off, susurro)"),
]))

# ===================== FORMATO B · cortos para llegar a gente nueva (3/semana) =====================
CORTOS = [
 dict(tipo="Humor", titulo="El gato que se quedó dentro de la maleta", seg=8, fotos="TOFFEE",
      idea="Toffee intenta cerrar la maleta del viaje sentándose encima… y termina adentro. Se entiende sin conocer la serie: gato orgulloso, plan malo.",
      p=f"{ST(8)} Cozy bedroom at night. {T} sits on top of an overstuffed small brown suitcase on the bed, pressing down to close it; the lid suddenly closes over him and only his head with the nightcap and camera sticks out of the zipper, deadpan, looking into the camera. Exactly one cat; the cat's whole head, nightcap and camera always in frame. No one speaks. No phone, no text, no music.",
      voz="«Todo bajo control.»", texto="Texto: «Plan perfecto 👍» · Sonido: un audio de fracaso que esté de moda"),
 dict(tipo="Personalidad", titulo="Revisión de piloto antes de despegar", seg=8, fotos="TOFFEE + GALLETA + TRINEO",
      idea="Toffee hace una revisión exagerada del trineo-cama como si fuera un avión. Galleta ya está dormido adentro. Muestra su carácter: se toma muy en serio algo ridículo.",
      p=f"{ST(8)} Living room at night. {T} walks slowly around {TR}, inspecting it like a serious airplane pilot, tapping the runners with his paw and nodding. Inside the sleigh, {G} is already asleep on his back, snoring. {END(C2, amb='soft room ambience and a snore')}",
      voz="«Patines: bien. Cascabeles: bien. Copiloto: inútil.»", texto="Texto: «Revisión de seguridad 🛷»"),
 dict(tipo="Tendencia adaptada", titulo="Desfile de disfraces (sonido de moda de Halloween)", seg=8, fotos="TOFFEE",
      idea="Usar el sonido de moda del desfile de disfraces, pero a la manera de Toffee: él camina en cámara lenta como modelo… y su «disfraz» es él mismo.",
      p=f"{ST(8)} A spooky runway at night with purple and orange lights and fog. {T} walks slowly toward the camera like a fashion model, in slow motion, chin up, very serious, his pompom bouncing. Exactly one cat; the cat's whole head, nightcap and camera always in frame. No one speaks. No phone, no text, no music.",
      voz="(sin voz: el sonido de moda se pone en TikTok)", texto="Texto: «Mi disfraz de Halloween: un gato guapo. Da miedo, lo sé.»"),
 dict(tipo="Humor", titulo="El botón que no se toca", seg=8, fotos="TOFFEE + GALLETA + TRINEO",
      idea="La escena 2 que propusiste: Toffee prohíbe tocar un botón rojo del trineo, se voltea, Galleta mira el botón, mira a la cámara… corte al desastre.",
      p=f"{ST(8)} Inside the sleigh in the night sky. On the left, {T} points at a big shiny red button on the front of the sleigh and turns away to look at the map. On the right, {G} looks at the button, looks at the camera and {GX['desastre']}. {END(C2, amb='wind')}",
      voz="«Ese botón no se toca. Nunca.»", texto="Segunda toma (4 s): el trineo sale disparado hacia arriba con chispas doradas (mismo prompt base, «the sleigh suddenly shoots straight up into the sky with golden sparks»). Texto: «Lo tocó.»"),
 dict(tipo="Personalidad", titulo="Toffee califica a los monstruos", seg=10, fotos="TOFFEE",
      idea="Toffee, de jurado, califica del 1 al 10 a los monstruos del valle. Frases cortas y crueles, pero graciosas.",
      p=f"{ST(10)} Spooky castle hall with candles. {T} sits behind a small judges' table with a tiny bell, very serious, looking into the camera like a strict judge. {HT('El vampiro: dos. Mide lo que una papa. La calabaza: cinco. Llora mucho.')} {END('one cat', 'the cat', 'candles crackling')}",
      voz="«El vampiro: dos. Mide lo que una papa. La calabaza: cinco. Llora mucho.»", texto="Texto: «Calificando a los monstruos del valle»"),
 dict(tipo="Tendencia adaptada", titulo="La Noche del Miau (coro)", seg=8, fotos="TOFFEE",
      idea="Toffee mueve la cabeza al ritmo del coro de nuestra propia canción, muy serio, como DJ. Sirve para que el sonido circule antes de Halloween.",
      p=f"{ST(8)} Halloween party at night, purple lights. Close-up of {T} nodding his head to a beat with his eyes closed, very serious, like a DJ. Exactly one cat; the cat's whole head, nightcap and camera always in frame. No one speaks. No phone, no text, no music.",
      voz="(sin voz: coro de «La Noche del Miau»)", texto="Texto: «Cuando suena tu canción en la fiesta del vampiro»"),
]

# ===================== FORMATO C · comerciales integrados (2/semana) =====================
COMERCIALES = [
 dict(producto="Orejeras para perros", titulo="La tormenta del valle",
      situacion="Truenos en el valle. Galleta tiembla debajo del trineo. Toffee dice que «no le importa», pero le pone la capucha de las orejeras. Galleta se acomoda y se apoya en él.",
      tomas=[
       f"{ST(6)} Snowy forest at night, lightning far away in the sky. {G} hides under the red sleigh bed, shaking, ears back. {END('one dog', amb='thunder far away')}",
       f"{ST(8)} Snowy forest at night. {T} looks away as if he doesn't care and gently pulls {O} over the head of {G} with his paws. The dog stops shaking and leans against the cat. {END(C2, amb='thunder far away, softer')}",
      ],
      voz="«No lo hice por él. Sus temblores no me dejaban dormir.»",
      cierre="Última toma: la foto real del producto (sin IA) con el texto: «Orejeras acolchadas para perros · tallas S a XL · soytoffee.store».",
      descripcion="Estas son las orejeras que Galleta usa en el viaje 🐶 Es una capucha acolchada que le cubre las orejas. Tallas S a XL (mide la cabeza de tu perro con la guía de tallas). No es un producto médico: a muchos perros les ayuda a estar más cómodos, pero no prometemos que elimine el ruido ni que le quite el miedo. Envío gratis · soytoffee.store · #publicidad"),
 dict(producto="Cama Trineo Navideña", titulo="El vehículo oficial también es cama",
      situacion="De vuelta en casa después de un episodio, Toffee se acuesta en la cama-trineo. Galleta quiere entrar; Toffee lo ignora… y al final le hace espacio.",
      tomas=[
       f"{ST(8)} Cozy living room at night with Christmas lights. {T} lies curled up inside {TR}, eyes half closed, very comfortable. On the right, {G} {GX['suplica']}. {END(C2, amb='soft room ambience')}",
       f"{ST(6)} Cozy living room at night. {T} sighs and moves a little to one side inside the sleigh bed; {G} climbs in happily and curls up next to him. {END(C2, amb='soft room ambience')}",
      ],
      voz="«Para volar no sirve. Para dormir es lo mejor que tengo. Bueno… tenemos.»",
      cierre="Última toma: fotos reales del producto y sus medidas (S 50×38 cm / M 65×52 cm).",
      descripcion="El trineo del viaje es esta cama 🛷 Peluche rojo con borde blanco, paredes altas y base acolchada. Talla S (50×38 cm) y M (65×52 cm). No vuela (lo comprobamos). Envío gratis · soytoffee.store · #publicidad"),
 dict(producto="Disfraz Árbol de Navidad", titulo="El disfraz más aterrador del valle",
      situacion="Se reutiliza el momento del episodio 4 (Galleta gana el concurso) y se agrega una toma nueva: Galleta posa con el disfraz en casa y Toffee lo «califica».",
      tomas=[
       f"{ST(8)} Cozy living room with Christmas lights. {G}, wearing {DIS}, poses proudly; on the left, {T} looks at him like a strict judge and slowly nods. {END(C2, amb='soft room ambience')}",
      ],
      voz="«Aprobado. Asusta monstruos y queda bien en las fotos de Navidad.»",
      cierre="Última toma: fotos reales del disfraz (verde y rojo) y la guía de tallas por peso.",
      descripcion="El disfraz con el que Galleta ganó el concurso de monstruos 🎄 Capa con capucha de árbol de Navidad, estrella y pompones. Para gatos y perros pequeños (guía por peso). Verde o rojo. Envío gratis · soytoffee.store · #publicidad"),
 dict(producto="Cama Trineo Navideña", titulo="¿Caben un gato y un perro?",
      situacion="Prueba honesta de tamaño: Toffee y Galleta se meten en la talla M para ver si caben. Galleta saca media pata. Datos reales de medidas al final.",
      tomas=[
       f"{ST(8)} Bright living room, day. {T} and {G} squeeze together inside {TR}; it is a bit tight, one of the dog's paws hangs over the white rim; the cat looks into the camera, deadpan. {END(C2, amb='soft room ambience')}",
      ],
      voz="«Caben un gato y un perro mediano… si el perro no respira mucho.»",
      cierre="Última toma: las medidas reales en texto grande y foto real del producto.",
      descripcion="Prueba de tamaño de la cama trineo 🛷 Talla M: 65×52×30 cm. Para un gato y un perro pequeño juntos, o un perro mediano solo. Envío gratis · soytoffee.store · #publicidad"),
]
REGLAS_COMERCIAL = [
 "El producto aparece porque tiene sentido en la escena, no al revés.",
 "Siempre se muestra al final el producto REAL (foto sin IA) y se dice qué es, tallas, precio o envío y dónde comprarlo.",
 "En la descripción se pone #publicidad (y en TikTok se activa «Contenido de marca» / divulgación comercial). Es entretenido y transparente.",
 "Orejeras: nunca decir que protegen la audición, que eliminan el ruido o que quitan el miedo. Decir lo que son: una capucha acolchada que cubre las orejas; «a muchos perros les ayuda a estar más cómodos».",
 "Medición: palabra clave por producto en comentarios (CALMA = orejeras, TRINEO = cama, ARBOLITO = disfraz) y enlaces con UTM distintos por formato para ver en Shopify de dónde vienen las visitas y ventas.",
]

# ===================== FOTOS para Instagram (2/semana) =====================
FOTOS = [
 dict(tipo="A · Retrato de Toffee", formato="4:5", fotos="TOFFEE",
      p="Photorealistic portrait, 4:5 vertical. The cream-caramel British Shorthair cat from the reference, wearing his navy knitted nightcap with a cream pompom and a small black action camera on top, sits on a snowy rock at night under a soft green aurora, looking slightly away with a proud, unimpressed expression, snowflakes on his fur. Cinematic, sharp, magical. No text.",
      texto="«Posando para la historia. De nada.» 🛷"),
 dict(tipo="B · Foto que amplía la historia", formato="4:5", fotos="TOFFEE + GALLETA + TRINEO",
      p="Photorealistic, 4:5 vertical. Morning after a crash in a snowy pine forest: the red plush sleigh pet bed from the reference lies tilted in the snow, half buried. The cream-caramel cat from the reference with his navy nightcap and action camera sits on top of it holding a small paper map upside down; the golden-brown criollo dog from the reference sits next to him, happily eating snow. No text.",
      texto="«Actualización del viaje: Galleta dice que el mapa está al revés. Galleta no sabe leer.»"),
 dict(tipo="C · Toffee y Galleta", formato="carrusel 4 fotos", fotos="TOFFEE + GALLETA",
      p="(1) Photorealistic, 4:5: the cream-caramel cat with navy nightcap and action camera and the golden-brown criollo dog with navy bandana sit side by side on a hill at sunset, the dog leaning his head on the cat, the cat pretending not to notice. (2) Same place, wide shot of the landscape. (3) Close-up of the cat rolling his eyes. (4) Close-up of the dog's innocent puppy face. No text.",
      texto="«Él dice que no tiene sentimientos. Desliza ➡️»"),
 dict(tipo="D · Producto dentro del universo", formato="4:5", fotos="TOFFEE + TRINEO",
      p="Photorealistic, 4:5 vertical. Cozy living room with warm Christmas lights at night. The cream-caramel cat with his navy nightcap and action camera sleeps curled up inside the red plush sleigh-shaped pet bed from the reference (red velvet, thick white fluffy rim, candy-cane striped runners, no letters). Calm, warm, cozy. No text.",
      texto="«Descanso después de la aventura. La cama-trineo del viaje está en soytoffee.store 🛷 #publicidad»"),
]

# ===================== Calendario y medición =====================
CALENDARIO = [
 ("Lunes", "Episodio de la historia", "Corto de humor"),
 ("Martes", "Corto de personalidad", "Foto de Toffee"),
 ("Miércoles", "Episodio de la historia", "Comercial integrado en una situación"),
 ("Jueves", "Corto de humor o tendencia", "Foto o carrusel"),
 ("Viernes", "Episodio de la historia", "Corto relacionado con el episodio"),
 ("Sábado", "Comercial", "Encuesta o actualización en Stories"),
 ("Domingo", "Episodio de la historia o desenlace", "Descanso, foto o contenido extra"),
]
SEMANAS = [
 ("Semana 1 (27-oct → 2-nov)", [
   ("Lun 27", "Ep. 2 · La bruja del bosque", "Corto: El gato que se quedó dentro de la maleta"),
   ("Mar 28", "Corto: Revisión de piloto", "Foto A: retrato de Toffee"),
   ("Mié 29", "Ep. 3 · La calabaza miedosa", "Comercial: La tormenta del valle (orejeras)"),
   ("Jue 30", "Corto: Desfile de disfraces (sonido de moda)", "Corto: La Noche del Miau (coro) — si está listo"),
   ("Vie 31", "Ep. 4 · El disfraz más aterrador (Halloween)", "—"),
   ("Sáb 1", "Comercial: El disfraz más aterrador del valle", "Stories: encuesta «¿Quién da más miedo?»"),
   ("Dom 2", "Ep. 5 · El Chupacabras (Día de Muertos)", "Foto B o C"),
 ]),
 ("Semana 2 (3-nov → 9-nov)", [
   ("Lun 3", "Ep. 6 · Perdidos en las nubes", "Corto: El botón que no se toca"),
   ("Mar 4", "Corto: Toffee califica a los monstruos", "Foto C (carrusel)"),
   ("Mié 5", "Ep. 7 · Galleta maneja un Willys", "Comercial: El vehículo oficial también es cama"),
   ("Jue 6", "Corto: momento gracioso del ep. 7 (nuevo, no repetido)", "Foto D"),
   ("Vie 7", "Ep. 8 · La alpaca de Machu Picchu", "—"),
   ("Sáb 8", "Comercial: ¿Caben un gato y un perro?", "Stories: «¿Qué animal va en la lista?»"),
   ("Dom 9", "Ep. 9 · Un ovni se llevó a Galleta", "—"),
 ]),
]
METRICAS = [
 ("Episodios (historia)", "¿La gente vuelve y sigue la serie?", "% visto completo · seguidores nuevos por video · comentarios que hablan de la historia · vistas del episodio anterior al día siguiente"),
 ("Cortos (formato B)", "¿Llegamos a gente nueva?", "vistas de no seguidores · compartidos por cada 1.000 vistas · visitas al perfil · seguidores ganados"),
 ("Comerciales (formato C)", "¿Los productos interesan?", "clics al enlace (UTM) · comentarios con palabra clave (CALMA/TRINEO/ARBOLITO) · sesiones en la tienda · añadidos al carrito · ventas"),
 ("Fotos", "¿Refuerzan al personaje?", "guardados y compartidos · visitas al perfil desde la foto"),
]
CASOS = [
 ("Muchas reproducciones, pocos seguidores", "El video entretiene pero no explica quién es Toffee. Revisa: ¿se entiende su personalidad? ¿hay invitación a seguir la historia?"),
 ("Pocas reproducciones pero muchos compartidos (frente al alcance)", "No lo descartes: la idea es buena. Pruébala otra vez con un gancho más fuerte en los primeros 2 segundos."),
 ("Muchas visitas al perfil, pocos seguidores", "Revisa la biografía, los videos fijados (el vlog 1 primero) y que se entienda la serie al ver el perfil."),
 ("Muchas visitas a la tienda, ninguna compra", "Revisa precio, confianza, envío, tallas y el pago. No asumas que necesitas más vistas."),
 ("Pocos resultados en todo", "Revisa los comienzos, la claridad de la historia y la emoción antes de subir más videos."),
]
REGLAS_MEDICION = [
 "Se mide cada domingo, en 15 minutos, con la hoja «MEDICION-SEMANAL.csv» (una fila por publicación).",
 "Se compara siempre contra el mismo tipo de contenido (episodio con episodio, corto con corto). Nunca se decide por un solo video: se buscan patrones en 3 o más.",
 "Cada 2 semanas (al final de cada mitad de sección) se decide: qué formato repetir más, qué quitar y qué cambiar en la siguiente sección.",
 "En TikTok y Reels, mirar el gráfico de retención: el segundo en que se va la gente dice qué toma hay que mejorar.",
]

DONACIONES = [
 "Por ahora la web no promete ningún porcentaje (se quitó el 3 % el 27-oct y no hubo ventas).",
 "Propuesta: que el programa vuelva en enero, contado dentro de la historia: en el Polo Norte Santa le entrega a Toffee una alcancía (sección 4–5) y desde ahí empieza «el marrano», ahora verificable.",
 "Cómo hacerlo verificable: (1) regla simple y pública (qué % y de qué: subtotal de pedidos pagados, sin envío); (2) un reporte mensual con número de pedidos, monto apartado y monto donado; (3) comprobante de cada donación (recibo de la fundación o del rescatista, con el nombre de la fundación) publicado en Stories destacadas y en la web; (4) dinero apartado en una cuenta o bolsillo separado.",
 "Mientras tanto, la misión de la historia (regalos para animales de la calle) se puede volver real a pequeña escala: el 24-dic llevar cobijas o comida a un refugio y mostrarlo (sin exagerar cifras).",
 "Jay: confírmame si el 3 % vuelve en enero (como dijiste antes) o si quieres otra forma. No lo pongo en ningún video hasta que lo confirmes.",
]

PERSONALIDAD = dict(
 toffee=[("Arquetipo", "El antihéroe con buen corazón: orgulloso, sarcástico, ambicioso, torpe cuando pierde el control y compasivo aunque lo disimule."),
         ("Contradicción", "Quiere que todos lo admiren, pero lo admirable es que ayuda a otros cuando nadie se lo pide."),
         ("Cómo habla", "Frases cortas y secas. Nunca dice «estoy preocupado»: dice que «no piensa perder el tiempo» mientras ya está corriendo. También tiene silencios y momentos sinceros (ep. 9 y 14)."),
         ("Qué NO es", "No insulta a nadie sin motivo, no se burla del sufrimiento animal, no ataca personas reales ni grupos, no cambia de personalidad según la moda.")],
 galleta=[("Arquetipo", "El corazón del grupo y el agente del caos: curioso, impulsivo, cariñoso, valiente sin pensarlo e inesperadamente astuto."),
          ("Contradicción", "Parece el menos preparado, pero es el primero en hacer lo correcto (ep. 2, 3, 6, 8, 14)."),
          ("Cómo «habla»", "No habla: actúa con la cara. Siete expresiones fijas: cara de inocente, sonrisa del desastre, mirada a cámara, escondite, súplica, celebración y abrazo. Se repiten para que se vuelvan su sello."),
          ("Qué NO es", "No es el tonto que siempre arruina todo: en muchos episodios es quien resuelve.")],
)
SALUDO = "«A ver, mis desgraciados…» (alternativa más suave: «Bueno, mis criaturas…»)"
FRASES = [
 ("Cuando algo sale mal", "«¿Quién fue el genio? Ah, fui yo.» · «Excelente. Otra desgracia.» · «Esto no estaba en mis planes.»"),
 ("Cuando Galleta hace algo", "«Galleta, te voy a pedir un favor: piensa.» · «Yo no lo conozco.» · «Galleta no sabía que no sabía.»"),
 ("Cuando presume", "«No es ego si es verdad.» · «La humildad es para los que no tienen talento.» · «El protagonista soy yo.»"),
 ("Cuando tiene miedo", "«Yo no tengo miedo. Estoy evaluando la situación.» · «No es cobardía, es estrategia.» · «Galleta, ve tú primero. Confío plenamente en ti.»"),
 ("Cuando ayuda", "«No lo hice por él. Me estorbaba.» · «Que nadie se entere.» · «No le vayas contando a nadie que tengo sentimientos.»"),
]
GROSERIAS = ("Malas palabras: máximo una por episodio y solo cuando sorprenda. Van siempre como voz en off (Flow puede bloquear un prompt con groserías). "
             "No uso «maricada»: viene de un insulto y puede leerse como burla a un grupo; se cambia por «bobada». Las fuertes («la puta madre», «jodidos») quedan para "
             "momentos puntuales y las marco antes de usarlas.")
ELENCO_FUTURO = [
 ("Don Turbio", "el vendedor sospechoso (mapache con gabardina). Aparece en los lugares más raros vendiendo soluciones absurdas. Debuta en el ep. 11."),
 ("Ratoncio", "el ratón famoso venido a menos (esmoquin viejo, estrella de plástico). Debuta en el ep. 13."),
 ("El superhéroe incompetente", "quiere salvar a todos y siempre empeora las cosas (sección 2)."),
 ("El explorador perdido", "dice ser el mayor aventurero del mundo y nunca sabe dónde está (sección 2–3)."),
 ("El villano que no es malo", "intenta dar miedo y termina ayudando por accidente (sección 3)."),
]
GANCHO_REGLAS = [
 "Cada episodio arranca con su toma GANCHO (⭐): el momento más loco o la revelación, aunque pase después en la historia. Dura 2–4 s en la edición.",
 "En el primer segundo ya está pasando algo (no presentación, no paisaje vacío). Texto arriba con la promesa y una palabra en color.",
 "Después del gancho entra el INICIO: Toffee dice en una frase cuál es el problema.",
 "Cada toma tiene una sola función: INICIO, DESARROLLO, OBSTÁCULO, RECOMPENSA o CONTINUACIÓN. Si una toma no cumple ninguna, se quita.",
 "La pregunta al público solo va cuando la respuesta puede cambiar o enriquecer la historia (marcada en cada episodio).",
]


# ===================== Versión 2.1 (27-oct): episodio día de por medio + video de viralización en cada día intermedio =====================
CORTOS += [
 dict(tipo="Tendencia adaptada", titulo="«Confía en mí» (formato POV)", seg=6, fotos="TOFFEE + GALLETA",
      idea="El meme de «POV: tu amigo dice confía en mí». Galleta al volante con la sonrisa del desastre y Toffee aterrado. Se entiende sin conocer la serie.",
      p=f"{ST(6)} Inside a colorful old Willys jeep on a mountain road, daylight. On the left, {G} sits in the driver's seat with his paws on the steering wheel and {GX['desastre']}; on the right, {T} grips the seat, eyes wide, slowly turning to look into the camera. {END(C2, amb='engine starting')}",
      voz="(sin voz)", texto="Texto: «POV: tu amigo dice “confía en mí”» · Sonido: un audio de suspenso o de moda"),
 dict(tipo="Personalidad", titulo="Toffee prueba una arepa (y dice que no le gusta)", seg=8, fotos="TOFFEE",
      idea="Toffee prueba comida típica del país del episodio. Dice que es «comida de plebeyos»… y se la come toda. Contraste = su personalidad.",
      p=f"{ST(8)} A small wooden table in a colorful Colombian town, morning. {T} sits in front of a plate with a golden Colombian arepa with cheese, sniffs it with a disgusted face, then takes a bite and keeps eating it fast, looking around to check no one is watching. Exactly one cat; the cat's whole head, nightcap and camera always in frame. No one speaks; only street sounds. No phone, no text, no music.",
      voz="«Comida de plebeyos. Horrible.» (voz en off, al inicio)", texto="Texto final: «Calificación de Toffee: 2/10 (se la comió toda)»"),
 dict(tipo="Tendencia adaptada", titulo="Expectativa vs. realidad del viaje", seg=12, fotos="TOFFEE + GALLETA + TRINEO",
      idea="Formato clásico de expectativa contra realidad, en dos tomas. Muy compartible.",
      p=f"TOMA 1 (6 s): {ST(6)} Magical night sky with a green aurora. {TR} flies majestically toward the camera with golden sparkles; {T} at the front looks heroic, {G} behind him. {END(C2, amb='epic wind')}\n\nTOMA 2 (6 s): {ST(6)} Daylight, a snowy pine tree. {TR} is stuck upside down in the branches; {T} hangs from the rim with a flat, tired face while {G} happily licks snow off the cat's face. {END(C2, amb='birds')}",
      voz="(sin voz)", texto="Texto: «Expectativa» / «Realidad»"),
 dict(tipo="Humor", titulo="Galleta contra el cascabel", seg=8, fotos="TOFFEE + GALLETA",
      idea="Un cascabel rebota y Galleta lo persigue sin pensar… directo contra Toffee, que estaba posando. Humor físico fácil de entender.",
      p=f"{ST(8)} Snowy forest at day. On the left, {T} sits posing proudly for the camera. A small golden bell bounces across the snow from the right; {G} chases it with his ears flying and crashes softly into the cat; both roll in the snow and the cat ends up sitting with snow on his face, deadpan. {END(C2, amb='bell jingling and soft thud')}",
      voz="«Galleta, te voy a pedir un favor: piensa.» (voz en off)", texto="Texto: «Estaba posando.»"),
 dict(tipo="Personalidad", titulo="La lista de los que NO reciben regalo", seg=8, fotos="TOFFEE",
      idea="Toffee lee su propia «lista de los que no se portaron bien». El primero siempre es Galleta (por algo ridículo). Invita a comentar.",
      p=f"{ST(8)} Cozy cabin at night with a fireplace. {T} sits holding a small long paper list, reading it very seriously, then looks into the camera over the paper. {HT('Lista de los que no reciben regalo. Número uno: Galleta. Se comió el mapa.')} {END('one cat', 'the cat', 'fire crackling')}",
      voz="«Lista de los que no reciben regalo. Número uno: Galleta. Se comió el mapa.»", texto="Texto: «¿Quién más va en la lista? 👇»"),
 dict(tipo="Humor", titulo="Don Turbio te vende algo", seg=8, fotos="TURBIO",
      idea="El vendedor sospechoso le habla a la cámara como si le vendiera algo a quien está viendo. Personaje que puede volverse favorito del público.",
      p=f"{ST(8)} A dark wet alley at night, steam from the ground. {TU} leans toward the camera and slowly opens his coat, showing a small glass jar with a tiny white cloud inside. {HX('Psst… ¿una nube en frasco? Para cuando estés triste. Original. Casi.', 'raccoon', VT_, 'whispers')} {END('one raccoon', 'the raccoon', 'city noise far away')}",
      voz="TURBIO: «Psst… ¿una nube en frasco? Para cuando estés triste. Original. Casi.»", texto="Texto: «¿Le comprarías?»"),
 dict(tipo="Tendencia adaptada", titulo="Instrucciones de seguridad del trineo", seg=10, fotos="TOFFEE + GALLETA + TRINEO",
      idea="Parodia de la demostración de seguridad de los aviones. Toffee explica serio; Galleta hace todo mal.",
      p=f"{ST(10)} Inside {TR}, parked in a living room. On the left, {T} stands very serious like a flight attendant, pointing to the right and to the left with his paw; on the right, {G} wears a tiny red scarf around his head instead of his neck and {GX['inocente']}. {HT('Las salidas de emergencia están aquí… y aquí. Galleta, eso no va en la cabeza.')} {END(C2, 'the cat', 'soft room ambience')}",
      voz="«Las salidas de emergencia están aquí… y aquí. Galleta, eso no va en la cabeza.»", texto="Texto: «Vuele con Toffee Airlines ✈️»"),
 dict(tipo="Humor", titulo="Cuando Toffee intenta salir tierno en la foto", seg=6, fotos="TOFFEE",
      idea="Toffee intenta poner cara tierna para una foto… y estornuda justo en el flash. Corto, universal, repetible.",
      p=f"{ST(6)} Cozy living room with Christmas lights. Close-up of {T} trying to make a cute face for a photo, eyes wide and head tilted; a camera flash goes off and he sneezes hard at that exact moment, his pompom bouncing. Exactly one cat; the cat's whole head, nightcap and camera always in frame. No one speaks; only a camera click and a tiny sneeze. No phone, no text, no music.",
      voz="(sin voz)", texto="Texto: «Foto de perfil, intento 47»"),
]
DIAS = [
 ("Lun 27-oct", "EPISODIO 2 · La bruja del bosque", "—"),
 ("Mar 28-oct", "VIRAL · El gato que se quedó dentro de la maleta", "Foto A (retrato)"),
 ("Mié 29-oct", "EPISODIO 3 · La calabaza miedosa", "Comercial: La tormenta del valle (orejeras)"),
 ("Jue 30-oct", "VIRAL · Desfile de disfraces (sonido de moda de Halloween)", "—"),
 ("Vie 31-oct", "EPISODIO 4 · El disfraz más aterrador (Halloween)", "—"),
 ("Sáb 1-nov", "VIRAL · La Noche del Miau (coro)", "Comercial: El disfraz más aterrador del valle"),
 ("Dom 2-nov", "EPISODIO 5 · El Chupacabras (Día de Muertos)", "Foto B"),
 ("Lun 3-nov", "VIRAL · El botón que no se toca", "—"),
 ("Mar 4-nov", "EPISODIO 6 · Perdidos en las nubes", "—"),
 ("Mié 5-nov", "VIRAL · Revisión de piloto antes de despegar", "Comercial: El vehículo oficial también es cama"),
 ("Jue 6-nov", "EPISODIO 7 · Galleta maneja un Willys", "—"),
 ("Vie 7-nov", "VIRAL · «Confía en mí» (formato POV)", "Foto C (carrusel)"),
 ("Sáb 8-nov", "EPISODIO 8 · La alpaca de Machu Picchu", "—"),
 ("Dom 9-nov", "VIRAL · Toffee prueba una arepa", "Comercial: ¿Caben un gato y un perro?"),
 ("Lun 10-nov", "EPISODIO 9 · Un ovni se llevó a Galleta", "—"),
 ("Mar 11-nov", "VIRAL · Expectativa vs. realidad del viaje", "Foto D"),
 ("Mié 12-nov", "EPISODIO 10 · Lucha libre", "—"),
 ("Jue 13-nov", "VIRAL · Galleta contra el cascabel", "Comercial (repetir el que mejor funcionó)"),
 ("Vie 14-nov", "EPISODIO 11 · Nueva York", "—"),
 ("Sáb 15-nov", "VIRAL · La lista de los que NO reciben regalo", "Foto"),
 ("Dom 16-nov", "EPISODIO 12 · El vendedor sospechoso", "—"),
 ("Lun 17-nov", "VIRAL · Don Turbio te vende algo", "Comercial"),
 ("Mar 18-nov", "EPISODIO 13 · La foto con el ratón famoso", "—"),
 ("Mié 19-nov", "VIRAL · Instrucciones de seguridad del trineo", "Foto"),
 ("Jue 20-nov", "EPISODIO 14 · Toffee se quiere rendir", "—"),
 ("Vie 21-nov", "VIRAL · Cuando Toffee intenta salir tierno en la foto", "Comercial"),
 ("Sáb 22-nov", "EPISODIO 15 · El barco de hielo (fin de la sección 1)", "—"),
]
