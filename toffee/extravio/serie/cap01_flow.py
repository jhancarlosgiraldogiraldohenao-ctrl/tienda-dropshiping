# -*- coding: utf-8 -*-
"""Capítulo 1 de Extravío (Dizzy) · parte 6: prompts de Google Flow (Omni 1.1 Flash), vertical 9:16.
python3 toffee/extravio/serie/cap01_flow.py -> CAP01-FLOW-P1.md (y datos para el HTML)
Cada generación da una o varias tomas del guion (CAP01-GUION.md).
"""
import os, json
AQUI = os.path.dirname(os.path.abspath(__file__))

HEAD = ("Vertical 9:16, {d} seconds. High-quality 3D animated movie style, exactly the same look as the character reference images, "
        "cinematic lighting, normal lens (no fisheye, no vignette, no dark corners). One continuous shot with no cuts, full vertical frame from edge to edge, no black bars.")
VOZ = {"DIZZY":"in Colombian Spanish with a raspy, hoarse, rough young male street voice",
       "GERTRUDIS":"in Colombian Spanish with a soft, shaky, sweet old grandmother voice",
       "TOCINO":"with a loud, raspy male voice and a very heavy American accent",
       "BARTOLO":"in Spanish with a very deep, slow, tired old male voice",
       "CUCA":"in Colombian Spanish with a fast, bright, sassy Caribbean female voice",
       "TUERTO":"in Colombian Spanish with a low, calm, husky male voice",
       "GALLINAZO":"in Spanish with a very deep, croaky male voice",
       "LLORONA":"in Spanish with a high, trembling, wailing female voice"}
QUIEN = {"DIZZY":"Dizzy","GERTRUDIS":"Doña Gertrudis","TOCINO":"Tocino","BARTOLO":"Bartolo","CUCA":"Cuca","TUERTO":"El Tuerto","GALLINAZO":"the vulture","LLORONA":"La Llorona"}
# Solo para que Flow mueva la boca: groserías suavizadas (la voz real de ElevenLabs lleva la grosería)
SUAVE = [("hijueputa","hijuepucha"),("Hijueputa","Hijuepucha"),
         ("malparidos","mal portados"),("malparida","mal portada"),("Gonorrea","Qué horror"),("pirobo","bobo"),("What the fuck","What the heck"),
         ("me mata","me regaña"),("compramos perico","compramos polvito"),("muestra esa cuca","muestra esa cara")]
def suave(t):
    for a,b in SUAVE: t=t.replace(a,b)
    return t

LOCK = {
 "DIZZY": "The rat looks exactly like the reference image: gray rat with big tired red-rimmed eyes, cap with a small action camera on top, gold chain, and he is ALWAYS wearing his black hoodie (never bare-chested, the hoodie covers his body and arms), white socks with black slides, backpack with keys",
 "PATA": "Only the gray paw and black hoodie sleeve of the rat from the reference image are visible",
 "GERTRUDIS": "The hen looks exactly like the reference image: old brown speckled hen with a flowered headscarf, rosary and real wings",
 "BARTOLO": "The mule looks exactly like the reference image: old brown mule wearing a black-and-white striped Colombian sombrero vueltiao (never a plain straw hat), leather bag and two plain sacks on his back",
 "TOCINO": "The pig looks exactly like the reference image: skinny dirty pink pig on four legs with a black mohawk, cracked sunglasses, torn leather vest and his old scratched electric guitar",
 "CUCA": "The cockroach looks exactly like the reference image: brown cockroach standing on her back legs, red bikini, gold hoop earrings on her antennae",
 "TUERTO": "The cat looks exactly like the reference image: small black-and-white cat with an eye patch, a toothpick and a gray tracksuit jacket",
 "LLORONA": "The ghost woman looks exactly like the reference image: pale glowing ghost in a torn white lace dress holding a burnt arepa",
 "VENDEDORES": "The market creatures look exactly like the reference image (black vulture in an apron, gray opossum, fat toad with gold chains, old rat with a hat, green iguana)",
}
NOMBRE = {"DIZZY":"the rat","GERTRUDIS":"the hen","BARTOLO":"the mule","TOCINO":"the pig","CUCA":"the cockroach","TUERTO":"the cat","LLORONA":"the ghost woman","GALLINAZO":"the vulture"}
REF = {"DIZZY":"DIZZY-FRENTE.jpg","PATA":"DIZZY-FRENTE.jpg","GERTRUDIS":"GERTRUDIS-FRENTE.jpg","BARTOLO":"BARTOLO-FRENTE.jpg","TOCINO":"TOCINO-FRENTE.jpg","CUCA":"CUCA-FRENTE.jpg","TUERTO":"TUERTO-FRENTE.jpg","LLORONA":"LLORONA-FRENTE.jpg","VENDEDORES":"VENDEDORES-HUECO.jpg","GALLINAZO":"VENDEDORES-HUECO.jpg"}

LUZ = {
 "ZARZO": "Inside the wooden farmhouse attic from the reference, soft golden sunrise light through the round window",
 "ZARZO-NOCHE": "Inside the wooden farmhouse attic from the reference at night, dark blue moonlight through the round window",
 "FINCA": "On the porch of the white Colombian coffee farmhouse from the reference, early morning, soft golden sunrise light",
 "CAMINO": "On the dirt mule trail between coffee plants and giant wax palms from the reference, bright morning sun with mist",
 "PLAZA": "In the colorful coffee-town square from the reference, sunny morning",
 "ESQUINA": "At the sunny street corner of the town square from the reference, the bench and lamp post beside them",
 "OLLA": "In the hidden night market at the bottom of a ravine from the reference, always night, bare light bulbs, burning barrels, smoke",
 "ESCALERAS": "On the broken concrete stairs that go down into the hidden neighborhood from the reference, at night, orange firelight below",
 "AEREA-FINCA": "High above the Colombian coffee mountains in the early morning, soft golden sunrise light and mist",
 "AEREA-PUEBLO": "High above the green coffee mountains on a sunny morning",
 "AEREA-OLLA": "High above a deep ravine at night, orange firelight glowing below",
 "CARNE": "At the dirty meat stall of the night market from the reference, a bare light bulb above",
 "RINCON": "In the dark corner of the night market from the reference with the car-seat armchair, red light bulb and burning barrel, at night",
}
SONIDO = {"AEREA-FINCA":"wind and birds far away","AEREA-PUEBLO":"wind and church bells far away","AEREA-OLLA":"wind and fire crackling far below","ZARZO":"roosters far away and creaking wood","ZARZO-NOCHE":"crickets at night","FINCA":"birds, wind in the coffee plants and hens","CAMINO":"hooves on dirt and birds","PLAZA":"church bells far away and a fountain splashing","ESQUINA":"a fountain splashing far away and a soft breeze","OLLA":"fire crackling, dripping water and a crowd of creatures murmuring","ESCALERAS":"footsteps on concrete and wind","CARNE":"a knife on a wooden board and fire crackling","RINCON":"fire crackling in the barrel"}

# (id, segundos, tomas del guion, lugar, [personajes], cámara, primer cuadro, acción, (quien, frase) o None, ref de lugar)
P1 = [
 ("G01",10,"1, 2 y 6","ZARZO",["DIZZY"],"Close-up very near the lens, static, his whole head, cap and camera inside the frame",
  "From the first frame Dizzy's face is very close to the lens",
  "He talks straight to the camera like a vlogger, looks left and right suspiciously, lowers his voice, then becomes serious",
  ("DIZZY","¿Quiubo pues, mis ratas? Este es mi primer vlog… y si mi cucha se entera de dónde saqué esta cámara, me mata. Que es distinto, malparidos."),"ZARZO.jpg"),
 ("G02",6,"3","RINCON",["DIZZY","TUERTO"],"Medium shot from the side of a small wooden domino table, static, warm golden flashback tint",
  "From the first frame Dizzy sits on the left and El Tuerto on the right of the table",
  "Dizzy pushes a big pile of colorful bottle caps into the middle of the table; El Tuerto places the small black action camera next to them",
  None,"HUECO-RINCON-TUERTO.jpg"),
 ("G03",4,"4","RINCON",["PATA"],"Extreme close-up insert under the table, shallow depth of field, warm golden flashback tint",
  "From the first frame we only see Dizzy's gray rat paw and the torn black hoodie sleeve under the table",
  "The paw secretly slides one white domino tile out of the hoodie sleeve",None,"HUECO-RINCON-TUERTO.jpg"),
 ("G04",6,"5","RINCON",["DIZZY","TUERTO"],"Medium shot from the side of the domino table, static, warm golden flashback tint",
  "From the first frame Dizzy sits on the left and El Tuerto on the right",
  "Dizzy slams a domino tile on the table, grins and drags the small action camera toward himself; El Tuerto stares at him with his one eye, very angry",None,"HUECO-RINCON-TUERTO.jpg"),
 ("G05",6,"7","AEREA-FINCA",[],"Aerial drone shot slowly descending toward the house",
  "Aerial view of the white coffee farmhouse from the reference alone on the green mountain",
  "The drone slowly glides down toward the house through the morning mist",None,"AEREA-FINCA.jpg"),
 ("G06",6,"8","FINCA",["DIZZY"],"Medium shot, the camera moves backward in front of him as he walks",
  "From the first frame Dizzy walks toward the camera along the wooden porch, the hammock and flower pots behind him",
  "He walks and talks to the camera, proud, showing the house with one paw",
  ("DIZZY","Esta es la finca de mi abuela. Aquí vivo… gratis."),"FINCA-ESPERANZA.jpg"),
 ("G07",4,"9","FINCA",["BARTOLO"],"Close-up of the mule's face, static, the camera at his eye level",
  "From the first frame Bartolo stands on the coffee-drying patio looking straight at the camera with half-closed eyes",
  "He stares, bored, then says one word and snorts",("BARTOLO","…No."),"FINCA-ESPERANZA.jpg"),
 ("G08",4,"10","FINCA",["DIZZY"],"Medium shot, static",
  "From the first frame Dizzy stands on the porch facing the camera",
  "He points with his thumb to his left, toward someone off screen, and rolls his eyes",
  ("DIZZY","Este es Bartolo, el hijueputa más amargado de Colombia."),"FINCA-ESPERANZA.jpg"),
 ("G09",6,"11","FINCA",["GERTRUDIS"],"Wide shot of the porch, the camera low at a small animal's height, static",
  "From the first frame the blue wooden door is closed",
  "The blue door bursts open and Doña Gertrudis comes out holding a yellow flip-flop sandal under one wing, alarmed",
  ("GERTRUDIS","¡Mijito! Ay, Dios mío, ¿y esa vaina qué es?"),"FINCA-ESPERANZA.jpg"),
 ("G10",4,"12","FINCA",["DIZZY"],"Medium shot, static",
  "From the first frame Dizzy stands on the porch facing the camera",
  "He quickly hides both paws behind his back and smiles innocently",
  ("DIZZY","Nada, abuelita, nada."),"FINCA-ESPERANZA.jpg"),
 ("G11",10,"13 y 14","FINCA",["GERTRUDIS","BARTOLO"],"Medium shot of the hen from a low angle, static",
  "From the first frame Doña Gertrudis stands on the porch in the center; Bartolo with his two sacks is blurred in the background on the right",
  "She points with her wing toward the sacks on the mule, then raises one feather like a finger, stern but loving",
  ("GERTRUDIS","Lleve esos dos bultos de café al pueblo, que debemos en la tienda. Y me trae la panela, mi amor. Y no se me demore, que a las seis hay comida. ¡Dios me lo bendiga!"),"FINCA-ESPERANZA.jpg"),
 ("G12",6,"15","CAMINO",["DIZZY","BARTOLO"],"Aerial drone shot following from behind and above",
  "From the first frame Bartolo walks down the trail with Dizzy riding on his back between the two sacks, small in the frame",
  "They go down the winding trail between the giant wax palms",None,"CAMINO-PALMAS.jpg"),
 ("G13",4,"16","CAMINO",["DIZZY","BARTOLO"],"Medium shot from the front, the camera moves backward with them",
  "From the first frame the small Dizzy sits on the saddle in the middle of Bartolo's back between the two sacks, both facing the camera",
  "Bartolo walks calmly; Dizzy talks to the camera, relaxed",
  ("DIZZY","Vamos pa'l pueblo, mis ratas. Facilito."),"CAMINO-PALMAS.jpg"),
 ("G14",4,"17","CAMINO",["DIZZY","BARTOLO"],"Wide shot in profile, static",
  "From the first frame Bartolo walks from left to right with the small Dizzy sitting on the saddle in the middle of his back",
  "Bartolo stops dead in one instant; Dizzy jolts forward and almost falls off, holding on to the sacks",None,"CAMINO-PALMAS.jpg"),
 ("G15",4,"18","CAMINO",["DIZZY","BARTOLO"],"Medium shot from the side, static, both whole bodies in frame",
  "From the first frame Bartolo stands still on the trail facing left and the small Dizzy sits on the saddle in the middle of Bartolo's back, between the two sacks, behind the mule's neck",
  "Dizzy leans forward and shouts very angrily at Bartolo's head; Bartolo does not move",
  ("DIZZY","¡Muévete, perro! ¿Qué te pasa, estúpido?"),"CAMINO-PALMAS.jpg"),
 ("G16",4,"19","CAMINO",["BARTOLO"],"Close-up of the mule's face from the front, static",
  "From the first frame Bartolo stands still on the trail",
  "He does not move at all, eyes half closed, not even blinking",None,"CAMINO-PALMAS.jpg"),
 ("G17",6,"20","CAMINO",["DIZZY","BARTOLO"],"Medium shot from the side, static",
  "From the first frame the small Dizzy sits on the saddle in the middle of Bartolo's back",
  "Dizzy leans forward and holds a small brown block of panela in front of Bartolo's nose; Bartolo's ears go up and he starts walking forward slowly; both stay fully inside the frame the whole time",None,"CAMINO-PALMAS.jpg"),
 ("G18",6,"21","AEREA-PUEBLO",[],"Aerial drone shot moving forward toward the main square",
  "Aerial view of the colorful coffee town on the green mountain ridge from the reference",
  "The drone flies forward over the roofs toward the white church and the square",None,"AEREA-PUEBLO.jpg"),
 ("G19",6,"22","PLAZA",["DIZZY","BARTOLO","LLORONA"],"Wide shot of the square, static",
  "From the first frame Bartolo with Dizzy on his back enters the square from the left in the foreground",
  "In the background La Llorona floats across the square from right to left, wailing dramatically at her burnt arepa",
  ("LLORONA","¡Se me quemó la arepaaa!"),"PLAZA.jpg"),
 ("G20",4,"23","PLAZA",["DIZZY"],"Close-up, static",
  "From the first frame Dizzy stands on the stone pavement of the square facing the camera, no vehicle, nothing in his paws",
  "He looks at the camera, tired and unimpressed",("DIZZY","Todos los días, parce."),"PLAZA.jpg"),
 ("G21",8,"24 y 25","ESQUINA",["TOCINO"],"Medium shot, static",
  "From the first frame Tocino sits on the sidewalk next to the bench holding his old scratched electric guitar across his front legs; an empty hat lies in front of him",
  "He strums the electric guitar badly; he keeps holding the guitar the whole time, it never disappears; then he looks up to the right, sees someone and nods happily",
  ("TOCINO","¡Hey, dude!"),"PLAZA-ESQUINA-TOCINO.jpg"),
 ("G22",6,"26","ESQUINA",["TOCINO"],"Close-up of the pig's face, static",
  "From the first frame Tocino looks straight at the camera",
  "He slowly lowers his cracked sunglasses with one hoof and stares, amazed, at the camera",
  ("TOCINO","Oh my God… ¿Eso es un cámara?"),"PLAZA-ESQUINA-TOCINO.jpg"),
 ("G23",4,"27","ESQUINA",["DIZZY"],"Medium shot, static",
  "From the first frame Dizzy stands facing the camera",
  "He puffs out his chest, proud, and points to the camera on his cap",
  ("DIZZY","Mía, mi llave. Ahora soy vlogger."),"PLAZA-ESQUINA-TOCINO.jpg"),
 ("G24",10,"28 y 29","ESQUINA",["TOCINO"],"Close-up of the pig, the camera slowly pushes in",
  "From the first frame Tocino looks at the camera",
  "He gets an idea, his eyes go wide with excitement, and at the end he raises one hoof making the rock horns sign",
  ("TOCINO","Con ese cámara y ese café… si lo vendemos en El Hueco nos pagan el doble: pagamos la deuda de tu abuela y nos sobra pa' ser famosos, man. Let's rock, baby!"),"PLAZA-ESQUINA-TOCINO.jpg"),
 ("G25",4,"30","ESQUINA",["DIZZY"],"Close-up, static",
  "From the first frame Dizzy faces the camera",
  "He smiles slowly with mischief",("DIZZY","Usted es un genio, gringo hijueputa."),"PLAZA-ESQUINA-TOCINO.jpg"),
 ("G26",6,"31","AEREA-OLLA",[],"Aerial drone shot slowly descending into the ravine at night",
  "Aerial night view of the hidden neighborhood at the bottom of the ravine from the reference",
  "The drone sinks down toward the glowing barrels and the smoke",None,"AEREA-OLLA.jpg"),
("G26b",6,"31b","ESCALERAS",["DIZZY"],"Medium shot, static, at the top of the broken stairs",
  "From the first frame Dizzy stands at the top of the stairs facing the camera, the night market glowing far below behind him",
  "He looks back over his shoulder at the market below, then turns to the camera and talks nervously, pointing down with his thumb",
  ("DIZZY","Pilas, mis ratas: si el Tuerto me ve aquí, me pela."),"HUECO-ENTRADA.jpg"),
 ("G27",6,"32","ESCALERAS",["DIZZY","TOCINO","BARTOLO"],"Wide shot from the bottom of the stairs looking up, static",
  "From the first frame the three are at the top of the stairs: Dizzy in front, Tocino behind him, Bartolo with the sacks last",
  "They walk down the broken stairs toward the camera; Tocino looks around amazed",
  ("TOCINO","Oh my God, this is insane…"),"HUECO-ENTRADA.jpg"),
 ("G28",8,"33 y 35","OLLA",["GALLINAZO"],"Close-up of the vulture from a low angle, static",
  "From the first frame the big black vulture meat seller in a dirty apron blocks the way, holding a big wooden spoon",
  "He asks a question, waits three seconds staring, then says one word and steps aside",
  ("GALLINAZO","¿Contraseña? … Siga."),"HUECO-DENTRO.jpg"),
 ("G29",4,"34","OLLA",["DIZZY"],"Close-up, static",
  "From the first frame Dizzy faces the camera",
  "He answers instantly without thinking, totally calm",("DIZZY","Hijueputa."),"HUECO-DENTRO.jpg"),
 ("G30",8,"36","OLLA",["CUCA","VENDEDORES"],"Crane shot rising slowly over the market street",
  "From the first frame we see the market stalls, smoke and light bulbs from a low height",
  "The camera rises to reveal the whole market; in the middle Cuca climbs onto a wooden table and starts dancing like a diva",None,"HUECO-DENTRO.jpg"),
 ("G31",8,"37 y 42","OLLA",["CUCA","VENDEDORES"],"Wide shot, static, the camera far away",
  "From the first frame Cuca dances on top of a wooden table in the center; the vendors stand around it",
  "Cuca dances champeta like a diva and ends with a proud pose; the vendors clap to the rhythm",None,"HUECO-DENTRO.jpg"),
 ("G32",6,"38","CARNE",["GALLINAZO"],"Medium shot, static",
  "From the first frame the black vulture meat seller stands behind the counter",
  "He cuts sausages with a kitchen knife to a dance rhythm, bobbing his head",None,"HUECO-PUESTO-CARNE.jpg"),
 ("G33",6,"39","OLLA",["VENDEDORES"],"Medium shot of the toad, static",
  "From the first frame the fat green toad with gold chains and dark glasses sits next to a stall",
  "He lifts a small glass jar of glowing white magic dust and shakes it proudly to the rhythm",None,"HUECO-DENTRO.jpg"),
 ("G34",6,"40","OLLA",["VENDEDORES"],"Medium shot, static",
  "From the first frame the old brown rat with a hat sits next to a huge pile of colorful bottle caps",
  "He counts the caps, greedy; behind him the gray opossum walks past carrying a sack of old second-hand radios and shoes",None,"HUECO-DENTRO.jpg"),
 ("G35",8,"41","OLLA",["DIZZY","TOCINO","VENDEDORES"],"Wide shot, the camera moves slowly sideways between the stalls",
  "From the first frame the vendors dance between the stalls; Dizzy stands on the left watching",
  "Everybody dances; Tocino dances very badly in the middle, shaking his mohawk",None,"HUECO-DENTRO.jpg"),
 ("G36",8,"43 y 44","OLLA",["TOCINO"],"Close-up of the pig, static",
  "From the first frame Tocino stares to the right at someone off screen",
  "He slowly lowers his cracked sunglasses, raises his eyebrows and smirks",
  ("TOCINO","Uy, mami… muestra esa cuca."),"HUECO-DENTRO.jpg"),
 ("G37",4,"45","OLLA",["DIZZY","TOCINO","CUCA","VENDEDORES"],"Wide shot, static",
  "From the first frame everybody in the market stands still",
  "The whole market goes silent and slowly turns to stare at Tocino",None,"HUECO-DENTRO.jpg"),
 ("G38",4,"46","OLLA",["CUCA","TOCINO"],"Medium shot in profile: Cuca on the left, Tocino on the right",
  "From the first frame Cuca and Tocino face each other",
  "Cuca gives Tocino a fast, cartoonish comedy slap with three of her legs; his head bounces funnily",None,"HUECO-DENTRO.jpg"),
 ("G39",4,"47","OLLA",["TOCINO"],"Close-up, static",
  "From the first frame Tocino holds one hoof on his red cheek",
  "He rubs his cheek, confused and offended",("TOCINO","What the fuck, dude?"),"HUECO-DENTRO.jpg"),
 ("G40",4,"48","OLLA",["DIZZY"],"Close-up, static",
  "From the first frame Dizzy looks to the right, very angry",
  "He yells at someone off screen to the right",("DIZZY","¡Es mi prima, cochino gran hijueputa!"),"HUECO-DENTRO.jpg"),
 ("G41",6,"49","OLLA",["TOCINO"],"Close-up, static",
  "From the first frame Tocino faces the camera",
  "He opens his front hooves, totally confused",
  ("TOCINO","¿Qué? Es una cucaracha, ¿no? Cuca… cucaracha… I'm confused, dude."),"HUECO-DENTRO.jpg"),
 ("G42",6,"50","OLLA",["CUCA"],"Medium shot, static",
  "From the first frame Cuca stands with her arms crossed",
  "Still angry, she leans forward and lowers her voice like telling a secret",
  ("CUCA","Eche, primo, aquí no se puede vender nada sin pagarle al Tuerto."),"HUECO-DENTRO.jpg"),
 ("G43",4,"51","OLLA",["DIZZY"],"Close-up, static",
  "From the first frame Dizzy faces the camera",
  "He smiles nervously, sweating",("DIZZY","Todo bien, todo bien…"),"HUECO-DENTRO.jpg"),
 ("G44",4,"52","OLLA",["DIZZY"],"Medium shot, static",
  "From the first frame Dizzy stands in the center facing the camera, smiling",
  "The huge dark shadow of a cat with pointy ears slowly covers him from behind; his smile freezes",None,"HUECO-DENTRO.jpg"),
 ("G45",4,"53","OLLA",["DIZZY"],"Close-up very near the lens, static, his whole head, cap and camera inside the frame",
  "From the first frame Dizzy's scared face is very close to the lens",
  "His eyes go huge with fear and he whispers",("DIZZY","Uy, no… triple hijueputa."),"HUECO-DENTRO.jpg"),
]

def prompt(g):
    gid,d,tomas,lugar,cast,cam,primero,accion,habla,ref=g
    locks=[LOCK[c] for c in cast if c in LOCK]
    if "GALLINAZO" in cast: locks.append("the vulture is the black vulture meat seller from the reference")
    partes=[HEAD.format(d=d), LUZ[lugar]+".", cam+".", primero+".", accion+"."]
    if locks:
        t=". ".join(locks)+"."
        partes.append(t[0].upper()+t[1:])
    if habla:
        q,fr=habla
        partes.append(f'{QUIEN[q]} speaks {VOZ[q]}: "{suave(fr)}" {'Her' if q in ('GERTRUDIS','CUCA','LLORONA') else 'His'} mouth moves clearly in sync with every word. Only {QUIEN[q]} speaks; everybody else keeps their mouth closed.')
    else:
        partes.append("No one speaks; all mouths stay closed.")
    if cast:
        partes.append("Only these characters appear; no other animals.")
    partes.append(f"No humans or people anywhere, no subtitles or captions, no phone, no selfie stick, no bicycle, no music; only {SONIDO[lugar]}.")
    out=" ".join(partes)
    # sin nombres propios: Flow los escribe como texto (salió «DIZZY» en la cadena)
    trozos=out.split('"')
    for i in range(0,len(trozos),2):  # solo fuera de las comillas (los diálogos no se tocan)
        for a,b in [("the small Dizzy","the small rat"),("Dizzy's","the rat's"),("Dizzy","the rat"),("Doña Gertrudis","the hen"),("El Tuerto","the cat"),("Tocino","the pig"),("Bartolo","the mule"),("Cuca","the cockroach"),("La Llorona","the ghost woman")]:
            trozos[i]=trozos[i].replace(a,b)
    out='"'.join(trozos)
    import re
    out=re.sub(r'(^|[.!?] )(the|its)\b',lambda m:m.group(1)+m.group(2).capitalize(),out)
    return out

def refs(g):
    r=[REF[c] for c in g[4]]
    out=[]
    for x in r+[g[9]]:
        if x not in out: out.append(x)
    return out

CRED={4:7,6:10,8:12,10:15}
def main():
    lines=["# Capítulo 1 · parte 6: prompts de Flow · PARTE 1 del video (tomas 1 a 53)\n",
           "Google Flow, **Omni 1.1 Flash**, **vertical 9:16**. Cada generación da una o varias tomas del guion.",
           "Adjuntar en cada una las referencias que dice (personajes en `refs/extravio/personajes/`, lugares en `refs/extravio/lugares/`).\n"]
    tot=0
    for g in P1:
        tot+=CRED[g[1]]
        lines.append(f"\n## {g[0]} · {g[1]} s · tomas {g[2]}\n\n**Referencias:** {', '.join(refs(g))}\n\n```\n{prompt(g)}\n```\n")
    lines.insert(3,f"**{len(P1)} generaciones · ≈ {tot} créditos** (720p, x1, sin repeticiones).\n")
    open(os.path.join(AQUI,"CAP01-FLOW-P1.md"),"w").write("\n".join(lines))
    json.dump([{"id":g[0],"d":g[1],"tomas":g[2],"refs":refs(g),"p":prompt(g)} for g in P1],open(os.path.join(AQUI,"cap01_flow_p1.json"),"w"),ensure_ascii=False)
    print(len(P1),tot,max(len(prompt(g)) for g in P1))
if __name__=="__main__":
    main()
