# EXTRAVÍO · Capítulo 1, PILOTO (30-oct-2026). Reescrito con el estudio de planos (ESTUDIO-PLANOS.md), el mundo vivo
# y el método de voces que funcionó: Flow hace la toma diciendo la frase → Claude mide el ritmo → Jay hace la voz en
# ElevenLabs con ese ritmo → Claude la pega a la boca.
# python3 toffee/extravio/capitulos/ex01p.py → web/capitulo-01-piloto.html (Artifact)
import os, sys, html
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, here)
from base import TEMP1, GX

# ---------------- Piezas de los prompts ----------------
def S(s): return (f"Horizontal 16:9, {s} seconds. Photorealistic cinematic film look, normal lens (no fisheye, no vignette, no dark corners), "
                  "natural colors, realistic physics. One continuous shot with no cuts, full frame from edge to edge, no black bars.")
T = ("Toffee, the chubby cream-caramel British Shorthair cat from the reference (very round face, big green eyes, navy knitted nightcap "
     "with a cream pompom and a small black action camera on top of the nightcap)")
G = ("Galleta, the scruffy golden-brown criollo dog from the reference (thin wiry fur, bushy eyebrows, white chest and paws, "
     "navy bandana with a gold bone tag)")
L = ("Lucho, the skinny scruffy gray mouse from the reference standing on two legs (huge dark eye bags, big tired eyes, one crooked front tooth, "
     "torn black hoodie, small backpack full of old keys, holding a chunk of yellow cheese)")
Y = "the Snail Postman from the reference (a big snail with a navy postman cap and a leather mail bag, his shell covered in stamps)"
BEAR = "a small one-eyed teddy bear shopkeeper (from the inhabitants reference)"
UMB = "the Umbrella Lady, an old black umbrella that walks with a tiny cane (from the inhabitants reference)"
SOCKS = "three mismatched striped socks crawling like caterpillars (from the inhabitants reference)"
TV = "the Walking TV, an old wooden television with little legs showing static (from the inhabitants reference)"
BALL = "a small yellow rubber squeaky ball"
VT = "with a light, soft and sweet young adult male voice (a 20-year-old light tenor: warm, lazy, smug; clearly a young man, not a child)"
VL = "with a hoarse, raspy, quiet adult male voice, slightly short of breath, with a faint wheezy whistle"
def TT(line, tone="calmly"):
    return f'Toffee speaks in Latin American Spanish {tone}, {VT}: "{line}" His mouth moves clearly in sync with every word. Only Toffee speaks.'
def LL(line, tone="secretively"):
    return f'Lucho speaks in Latin American Spanish {tone}, {VL}: "{line}" His mouth moves clearly in sync with every word. Only Lucho speaks.'
def END(cast, amb, cat=True, dog=False, extras=False):
    s = f"Exactly {cast} as main characters, identical to the references"
    s += ("; the inhabitants are lost objects and small non-cat, non-dog creatures; no other cats or dogs appear." if extras
          else "; no other animals appear.")
    if cat: s += " The cat's whole head, nightcap and camera always in frame."
    if dog: s += " The dog never speaks."
    return s + f" No text, letters or signs with words anywhere, no phone, no selfie stick, no music; only {amb}."

HOME = ("Cozy small apartment living room in the late afternoon, warm window light, a gray sofa, the red sleigh-shaped pet bed on the rug, "
        "the front door on the right side.")
STREET = ("A quiet residential street of a Latin American neighborhood on a rainy late afternoon, wet asphalt, colorful two-story houses, "
          "a sidewalk curb with a metal storm drain grate.")
VORTEX = ("Inside a huge swirling vortex tunnel of lost objects (socks, remote controls, keys, toys, balls, umbrellas, letters) lit by turquoise "
          "magical light (like the vortex reference).")
SEA = ("An endless sea made of millions of colorful balls rolling in slow waves under a huge warm sunset, a beach of lost toys "
       "(like the sea reference).")
CITYV = "the living city of lost things (like the city reference)"
STREETX = ("The main street of the city of lost things at dusk (like the street reference): crooked houses and shops built from stacked suitcases, "
           "books and shoes, round doors, balconies with clothes hanging, paper lanterns, shop signs made of giant objects (no words), "
           "lost objects slowly falling from the amber sky like snow.")
SHOPOUT = "In front of Lucho's key shop (like the shop front reference), in the market street at dusk, paper lanterns and hanging keys."
SHOPIN = ("Inside Lucho's key shop (like the shop interior reference): thousands of old keys hanging from the ceiling on strings like rain, "
          "a wooden counter, shelves of glass jars with glowing turquoise memory spheres, a warm oil lamp, a rolling metal shutter at the front.")
NIGHT = "It is night now: dark blue light, lanterns off, only the faint turquoise glow of the memory jars."
STREETN = ("The main street of the city of lost things at night (like the street reference): crooked houses and shops built from stacked suitcases, "
           "books and shoes, round doors all closed, shop signs made of giant objects (no words), dark blue light, the paper lanterns are off, "
           "only faint turquoise glows behind closed windows.")
SHOPOUTN = "In front of Lucho's key shop (like the shop front reference), in the market street at night: dark blue light, the paper lanterns are off, the shutter closed."
ROOF = ("On the flat roof of Lucho's shop at night (like the rooftop reference): chimneys made of old teapots, a clothesline of single socks, "
        "the glowing turquoise city spread below, lost objects slowly falling like snow.")
BEAM = "a wide beam of soft turquoise light comes down from the dark sky, sweeping slowly over the cobblestones, with the huge shadow of moth wings gliding over the ground"

# ---------------- Las tomas ----------------
REF = dict(T="TOFFEE-viajero.jpg", G="GALLETA-viajero.jpg", L="LUCHO.jpg", S="REF-trineo-rojo.jpg", R="REMOLINO.jpg", M="MAR-DE-PELOTAS.jpg",
           V="CIUDAD-VIVA.jpg", Q="CALLE-PRINCIPAL.jpg", H="HABITANTES.jpg", A="LOCAL-LUCHO-FUERA.jpg", D="LOCAL-LUCHO-DENTRO.jpg",
           Z="AZOTEA-LUCHO.jpg", O="RECUERDO.jpg", X="PLACA-MAX.jpg", Y="CARTERO-CARACOL.jpg", P="POLILLA.jpg")
ESC, N = [], [0]
def esc(t, f): ESC.append(dict(t=t, f=f, tomas=[]))
def nueva(s, fotos, plano, p, quien, voz=None, cont=None, nota=None):
    N[0] += 1
    ESC[-1]['tomas'].append(dict(id=f"P{N[0]:02d}", s=s, fotos=[REF[x] for x in fotos], plano=plano, p=p, quien=quien, voz=voz, cont=cont, nota=nota))
def reusar(n, que, plano, nota=None):
    ESC[-1]['tomas'].append(dict(id=f"R{n:02d}", reuso=True, que=que, plano=plano, nota=nota))

esc("0 · Gancho", "Lo más loco primero (Gnomo): 3–5 s del remolino, después el logo")
nueva(6, "TGR", "Snorricam + primerísimo primer plano",
      f"{S(6)} {VORTEX} Snorricam shot: the camera is rigidly fixed in front of the face of {T} and falls with him; his face stays locked in the center of the frame, screaming with a huge open mouth and huge eyes, while the vortex behind him spins and shakes wildly. For a moment {G} flies past in the background, happy, trying to bite {BALL}. {TT('¡¡GALLETAAAA!!', 'screaming in terror')} {END('one cat and one dog', 'rushing wind', dog=True)}",
      "TOFFEE grita", voz="¡¡GALLETAAAA!!", nota="En la edición: el centro del remolino se convierte en la O-cerradura del logo (match cut).")

esc("1 · La vida de un «influencer»", "INICIO · quién es Toffee y qué quiere (casa, tarde de lluvia)")
nueva(6, "", "Gran plano general de ubicación + grúa que baja",
      f"{S(6)} Extreme wide establishing shot on a rainy late afternoon: a small colorful three-story apartment building in a Latin American neighborhood, wet street, plants on the balconies. Crane shot descending slowly from the rooftop to a second-floor window with warm light, where a small round cat silhouette with a nightcap sits behind the glass. No animals visible except that silhouette. No text, no people, no music; only rain and distant traffic.",
      "(sin voz: llegamos a la casa)")
nueva(6, "TS", "Plano detalle → alejamiento que revela",
      f"{S(6)} {HOME} The shot starts on an extreme close-up of the small black action camera on top of the navy nightcap: its little red recording light turns on. Then the camera pulls back smoothly to reveal {T} sitting proudly on the red sleigh-shaped pet bed like a king on a throne, looking into the lens. {END('one cat', 'a quiet room and soft rain outside')}",
      "(sin voz: empieza la grabación)", nota="Corte a R01 en el momento en que termina de alejarse.")
reusar(1, "Toffee en el trineo: «A ver, mis desgraciados…»", "Plano general frontal (estilo vlog)")
reusar(2, "«Bueno… casi famoso. Tengo doce seguidores…»", "Mismo plano", nota="En la edición: acercamiento lento a su cara en «Y tres son bots» y 1 s de silencio incómodo (deadpan).")
reusar(3, "Galleta mordiendo la pelota en el tapete (voz en off de Toffee: «Él es Galleta…»)", "Ras de suelo")
nueva(5, "", "Plano detalle + acercamiento lento",
      f"{S(5)} {HOME} Extreme close-up insert of an empty wooden key hook on the wall next to the front door, with a faint dusty outline where a set of keys used to hang. The hook is completely EMPTY: no keys, no keychain, nothing hangs on it. Soft rainy daylight. The camera slowly pushes in toward the empty hook. Shallow depth of field. No animals visible. No text, no people, no music; only soft rain.",
      "(Toffee en off: «Mi humana perdió las llaves de la casa hace tres meses…»)", nota="Siembra la meta del capítulo: la llave de casa.")
reusar(4, "Toffee junto a la puerta entreabierta: «Desde entonces deja la puerta… así.»", "Plano general")

esc("2 · La pelota", "DESARROLLO · Galleta lo empieza todo")
reusar(5, "La pelota rebota y sale por la puerta; cara de travieso de Galleta", "Plano general")
nueva(6, "G", "POV de un objeto (la pelota) a ras de suelo",
      f"{S(6)} Camera at floor level fixed just behind {BALL}, moving with it as it bounces out through a slightly open apartment door, down three wet outdoor steps and onto a rainy sidewalk. Behind the ball, {G} runs after it, happy, ears flapping, getting closer to the camera. {END('one dog', 'rain and a squeaky bounce', cat=False, dog=True)}",
      "(sin voz: persecución desde la pelota)")
reusar(6, "Toffee salta del trineo: «Galleta. No. ¡GALLETA!»", "Plano general")
reusar(8, "En la puerta: «Yo no salgo. Yo nunca salgo.» … «Puta madre.»", "Plano medio", nota="La grosería va entre dientes, después del segundo 10.")
nueva(6, "TG", "Cenital (vista de pájaro)",
      f"{S(6)} {STREET} Top-down bird's-eye view from high above the rainy street: tiny {T} walks in the rain along the wet sidewalk toward the storm drain, where tiny {G} is sniffing with his head in the drain opening. Raindrops fall toward the camera. {END('one cat and one dog', 'rain', dog=True)}",
      "(sin voz: Toffee solo y chiquito bajo la lluvia)")
reusar(9, "La alcantarilla brilla: «¿Por qué está brillando la alcantarilla?»", "Plano medio")
nueva(6, "TG", "POV de un objeto (desde adentro de la alcantarilla) + contrapicado",
      f"{S(6)} Camera inside a dark storm drain looking straight up through the metal grate: on the left the face of {T}, on the right the face of {G}, peek down, lit from below by a growing turquoise glow. The grate dissolves into light and both fall down toward the camera, the cat screaming. {END('one cat and one dog', 'rain, a magical whoosh and a scream', dog=True)}",
      "TOFFEE grita (sin palabras)", nota="Reemplaza la toma 10. En la edición: corte en la caída → remolino.")

esc("3 · El Remolino", "OBSTÁCULO · caen a otro mundo")
reusar(11, "Caen por el remolino (la parte después del grito)", "Plano general", nota="Solo 2–3 s: el grito ya lo dio el gancho.")
reusar(12, "Toffee agarrado a un control remoto (en off: «Si me muero, quiero que sepan que fue culpa del perro.»)", "Primer plano")
nueva(4, "TR", "Primerísimo primer plano para match cut",
      f"{S(4)} {VORTEX} Extreme close-up of one big green eye of the cream-caramel British Shorthair cat from the reference, the swirling turquoise vortex reflected in it; the pupil shrinks as a warm golden light floods his face from below. Only the eye and the fur around it fill the frame. {END('one cat', 'rushing wind', cat=False)}",
      "(sin voz)", nota="Match cut: el ojo → el sol del Mar de Pelotas (P09). Aquí no se ven el gorro ni la cámara; es solo el ojo.")

esc("4 · El Mar de Pelotas", "OBSTÁCULO + CORAZÓN · Galleta se hunde y Toffee lo salva")
nueva(6, "M", "Gran plano general de ubicación + travelling lateral",
      f"{S(6)} {SEA} Extreme wide establishing shot, the camera tracking slowly sideways along the shore: the huge sun sits in the center of the frame; waves of colorful balls roll onto a beach of lost toys; lost kites drift in the sky, rubber ducks and a toy sailboat bob on the waves of balls, a flock of lost umbrellas flies like birds; far away, the silhouette of a city of lost things. No animals visible. No text, no people, no music; only rattling waves of balls and wind.",
      "(sin voz: el mundo nuevo)")
reusar(13, "Caen sobre el mar de pelotas", "Plano general")
reusar(14, "«¿Qué… es… esto?»", "Plano medio")
reusar(15, "Galleta se hunde (en off: «¿Galleta?»)", "Plano general")
reusar(16, "Toffee escarba: «¡Galleta! ¡No te mueras, que tú eres el que carga todo!»", "Plano medio", nota="En la edición: temblor de cámara en mano.")
reusar(17, "Lo saca: «Casi me da algo. Por la pelota. Me preocupaba la pelota.»", "Plano medio")

esc("5 · Lucho", "DESARROLLO · las reglas de Extravío (conversación con planos distintos y caminando)")
nueva(6, "LM", "Cambio de foco (rack focus)",
      f"{S(6)} {SEA} On the beach of lost toys: in the foreground a broken red toy car is in sharp focus and the background is blurry. Rack focus to the background: {L} peeks out from behind a pile of lost toys, looks left and right, nervous, and leans toward the camera. {LL('Psst… gato.', 'in a whisper')} {END('one mouse', 'distant waves of balls', cat=False)}",
      "LUCHO: «Psst… gato.»")
nueva(8, "TLM", "Plano de dos personajes + gag de fondo",
      f"{S(8)} {SEA} Two-shot on the beach of lost toys: on the right {L} talks proudly, spreading his arms; on the left {T} listens, wet and offended. Behind them lost objects fall from the sky onto the beach (a remote control, a key, a doll shoe), and at the end a single striped sock falls and lands on the cat's nightcap; the cat shakes it off, disgusted. {LL('Bienvenidos a Extravío. Aquí cae todo lo que se pierde. Medias, controles, llaves… y mascotas.')} {END('one cat and one mouse', 'distant waves of balls')}",
      "LUCHO: «Bienvenidos a Extravío…»", nota="Regla de tres + gag de fondo (la media en la cabeza).")
reusar(20, "Toffee: «Nosotros no estamos perdidos. Yo soy famoso.»", "Plano de dos")
nueva(8, "TLM", "Por encima del hombro (OTS)",
      f"{S(8)} {SEA} Over-the-shoulder shot from behind the cat: the back of the navy nightcap and the small black camera of {T} are blurred in the foreground on the left; on the right, in focus, {L} squints at the cat, then his face lights up as if he recognizes a celebrity. {LL('¿Famoso? ¡Ah, claro! Tú eres el Gato con Botas, ¿cierto?', 'excitedly')} {END('one cat and one mouse', 'distant waves of balls')}".replace(" The cat's whole head, nightcap and camera always in frame.", " The back of the cat's nightcap and camera stay in frame."),
      "LUCHO: «¿Famoso? ¡Ah, claro! Tú eres el Gato con Botas, ¿cierto?»", nota="En la edición: burbuja de pensamiento con el Gato con Botas.")
reusar(22, "Toffee furioso: «¿¡Me ves botas, desgraciado!?»", "Primer plano", nota="Corte seco desde la burbuja.")
reusar(23, "Lucho: «Tranquilo, Botas. Aquí hay una regla…»", "Primer plano")
reusar(24, "Toffee: «Mi humana me está buscando. Seguro. Creo.»", "Primer plano", nota="En la edición: acercamiento lento mientras duda.")
nueva(8, "TGLM", "Travelling lateral (caminar y hablar)",
      f"{S(8)} {SEA} Side tracking shot moving along with them as they walk along the beach of lost toys toward the far city, all seen from the side: in front on the right {L} walking and talking over his shoulder, his backpack of keys jingling; behind him {T}; at the back {G} carrying {BALL}. Kites and lost umbrellas fly in the sky. {LL('¿Y la llave de tu casa? Para volver, necesitas la llave.')} {END('one cat, one dog and one mouse', 'jingling keys and waves of balls', dog=True)}",
      "LUCHO: «¿Y la llave de tu casa? Para volver, necesitas la llave.»")
nueva(6, "TM", "Primer plano en movimiento (travelling lateral)",
      f"{S(6)} {SEA} Side tracking close-up of {T} walking along the beach, looking straight ahead with a flat, annoyed face. {TT('Mi humana la perdió hace tres meses.', 'flatly')} {END('one cat', 'waves of balls')}",
      "TOFFEE: «Mi humana la perdió hace tres meses.»", cont="Mismo movimiento que P13 (siguen caminando).")
nueva(6, "LM", "Primer plano en movimiento",
      f"{S(6)} {SEA} Side tracking close-up of {L} walking along the beach; he grins slowly with his crooked tooth, his eyes shine with business, then a nervous little giggle. {LL('Entonces está aquí. En algún lado. Je, je.', 'slyly')} {END('one mouse', 'jingling keys', cat=False)}",
      "LUCHO: «Entonces está aquí. En algún lado. Je, je.»")

esc("6 · La ciudad viva", "RECOMPENSA · el mundo que nadie ha grabado")
nueva(8, "TGLV", "Grúa que sube y revela (el «wow»)",
      f"{S(8)} At dusk, on top of a hill of lost objects. Crane shot rising from behind {T}, {G} and {L}, who stand small at the edge of the hill, over their heads to reveal {CITYV} below: streets full of tiny moving inhabitants, houses and shops built from stacked suitcases with glowing turquoise windows, round doors, balconies, bridges made of giant keys, paper lanterns lighting up, lost objects slowly falling like snow, a flock of umbrellas flying across the amber sky. {END('one cat, one dog and one mouse', 'a distant lively murmur and soft magical wind', dog=True, extras=True)}",
      "(Toffee en off: «Un mundo entero… que nadie ha grabado nunca.»)", nota="Toma de miniatura y de short.")
reusar(28, "Toffee: «Voy a ser el gato más famoso del multiverso.»", "Primer plano", nota="Voz con «Vooooy».")
reusar(29, "Lucho: «Primero sobrevive a esta noche, Botas.»", "Primer plano")
nueva(8, "TGLQHY", "Travelling de seguimiento por la calle viva",
      f"{S(8)} {STREETX} Tracking shot following from behind as they walk into the busy main street: in the middle {T} turning his head everywhere, on the left {L}, on the right {G}. The world lives around them: {Y} slides past delivering a letter to a round door; {BEAR} opens the door of his sock shop; {SOCKS} climb up a wall; {TV} crosses the street; a lost parrot watches from a balcony; paper letters flutter like birds. {END('one cat, one dog and one mouse', 'a lively street murmur, footsteps and clinking', dog=True, extras=True)}",
      "(sin voz: entran a la ciudad)")
nueva(6, "TQH", "Cámara en mano estilo vlog (caminando de espaldas)",
      f"{S(6)} {STREETX} Handheld camera with natural slight shake: {T} walks backwards down the busy street facing the camera like a vlogger, excited, while behind him {UMB} crosses slowly and {TV} waves its little legs. {TT('Esto es contenido. Esto es puro contenido.', 'excitedly and fast')} {END('one cat', 'a lively street murmur', extras=True)}",
      "TOFFEE: «Esto es contenido. Esto es puro contenido.»")
nueva(6, "GQH", "Plano general cómico (el mundo reacciona)",
      f"{S(6)} {STREETX} In front of a tiny sock shop with a giant sock hanging as its sign: {G} snatches a striped sock from the display table and runs off happily with it in his mouth; {BEAR} comes out of the door and shakes his tiny paw angrily at the dog. {END('one dog', 'a lively street murmur and a little bell', cat=False, dog=True, extras=True)}",
      "(sin voz: Galleta se roba una media)")
nueva(6, "LA", "Contrapicado + cortina metálica",
      f"{S(6)} {SHOPOUT} Low angle looking up at {L} in front of his narrow shop, under a giant rusty key hanging as its sign. He grabs the rolling metal shutter and pulls it up with a loud rattle, then turns to the camera with a proud salesman smile. {LL('Bienvenidos a mi negocio.', 'proudly')} {END('one mouse', 'a rattling shutter and a market murmur', cat=False)}",
      "LUCHO: «Bienvenidos a mi negocio.»")

esc("7 · El local de Lucho", "DESARROLLO · la meta: encontrar la llave de casa entre millones")
nueva(8, "TGLD", "Travelling hacia adelante entre capas (llaves en primer plano)",
      f"{S(8)} {SHOPIN} The camera dollies forward slowly between curtains of hanging keys that pass close to the lens in the foreground; in the midground {T} and {G} walk in, looking up, amazed; in the background {L} stands behind the counter. Lucho wears NO hat and NO camera; only the cat wears the navy nightcap with the camera. {LL('Aquí están todas las llaves que se han perdido en la historia.', 'proudly')} {END('one cat, one dog and one mouse', 'softly jingling keys', dog=True)}",
      "LUCHO: «Aquí están todas las llaves que se han perdido en la historia.»")
nueva(6, "TD", "Dolly zoom (vértigo) · el único del capítulo",
      f"{S(6)} {SHOPIN} Dolly zoom (vertigo effect) on {T} standing in the middle of the shop: the camera moves backward while zooming in, so the cat stays the same size while the endless curtains of hanging keys behind him stretch away into infinity. His face falls, then he looks into the lens. {TT('¿Y cuál es la mía?', 'in a flat, defeated way')} {END('one cat', 'softly jingling keys')}",
      "TOFFEE: «¿Y cuál es la mía?»")
nueva(6, "LD", "Plano medio con remate cómico",
      f"{S(6)} {SHOPIN} Medium shot of {L} behind his wooden counter: he shrugs, takes a bite of his cheese, then a nervous little giggle, his eye bags trembling. {LL('Ni idea. Por eso es negocio. Je, je.', 'casually')} {END('one mouse', 'softly jingling keys', cat=False)}",
      "LUCHO: «Ni idea. Por eso es negocio. Je, je.»")
nueva(6, "GD", "Ras de suelo (mundo de mascota)",
      f"{S(6)} {SHOPIN} Camera on the floor: {G} sniffs along a low dusty shelf full of old keys; his nose stops at one old brass key, his ears go up, and he sneezes, sending a little cloud of dust into the air. Nobody else notices. {END('one dog', 'softly jingling keys and a sneeze', cat=False, dog=True)}",
      "(sin voz: Galleta huele algo… pista para después)", nota="Siembra un misterio: ¿Galleta puede oler la llave de casa?")

esc("8 · La noche de la Polilla", "OBSTÁCULO + CLÍMAX · el mundo se esconde; Galleta persigue un recuerdo y Toffee lo salva")
nueva(8, "QHY", "Gran plano general cenital (todos se esconden)",
      f"{S(8)} {STREETX} A deep bell tolls. Top-down bird's-eye view of the street as night falls: {BEAR} pulls down the shutter of his shop, {Y} pulls his head into his shell, {TV} turns itself off and lies still, the socks hide in a drainpipe, round doors slam shut, the paper lanterns go out one by one. The huge shadow of moth wings glides over the rooftops. No cat, dog or mouse visible. {END('no main characters', 'a deep bell, slamming doors and deep slow wing flaps', cat=False, extras=True)}".replace("Exactly no main characters as main characters, identical to the references; the inhabitants", "The inhabitants"),
      "(sin voz: el mundo reacciona)", nota="La campana empieza a sonar en la toma anterior (sonido adelantado).")
nueva(6, "TGLD", "Plano medio dentro del local, de noche",
      f"{S(6)} {SHOPIN} {NIGHT} {L} slams the rolling metal shutter down from the inside and turns around, terrified, holding his cheese against his chest; behind him {T} and {G} freeze. {LL('Escóndanse. Ella no puede saber que llegaron.', 'in a terrified whisper')} {END('one cat, one dog and one mouse', 'deep slow wing flaps outside', dog=True)}",
      "LUCHO (susurro): «Escóndanse. Ella no puede saber que llegaron.»")
nueva(6, "TGLD", "POV de un objeto (una llave colgada) + picado",
      f"{S(6)} {SHOPIN} {NIGHT} High angle from among the hanging keys near the ceiling, looking down: the keys sway softly in the foreground; below, {T}, {G} and {L} hide crouched under the counter. Thin beams of turquoise light slip through the gaps of the metal shutter and sweep slowly across the room. {END('one cat, one dog and one mouse', 'deep slow wing flaps and a low magical hum', dog=True)}",
      "(sin voz: tensión)")
nueva(6, "GOD", "Primer plano + encuadre dentro del encuadre",
      f"{S(6)} {SHOPIN} {NIGHT} Close-up of {G} lying under the counter, looking through a small square pet flap at the bottom of the metal shutter: outside on the cobblestones, a glowing turquoise memory sphere (like the sphere reference) rolls slowly past, like a ball. The dog's ears go up, {GX['desastre']}, and he squeezes out through the flap. {END('one dog', 'a soft magical hum', cat=False, dog=True)}",
      "(sin voz: Galleta ve el recuerdo como si fuera una pelota)")
nueva(6, "TD", "Primer plano (holandés)",
      f"{S(6)} {SHOPIN} {NIGHT} Dutch angle, the camera tilted about 15 degrees. Close-up of {T} under the counter watching the dog leave, eyes wide; he whispers in panic, then sighs, closes his eyes for a second and crawls toward the flap. His fur stays warm cream-caramel, never white or gray, even in the blue night light. {TT('Galleta… no. Yo no corro. Yo nunca corro.', 'in a panicked whisper')} {END('one cat', 'deep slow wing flaps outside')}",
      "TOFFEE (susurro): «Galleta… no. Yo no corro. Yo nunca corro.»", nota="Callback de «Yo no salgo» → corte seco a P30.")
nueva(6, "TQ", "Snorricam (pánico)",
      f"{S(6)} {STREETN} Snorricam shot: the camera is rigidly fixed in front of the face of {T} and runs with him; he sprints down the dark empty street as fast as he can, his face locked in the center of the frame, while the dark houses and the turquoise light behind him shake and swing wildly. {END('one cat', 'running paws, panting and deep wing flaps')}",
      "(sin voz: Toffee corre… sí corre)")
nueva(6, "TGOQ", "Picado general",
      f"{S(6)} {STREETN} High angle wide shot of the empty street: in the middle, {G} happily pushes the glowing memory sphere with his nose; {BEAM}, getting closer to him. From the left, {T} sprints toward the dog. {END('one cat and one dog', 'wing flaps getting louder', dog=True)}",
      "(sin voz)")
nueva(6, "TGOQ", "Plano general con corte en la acción",
      f"{S(6)} {STREETN} {T} grabs {G} by the navy bandana with his front paw and pulls him behind an overturned wooden cart full of lost umbrellas at the side of the street. A moment later the turquoise light beam passes over the spot where the dog was, and the glowing memory sphere floats up into the light and disappears into the sky. The cat wears NO bandana and NO tag. {END('one cat and one dog', 'a loud whoosh and deep wing flaps', dog=True)}",
      "(sin voz: el rescate)", cont="Usar el último cuadro de P31 como primer cuadro.")
nueva(6, "TGQ", "Primer plano de dos (escondidos)",
      f"{S(6)} Behind an overturned wooden cart of lost umbrellas, at night, close two-shot: on the left {T} holds one front paw over the mouth of {G}, on the right; both have huge eyes, frozen. Turquoise light slides slowly over the umbrellas and their faces, then darkness and silence. The cat wears NO bandana and NO tag. {END('one cat and one dog', 'deep wing flaps fading away', dog=True)}",
      "(sin voz: el silencio)")
nueva(6, "TGQ", "Mismo plano (remate)",
      f"{S(6)} Behind the overturned cart of lost umbrellas, at night, same close two-shot, dim turquoise light: on the left {T}, still shaking, looks at {G} and whispers furiously; the dog licks the cat's face. The cat wears NO bandana and NO tag. {TT('Si me vuelves a hacer eso, te vendo. A Lucho.', 'in a furious whisper')} {END('one cat and one dog', 'a quiet night', dog=True)}",
      "TOFFEE (susurro): «Si me vuelves a hacer eso, te vendo. A Lucho.»", cont="Usar el último cuadro de P33 como primer cuadro.")
nueva(6, "LA", "Plano medio (remate cómico)",
      f"{S(6)} {SHOPOUTN} {L} pokes his head out of the small pet flap at the bottom of his shop's metal shutter, looking at the camera, surprised, then forces a big fake smile with his crooked tooth. {LL('¿Siguen vivos? Qué decepción… digo, ¡qué alegría! Je, je.', 'nervously')} {END('one mouse', 'a quiet night', cat=False)}",
      "LUCHO: «¿Siguen vivos? Qué decepción… digo, ¡qué alegría!»")

esc("9 · La azotea y Max", "RECOMPENSA + CONTINUACIÓN · a salvo… y el misterio")
nueva(8, "TGLZ", "Plano general de espaldas (espacio negativo)",
      f"{S(8)} {ROOF} Wide shot from behind: {L}, {T} and {G} sit small at the edge of the roof looking at the glowing city; lots of empty night sky above them. Calm. {END('one cat, one dog and one mouse', 'soft magical wind', dog=True)}",
      "(Lucho en off: «Aquí arriba no sube. Por ahora.»)")
nueva(6, "GXZ", "Acercamiento lento a la placa",
      f"{S(6)} {ROOF} Medium shot of {G} sitting calmly on the roof. The camera slowly and smoothly pushes in toward his neck until the gold bone tag on his navy bandana fills the frame; the tag starts glowing softly and the name MAX engraved on it becomes clear (like the tag reference). {END('one dog', 'a soft magical hum', cat=False, dog=True)}".replace(" No text, letters or signs with words anywhere,", " No other text anywhere,"),
      "(sin voz: MAX)", nota="Si no se lee MAX bien claro, se repite.")
nueva(6, "TGZ", "Plano de dos → primer plano",
      f"{S(6)} {ROOF} On the left, {T} leans close to the softly glowing tag on the bandana of {G}, reads it, frowns and turns to look into the lens, confused. {TT('¿Max? ¿Quién carajos es Max?', 'confused')} {END('one cat and one dog', 'soft magical wind', dog=True)}",
      "TOFFEE: «¿Max? ¿Quién carajos es Max?»")
nueva(10, "TGLZ", "Plano general fijo (pantalla final)",
      f"{S(10)} {ROOF} Calm wide shot from behind, slightly higher: {L} asleep curled around his cheese, {T} and {G} sitting side by side at the edge of the roof, the glowing city below and lost objects falling like snow. Lots of empty sky in the upper half. {END('one cat, one dog and one mouse', 'soft magical wind', dog=True)}",
      "(Toffee en off: «¿Ustedes saben quién es Max? Los leo. Sígueme para no perderte el próximo episodio.»)", nota="Pantalla final de YouTube: 15–20 s (congelo el final si hace falta).")


# ---------------- Puentes (30-oct-2026): tomas que unen escenas para que el capítulo fluya como una serie ----------------
esc("Puentes · tomas que unen escenas", "SECUENCIA · cada una va entre dos tomas que ya existen; así no hay saltos de lugar")
nueva(6, "TS", "Plano general (une R03/P04 con R04)",
      f"{S(6)} {HOME} Wide shot: {T} hops down from the red sleigh-shaped pet bed, walks slowly and lazily across the rug toward the front door on the right, and sits down next to the slightly open door, looking at it with a judging face. {END('one cat', 'a quiet room and soft rain outside')}",
      "(sin voz: Toffee va hasta la puerta)", cont="Usar el último cuadro de la toma R02 (Toffee en el trineo) como primer cuadro.", nota="Va justo antes de R04 (la puerta entreabierta).")
nueva(8, "TGLM", "Plano general siguiendo de espaldas (une P15 con P16)",
      f"{S(8)} {SEA} Wide tracking shot from behind: the three walk away from the beach of lost toys and climb a gentle slope made of lost objects (suitcases, umbrellas, old toys) toward the top of a hill at sunset: in front {L}, then {T}, then {G}. Kites and umbrellas fly in the warm sky. {END('one cat, one dog and one mouse', 'soft wind and footsteps on objects', dog=True)}",
      "(sin voz: suben la colina)", nota="Va después de P15 y antes de P16 (la grúa que revela la ciudad).")
nueva(8, "TGLV", "Plano general de frente (une R29 con P17)",
      f"{S(8)} At dusk, a wide path made of stacked old suitcases goes down from the hill into the city of lost things (like the city reference) and passes under a tall arch made of two giant crossed keys, the entrance to the city. Wide shot from the front: {L}, {T} and {G} walk down the path toward the camera and pass under the arch, the busy city glowing behind them. {END('one cat, one dog and one mouse', 'a distant lively murmur and footsteps', dog=True, extras=True)}",
      "(sin voz: entran a la ciudad)", nota="Va después de R29 y antes de P17 (la calle viva).")
nueva(6, "TGLA", "Plano general de espaldas (une P20 con P21)",
      f"{S(6)} {SHOPOUT} {L} holds the rolling metal shutter up; the camera follows from behind as {T} and {G} walk under it into the shop, looking up at the thousands of keys hanging inside. {END('one cat, one dog and one mouse', 'a rattling shutter and jingling keys', dog=True)}",
      "(sin voz: entran al local)", cont="Usar el último cuadro de P20 como primer cuadro.", nota="Va después de P20 y antes de P21.")
nueva(6, "TGLZ", "Contrapicado desde la azotea (une P35 con P36)",
      f"{S(6)} {ROOF} Low camera on the roof looking down into a square open hatch in the roof floor: {L} climbs up a narrow wooden ladder and out through the hatch, then {T} squeezes out after him, then {G} jumps out; they shake off the dust and walk toward the edge of the roof. {END('one cat, one dog and one mouse', 'creaking wood and soft magical wind', dog=True)}",
      "(sin voz: suben a la azotea)", nota="Va después de P35 y antes de P36.")

# ---------------- Repetidas (31-oct-2026): Jay no aprobó estas tomas; nuevos ángulos ----------------
esc("Repetir · nuevos ángulos", "REEMPLAZAN a P01, P05 y P13 (P47 y P48 quedan de reserva: Jay aprobó los puentes)")
nueva(6, "TGR", "Plano general cayendo junto a ellos (reemplaza P01)",
      f"{S(6)} {VORTEX} Medium-wide shot, the camera falls together with them and rotates slowly: the whole body of {T} is visible, tumbling head over heels, legs and tail flailing, screaming toward the dog with a huge open mouth; on the right, {G} falls happily, upside down, trying to bite {BALL} floating next to him. Lost objects (socks, keys, remote controls) swirl past between them and the camera. {TT('¡¡GALLETAAAA!!', 'screaming in terror')} {END('one cat and one dog', 'rushing wind', dog=True)}".replace("The cat's whole head, nightcap and camera always in frame.", "The cat's whole body, nightcap and camera always in frame."),
      "TOFFEE grita: «¡¡GALLETAAAA!!»", nota="Se ve a Toffee entero (no solo la cabeza).")
nueva(6, "G", "Travelling lateral a ras de suelo (reemplaza P05)",
      f"{S(6)} Side tracking shot at floor level, the camera moving from left to right: {BALL} bounces out through an open apartment door, AWAY from the house, down three wet outdoor steps and onto a rainy sidewalk, always moving forward to the right, ahead of the dog. {G} runs after it from left to right, happy, ears flapping, following the ball. The ball never moves backward. {END('one dog', 'rain and a squeaky bounce', cat=False, dog=True)}",
      "(sin voz: Galleta persigue la pelota)")
nueva(8, "TGLM", "Plano lateral bajo, caminando (reemplaza P41)",
      f"{S(8)} At sunset, a slope made of lost objects (suitcases, umbrellas, old toys) rises from the beach of the sea of balls toward a hilltop. Low-angle side shot, the camera tracking slowly from left to right with them: the three walk in a line up the slope, clearly walking step by step, their legs moving: in front {L}, pointing ahead with his cheese, then {T}, puffing, then {G}, trotting happily. The huge sun is behind them, kites and umbrellas fly in the sky. {END('one cat, one dog and one mouse', 'soft wind and footsteps on objects', dog=True)}",
      "(sin voz: suben la colina)", nota="Tienen que CAMINAR (que se les muevan las patas), no quedarse parados.")
nueva(8, "TGLV", "Travelling de espaldas que sube al pasar el arco (reemplaza P42)",
      f"{S(8)} At dusk, a path made of stacked old suitcases goes down from the hill toward a tall arch made of two giant crossed keys, the entrance to the city of lost things (like the city reference). Tracking shot from behind: {L}, {T} and {G} walk down the path away from the camera, side by side, clearly walking; as they pass under the arch, the camera rises slightly and reveals the busy glowing street of the city ahead of them, full of lanterns and tiny inhabitants. {END('one cat, one dog and one mouse', 'a distant lively murmur and footsteps', dog=True, extras=True)}",
      "(sin voz: entran a la ciudad)")
nueva(8, "TGLM", "Plano medio lateral, cerca (reemplaza P13: se veían muy pequeños)",
      f"{S(8)} {SEA} Medium shot from the side at their eye level, the camera tracking along with them as they walk along the beach of lost toys, close enough that the three fill most of the frame (their heads and bodies big in the frame, the sea of balls blurred behind them): in front on the right {L}, walking and talking over his shoulder, his backpack of keys jingling; in the middle {T}, listening; at the back on the left {G}, carrying {BALL}. {LL('¿Y la llave de tu casa? Para volver, necesitas la llave.')} {END('one cat, one dog and one mouse', 'jingling keys and waves of balls', dog=True)}",
      "LUCHO: «¿Y la llave de tu casa? Para volver, necesitas la llave.»", nota="Que se vean grandes, cerca de la cámara.")

# ---------------- Arreglos del 31-oct-2026 (revisión de Jay): queso que aparece/desaparece y la persecución nocturna ----------------
esc("Arreglos · queso y persecución", "P50–P54: el queso de Lucho siempre en la mano; la huida con la Polilla visible y cómo se meten al carrito")
CHEESE = "Lucho holds the same chunk of yellow cheese in his left paw from the first frame to the last frame; the cheese never disappears and never appears suddenly."
nueva(8, "TGLM", "Plano medio lateral, cerca (reemplaza P49/P13: el queso aparecía de golpe)",
      f"{S(8)} {SEA} Medium shot from the side at their eye level, the camera tracking along with them as they walk along the beach of lost toys, close enough that the three fill most of the frame (the sea of balls blurred behind them): in front on the right {L}, walking and talking over his shoulder, his backpack of keys jingling; in the middle {T}, listening; at the back on the left {G}, carrying {BALL}. {CHEESE} {LL('¿Y la llave de tu casa? Para volver, necesitas la llave.')} {END('one cat, one dog and one mouse', 'jingling keys and waves of balls', dog=True)}",
      "LUCHO: «¿Y la llave de tu casa? Para volver, necesitas la llave.»", nota="El queso, en su mano TODO el tiempo.")
nueva(6, "TGLA", "Plano general frente al local (reemplaza P43: el queso desaparecía)",
      f"{S(6)} {SHOPOUT} {L} holds his chunk of yellow cheese between his teeth and lifts the rolling metal shutter with both paws; then he takes the cheese back in his left paw and steps aside. {T} and {G} walk in under the shutter, looking up at the thousands of keys hanging inside. The cheese is always visible: first in his mouth, then in his paw. {END('one cat, one dog and one mouse', 'a rattling shutter and jingling keys', dog=True)}",
      "(sin voz: entran al local)", cont="Usar el último cuadro de P20 como primer cuadro.")
nueva(6, "GOPQ", "Plano general de noche: la Polilla aparece (va después de P28)",
      f"{S(6)} {STREETN} Wide shot from behind {G}: the dog trots happily down the middle of the dark empty street, following the glowing turquoise memory sphere (like the sphere reference) that rolls slowly ahead of him like a ball. Above the rooftops at the end of the street, the giant moth from the moth reference rises slowly into view as a dark silhouette with huge stained-glass wings and two glowing turquoise eyes; a wide beam of soft turquoise light comes down from her eyes and starts sweeping the cobblestones toward the dog. {END('one dog and the giant moth', 'deep slow wing flaps and a low magical hum', cat=False, dog=True)}",
      "(sin voz: Galleta sigue el recuerdo; aparece la Polilla)", nota="Así se ve que la Polilla está ahí desde el principio de la huida.")
nueva(6, "TGOPQ", "Plano general con corte en la acción: se meten al carrito (reemplaza P32)",
      f"{S(6)} {STREETN} At the side of the street there is an overturned wooden cart full of old lost umbrellas. {T} sprints in from the left, grabs {G} by the navy bandana and pulls him, and both jump head first into the cart and disappear among the umbrellas. One second later the turquoise light beam from the giant moth above sweeps over the spot where the dog was, and the glowing memory sphere floats up into the light. The cat wears NO bandana and NO tag. Same dark blue night light for the whole shot. {END('one cat, one dog and the giant moth (only her light and shadow)', 'a loud whoosh, umbrellas rustling and deep wing flaps', dog=True)}",
      "(sin voz: el rescate y el escondite)", cont="Usar el último cuadro de P31 como primer cuadro.")
nueva(6, "LQ", "Plano medio: Lucho los encuentra en el carrito (reemplaza P35)",
      f"{S(6)} {STREETN} The moth is gone and the street is quiet. {L} walks up to the overturned wooden cart full of lost umbrellas, pushes two umbrellas aside with his free paw and peeks inside at the camera (the camera is inside the cart, looking up at him through the umbrellas), surprised, then forces a big fake smile with his crooked tooth. {CHEESE} {LL('¿Siguen vivos? Qué decepción… digo, ¡qué alegría! Je, je.', 'nervously')} {END('one mouse', 'a quiet night', cat=False)}",
      "LUCHO: «¿Siguen vivos? Qué decepción… digo, ¡qué alegría!»", nota="Mismo lugar que el escondite (el carrito), así se entiende la escena.")

# ---------------- Imágenes nuevas (Nano Banana Pro) ----------------
IMG = [
 ("CIUDAD-VIVA", "16:9 · referencia: EXTRAVIO-CIUDAD",
  "Photorealistic cinematic 16:9 extreme wide shot at dusk from a hill: a living fantastical city built entirely from lost things. Streets and alleys full of tiny moving inhabitants (a teddy bear pushing a cart, walking socks, an old TV with legs, a snail with a mail bag, lost parrots and hamsters). Crooked houses and shops made of stacked old suitcases, books and shoes, with round doors, glowing turquoise windows, balconies with clothes hanging, chimneys made of teapots, paper lanterns lighting up, bridges made of giant keys between buildings, a market street full of stalls. Lost objects (socks, keys, letters, small umbrellas) slowly falling from a warm amber sky like snow, a flock of umbrellas flying like birds. Same style and colors as the reference. No people, no cats, no dogs, no text."),
 ("CALLE-PRINCIPAL", "16:9 · referencia: EXTRAVIO-CIUDAD",
  "Photorealistic cinematic 16:9 street-level wide shot at dusk: the busy main street of a fantastical city built from lost things. Both sides lined with crooked houses and small shops made of stacked suitcases, books and shoes: round wooden doors, shop windows, balconies with single socks hanging on clotheslines, paper lanterns strung across the street, shop signs made of giant objects instead of words (a giant sock, a giant key, a giant envelope, a giant teacup). Cobblestones, puddles reflecting turquoise windows, lost objects slowly falling like snow. A few inhabitants: a small one-eyed teddy bear in front of a sock shop, an old umbrella walking with a tiny cane, an old TV with little legs. The center of the street is empty for the characters. No people, no cats, no dogs, no text or letters anywhere."),
 ("HABITANTES", "1:1 · hoja de 2×2, fondo neutro",
  "Character reference sheet, 2x2 grid, photorealistic 3D cinematic style, neutral studio background, full body, each character alone in its square: top left, a small worn one-eyed teddy bear shopkeeper with a button eye and a tiny apron, standing on two legs; top right, the Umbrella Lady, an old black umbrella with a lace trim that walks with a tiny wooden cane and has two small kind eyes on the handle; bottom left, three mismatched striped socks crawling like caterpillars with tiny button eyes; bottom right, the Walking TV, an old wooden 1970s television with an antenna, static on its screen and two thin metal legs. Same lighting and scale feel in all four. No text, no labels."),
 ("LOCAL-LUCHO-FUERA", "16:9 · referencias: MERCADO-DE-LLAVES y LUCHO",
  "Photorealistic cinematic 16:9 shot at dusk: the narrow front of a tiny key shop squeezed between two crooked buildings in a market street of a fantastical city of lost things. A giant rusty old key hangs above the door as the shop sign; the front has a half-open rolling metal shutter with a small square pet flap at the bottom; strings of old keys hang in the shop window like curtains; glass jars with glowing turquoise orbs on a little table outside; paper lanterns; cobblestones. Same style as the market reference. No characters, no people, no animals, no text or letters anywhere."),
 ("LOCAL-LUCHO-DENTRO", "16:9 · referencia: MERCADO-DE-LLAVES",
  "Photorealistic cinematic 16:9 interior of a tiny cluttered key shop in a fantastical city of lost things: thousands of old keys of every size hanging from the ceiling on strings like glittering rain, a worn wooden counter with a brass bell and a chunk of cheese on it, dusty shelves with glass jars holding glowing turquoise memory spheres, low shelves full of loose keys, a warm oil lamp, the rolling metal shutter of the front closed with thin gaps of light. Warm and mysterious. No characters, no people, no animals, no text or letters anywhere."),
 ("AZOTEA-LUCHO", "16:9 · referencia: CIUDAD-VIVA",
  "Photorealistic cinematic 16:9 shot at night: the flat rooftop of a tiny shop in a fantastical city of lost things, with chimneys made of old teapots, a clothesline of single socks, an old armchair without legs, and a low edge. Below and far away, the whole city glows with turquoise windows and paper lanterns; lost objects slowly fall from the dark blue sky like snow. Calm and magical, lots of sky. No characters, no people, no animals, no text."),
]

# ---------------- Página ----------------
ORDEN = [t['id'] for e in ESC for t in e['tomas']]
NUEVAS = [t for e in ESC for t in e['tomas'] if not t.get('reuso')]
def page():
    e_ = html.escape
    tot = sum(t['s'] for t in NUEVAS)
    h = ['<h1>Extravío · Capítulo 1 (piloto): Me caí a otro mundo persiguiendo a mi perro</h1>',
         f'<p class="sub">{len(NUEVAS)} tomas nuevas ({tot // 60}:{tot % 60:02d} sin recortar) + {len(ORDEN) - len(NUEVAS)} que ya tienes · Omni 1.1 Flash · 16:9 · duración final ≈ 4:30</p>',
         '<h2>Cómo se hace (en este orden)</h2><ol>'
         '<li><b>Imágenes nuevas</b> (abajo): primero, porque las tomas las usan de referencia.</li>'
         '<li><b>Tomas nuevas en Flow</b> (P01–P' + f'{len(NUEVAS):02d}' + '): con la frase dentro del prompt; Flow la dice y mueve la boca.</li>'
         '<li>Me mandas las tomas → mido cómo habló Flow en cada una → te mando el <b>texto con ritmo</b> para ElevenLabs (como en la prueba que funcionó).</li>'
         '<li>Haces las voces (2 versiones de cada una) → yo las pego a la boca y armo el capítulo con música, sonidos y transiciones.</li></ol>'
         '<p>Las tomas «R» ya las tienes (son las del capítulo anterior); solo cambia el orden y el montaje.</p>',
         '<h2>Imágenes nuevas (Nano Banana Pro)</h2>']
    for n, fmt, p in IMG:
        h.append(f'<h3>{e_(n)}</h3><p class="sub">{e_(fmt)}</p><pre>{e_(p)}</pre>')
    h.append('<h2>El capítulo, toma por toma</h2>')
    for es in ESC:
        h.append(f'<h3>{e_(es["t"])}</h3><p class="sub">{e_(es["f"])}</p>')
        for t in es['tomas']:
            if t.get('reuso'):
                h.append(f'<div class="toma"><div class="meta">{t["id"]} · YA LA TIENES (toma {int(t["id"][1:])}) · {e_(t["plano"])}</div><div class="voz">{e_(t["que"])}</div>'
                         + (f'<div class="sub">{e_(t["nota"])}</div>' if t['nota'] else '') + '</div>')
                continue
            chips = ''.join(f'<span class="chip">{e_(f)}</span>' for f in t['fotos']) or '<span class="chip">sin fotos</span>'
            h.append(f'<div class="toma"><div class="meta">{t["id"]} · NUEVA · {t["s"]} s · {e_(t["plano"])}</div>{chips}')
            if t['cont']: h.append(f'<div class="cont">{e_(t["cont"])}</div>')
            h.append(f'<div class="voz"><b>{e_(t["quien"])}</b></div>')
            if t['nota']: h.append(f'<div class="sub">{e_(t["nota"])}</div>')
            h.append(f'<pre>{e_(t["p"])}</pre></div>')
    h.append('<h2>Lo que hago yo en la edición</h2><ul><li>Logo que sale del remolino (match cut a la O-cerradura).</li>'
             '<li>Match cut del ojo de Toffee al sol del Mar de Pelotas.</li><li>Burbuja de pensamiento del Gato con Botas.</li>'
             '<li>Acercamientos lentos, temblor de cámara en mano, sonido que se adelanta (la campana de la noche), fundido del atardecer a la noche.</li>'
             '<li>Música: Lost Things Waltz (casa y ciudad), Run For It (caída y persecución), Moonfall Charm (logo, misterio y final). Los sonidos del mundo salen de las tomas de Flow.</li></ul>')
    return "\n".join(h)

if __name__ == '__main__':
    src = open(os.path.join(TEMP1, 'build_web.py')).read()
    head = src[src.index("head = '''") + 10: src.index("'''", src.index("head = '''") + 10)].replace('<title>El viaje de Toffee</title>', '<title>Extravío · Piloto</title>')
    script = src[src.index("<script>"): src.index("</script>") + 9]
    os.makedirs(os.path.join(here, 'web'), exist_ok=True)
    open(os.path.join(here, 'web', 'capitulo-01-piloto.html'), 'w').write(head + '<main>' + page() + '</main>\n' + script)
    print('nuevas:', len(NUEVAS), 'segundos:', sum(t['s'] for t in NUEVAS), '· reusadas:', len(ORDEN) - len(NUEVAS), '· orden:', ' '.join(ORDEN))
