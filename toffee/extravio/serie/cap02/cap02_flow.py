# -*- coding: utf-8 -*-
"""Capítulo 2 (México) · PARTE 1: guion y prompts de Google Flow, Omni 1.2 Flash, vertical 9:16, x1.
python3 toffee/extravio/serie/cap02/cap02_flow.py -> CAP02-FLOW-P1.md y web/cap02-flow-p1.html (con las fotos)
Reglas: memoria/ (PROMPTS-FLOW, ERRORES, MODO-PELICULA). 10 cuentas x 16 s (48 créditos) = 160 s.
"""
import os, re, html, shutil
from PIL import Image
AQUI=os.path.dirname(os.path.abspath(__file__))
RAIZ=os.path.abspath(os.path.join(AQUI,'..','..','..'))
PERS=os.path.join(RAIZ,'refs','extravio','personajes'); LUG=os.path.join(RAIZ,'refs','extravio','lugares')

HEAD=("Vertical 9:16, {d} seconds. High-quality 3D animated movie style, exactly the same look as the character reference images, "
      "cinematic lighting, normal lens (no fisheye, no vignette, no dark corners). One continuous shot with no cuts, full vertical frame from edge to edge, no black bars.")
LOCK={
 "DIZZY":"The rat looks exactly like the reference image: gray rat with big tired red-rimmed eyes, flat cap with a small action camera on top, plain gold chain with a plain bottle-cap pendant (no letters), and he is ALWAYS wearing his black hoodie (never bare-chested, the hoodie covers his body and arms), white socks with black slides",
 "TOCINO":"The pig looks exactly like the reference image: skinny dirty pink pig that ALWAYS stands and walks on all four legs like a real pig (never upright on two legs), only four legs and no arms or hands, black mohawk, cracked sunglasses, torn leather vest and his old scratched electric guitar hanging on his back (he never holds it)",
 "CATRINA":"The skeleton cat lady looks exactly like the reference image: tall elegant lady cat made of ivory-white bones, face painted like a colorful sugar skull, glowing orange eyes, huge black hat with orange marigolds and purple ribbons, long purple and black lace dress, marigold necklace, black lace gloves, a black folding fan in one hand, thin bone tail; she is funny and charming, never scary",
 "CHUY":"The axolotl looks exactly like the reference image: chubby pink axolotl with six fluffy pink gills, sleepy half-closed red eyes, lazy smile, small frayed straw sombrero, a long faded striped poncho that covers his body down to his knees, a crooked hand-rolled cigarette in the corner of his mouth with a thin line of soft gray smoke",
}
NOM={"DIZZY":"the rat","TOCINO":"the pig","CATRINA":"the skeleton cat lady","CHUY":"the axolotl"}
REFP={"DIZZY":"DIZZY-FRENTE.jpg","TOCINO":"TOCINO-FRENTE.jpg","CATRINA":"CATRINA-FRENTE.jpg","CHUY":"CHUY-FRENTE.jpg"}
VOZ={"DIZZY":"in Colombian Spanish with a raspy, hoarse, rough young male street voice",
     "TOCINO":"in English with a loud, raspy male voice and a very heavy American accent",
     "CATRINA":"in Mexican Spanish with an elegant, theatrical, seductive female voice like an old telenovela star",
     "CHUY":"in Mexican Spanish with a very slow, sleepy, raspy young male voice, lazy and relaxed"}
ELLA={"CATRINA"}
LUZ={
 "ZARZO-NOCHE":"Inside the wooden farmhouse attic from the reference at midnight, dark blue moonlight through the small round window, a warm candle glow",
 "PUEBLO-CALLE":"On the empty cobblestone street of a small Colombian colonial village from the reference at midnight, colorful closed doors, one warm street lamp, a starry night sky with exactly one moon or no moon (never two moons)",
 "CALLEJON":"In the narrow dark alley with old brick walls, peeling plaster, tangled electric cables and black trash bags from the reference, at midnight, bright magical green light glowing up from the round sewer cover",
 "TUNEL":"Inside the deep round brick sewer shaft from the reference that turns into a swirling spiral of glowing green light with golden sparkles",
 "MX-ALCANTARILLA":"On the colonial street in Mexico on the Night of the Dead from the reference, the round iron sewer cover in the cobblestones bursting with magical green light and mist, marigold petals, candles and an altar",
 "MX-ALTAR":"In front of the lowest step of the Day of the Dead home altar from the reference at night: big painted sugar skulls, sweet breads, lit candles, empty wooden picture frames (no photos, no faces) and a soft pile of orange marigold petals",
 "MX-CALLE":"On the colonial street in Mexico on the Night of the Dead from the reference: painted houses, strings of colorful cut paper flags moving in the breeze, a path of orange marigold petals, candles and a big home altar",
 "MX-MERCADO":"In the Mexican night market on the Day of the Dead from the reference: stalls with sugar skulls, clay pots and piñatas, orange and purple fabric roofs, glowing paper lanterns swaying",
 "MX-ESCONDITE":"In the cozy hidden corner under a market stall from the reference: a long colorful tablecloth hanging to the floor, a woven rug, a clay jug, wooden crates, warm lantern light and a soft haze of smoke",
}
FONDO={
 "ZARZO-NOCHE":"The candle flame flickers softly and dust floats in the moonlight",
 "PUEBLO-CALLE":"The street lamp glows and a few moths fly around it",
 "CALLEJON":"Thin green mist rises from the sewer cover and drifts along the wet ground; a loose cable sways slightly",
 "TUNEL":"Green sparkles swirl around and water drops fall",
 "MX-ALCANTARILLA":"Candle flames flicker and marigold petals blow in the air",
 "MX-ALTAR":"The candle flames flicker and a few petals float in the warm air",
 "MX-CALLE":"Far in the background, out of focus, a few small chihuahua mariachi musicians in black charro suits walk by; the paper flags flutter and the candles flicker",
 "MX-MERCADO":"Far in the background, out of focus, an old turtle vendor and a green parrot vendor tend their stalls; the lanterns sway and steam rises from a pot",
 "MX-ESCONDITE":"The smoke drifts slowly and the lantern light shifts through the tablecloth",
}
SONIDO={"ZARZO-NOCHE":"crickets at night and creaking wood","PUEBLO-CALLE":"crickets and a dog barking very far away",
 "CALLEJON":"dripping water and a deep magical hum","TUNEL":"a rushing wind and a deep magical hum",
 "MX-ALCANTARILLA":"a magical whoosh and distant mariachi music","MX-ALTAR":"soft wind and distant mariachi music",
 "MX-CALLE":"distant mariachi trumpets and small fireworks very far away","MX-MERCADO":"pots clinking and distant mariachi music",
 "MX-ESCONDITE":"muffled market sounds from outside"}
REFL={}  # lugar -> foto por defecto (cada toma dice la suya)
SUAVE=[("hijueputa","hijuepucha"),("Damn","Dang")]

# (id, seg, lugar, foto de lugar, [personajes], cámara, primer cuadro, acción, (quien, frase) o None, nota en español, voz real si cambia)
P1=[
 # --- ESCENA 1 · el zarzo a medianoche (sigue al «¿Me meto por esa alcantarilla?» del cap. 1)
 ("T01",8,"ZARZO-NOCHE","ZARZO-NOCHE.jpg",["DIZZY"],"Close-up very near the lens, the camera slowly pushes in, his whole head, cap and camera inside the frame",
  "From the first frame the rat sits on his small mattress wearing his cap, his face very close to the lens, whispering",
  "He whispers to the lens like a vlogger, excited and nervous, then grins",
  ("DIZZY","¿Quiubo, mis ratas? Son las doce. Ustedes votaron que sí… entonces nos metemos."),"Dizzy en el zarzo, en susurro: arranca la aventura."),
 ("T02",5,"ZARZO-NOCHE","ZARZO-NOCHE.jpg",["DIZZY"],"Wide shot from inside the attic, static, the round window in the center",
  "From the first frame the rat stands on the wooden floor below the small round window",
  "He climbs up and squeezes out through the small round window into the night, his tail disappearing last",None,"Sale por la ventanita redonda (puente)."),
 # --- ESCENA 2 · la calle del pueblo: Tocino lo espera
 ("T03",6,"PUEBLO-CALLE","PUEBLO-CALLE-NOCHE.jpg",["DIZZY","TOCINO"],"Wide shot, static, both whole bodies inside the frame",
  "From the first frame the pig stands under the street lamp on the right; the rat walks in from the left side of the frame along the stone pavement",
  "The rat walks from left to right and stops next to the pig; the pig looks at him and complains, nervous",
  ("TOCINO","Bro, it's midnight. This is a terrible idea."),"Tocino lo espera bajo el farol."),
 ("T04",6,"PUEBLO-CALLE","PUEBLO-CALLE-NOCHE.jpg",["DIZZY"],"Medium close-up of the rat from a low angle, static, his whole head, cap and camera inside the frame",
  "From the first frame the rat stands on the stone pavement looking to his right, toward the pig",
  "He answers with a cocky smile and points with his thumb toward the dark alley entrance behind him",
  ("DIZZY","Por eso lo traje, Pinche Gringo… pa' que se caiga usted primero."),"Plano y contraplano: Dizzy a la izquierda mira a la derecha."),
 # --- ESCENA 3 · el callejón de la visión
 ("T06",5,"CALLEJON","CALLEJON-ALCANTARILLA-CONTRA.jpg",["DIZZY","TOCINO"],"Medium-wide shot from deep inside the alley, the camera slowly moves backward as they walk in",
  "From the first frame the rat on the left and the pig on the right walk into the alley toward the camera, the warm street visible behind them",
  "They walk slowly toward the camera, the green light from the ground lights their faces; the pig stares at the light, amazed",
  ("TOCINO","Dude… it's glowing."),"Entran al callejón (contraplano desde adentro)."),
 ("T07",5,"CALLEJON","CALLEJON-ALCANTARILLA.jpg",["DIZZY"],"Close-up of the rat, static, his whole head, cap and camera inside the frame, green light on his face from below",
  "From the first frame the rat looks down at the glowing sewer cover in front of him",
  "He looks at the lens with wide eyes and a nervous smile",
  ("DIZZY","Igualito a la visión, mis ratas."),"Lo que se anunció se cumple. Va seguido de 2 s de la visión del cap. 1 (G99, gratis)."),
 ("T08",4,"CALLEJON","CALLEJON-ALCANTARILLA-PISO.jpg",[],"Extreme close-up insert at ground level next to the glowing sewer cover, shallow depth of field",
  "From the first frame we only see one small gray rat foot in a white sock and a black slide, exactly like the reference image, stepping toward the glowing cover",
  "The black slide catches on the raised edge of the sewer cover and the foot trips forward",None,"Inserto: la chancla se engancha (sin personaje completo).",None),
 ("T09",5,"CALLEJON","CALLEJON-ALCANTARILLA.jpg",["DIZZY","TOCINO"],"Medium-wide shot, static, both whole bodies inside the frame, the glowing sewer hole in the center",
  "From the first frame the rat stands at the edge of the glowing sewer hole in the center and the pig stands behind him on the right",
  "The rat trips and falls head first into the glowing green hole, screaming; the pig's mouth stays closed in shock",
  ("DIZZY","¡Aaaaah!"),"La caída, igual que la visión."),
 ("T10",5,"CALLEJON","CALLEJON-ALCANTARILLA.jpg",["TOCINO"],"Medium shot of the pig from the side, static, his whole body inside the frame",
  "From the first frame the pig stands alone at the edge of the glowing green sewer hole, looking down",
  "He looks down, shrugs his shoulders and jumps into the hole head first, yelling",
  ("TOCINO","Wait for meee!"),"Tocino se tira detrás."),
 # --- ESCENA 4 · la caída por el túnel verde
 ("T11",5,"TUNEL","TUNEL-VERDE.jpg",["DIZZY","TOCINO"],"Shot from below looking up, the camera spins slowly with them",
  "From the first frame the rat falls down the glowing green tunnel toward the camera, with the pig falling right behind him above",
  "Both fall and spin through the swirling green light; the rat screams with his arms open while the pig keeps his mouth closed and his eyes wide",
  ("DIZZY","¡Ayyyy, mamá!"),"La caída por el túnel. Después va el mapa animado con la raya verde (gratis)."),
 # --- ESCENA 5 · México: salen disparados
 ("T13",5,"MX-ALCANTARILLA","MX-ALCANTARILLA-NOCHE.jpg",["DIZZY"],"Wide shot from the ground, static, the sewer cover in the lower center",
  "From the first frame the iron cover lies on the street with green light bursting from under it",
  "The cover pops up and the rat shoots out of the hole with a burst of green light, flying up and out of the top of the frame, screaming",
  ("DIZZY","¡Aaaah!"),"Sale disparado (también va en el GANCHO)."),
 ("T14",5,"MX-ALTAR","MX-ALTAR-CERCA.jpg",["DIZZY"],"Close shot from very low, static, the pile of marigold petals in the center",
  "From the first frame the pile of orange marigold petals lies still in front of the altar",
  "The rat falls from above into the pile of petals with a soft puff, petals fly everywhere and slowly rain down; only his cap and the tip of his tail stick out",None,"Cae en las flores (GANCHO)."),
 ("T16",6,"MX-CALLE","MX-CALLE-ALTAR.jpg",["DIZZY","TOCINO"],"Medium shot, the camera slowly pulls back to reveal the street",
  "From the first frame the rat sits in the pile of marigold petals next to the altar on the left and the pig lies on his back beside him on the right with his sunglasses crooked",
  "The rat looks around the colorful street, amazed and confused",
  ("DIZZY","¿Y esto qué es? ¿Me morí o qué?"),"Dónde estamos: la calle del altar."),
 ("T17",4,"MX-CALLE","MX-CALLE-ALTAR-2.jpg",["TOCINO"],"Close-up of the pig framed from the chest up, static",
  "From the first frame the pig stands on the cobblestones, his sunglasses crooked",
  "He fixes his sunglasses with a shake of his head and smiles widely",
  ("TOCINO","Bro… we're in Mexico. Tacos!"),"Tocino feliz."),
 # --- ESCENA 6 · la Catrina
 ("T18",6,"MX-CALLE","MX-CALLE-ALTAR-CONTRA.jpg",["CATRINA"],"Wide shot, static, then a slow push-in",
  "From the first frame the skeleton cat lady is far away at the end of the marigold petal path",
  "She walks elegantly along the petal path toward the camera, swaying her hips and fanning herself with the black lace fan",None,"Entra la Catrina (suena M16 y los huesitos E29)."),
 ("T19",5,"MX-CALLE","MX-CALLE-ALTAR.jpg",["CATRINA"],"Close-up of her face, static, her whole head and hat inside the frame",
  "From the first frame the skeleton cat lady looks down at someone small in front of her",
  "She gasps, delighted, and opens her fan",
  ("CATRINA","¡Un alma perdida! Pobrecito… ¡tan feíto!"),"(También va en el GANCHO.)"),
 ("T20",5,"MX-CALLE","MX-CALLE-ALTAR.jpg",["DIZZY"],"Close-up of the rat from a high angle, as if seen by someone tall standing in front of him, static, his whole head, cap and camera inside the frame",
  "From the first frame the rat sits in the marigold petals looking up",
  "He looks up, offended, then unsure",
  ("DIZZY","¿Alma perdida? Yo estoy vivo, señora… creo."),"Contraplano desde arriba."),
 ("T21",6,"MX-CALLE","MX-CALLE-ALTAR-CONTRA.jpg",["CATRINA"],"Medium shot from a low angle, static, her whole body inside the frame",
  "From the first frame the skeleton cat lady stands tall on the petal path, the altar on the left",
  "She points her closed fan toward the end of the street, theatrical",
  ("CATRINA","Todas las almas perdidas se vienen conmigo… ¡al panteón!"),"La amenaza."),
 ("T22",4,"MX-CALLE","MX-CALLE-ALTAR-2.jpg",["TOCINO"],"Close-up of the pig framed from the chest up, slow push-in",
  "From the first frame the pig stares straight ahead, his mouth open",
  "He slowly lowers his head so his sunglasses slide down his snout, staring with love; his ears stand up",
  ("TOCINO","Dang… she's hot."),"Tocino se enamora (suena M6, el saxofón)."),
 ("T23",7,"MX-CALLE","MX-CALLE-ALTAR.jpg",["CATRINA","TOCINO"],"Medium two-shot, static, both whole bodies inside the frame",
  "From the first frame the skeleton cat lady stands on the left and the pig walks in on four legs from the right",
  "The pig stops in front of her, raises one eyebrow and flirts, wiggling his mohawk",
  ("TOCINO","Mamacita, I don't care you're all bones… I like 'em skinny."),"El coqueteo (subtítulo traducido)."),
 ("T24",4,"MX-CALLE","MX-CALLE-ALTAR.jpg",["CATRINA"],"Close-up of her face, static",
  "From the first frame the skeleton cat lady looks down to her right, toward the pig",
  "She flutters her fan fast in front of her face, flattered and shocked",
  ("CATRINA","¡Ay, qué marrano tan atrevido!"),"Reacción."),
 ("T25",4,"MX-CALLE","MX-CALLE-ALTAR-2.jpg",["DIZZY","TOCINO"],"Medium shot, static, both whole bodies inside the frame",
  "From the first frame the rat stands on the left and the pig on the right, both on the cobblestones",
  "The rat grabs the pig by one ear and both run out of the frame to the right",
  ("DIZZY","¡Corra, Gringo!"),"Huyen hacia la derecha (dirección de toda la persecución). Después va la aérea del barrio (gratis)."),
 # --- ESCENA 7 · la persecución en el mercado
 ("T26",5,"MX-MERCADO","MX-MERCADO-CONTRA.jpg",["DIZZY","TOCINO"],"Low shot, handheld camera moving backward fast in front of them",
  "From the first frame the rat and the pig run down the market aisle toward the camera, the rat in front",
  "They run fast between the stalls, knocking a clay pot that rolls; both look back over their shoulders",None,"Corren por el mercado (suena M13)."),
 ("T27",5,"MX-MERCADO","MX-MERCADO.jpg",["CATRINA"],"Medium shot, the camera moves backward in front of her",
  "From the first frame the skeleton cat lady walks fast and elegantly down the market aisle toward the camera",
  "She calls out sweetly while fanning herself, never running",
  ("CATRINA","¡No corran, almitas!"),"La Catrina detrás."),
 ("T28",4,"MX-MERCADO","MX-MERCADO-2.jpg",["DIZZY","TOCINO"],"Low shot at floor level, static",
  "From the first frame the rat and the pig run along the floor from the left toward a colorful tablecloth hanging to the floor on the right",
  "Both dive under the tablecloth and disappear; the cloth sways",None,"Se esconden debajo del puesto."),
 # --- ESCENA 8 · el escondite de Chuy
 ("T29",7,"MX-ESCONDITE","MX-MERCADO-ESCONDITE.jpg",["CHUY"],"Medium shot from a low angle, static, the axolotl framed from the knees up",
  "From the first frame the axolotl sits on the woven rug next to the clay jug, very relaxed",
  "He slowly turns his head toward the camera with sleepy eyes and a lazy smile",
  ("CHUY","Qué onda, carnales… ¿también vienen huyendo de la flaca?"),"Aparece Chuy (suena M15)."),
 ("T30",4,"MX-ESCONDITE","MX-MERCADO-ESCONDITE.jpg",["DIZZY"],"Close-up of the rat, static, his whole head, cap and camera inside the frame",
  "From the first frame the rat lies on the floor under the table, breathing hard",
  "He stares at someone in front of him, confused, and whispers",
  ("DIZZY","¿Y usted quién es?"),"Contraplano."),
 ("T31",8,"MX-ESCONDITE","MX-MERCADO-ESCONDITE.jpg",["CHUY"],"Close-up of the axolotl framed from the chest up, slow push-in",
  "From the first frame the axolotl looks at the camera with half-closed red eyes",
  "He answers very slowly with long lazy pauses, then coughs softly and giggles",
  ("CHUY","Chuy… el ajolote más tranquilo… de todo México."),"Chuy se presenta (la calada y la tos E28)."),
 # --- ESCENA 9 · el suspenso
 ("T33",4,"MX-ESCONDITE","MX-MERCADO-ESCONDITE.jpg",["CATRINA"],"Extreme close-up insert on the edge of the tablecloth, static",
  "From the first frame the long colorful tablecloth hangs still",
  "A thin elegant skeleton hand in a black lace glove slowly lifts the edge of the tablecloth and warm light pours in",None,"La mano de hueso levanta el mantel (suena E17)."),
 ("T34",4,"MX-ESCONDITE","MX-MERCADO-ESCONDITE.jpg",["CATRINA"],"Close-up from inside the hideout, static",
  "From the first frame her painted face peeks in through the gap under the lifted tablecloth, very close to the camera",
  "She smiles slowly and whispers",
  ("CATRINA","Los encontré…"),"Ella los encuentra."),
 ("T35",4,"MX-ESCONDITE","MX-MERCADO-ESCONDITE.jpg",["DIZZY"],"Extreme close-up of the rat's face, static, his whole head inside the frame",
  "From the first frame the rat lies under the table and stares up toward the lifted tablecloth, frozen",
  "His eyes go huge and he whispers to the lens",
  ("DIZZY","Ya estamos muertos… literal."),"Cierre en suspenso de la parte 1."),
]
CUENTAS=[["T01","T08","T17"],["T31","T22","T24"],["T23","T02","T25"],["T29","T06","T28"],["T03","T07","T09"],
         ["T04","T10","T11"],["T16","T13","T14"],["T18","T19","T20"],["T21","T26","T27"],["T30","T33","T34","T35"]]

def suave(t):
    for a,b in SUAVE: t=t.replace(a,b)
    return t
def prompt(g):
    gid,d,lug,foto,cast,cam,prim,acc,habla,nota=g[:10]
    p=[HEAD.format(d=d), LUZ[lug]+".", cam+".", prim+".", acc+".", FONDO[lug]+"."]
    if cast: p.append(" ".join(LOCK[c]+"." for c in cast))
    if len(cast)==2: p.append(f"{NOM[cast[0]].capitalize()} and {NOM[cast[1]]} keep the same sides of the frame for the whole shot.")
    if habla:
        q,fr=habla; s="Her" if q in ELLA else "His"
        p.append(f'{NOM[q].capitalize()} speaks {VOZ[q]}: "{suave(fr)}" {s} mouth moves clearly in sync with every word. Only {NOM[q]} speaks; everybody else keeps their mouth closed.')
    else: p.append("No one speaks; all mouths stay closed.")
    extra=" and the small blurred background extras" if lug in ("MX-CALLE","MX-MERCADO") else ""
    uno=", only one rat" if "DIZZY" in cast else ""
    p.append(("Only these characters appear"+extra+"; no other animals"+uno+". " if cast else "No characters appear except the foot described; no other animals. ")+
             f"No humans or people anywhere, no subtitles or captions, no text, no phone, no selfie stick, no vehicle, no music; only {SONIDO[lug]}.")
    return " ".join(p)
def fotos(g):
    c=g[4] or (["DIZZY"] if g[0]=="T08" else [])
    return [("personajes",REFP[x]) for x in c]+[("lugares",g[3])]

def main():
    T={g[0]:g for g in P1}
    assert sorted(sum(CUENTAS,[]))==sorted(T), "toma sin cuenta"
    for c in CUENTAS: assert sum(T[t][1] for t in c)==16, c
    # fotos livianas para la página
    W=os.path.join(AQUI,'web','fotos'); os.makedirs(W,exist_ok=True)
    usadas=sorted({f for g in P1 for f in fotos(g)})
    for carp,n in usadas:
        im=Image.open(os.path.join(RAIZ,'refs','extravio',carp,n)).convert('RGB'); im.thumbnail((1080,1920))
        im.save(os.path.join(W,n),quality=88)
    md=["# Capítulo 2 · PARTE 1 · prompts de Flow (Omni 1.2 Flash, 9:16, 720p, x1)\n",
        "10 cuentas × 16 s = 160 s (48 créditos por cuenta; sobran 2). Las aéreas, el mapa y la visión del cap. 1 van animados en la edición (gratis).\n"]
    cards=[]
    for i,c in enumerate(CUENTAS,1):
        md.append(f"\n## Cuenta {i} · {' + '.join(str(T[t][1])+' s' for t in c)} = 16 s (48 créditos)\n")
        cards.append(f"<h2>Cuenta {i} <small>{' + '.join(str(T[t][1])+' s' for t in c)} = 16 s · 48 créditos</small></h2>")
        for t in c:
            g=T[t]; pr=prompt(g)
            md.append(f"\n### {t} · {g[1]} s · {g[9]}\n```\n{pr}\n```\nFotos: "+", ".join(n for _,n in fotos(g))+"\n")
            imgs="".join(f'<figure><img src="fotos/{n}" alt="{n}"><figcaption>{n[:-4]}</figcaption></figure>' for _,n in fotos(g))
            cards.append(f'<div class=card><div class=hd><b>{t} · {g[1]} s</b><button onclick="cp(this)">Copiar prompt</button></div>'
                         f'<p>{html.escape(g[9])}</p><pre>{html.escape(pr)}</pre><div class=fot>{imgs}</div></div>')
    open(os.path.join(AQUI,'CAP02-FLOW-P1.md'),'w').write("".join(md))
    css=(":root{--bg:#fbf6ef;--fg:#2a2118;--card:#fff;--ac:#e8590c;--mut:#6b5d50;--bd:#eadfce}"
     "@media (prefers-color-scheme:dark){:root:not([data-theme=light]){--bg:#17120d;--fg:#f3ebe1;--card:#221a13;--ac:#ff8a3d;--mut:#b6a796;--bd:#3a2e22}}"
     ":root[data-theme=dark]{--bg:#17120d;--fg:#f3ebe1;--card:#221a13;--ac:#ff8a3d;--mut:#b6a796;--bd:#3a2e22}"
     "body{background:var(--bg);color:var(--fg);font:16px/1.5 system-ui,sans-serif;margin:0 auto;padding:16px;max-width:860px}"
     "h1{font-size:1.45rem}h2{color:var(--ac);font-size:1.15rem;margin-top:1.8em}h2 small{color:var(--mut);font-weight:400;font-size:.8em}"
     ".card{background:var(--card);border:1px solid var(--bd);border-radius:12px;padding:12px;margin:10px 0}"
     ".hd{display:flex;justify-content:space-between;align-items:center;gap:8px}.card p{margin:.3em 0;color:var(--mut)}"
     "pre{white-space:pre-wrap;word-break:break-word;font-size:.82rem;background:var(--bg);padding:10px;border-radius:8px}"
     ".fot{display:flex;gap:8px;flex-wrap:wrap}figure{margin:0;width:120px;text-align:center}figure img{width:120px;border-radius:8px;display:block}"
     "figcaption{font-size:.7rem;color:var(--mut);word-break:break-all}button{background:var(--ac);color:#fff;border:0;border-radius:8px;padding:6px 12px;font-weight:600;cursor:pointer}")
    page=(f"<!doctype html><html lang=es><head><meta charset=utf-8><meta name=viewport content='width=device-width,initial-scale=1'><title>Capítulo 2 Flow</title><style>{css}</style></head><body>"
      "<h1>Extravío · Capítulo 2 · Parte 1 · Flow</h1><p>Omni 1.2 Flash · vertical 9:16 · 720p · <b>x1</b>. Cada cuenta suma 16 s (48 créditos). "
      "Debajo de cada prompt están las fotos que hay que subir: en el computador arrástrala a Flow o clic derecho → «Copiar imagen»; en el celular mantenla presionada → «Copiar» o «Guardar».</p>"
      +"".join(cards)+
      "<script>function cp(x){navigator.clipboard.writeText(x.closest('.card').querySelector('pre').innerText).then(()=>{x.textContent='¡Copiado!';setTimeout(()=>x.textContent='Copiar prompt',1500)})}</script></body></html>")
    open(os.path.join(AQUI,'web','cap02-flow-p1.html'),'w').write(page)
    print("ok", len(P1), "tomas", sum(g[1] for g in P1), "s", len(usadas), "fotos")
if __name__=="__main__": main()
