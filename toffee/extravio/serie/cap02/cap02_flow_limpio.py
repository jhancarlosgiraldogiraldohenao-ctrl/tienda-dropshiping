# Plantilla LIMPIA (9-nov-2026): la prueba G comprobó que el prompt corto pasa donde el largo era bloqueado
# («intereses de proveedores de contenido de terceros»). Sin encabezado largo, sin «has this original design»,
# sin el bloque de prohibiciones, sin listas largas de extras. Solo: formato, estilo corto, lugar, cámara,
# personajes (descripción corta), acción, diálogo y sonido.
H="Horizontal 16:9, {d} seconds. Stylized 3D animation, cinematic night lighting, shallow depth of field. "
CALLE="A colorful colonial street in Mexico on the Night of the Dead, with paper flags, a path of orange marigold petals, candles and a big home altar, as in the reference photo. "
MERC="A Mexican night market on the Night of the Dead, with stalls of sugar skulls, clay pots and piñatas, orange and purple fabric roofs and glowing paper lanterns, as in the reference photo. "
ESC="A cozy hidden spot under a market stall, with a long colorful tablecloth hanging to the floor, a woven rug, a clay jug and warm lantern light through the cloth, as in the reference photo. "
RAT="a small gray rat with big tired red-rimmed eyes, a flat cap with a small action camera on top, a black hoodie, a gold chain with a bottle-cap pendant, white socks and black slides"
PIG="a skinny pink pig with a black mohawk, cracked sunglasses, a torn leather vest and an old electric guitar on his back, always on all four legs"
CAT="a tall elegant skeleton cat lady with a sugar-skull painted face, orange eyes, a huge black hat with marigolds and purple ribbons, a long purple and black lace dress, black lace gloves and a black folding fan"
AXO="a chubby pink axolotl with six fluffy pink gills, sleepy half-closed red eyes, a lazy smile, a small frayed straw sombrero, a long striped poncho and a crooked hand-rolled cigarette in the corner of his mouth with thin gray smoke"
FONDO_CALLE="Behind them, out of focus, small musicians play and neighbors walk by with flowers and candles; petals blow in the wind and candles flicker. "
FONDO_MERC="Behind, out of focus, animal vendors tend their stalls; lanterns sway and steam rises from pots. "
VOZ_PIG="in English with a loud, raspy male voice and a heavy American accent"
VOZ_RAT="in Colombian Spanish with a raspy, hoarse young male street voice"
VOZ_CAT="in Mexican Spanish with an elegant, theatrical, flirtatious female voice"
VOZ_AXO="in Mexican Spanish with a very slow, sleepy, raspy young male voice"
SON_CALLE="Ambient sound of distant trumpets and a festive crowd."
SON_MERC="Ambient sound of a busy market and distant trumpets."
SON_ESC="Muffled market sounds from outside."
T={
"T23":(8,["CATRINA","TOCINO","MX-CALLE-ALTAR","HABITANTES-MEXICO"],H.format(d=8)+CALLE+
 "Medium two-shot, static camera, both whole bodies in the frame. On the left stands "+CAT+". "+PIG[0].upper()+PIG[1:]+", walks in from the right and stops in front of her. He raises one eyebrow and smiles proudly at her, wiggling his mohawk, and says "+VOZ_PIG+': "Mamacita, I don\'t care you\'re all bones… I like \'em skinny." His mouth moves with the words. She keeps her mouth closed and fans herself, amused. '+FONDO_CALLE+SON_CALLE),
"T24":(4,["CATRINA","MX-CALLE-ALTAR","HABITANTES-MEXICO"],H.format(d=4)+CALLE+
 "Close-up, static camera: "+CAT+", on the right side of the frame, her whole head and hat in the frame, looking down to the left. She flutters her fan fast in front of her face, flattered and shocked, and says "+VOZ_CAT+': "¡Ay, qué marrano tan atrevido!" Her mouth moves with the words. '+FONDO_CALLE.replace("Behind them","Behind her")+SON_CALLE),
"T25":(6,["DIZZY","TOCINO","MX-CALLE-ALTAR-2","HABITANTES-MEXICO"],H.format(d=6)+CALLE+
 "Medium shot, static camera, both whole bodies in the frame, feet on the cobblestones. On the left stands "+RAT+"; on the right stands "+PIG+". The rat is much smaller, about half the pig's height. The rat grabs the pig by one ear, shouts "+VOZ_RAT+': "¡Corra, Gringo!" and both run out of the frame to the right. Only the rat speaks. '+FONDO_CALLE+SON_CALLE),
"T26":(6,["DIZZY","TOCINO","MX-MERCADO-CONTRA"],H.format(d=6)+MERC+
 "Low handheld camera moving fast backwards in front of them. "+RAT[0].upper()+RAT[1:]+" runs in front and "+PIG+" runs right behind him, down the market aisle toward the camera. They knock over a clay pot that rolls, and both look back over their shoulders, scared. "+FONDO_MERC+"No one speaks. "+SON_MERC),
"T27":(6,["CATRINA","MX-MERCADO"],H.format(d=6)+MERC+
 "Medium shot, the camera moves backwards in front of her: "+CAT+" walks fast and elegantly down the market aisle toward the camera, fanning herself, never running, and calls out sweetly "+VOZ_CAT+': "¡No corran, almitas!" Her mouth moves with the words. '+FONDO_MERC+SON_MERC),
"T28":(4,["DIZZY","TOCINO","MX-MERCADO-2"],H.format(d=4)+MERC+
 "Low shot at floor level, static camera. "+RAT[0].upper()+RAT[1:]+" and "+PIG+" run along the floor from the left toward a colorful tablecloth hanging to the floor on the right, dive under it and disappear; the cloth sways. No one speaks. "+SON_MERC),
"T29":(8,["CHUY","MX-MERCADO-ESCONDITE"],H.format(d=8)+ESC+
 "Medium shot from a low angle, static camera: "+AXO+", sitting very relaxed on the rug next to the clay jug, framed from the knees up on the right side of the frame. He slowly turns his head toward the camera and says "+VOZ_AXO+': "Qué onda, carnales… ¿también vienen huyendo de la flaca?" His mouth moves with the words; the cigarette stays in his mouth. Soft smoke drifts. '+SON_ESC),
"T30":(4,["DIZZY","MX-MERCADO-ESCONDITE"],H.format(d=4)+ESC+
 "Close-up, static camera: "+RAT+", lying on the rug on the left side of the frame, breathing hard, his whole head, cap and camera in the frame, both eyes looking the same way. He stares at someone to the right, confused, and whispers "+VOZ_RAT+': "¿Y usted quién es?" His mouth moves with the words. '+SON_ESC),
"T31":(8,["CHUY","MX-MERCADO-ESCONDITE"],H.format(d=8)+ESC+
 "Close-up with a slow push-in: "+AXO+", framed from the chest up on the right side of the frame. He answers very slowly with long lazy pauses "+VOZ_AXO+': "Chuy… el ajolote más tranquilo… de todo México." Then he coughs softly and giggles. His mouth moves with the words; the cigarette stays in his mouth. '+SON_ESC),
"T33":(4,["CATRINA","MX-MERCADO-ESCONDITE"],H.format(d=4)+
 "Seen from INSIDE a dark cozy hideout under a market stall: in front of the camera hangs a long colorful patterned tablecloth from top to bottom like a closed curtain, touching the floor; a woven rug and a clay jug on the floor, warm lantern glow. Static camera, close shot of the bottom edge of the cloth. From OUTSIDE, one single thin skeleton hand in a black lace glove slips in under the bottom edge of the cloth and slowly lifts the cloth upward; warm light from the market pours in through the gap. We only see that one gloved hand and part of the wrist; no arm from any other side, no face, no body, no other hands. No one speaks. Muffled market sounds from outside."),
"T34":(6,["DIZZY","TOCINO","CHUY","CATRINA","MX-MERCADO-ESCONDITE"],H.format(d=6)+ESC+
 "Medium-wide shot from inside the hideout, static camera, all four whole bodies in the frame. On the left, huddled together on the rug, frozen with fear: "+RAT+"; "+PIG+"; and "+AXO+". On the right, "+CAT+" lifts the edge of the tablecloth with one gloved hand, bends down to look in, smiles slowly and whispers "+VOZ_CAT+': "¡Los encontré!" Her mouth moves with the words; only she speaks. '+SON_ESC),
"T35":(4,["DIZZY","MX-MERCADO-ESCONDITE"],H.format(d=4)+ESC+
 "Extreme close-up, static camera: "+RAT+", lying under the table, his whole head in the frame, both eyes looking the same way, staring up toward the lifted tablecloth, frozen. His eyes go huge and he whispers to the camera "+VOZ_RAT+': "Ya estamos muertos… literal." His mouth moves with the words. '+SON_ESC),
}
if __name__=="__main__":
    for k,(d,f,p) in T.items(): print(k,d,len(p),f)
