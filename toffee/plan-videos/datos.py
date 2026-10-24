# -*- coding: utf-8 -*-
# Plan de 7 días · 3 videos diarios · Soy Toffee (24 al 30 de octubre de 2026)

T_FULL = ("the chubby round cream-caramel British Shorthair cat from the reference (solid color, no stripes, "
          "very round face with big cheeks, small ears, big round green eyes with very dilated pupils) wearing "
          "his navy blue knitted nightcap with a drooping tip and a cream pompom")
G_FULL = ("the scruffy golden-brown criollo dog from the reference (thin and long-legged, wiry messy fur, bushy "
          "eyebrows and a little beard, floppy half-folded ears, white chest and paws, big nervous brown eyes) "
          "wearing his navy blue bandana with a golden bone-shaped tag")
G_CALLE = ("the scruffy golden-brown criollo dog from the reference (thin and long-legged, wiry messy fur, bushy "
           "eyebrows and a little beard, floppy half-folded ears, white chest and paws, big nervous brown eyes), "
           "dirty and wet, WITHOUT bandana")
O_FULL = ("the dark gray padded ear muff HOOD from the reference (exact copy: one piece of thick dark gray fabric "
          "that wraps over the top and back of the head like a snood and completely covers BOTH ears; the ears are "
          "tucked inside and NOT visible; thin black elastic trim around the face opening; velcro strap under the "
          "chin; muzzle and eyes free; it is NOT headphones, NOT a headband and NOT straps)")
TR_FULL = ("the red plush sleigh-shaped pet bed from the reference (exact copy: red velvet body with a high curved "
           "back, white fluffy faux-fur trim on the edges, white snowflake prints, black runners)")
D_FULL = ("the green Christmas tree pet costume from the reference (exact copy: soft green ruffled cape with small "
          "colorful pompoms, white tie with pompoms under the chin)")
M_FULL = "the big clear glass piggy bank from the reference, filled with coins and a few folded bills"

FOTOS = {
    'T': ('TOFFEE-ficha', 'Toffee'),
    'G': ('GALLETA-oficial', 'Galleta'),
    'O': ('REF-orejeras-gris', 'Orejeras'),
    'TR': ('REF-trineo-rojo', 'Cama trineo'),
    'D': ('REF-disfraz-verde', 'Disfraz árbol'),
    'M': ('F03-marrano-cristal', 'Marrano'),
}


def prompt(dur, escena, cast, sonido='', voz=False, evitar=''):
    """Arma el prompt en inglés con la misma estructura en todos los videos."""
    p = [f"Vertical 9:16, {dur} seconds, 720p, realistic smartphone home video, handheld, natural home lighting, "
         "realistic physics, photorealistic (not cartoon, not 3D)."]
    rep = {'{T}': T_FULL, '{G}': G_FULL, '{GC}': G_CALLE, '{O}': O_FULL, '{TR}': TR_FULL, '{D}': D_FULL, '{M}': M_FULL}
    for k, v in rep.items():
        escena = escena.replace(k, v)
    p.append(escena)
    gato = 'T' in cast
    perro = 'G' in cast
    if gato and perro:
        p.append("The cat and the dog look exactly like the references in every frame; only one cat and one dog.")
    elif gato:
        p.append("The cat looks exactly like the reference in every frame; only one cat, no other animals.")
    elif perro:
        p.append("The dog looks exactly like the reference in every frame; only one dog, no other animals.")
    if gato:
        p.append("The cat keeps his navy nightcap on the whole time.")
    if voz:
        p.append("The animals' mouths stay closed; nobody talks (a voice-over is added later).")
    s = f" ({sonido})" if sonido else ''
    p.append(f"Natural ambient sound only{s}, no voices, no talking, no music.")
    p.append("Avoid: on-screen text, subtitles, logos, watermark, cartoon, 3D render, extra paws, extra animals, "
             "morphing, changing colors" + (", cat without nightcap" if gato else '')
             + (", dog ears visible outside the hood, headphones, headband, thin straps" if 'O' in cast else '')
             + (', ' + evitar if evitar else '') + '.')
    return ' '.join(p)


def toma(dur, cast, escena, sonido='', voz=None, texto=None, evitar=''):
    return dict(dur=dur, cast=cast, prompt=prompt(dur, escena, cast, sonido, bool(voz), evitar), voz=voz, texto=texto)


DIAS = []

# ---------------------------------------------------------------- DÍA 1 · sábado 24-oct
DIAS.append(dict(n=1, fecha='Sábado 24 de octubre', videos=[
 dict(letra='A', red='TikTok', titulo='«Hola, humano»', palabra='TRINEO',
  porque='Formato Chonk: cámara en el piso, la cara llena la pantalla, la pata toca el lente y el final empalma con el inicio. Tu video de Toffee moviendo la cabecita fue el de mejor retención.',
  tomas=[toma(8, ['T'],
   "Extreme low-angle first-person shot: the camera itself lies on the wooden floor of a cozy Colombian living room looking straight up, ultra-wide 0.5x lens; we see the ceiling and a hanging lamp behind the cat. The viewer IS the camera: no phone, no screen and no device visible anywhere in the frame. From the very first frame, the round face of {T} fills the upper half of the frame, looking down into the lens with huge curious eyes. He slowly lowers his face until his nose almost touches the lens, then reaches down and taps the lens itself twice with one soft round paw (the paw pad fills the frame), tilts his head, then lifts his face back to exactly the same position as in the first frame (seamless loop). One single continuous shot, no cuts.",
   sonido='quiet room, soft paw taps on the lens',
   texto='Sticker que gira con la cámara (lo pongo yo): «hola, humano 👋»')],
  edicion='Sin voz. Recorto el final para que empalme perfecto con el inicio. El audio en tendencia lo eliges tú en TikTok al publicar (sonido de Flow bajito).',
  desc='hola, humano 👋 soy Toffee. me dicen gordo; yo digo esponjoso.\nDuermo 14 horas en mi cama trineo. Comenta TRINEO y te la paso 🛷',
  yt='Hola, humano 👋 Soy Toffee, el gato esponjoso',
  tags='#ToffeeyGalleta #gatos #britishshorthair #gatosdetiktok'),

 dict(letra='B', red='Instagram', titulo='«Tu perro no es miedoso»', palabra='CALMA',
  porque='Idea ganadora I2 (contracorriente) + problema real de diciembre. Útil para mandarle a alguien con perro.',
  tomas=[
   toma(8, ['G', 'T'],
    "Night in a cozy Latin American living room; colorful fireworks flash through the window. The camera is placed on the floor UNDER a wooden dining table, looking at the dog, who is also under the table: the dark underside of the table top is visible like a low ceiling at the top of the frame, and chair legs frame the dog on both sides. The dog, {G}, lies flat and pressed against the floor in the far corner under the table, terrified, visibly trembling and shaking the whole time, ears flat back against his head, tail tucked, eyes wide and scared, panting. He stays in exactly the same hiding spot for the whole clip: he does not stand up, does not sit up, does not walk. His scared face is close to the camera from the first frame; each colorful flash lights his face. Between the chair legs, in the background, the round cream legs and the nightcap pompom of {T} are visible on a chair, calm. Slow, small handheld push-in.",
    sonido='distant fireworks', voz='«Humano, tu perro no es miedoso. Su oído es mucho más fino que el tuyo.»',
    evitar='calm dog, dog sitting, dog standing, dog walking toward the camera, dog outside the table, relaxed ears',
    texto='0–3 s: «Tu perro NO es miedoso 🎆»'),
   toma(8, ['G', 'T', 'O'],
    "Same living room at night, fireworks still flashing through the window. From the first frame: {G} lies calm and relaxed on a worn patterned sofa wearing {O}; the dark gray hood clearly covers both of his ears, which are hidden inside it; his eyes slowly close. From the first frame, {T} is already lying curled up against the dog's side on the sofa, facing the camera; near the end the cat looks straight into the camera and slowly blinks. Medium shot, both animals fully visible, gentle handheld camera.",
    sonido='distant fireworks, softer', voz='«Mételo a la casa, acompáñalo y ponle orejeras antes del ruido. Comenta CALMA.»',
    texto='«✔ Adentro  ✔ Acompáñalo  ✔ Orejeras ANTES del ruido» · al final: «Comenta CALMA 🐾»')],
  edicion='Uno las 2 tomas, subtítulos de la voz y la lista en pantalla.',
  desc='Galleta le tenía pánico a la pólvora. Toffee no le dijo «miedoso»: le preparó la noche 🎆🐶\nGuárdalo para diciembre y mándaselo a alguien con perro. Comenta CALMA y Toffee te pasa las orejeras.',
  yt='Mi perro le tiene miedo a la pólvora: qué hacer 🎆',
  tags='#ToffeeyGalleta #pólvora #perros #perrosdecolombia #mascotas'),

 dict(letra='C', red='YouTube', titulo='El diario de Galleta, cap. 1: «La noche que llegó»', palabra='CALMA',
  porque='Historia por capítulos (inicio, problema, final) con un título que la gente busca. La pólvora y Galleta ya son tu mejor video en YouTube.',
  tomas=[
   toma(8, ['G'],
    "New Year's Eve night on a Colombian residential street, colorful fireworks exploding in the sky. The camera lies on the wet asphalt looking UNDER a parked car: the dark underside of the car fills the top of the frame like a low ceiling, with a tire on each side. The dog, {GC}, lies flat on the asphalt UNDER the car, between the front and rear wheels, pressed down, only his head and front paws in the light, visibly trembling, ears flat back, eyes wide and scared, the colorful fireworks reflected in his eyes. He stays in exactly the same hiding spot the whole clip: he does not stand up, does not sit, does not walk out. Low static camera.",
    sonido='fireworks, distant celebration', voz='«Treinta y uno de diciembre. Afuera, todos celebraban. Debajo de un carro, alguien temblaba.»',
    evitar='bandana on the dog, dog sitting next to the car, dog standing, dog outside the car, calm dog'),
   toma(8, ['T'],
    "Inside a cozy house at night: {T} sits on the windowsill looking out through the glass at the street, where fireworks flash and light his face with colors. He narrows his eyes, then hops down decisively. Camera from the side, behind the cat.",
    sonido='fireworks muffled by the window', voz='«Yo no salgo de noche. Yo no salgo nunca. Pero ese perro… estaba solo.»'),
   toma(8, ['T', 'G'],
    "Street at night, fireworks in the distance. {T} walks slowly along the sidewalk to a parked car and lies down next to it, looking underneath. {GC} slowly crawls out from under the car and sniffs the cat's nightcap. Low camera at ground level.",
    sonido='distant fireworks', voz='«Le dije: “Sígueme, humano de cuatro patas”. Y me siguió.»',
    evitar='bandana on the dog'),
   toma(8, ['T', 'G'],
    "Inside a bedroom at night, warm dim light, faint fireworks flashes on the wall. The camera is on the floor facing the side of a bed: between the floor and the bed frame there is a low dark gap. The dog, {GC}, is hidden INSIDE that dark gap UNDER the bed: we only see his two scared eyes shining and the tip of his nose in the shadow; the rest of his body is hidden under the bed and he never comes out. In front of the bed, on the floor, {T} lies like a loaf, facing the camera, guarding the dog, and slowly blinks at the camera. Static camera.",
    sonido='muffled fireworks', voz='«Esa fue la peor noche de su vida.»',
    texto='Al final: «Cap. 2 mañana 🐾»', evitar='bandana on the dog, dog outside the bed, dog standing, dog body visible, dog next to the bed')],
  edicion='Uno las 4 tomas (32 s), subtítulos de la narración y el cierre «Cap. 2 mañana».',
  desc='Así llegó Galleta a la vida de Toffee: un 31 de diciembre, temblando debajo de un carro 🎆🐶 Capítulo 1 de su diario.\n¿Tu perro también sufre con la pólvora? Comenta CALMA.',
  yt='Mi perro le tenía miedo a la pólvora 🎆 El diario de Galleta, cap. 1',
  tags='#ToffeeyGalleta #DiarioDeGalleta #perrorescatado #pólvora'),
]))

# ---------------------------------------------------------------- DÍA 2 · domingo 25-oct
DIAS.append(dict(n=2, fecha='Domingo 25 de octubre', videos=[
 dict(letra='A', red='TikTok', titulo='«La pata que salva la Navidad»', audio='«Chopin» (piano dramático, de RYOpianoforte): convierte el plato de uvas en una escena de película. Alternativa: «Sey Mami» (Cinco Suave).', palabra='CALMA',
  porque='Gancho visual del estudio: la pata de Toffee frena el plato de uvas frente a la cámara. Un solo plano, 6 segundos.',
  tomas=[toma(6, ['T', 'G'],
   "The camera sits directly on a dining table with a Christmas tablecloth, very close, at table level (no phone or device visible in the frame). From the very first frame: a small bowl of green grapes in the center of the frame. The nose and beard of {G} slowly rise from the bottom edge, sniffing toward the bowl. The round cream paw of {T} enters from the side and calmly slides the bowl out of the dog's reach. Then the cat's round face leans into the frame and stares into the lens with total seriousness. One continuous shot.",
   sonido='quiet dining room, bowl sliding on fabric')],
  edicion='Sin voz. Corte justo cuando Toffee mira al lente, para que se repita. Audio en tendencia en TikTok.',
  desc='yo no tiro cosas de la mesa por gusto. bueno, sí. pero esta vez fue por Galleta 🍇🚫\ny si tu perro sufre con la pólvora, comenta CALMA 🎆',
  yt='Mi gato le salvó la Navidad a mi perro 🍇',
  tags='#ToffeeyGalleta #gatos #perros #navidad'),

 dict(letra='B', red='Instagram', titulo='«El error que todos cometen con su perro el 31»', palabra='CALMA',
  porque='Idea ganadora I10: muy colombiana (las 12 uvas) y con un dato real que la gente guarda y comparte. Toffee tira las cosas de la mesa: es su frase.',
  tomas=[
   toma(8, ['T', 'G'],
    "Colombian New Year's Eve dinner table at night: a plate with twelve green grapes, glasses, a small bowl of lentils, yellow decorations. From the first frame: {T} sits on the table next to the grapes, looks into the camera, then deliberately pushes the plate of grapes with his paw until it slides off the edge of the table. {G} sits on the floor, watching, confused.",
    sonido='plate sliding, grapes falling on the floor, distant celebration', voz='«El 31, en Colombia, nos comemos 12 uvas. Pero las uvas son tóxicas para los perros.»',
    texto='0–3 s: «El error del 31 con tu perro 🍇»'),
   toma(8, ['T', 'G'],
    "Same New Year's Eve table: the grapes are gone from the table; {T} sits on the table proudly, chest out, slowly blinking at the camera; {G} rests his chin on the table edge and looks up at the cat with adoration. Fireworks faintly flash through the window.",
    sonido='distant fireworks', voz='«Incluso unas pocas le pueden dañar los riñones. Por eso las tiré. De nada.»',
    texto='«Uvas = TÓXICAS para perros 🚫» · al final: «Mándaselo a quien hace las uvas»')],
  edicion='Uno las 2 tomas, subtítulos y los 2 textos.',
  desc='Toffee tiró las uvas del 31 de la mesa. Esta vez tenía razón: las uvas son tóxicas para los perros 🍇🚫\nMándaselo a quien prepara las uvas en tu casa. Y si tu perro sufre con la pólvora, comenta CALMA.',
  yt='¿Los perros pueden comer uvas? 🍇 El error del 31 de diciembre',
  tags='#ToffeeyGalleta #añonuevo #perros #mascotas #Colombia'),

 dict(letra='C', red='YouTube', titulo='El diario de Galleta, cap. 2: «El primer día»', palabra='CALMA',
  porque='Sigue la serie. Enseña algo útil (a un perro asustado no se le obliga) dentro de la historia.',
  tomas=[
   toma(8, ['T', 'G'],
    "Morning light in a cozy Colombian house with tiled floor. From the first frame: {GC}, peeks out from under a bed, only his nose and nervous eyes visible. In the doorway, {T} sits looking at him. Static camera low on the floor.",
    sonido='quiet morning, birds outside', voz='«Día uno. Galleta no salió de debajo de la cama. A un perro asustado no se le obliga.»',
    evitar='bandana on the dog'),
   toma(8, ['T', 'G'],
    "Morning light, bedroom with tiled floor, static camera low on the floor facing the side of a bed with a dark gap under it. A small white ceramic bowl full of water already sits on the tiles right in front of the dark gap. {T} sits next to the bowl, facing the bed, and gently taps the rim of the bowl once with his paw, as if offering it. He keeps his head up and never puts his face near the water. Then he turns around, walks away and sits down far from the bed, in the background, looking away from it, giving the dog space. Under the bed, {GC} stays hidden in the dark gap: only his nose and the tip of his beard slowly come out of the shadow and sniff the water. His body and legs stay under the bed the whole time",
    sonido='bowl sliding on tiles', voz='«Le dejé agua, me senté lejos y lo ignoré. Los jefes sabemos esperar.»',
    evitar='bandana on the dog, cat drinking, cat licking, cat face in the bowl, dog walking out from under the bed, dog front legs outside the bed, dog drinking, dog body visible'),
   toma(8, ['T', 'G'],
    "Afternoon warm light: {GC}, is out from under the bed, lying on a soft blanket on the floor; {T} lies a short distance away; both slowly fall asleep; the cat's nightcap pompom moves with his breathing. Camera slowly pushes in.",
    sonido='quiet afternoon', voz='«En la tarde salió. Y por primera vez, se durmió cerca de mí.»',
    texto='Al final: «Cap. 3 mañana 🐾»', evitar='bandana on the dog')],
  edicion='Uno las 3 tomas (24 s) y pongo subtítulos.',
  desc='Galleta pasó su primer día escondido debajo de la cama. Toffee no lo obligó: le dejó agua, espacio y paciencia 🐶 Capítulo 2.\n¿Adoptaste un perro? Cuéntale a Toffee cómo fue su primer día. Y si tu perro sufre con la pólvora, comenta CALMA.',
  yt='Perro rescatado: su primer día en casa 🐶 El diario de Galleta, cap. 2',
  tags='#ToffeeyGalleta #DiarioDeGalleta #adopta #perrorescatado'),
]))

# ---------------------------------------------------------------- DÍA 3 · lunes 26-oct
DIAS.append(dict(n=3, fecha='Lunes 26 de octubre', videos=[
 dict(letra='A', red='TikTok', titulo='«Los lunes»', audio='«we fell in love in october» (girl in red): suave y de cama, perfecto para Toffee que no quiere levantarse. Alternativa: «Hello, October» (Tung Tulip).', palabra='TRINEO',
  porque='Personaje congruente (Toffee les tiene pánico a los lunes) y algo que todos viven. Cámara pegada a la cara, como Chonk.',
  tomas=[toma(8, ['T'],
   "Early morning bedroom with soft gray light. Camera POV from the pillow, very close. From the first frame: {T} lies in a messy bed under a blanket, eyes half closed. A phone on the nightstand next to him lights up and buzzes with an alarm. Without opening his eyes, the cat slowly extends one paw, pushes the phone off the edge of the nightstand, pulls the paw back under the blanket and goes back to sleep. Single continuous shot.",
   sonido='phone alarm buzzing, then a soft thud, then silence',
   texto='Una palabra arriba: «lunes.»')],
  edicion='Sin voz. Audio en tendencia en TikTok.',
  desc='no sé qué es un lunes y no quiero saber 😾\nPara los lunes, mi cama trineo. Comenta TRINEO 🛷',
  yt='Mi gato y los lunes 😾',
  tags='#ToffeeyGalleta #lunes #gatos #gatosgraciosos'),

 dict(letra='B', red='Instagram', titulo='«¿Por qué tu perro te sigue al baño?»', palabra='CALMA',
  porque='Idea K: todos lo viven y les da risa. Es el «esto es mi perro» que se manda por mensaje.',
  tomas=[
   toma(8, ['G'],
    "First-person POV of a person walking down a home hallway toward a bathroom, camera at chest height looking down. From the first frame: {G} walks right at the person's feet, looking up, tail wagging. The bathroom door opens and the dog enters first.",
    sonido='footsteps, door opening', voz='«¿Tu perro te sigue al baño? No está loco: tú eres su manada.»',
    texto='0–3 s: «POV: no puedes ir al baño solo 🚽🐶»'),
   toma(8, ['G', 'T'],
    "Inside a small bathroom, first-person POV looking down: {G} sits on the bath mat staring up with love. {T} walks in behind him, sits next to the dog and also stares up at the camera, slowly blinking. Both waiting.",
    sonido='small bathroom echo', voz='«Yo también lo sigo, pero es para vigilar. Etiqueta a alguien que no va al baño solo.»',
    texto='Al final: «Etiqueta a esa persona 👇»')],
  edicion='Uno las 2 tomas y pongo subtítulos.',
  desc='Galleta sigue a su humano hasta el baño. Toffee dice que él solo va a vigilar 🐶🐱\nEtiqueta a alguien que no puede ir al baño solo. Y si tu perro sufre con la pólvora, comenta CALMA.',
  yt='¿Por qué mi perro me sigue al baño? 🚽🐶',
  tags='#ToffeeyGalleta #perros #gatos #mascotas #humor'),

 dict(letra='C', red='YouTube', titulo='El diario de Galleta, cap. 3: «La primera pólvora en casa»', palabra='CALMA',
  porque='Algo colombiano (gana la Selección = pólvora) + el problema real + el título que la gente busca.',
  tomas=[
   toma(8, ['G'],
    "Night, cozy Colombian living room with a plain yellow football jersey (no logos) hanging on a chair; through the window, fireworks explode in the sky. From the first frame: {G} jumps off the sofa in panic and runs out of the frame. Handheld camera.",
    sonido='loud fireworks outside, people cheering far away', voz='«Ganó la Selección. Y en mi barrio, ganar es sinónimo de pólvora.»'),
   toma(8, ['G', 'T'],
    "{G} trembles curled up in a corner behind the sofa, panting, ears back. {T} approaches slowly and sits right next to him. Low camera.",
    sonido='fireworks outside', voz='«Galleta se escondió detrás del sofá. Temblaba como aquel 31.»'),
   toma(8, ['T'],
    "{T} pulls the living room curtain closed with his paw, then climbs onto the TV cabinet and paws at the remote control until the TV turns on with soft light.",
    sonido='fireworks muffled, TV turning on softly', voz='«Cerré las cortinas, prendí la tele y me quedé con él. Ayudó. Pero no fue suficiente.»'),
   toma(8, ['T', 'G'],
    "{G} lies on his bed in a quiet corner of the living room, still alert but calmer; {T} lies pressed against him; the TV glows softly; muffled fireworks flash behind the closed curtain. The cat looks into the camera.",
    sonido='muffled fireworks, soft TV sound', voz='«Esa noche entendí que sus orejas necesitaban ayuda.»',
    texto='Al final: «Cap. 4 mañana 🐾 · Comenta CALMA»')],
  edicion='Uno las 4 tomas (32 s) y pongo subtítulos.',
  desc='Ganó la Selección y el barrio se llenó de pólvora. Toffee cerró las cortinas, prendió la tele y no dejó solo a Galleta 🎆 Capítulo 3.\nComenta CALMA si tu perro también sufre con la pólvora.',
  yt='¿Qué hacer si tu perro le tiene miedo a la pólvora? 🎆 El diario de Galleta, cap. 3',
  tags='#ToffeeyGalleta #DiarioDeGalleta #pólvora #perrosdecolombia'),
]))

# ---------------------------------------------------------------- DÍA 4 · martes 27-oct
DIAS.append(dict(n=4, fecha='Martes 27 de octubre', videos=[
 dict(letra='A', red='TikTok', titulo='«La caja contra el trineo»', audio='«Ramalama (Bang Bang)» (Róisín Murphy): es el sonido de las «revelaciones»; que el golpe de la canción caiga cuando Toffee se tira al trineo.', palabra='TRINEO',
  porque='Idea C: todo dueño de gato ha visto que prefiere la caja. El giro: el trineo le gana a la caja.',
  tomas=[toma(10, ['T', 'TR'],
   "Cozy living room in the afternoon, camera on the floor, wide shot. From the first frame: {T} sits inside an empty cardboard box, only his round head and nightcap visible, staring at the camera. Next to the box stands {TR}, empty. The cat slowly looks at the sleigh bed, looks back at the camera, then climbs out of the box, walks into the sleigh bed, turns around once and flops down with a big satisfied sigh, chin resting on the fluffy edge. Single continuous shot.",
   sonido='cardboard rustling, soft sigh',
   texto='«la caja: 0 · el trineo: 1»')],
  edicion='Sin voz. Audio en tendencia en TikTok.',
  desc='dicen que los gatos preferimos la caja. la caja nunca tuvo bordes de peluche 😼\nComenta TRINEO y te paso la cama 🛷',
  yt='Mi gato prefiere la caja… hasta que llegó esto 🛷',
  tags='#ToffeeyGalleta #gatos #camaparagatos #navidad'),

 dict(letra='B', red='Instagram', titulo='«Tu gato no odia la cama que le compraste»', palabra='TRINEO',
  porque='Idea I6 (contracorriente): la culpa no es del gato, es de la cama. Útil y termina en el producto.',
  tomas=[
   toma(8, ['T'],
    "From the first frame: close-up of {T} sitting next to a flat, thin gray pet cushion on the floor, looking at it with disgust, then looking at the camera with a judging face. Static camera at floor level.",
    sonido='quiet room', voz='«Tu gato no odia la cama que le compraste. Odia que sea plana.»',
    texto='0–3 s: «Tu gato NO odia su cama 🛏️»'),
   toma(8, ['T', 'TR'],
    "{T} inside {TR}, curled up in a perfect ball, chin resting on the high padded fluffy edge, eyes slowly closing. The camera slowly moves a little around the bed.",
    sonido='soft purring', voz='«Nos gustan los bordes: nos hacen sentir protegidos. Busca una con bordes altos. Comenta TRINEO.»',
    texto='«Busca BORDES altos ✔» · al final: «Comenta TRINEO 🛷»')],
  edicion='Uno las 2 tomas, subtítulos y los textos.',
  desc='Toffee rechazó la cama plana y aprobó el trineo. La razón: los bordes 🛏️😼\nMándaselo a quien gastó plata en una cama que su gato no usa. Comenta TRINEO.',
  yt='¿Por qué mi gato no usa su cama? 🛏️',
  tags='#ToffeeyGalleta #gatos #camaparagatos #consejos'),

 dict(letra='C', red='YouTube', titulo='El diario de Galleta, cap. 4: «Las orejeras»', palabra='CALMA',
  porque='La historia llega al producto sin venderlo: enseña los pasos para acostumbrarlo (los mismos de la ficha de la tienda).',
  tomas=[
   toma(8, ['T', 'G', 'O'],
    "Daytime living room. From the first frame: a cardboard delivery box on the floor; {T} sits on top of it like a boss; {G} sniffs the box nervously. The cat hops off; the open box shows {O} inside.",
    sonido='cardboard', voz='«Llegó el paquete. Yo me senté encima: control de calidad.»'),
   toma(8, ['T', 'G', 'O'],
    "{G} sniffs {O} lying on the floor; {T} sits beside them; a human hand enters the frame and gives the dog a small treat while he sniffs. The dog's tail starts to wag.",
    sonido='quiet room', voz='«Primero, que las huela. Y premio. Nada de ponérselas a la fuerza.»'),
   toma(8, ['T', 'G', 'O'],
    "Two gentle human hands put {O} on the head of {G} for a few seconds while {T} watches; the dog gets a treat and caresses and stays calm.",
    sonido='quiet room', voz='«Luego, unos minutos al día, con caricias. Así las siente como algo bueno.»'),
   toma(8, ['T', 'G', 'O'],
    "Night, curtains closed, faint fireworks flashes: {G} lies relaxed on the sofa wearing {O}, eyes closing; {T} sleeps pressed against him, both breathing slowly. Slow camera push-in.",
    sonido='muffled fireworks', voz='«Y la noche de pólvora, se las puse antes del ruido. Amortiguan; no hacen magia. Pero mira.»',
    texto='Al final: «Cap. 5 mañana 🐾 · Comenta CALMA»')],
  edicion='Uno las 4 tomas (32 s) y pongo subtítulos.',
  desc='Las orejeras llegaron y Toffee hizo control de calidad (se sentó encima). Así acostumbraron a Galleta: olerlas, premio, unos minutos al día y ponérselas antes del ruido 🎆 Capítulo 4.\nComenta CALMA y Toffee te pasa el link.',
  yt='Orejeras para perros: cómo acostumbrarlo 🐶 El diario de Galleta, cap. 4',
  tags='#ToffeeyGalleta #DiarioDeGalleta #orejerasparaperros #pólvora'),
]))

# ---------------------------------------------------------------- DÍA 5 · miércoles 28-oct
DIAS.append(dict(n=5, fecha='Miércoles 28 de octubre', videos=[
 dict(letra='A', red='TikTok', titulo='Toffee trabaja en Colombia: «Vendedor de tintos»', palabra='TRINEO',
  porque='Formato de @just.monki (191 mil seguidores en 7 semanas): el personaje hace un oficio local, visto desde los ojos del cliente. Toffee «el jefe» probando trabajos es una serie que no se acaba. Algo colombiano de la semana.',
  tomas=[
   toma(8, ['T', 'G'],
    "Sunny morning on a busy street in a Colombian city center, colorful old buildings. First-person POV of a customer standing in front of a small street coffee cart with big steel thermoses and tiny plastic cups. From the first frame: behind the cart, {T} sits on a stool wearing a tiny white apron, half asleep, like a bored street vendor. The customer's hand enters the frame holding a coin; the cat slowly slides a small steaming plastic cup of black coffee across the cart toward the hand with one paw, without changing his sleepy expression. Under the cart, {G} lies on the sidewalk, watching. Handheld phone footage.",
    sonido='busy street, cars, distant vendors', voz='«Tinto: mil pesos. La sonrisa no viene incluida.»',
    texto='Arriba: «Toffee trabaja en Colombia ☕» · subtítulos en inglés'),
   toma(8, ['T', 'G'],
    "Same street coffee cart, same first-person customer POV. On the cart there is a small plate with one golden buñuelo (round fried cheese bread). The customer's hand slowly reaches for the buñuelo; {T}, wearing the tiny white apron, slowly pulls the plate away with one paw and stares into the camera with total seriousness. From under the cart, the nose of {G} rises toward the plate. Handheld phone footage.",
    sonido='busy street', voz='«El buñuelo no está a la venta. Es mi desayuno.»',
    texto='Al final: «Mañana: otro trabajo 🐾»')],
  edicion='Uno las 2 tomas, subtítulos en inglés y el texto de arriba en español. Sin audio en tendencia: lleva voz.',
  desc='Toffee probó trabajar vendiendo tintos. Duró poco: no quiso vender el buñuelo ☕😾\n¿Qué trabajo le pongo mañana? Y si quieres la cama donde Toffee se recupera de trabajar, comenta TRINEO.',
  yt='Mi gato vende tintos en Colombia ☕ Toffee trabaja, cap. 1',
  tags='#ToffeeyGalleta #Colombia #tinto #gatos'),

 dict(letra='B', red='Instagram', titulo='«¿Gato o perro?»', palabra='TRINEO o CALMA',
  porque='Idea F: el debate más grande de las mascotas, actuado por Toffee y Galleta. La gente opina y etiqueta a su amigo «del otro equipo».',
  tomas=[
   toma(8, ['T', 'G'],
    "Cozy living room, one static shot: on the left, {T} lies on a velvet cushion like a king, half asleep; on the right, {G} sits on the floor wagging his tail fast, holding a slobbery rope toy. From the first frame both look at the camera.",
    sonido='quiet room, tail thumping', voz='«¿Gato o perro? Él te trae la pelota. Yo te dejo dormir conmigo… si hay espacio.»',
    texto='0–3 s: «¿Equipo 🐱 o equipo 🐶?»'),
   toma(8, ['T', 'G'],
    "{G} drops the toy next to the cushion and lies down beside it; {T} opens one eye, rests a paw on the dog's head, and both fall asleep together. Warm light, slow push-in.",
    sonido='quiet room', voz='«Dicen que nos odiamos. Nosotros dormimos juntos. ¿Equipo Toffee o equipo Galleta?»',
    texto='Al final: «Comenta tu equipo 👇»')],
  edicion='Uno las 2 tomas y pongo subtítulos.',
  desc='Dicen que perros y gatos se odian. Toffee y Galleta duermen juntos 🐱🐶\n¿Equipo Toffee o equipo Galleta? Etiqueta a tu amigo del otro equipo. Equipo Toffee: comenta TRINEO (su cama). Equipo Galleta: comenta CALMA (sus orejeras).',
  yt='¿Gato o perro? El debate 🐱🐶',
  tags='#ToffeeyGalleta #gatovsperro #gatos #perros'),

 dict(letra='C', red='YouTube', titulo='El diario de Galleta, cap. 5: «El plan para velitas»', palabra='CALMA',
  porque='Fecha real y muy colombiana (7 de diciembre), sin inventar escasez. Enseña el plan de la guía gratis de la tienda.',
  tomas=[
   toma(8, ['T', 'G'],
    "Evening, Colombian living room with early Christmas lights. From the first frame: {T} sits at a small table next to a paper wall calendar with a big red circle drawn on one day; he taps the circle with his paw; {G} looks at the calendar nervously.",
    sonido='quiet evening', voz='«Faltan unas semanas para velitas. Y esta vez tengo un plan.»',
    evitar='readable text or numbers on the calendar'),
   toma(8, ['T', 'G'],
    "{T} watches while a human hand attaches a small golden ID tag to the bandana of {G}; the dog licks the hand.",
    sonido='tag clinking', voz='«Uno: placa con el número de su humano. Si se escapa, que lo puedan devolver.»'),
   toma(8, ['T', 'G'],
    "{T} drags a soft blanket with his mouth into a quiet corner far from the window, where the dog's bed is, and arranges it with his paws; {G} follows him and lies down.",
    sonido='blanket dragging on the floor', voz='«Dos: un refugio lejos de la ventana. Tres: orejeras antes del ruido.»'),
   toma(8, ['T', 'G', 'O'],
    "Night: {T} sits by the window looking out at small candles glowing on the neighbors' sidewalks; behind him, {G} sleeps calmly wearing {O}. The cat looks back at the camera.",
    sonido='distant celebration, soft', voz='«El plan completo está gratis en mi tienda.»',
    texto='Al final: «Plan gratis en soytoffee.store 🐾 · Comenta CALMA»')],
  edicion='Uno las 4 tomas (32 s) y pongo subtítulos.',
  desc='Faltan unas semanas para velitas y Toffee ya tiene el plan para Galleta: placa con su número, un refugio lejos de la ventana y orejeras antes del ruido 🕯️ Capítulo 5.\nEl plan completo es gratis en soytoffee.store. Comenta CALMA.',
  yt='Cómo preparar a tu perro para la pólvora de diciembre 🕯️ El diario de Galleta, cap. 5',
  tags='#ToffeeyGalleta #DiarioDeGalleta #velitas #pólvora #Colombia'),
]))

# ---------------------------------------------------------------- DÍA 6 · jueves 29-oct
DIAS.append(dict(n=6, fecha='Jueves 29 de octubre', videos=[
 dict(letra='A', red='TikTok', titulo='Toffee trabaja en Colombia: «Peluquero de perros»', palabra='CALMA',
  porque='Segundo oficio de la serie, estilo @just.monki. Cliente: Galleta. Muestra un uso real de las orejeras (el secador de la peluquería) sin que parezca anuncio.',
  tomas=[
   toma(8, ['T', 'G', 'O'],
    "Small, cozy Colombian pet grooming salon with tiled walls and a stainless steel grooming table. First-person POV of the groomer's assistant. From the first frame: {G} stands on the grooming table, wet after a bath, looking nervous. Next to him on the table, {T} sits like the boss of the salon with a small towel over his shoulder. On the table lies {O}; the cat slowly pushes it toward the dog with one paw, then looks at the camera as if giving an order. Handheld phone footage.",
    sonido='small salon, water dripping, distant radio', voz='«Primer cliente del día. Antes del secador: orejeras. Regla de la casa.»',
    texto='Arriba: «Toffee trabaja en Colombia ✂️»'),
   toma(8, ['T', 'G', 'O'],
    "Same grooming salon. Two human hands blow-dry the fur of {G}, who now wears {O} and stands calm and relaxed on the grooming table, eyes half closed, enjoying it. {T} sits next to him with the towel on his shoulder, supervising, and slowly blinks at the camera. Handheld phone footage.",
    sonido='hair dryer running', voz='«Ni se inmutó. Si el tuyo odia el secador, comenta CALMA.»',
    texto='Al final: «Comenta CALMA 🐾»')],
  edicion='Uno las 2 tomas, subtítulos en inglés y los textos en español.',
  desc='Hoy Toffee fue peluquero de perros. Su primer cliente: Galleta. La regla de la casa: orejeras antes del secador ✂️🐶\nSi tu perro odia el secador o la pólvora, comenta CALMA.',
  yt='Mi gato es peluquero de perros ✂️ Toffee trabaja, cap. 2',
  tags='#ToffeeyGalleta #peluqueriacanina #perros #gatos'),

 dict(letra='B', red='Instagram', titulo='«¿Disfrazar a tu mascota es maltrato?»', palabra='ÁRBOL',
  porque='Idea I7: polémica de verdad. Toffee da una respuesta responsable y termina en el disfraz suave.',
  tomas=[
   toma(8, ['T', 'D'],
    "From the first frame: close-up of {T} looking unimpressed at {D} lying on the sofa; he pokes it with his paw, then looks at the camera. Static camera.",
    sonido='quiet room', voz='«¿Disfrazar a tu mascota es maltrato? Depende. Si le aprieta o le tapa ojos y orejas: quítaselo.»',
    texto='0–3 s: «¿Disfrazarlo es maltrato? 🎄»'),
   toma(8, ['T', 'D'],
    "{T} wears {D} on his body (hood down, his navy nightcap still on), walks calmly across a living room with Christmas lights, then sits down and looks at the camera, comfortable.",
    sonido='quiet room', voz='«Si es suave, liviano y solo para la foto, sin obligarlo: está bien. Yo me dejé.»',
    texto='«✔ Suave ✔ Liviano ✔ Poco tiempo ✖ Nunca a la fuerza» · al final: «Comenta ÁRBOL 🎄»')],
  edicion='Uno las 2 tomas, subtítulos y la lista.',
  desc='La pregunta que divide cada diciembre: ¿disfrazar a tu mascota es maltrato? Toffee responde: depende de cómo 🎄\nGuárdalo antes de la foto de Navidad. Comenta ÁRBOL y te pasa el disfraz (para mascotas de 1,5 a 7,5 kg).',
  yt='¿Disfrazar a tu perro o gato es maltrato? 🎄',
  tags='#ToffeeyGalleta #navidad #mascotas #disfrazparaperros'),

 dict(letra='C', red='YouTube', titulo='El diario de Galleta, cap. 6: «La aspiradora»', palabra='CALMA',
  porque='Pregunta común (#40 de tus 100: «¿Por qué mi perro le tiene miedo a la aspiradora?») contada como capítulo.',
  tomas=[
   toma(8, ['T', 'G'],
    "From the first frame: an upright vacuum cleaner stands in a living room, turned off. {G} peeks at it from behind a door frame, ears back. {T} sits right next to the vacuum, unbothered.",
    sonido='quiet room', voz='«Galleta le tiene miedo a dos cosas: la pólvora y la aspiradora. Hoy, la aspiradora.»'),
   toma(8, ['T', 'G'],
    "{G} slowly approaches the turned-off vacuum while a human hand places small treats on the floor near it; the dog eats them, glancing nervously; {T} lies beside the vacuum like a guard.",
    sonido='quiet room', voz='«Apagada, de lejos y con premios. Sin prisa. Que entienda que no muerde.»'),
   toma(8, ['T', 'G'],
    "Later: the vacuum is running at the far end of the room, handled by a person out of focus; {G} lies on his bed at a distance, calm, chewing a toy; {T} sleeps next to him.",
    sonido='vacuum running far away', voz='«Días después, ni la mira. Yo sigo sin perdonarla.»',
    texto='Al final: «Cap. 7 mañana 🐾»')],
  edicion='Uno las 3 tomas (24 s) y pongo subtítulos.',
  desc='Galleta le tiene miedo a la aspiradora. Toffee lo ayudó así: apagada, de lejos y con premios 🐶 Capítulo 6.\nY para la pólvora de diciembre, comenta CALMA.',
  yt='Mi perro le tiene miedo a la aspiradora 😱 El diario de Galleta, cap. 6',
  tags='#ToffeeyGalleta #DiarioDeGalleta #perros #consejos'),
]))

# ---------------------------------------------------------------- DÍA 7 · viernes 30-oct
DIAS.append(dict(n=7, fecha='Viernes 30 de octubre', videos=[
 dict(letra='A', red='TikTok', titulo='«Halloween: Toffee no se disfrazó»', audio='«Halloween ・ cute horror song» (PeriTune): terror tierno. Alternativa: «Ramalama (Bang Bang)», que también se está usando en Halloween.', palabra='ÁRBOL',
  porque='Surfear la tendencia de la semana (Halloween es mañana), como hace Molang. Chiste visual: Toffee parece una calabaza más.',
  tomas=[toma(8, ['T', 'G'],
   "Night, living room decorated for Halloween with carved pumpkins glowing with LED candles and paper bats hanging from the ceiling. From the first frame: {T} sits perfectly still among the pumpkins, his round face glowing orange like another pumpkin. A paper bat drops from the ceiling right in front of {G}, who jumps backward and hides behind the cat. The cat doesn't move at all and slowly blinks at the camera. Single continuous shot.",
   sonido='quiet night, paper rustle',
   texto='Arriba: «el disfraz de calabaza me salió natural 🎃»')],
  edicion='Sin voz. Audio en tendencia de Halloween en TikTok.',
  desc='no me disfracé. así de redondo soy 🎃\npara Navidad sí me dejo: comenta ÁRBOL y te paso el disfraz 🎄',
  yt='Mi gato es la mejor calabaza de Halloween 🎃',
  tags='#ToffeeyGalleta #Halloween #gatos #perros'),

 dict(letra='B', red='Instagram', titulo='«5 cosas para la mejor Navidad de tu perro»', palabra='CALMA',
  porque='Idea I8: la lista de «5 cosas» de Víctor: 4 consejos generales y el quinto es tu producto. Se guarda y se comparte.',
  tomas=[
   toma(8, ['T', 'G'],
    "Christmas living room with warm lights. From the first frame: {G} sits in front of a decorated Christmas tree wagging his tail; {T} sits on the sofa arm above him, looking at the camera like a strict teacher. Static camera.",
    sonido='quiet room', voz='«Cinco cosas para la Navidad de tu perro. Uno: sin uvas ni chocolate. Dos: sin huesos.»',
    texto='«5 cosas para su mejor Navidad 🎄» · «1. Sin uvas ni chocolate» · «2. Sin huesos de pernil o pollo»'),
   toma(8, ['T', 'G', 'O'],
    "Night, faint fireworks flashes through closed curtains: {G} sleeps on his bed in a quiet corner wearing {O}; {T} curls up next to him. Slow push-in.",
    sonido='muffled fireworks', voz='«Tres: placa con tu número. Cuatro: un rincón tranquilo. Cinco: orejeras antes de la pólvora.»',
    texto='«3. Placa con tu número» · «4. Un rincón tranquilo» · «5. Orejeras ANTES del ruido» · al final: «Comenta CALMA»')],
  edicion='Uno las 2 tomas; cada consejo aparece en pantalla cuando Toffee lo dice.',
  desc='La lista de Toffee para que Galleta tenga la mejor Navidad: sin uvas ni chocolate, sin huesos, con placa, con su rincón y con orejeras antes de la pólvora 🎄🐶\nGuárdala y mándasela a quien tenga perro. Comenta CALMA.',
  yt='5 cosas para que tu perro tenga una Navidad tranquila 🎄',
  tags='#ToffeeyGalleta #navidad #perros #consejos #pólvora'),

 dict(letra='C', red='YouTube', titulo='El diario de Galleta, cap. 7: «El valiente» (fin de temporada)', palabra='CALMA',
  porque='Cierra la historia con el cambio (el perro que temblaba, ahora tranquilo: es lo que vende según tu estudio) y explica el marrano.',
  tomas=[
   toma(8, ['T', 'G', 'O'],
    "Night, living room with closed curtains and Christmas lights; fireworks flash faintly behind the curtains. From the first frame: {G}, wearing {O}, lies on the sofa awake but calm, watching the flashes; {T} sits beside him.",
    sonido='muffled fireworks', voz='«Casi un año después de aquel carro. Pólvora otra vez. Galleta, despierto… pero tranquilo.»'),
   toma(8, ['T', 'G', 'O'],
    "Close-up: {G}, wearing {O}, yawns and rests his head on the round back of {T}; the nightcap pompom moves as the cat breathes.",
    sonido='muffled fireworks, soft breathing', voz='«Las orejeras amortiguan. Lo demás lo hicimos juntos: refugio, compañía y paciencia.»'),
   toma(8, ['T', 'G', 'M'],
    "Daytime, a wooden shelf: {T} sits next to {M}; he taps the glass with his paw; {G} looks at it with curiosity.",
    sonido='coins clinking softly', voz='«Por eso, el 3 % de cada venta va a mi marrano: para los que siguen en la calle.»'),
   toma(8, ['T', 'G'],
    "Sunny Colombian street: {T} and {G} sit side by side on the front step of their house, looking at the street; the dog wags his tail; the cat looks into the camera and slowly blinks.",
    sonido='calm street, birds', voz='«Fin de la temporada uno. Si tu perro sufre en diciembre, comenta CALMA.»',
    texto='Al final: «Fin de la temporada 1 🐾 · Comenta CALMA»')],
  edicion='Uno las 4 tomas (32 s) y pongo subtítulos.',
  desc='Casi un año después del carro, Galleta pasó la pólvora despierto pero tranquilo 🐶🎆 Fin de la temporada uno del diario.\nEl 3 % de cada venta va al marrano de Toffee para perritos de la calle. Comenta CALMA.',
  yt='Perro rescatado pasa la pólvora tranquilo 🐶🎆 El diario de Galleta, cap. 7',
  tags='#ToffeeyGalleta #DiarioDeGalleta #pólvora #perrorescatado'),
]))
