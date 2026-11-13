# Capítulo 2 · PARTE 2 · prompts de Flow con la PLANTILLA LIMPIA (11-nov-2026). Ver memoria/REGLAS-DE-ORO.md.
from cap02_flow_limpio import H, RAT, PIG, CAT, AXO, VOZ_RAT, VOZ_CAT, VOZ_AXO
P = lambda s: s[0].upper() + s[1:]
LUPE = "a small tan female chihuahua with huge pointed ears, big shiny dark eyes with long eyelashes, a pink bow on one ear, a fitted black mariachi suit with silver buttons, a red bow tie and a giant black and silver sombrero, holding a small violin and its bow"
GER = "an old brown speckled hen with a flowered headscarf and a rosary, with real wings, holding one rubber slipper in her wing"
VOZ_PIG = "in Spanish with a heavy American accent and a loud, raspy male voice"  # sin «mixing English»: falló el audio en U09
VOZ_LUPE = "in Mexican Spanish with a high-pitched, fast, sassy and bossy female voice"
VOZ_GER = "in Colombian Spanish with a soft, shaky, sweet old grandmother voice"
ESC = "A cozy hidden spot under a market stall at night, with a long colorful tablecloth, a woven rug, a clay jug and warm lantern light, as in the reference photo. "
MUE = "The back of the market stall at night, opening onto a small wooden dock on a calm canal, with a colorful flower-covered boat tied to it, lanterns and string lights, as in the reference photo. "
TRA = "On board a small colorful wooden canal boat at night, with a hammock, a small table and a painted arch covered only with flowers, gliding on a dark canal with floating marigolds and lit boats behind, as in the reference photo. "
MAR = "A colorful wooden canal boat at night with a small wooden stage, string lights and an arch covered only with flowers and painted swirls, floating on a calm canal with marigolds, as in the reference photo. "
PUE = "A wooden arched bridge over a calm canal at the blue hour just before sunrise, pink and orange sky, soft mist on the water, flower-covered boats, as in the reference photo. "
CAL = "A colorful colonial street in Mexico at the blue hour just before sunrise, pink sky, paper flags, a marigold petal path, burnt-out candles with thin smoke, soft mist, as in the reference photo. "
ALC = "A narrow Mexican colonial alley at blue dawn, a round iron manhole cover glowing faint magical green, marigold petals and burnt-out candles on the cobblestones, pink sky, as in the reference photo. "
ZAR = "Inside a wooden farmhouse attic at sunrise, warm golden light through a round window, a small mattress on the floor, a wooden door on one side, as in the reference photo. "
SON_ESC = "Muffled market sounds from outside."
SON_CAN = "Soft water lapping, wooden boat creaks, frogs and distant trumpets."
SON_AMA = "Church bells far away, birds waking up and soft wind."
SON_ZAR = "Roosters far away and soft morning birds."
U = {}
def t(i, d, fotos, res, txt): U[i] = (d, fotos, res, txt if txt.startswith("Horizontal 16:9") else H.format(d=d) + txt)
t("U02", 6, ["CATRINA", "MX-MERCADO-ESCONDITE"], "720p", ESC +
  "Medium shot, static camera: " + CAT + ", on the right side of the frame, bends down toward someone small on the left, her whole body in the frame, smiling slowly and charmingly. She says " + VOZ_CAT + ': "Vamos, almitas… el panteón los espera." Her mouth moves with the words; only she speaks. ' + SON_ESC)
t("U03", 6, ["CHUY", "MX-MERCADO-ESCONDITE"], "720p", ESC +
  "Medium close-up, static camera: " + AXO + ", standing on the left side of the frame, a thick rope hanging from the roof next to him. Very slowly and calmly he grabs the rope with one hand and says " + VOZ_AXO + ': "Tranquila, flaca…" His mouth moves with the words; the cigarette stays in his mouth. Soft smoke drifts. ' + SON_ESC)
t("U04", 4, ["CATRINA", "MX-MERCADO-ESCONDITE"], "360p", ESC +
  "Medium shot, static camera. " + P(CAT) + " stands on the right. A huge heavy colorful fabric awning falls from the roof and lands on top of her, burying her completely from head to toe so that her face and body are hidden; she turns into a big wiggling lump of cloth that spins around blindly and bumps into a crate. No one speaks. " + SON_ESC)
t("U05", 6, ["DIZZY", "TOCINO", "CHUY", "MX-MERCADO-MUELLE"], "720p", MUE +
  "Low wide shot, static camera, all three whole bodies in the frame, running from the left toward the boat on the right: " + RAT + " in front, " + PIG + " behind him, and " + AXO + " walking slowly last. The rat is much smaller than the pig. The rat shouts " + VOZ_RAT + ': "¡Patitas pa\' qué las quiero!" Only the rat speaks. Lanterns sway and petals float on the water. ' + SON_CAN)
t("A-CANALES", 6, ["AEREA-XOCHIMILCO-NOCHE"], "360p",
  "Cinematic aerial drone shot at night over long calm canals with floating gardens and many colorful flower-covered boats lit by paper lanterns, marigolds floating on the dark water, one full moon, as in the reference photo. The drone glides slowly forward. Lanterns flicker and reflections shimmer. No characters, no text. " + SON_CAN)
t("U06", 6, ["DIZZY", "TOCINO", "CHUY", "MX-TRAJINERA-CHUY"], "720p", TRA +
  "Medium-wide shot, slow side tracking camera, all three whole bodies in the frame. " + P(AXO) + " stands at the back on the right and slowly pushes the boat with a long wooden pole; " + RAT + " and " + PIG + " sit on the bench on the left. The pig looks around and says " + VOZ_PIG + ': "Bro… ¿esto es un taxi de agua?" Only the pig speaks. ' + SON_CAN)
t("U07", 6, ["DIZZY", "MX-TRAJINERA-CHUY-CONTRA"], "720p", TRA +
  "Medium close-up, static camera: " + RAT + ", sitting on the boat bench on the left side of the frame, his whole head, cap and camera in the frame, both eyes looking the same way. He turns to someone on the right and asks " + VOZ_RAT + ': "Chuy, ¿y cómo volvemos a Colombia?" His mouth moves with the words. ' + SON_CAN)
t("U08", 8, ["CHUY", "MX-TRAJINERA-CHUY"], "720p", TRA +
  "Close-up with a slow push-in: " + AXO + ", standing at the back of the boat on the right side of the frame, holding the long pole. He answers very slowly with lazy pauses " + VOZ_AXO + ': "Por donde llegaron, carnal… antes de que salga el sol… si no, se quedan aquí pa\' siempre." His mouth moves with the words; the cigarette stays in his mouth. ' + SON_CAN)
t("U09", 6, ["TOCINO", "MX-TRAJINERA-CHUY-CONTRA"], "720p", TRA +
  "Medium close-up, static camera: " + PIG + ", sitting on the boat bench on the left side of the frame, his ears flat and his eyes wide, scared; his four hooves stay down. He says " + VOZ_PIG + ': "¿Pa\' siempre? Bro, yo amo México… pero no tanto." His mouth moves with the words. ' + SON_CAN)
t("U11", 6, ["CHUY", "MX-TRAJINERA-CHUY"], "720p", TRA +
  "Close-up, static camera: " + AXO + ", on the right side of the frame. He stares into the air with a blank face, totally lost, then giggles softly and says " + VOZ_AXO + ': "¿Qué les estaba diciendo?…" His mouth moves with the words; the cigarette stays in his mouth. ' + SON_CAN)
t("U12", 6, ["LUPE", "MX-TRAJINERA-MARIACHI"], "720p", MAR +
  "Medium shot, slow side tracking camera as if passing by in another boat: " + LUPE + ", standing proudly on the small stage on the boat, plays a sweet melody on her violin with her eyes closed. No one speaks. String lights twinkle and petals float. Sweet violin music and water lapping.")
t("U13", 4, ["TOCINO", "MX-TRAJINERA-CHUY-CONTRA"], "720p", TRA +
  "Medium close-up with a slow push-in: " + PIG + ", sitting on the bench on the left side of the frame, looking to the right. His four hooves stay down; he slowly lowers his head so his sunglasses slide down to the tip of his snout, staring with love; his ears stand straight up. No one speaks. " + SON_CAN)
t("U14", 4, ["DIZZY", "MX-TRAJINERA-CHUY-CONTRA"], "720p", TRA +
  "Medium close-up, static camera: " + RAT + ", sitting on the bench on the right side of the frame, his whole head, cap and camera in the frame, both eyes looking the same way. He looks at someone on the left with a tired, annoyed face and says " + VOZ_RAT + ': "¿Otra vez, Gringo?" His mouth moves with the words. ' + SON_CAN)
t("U15", 5, ["TOCINO", "MX-TRAJINERA-MARIACHI"], "360p", MAR +
  "Medium-wide shot, static camera, from the water. " + P(PIG) + " leaps on all four legs from a boat on the left side of the frame across the water onto the stage of the flower-covered boat on the right, landing on his four hooves with a wobble. No one speaks. " + SON_CAN)
t("U16", 8, ["TOCINO", "LUPE", "MX-TRAJINERA-MARIACHI"], "720p", MAR +
  "Medium two-shot, static camera, both whole bodies on the small stage: on the left " + LUPE + ", with her arms crossed and one eyebrow raised; on the right " + PIG + ", standing on his four hooves, eyes closed, singing a cheesy romantic song to her. He sings " + VOZ_PIG + ': "Mi amor… you are my tamalito…" His mouth moves with the words; only the pig sings. Slow romantic guitar music and water lapping.')
t("U17", 4, ["LUPE", "MX-TRAJINERA-MARIACHI"], "720p", MAR +
  "Close-up, static camera: " + LUPE + ", on the left side of the frame, her whole head and sombrero in the frame, outraged, ears straight up. She says " + VOZ_LUPE + ': "¿Tamalito? ¡Tamalito su abuela!" Her mouth moves with the words. ' + SON_CAN)
t("U18", 4, ["LUPE", "TOCINO", "MX-TRAJINERA-MARIACHI"], "720p", MAR +
  "Medium two-shot, static camera, both whole bodies on the small stage: on the left " + LUPE + "; on the right " + PIG + ". She swings her small violin and smashes it on top of the pig's head with a funny crack; the violin breaks and ends up hanging around his neck; he blinks, dizzy, with tiny stars. No one speaks. " + SON_CAN)
t("U19", 5, ["DIZZY", "MX-TRAJINERA-CHUY-CONTRA"], "720p", TRA +
  "Medium shot, static camera, his whole body in the frame: " + RAT + ", sitting relaxed on the boat bench, leaning back with both hands behind his head and his feet in black slides resting up on the small wooden table in front of him, the hammock and lanterns behind. He looks into the lens, shakes his head slowly with a lazy smile and says " + VOZ_RAT + ': "Cero suerte, mi llave." His mouth moves with the words; both eyes look the same way. ' + SON_CAN)
t("U20", 4, ["MX-CATEDRAL-AMANECER"], "360p",
  "Horizontal 16:9, 4 seconds. Stylized 3D animation, cinematic light. The old cathedral with two bell towers at the blue hour just before sunrise, as in the reference photo; the bells swing and ring, birds fly out of the towers, the sky turns pink and orange behind. No characters, no text. Loud church bells and birds.")
t("U21", 5, ["CHUY", "MX-TRAJINERA-CHUY"], "720p", TRA.replace("at night", "at the blue hour just before sunrise, the sky turning pink") +
  "Close-up, static camera: " + AXO + ", on the right side of the frame, slowly looks up at the sky, his sleepy eyes opening a little more, and says " + VOZ_AXO + ': "Uy… ya va a salir el sol." His mouth moves with the words; the cigarette stays in his mouth. ' + SON_AMA)
t("U22", 6, ["DIZZY", "TOCINO", "CHUY", "MX-CANAL-PUENTE-AMANECER"], "720p", PUE +
  "Low front shot on the bridge, the camera moves backwards in front of them. Exactly three characters, only one of each: " + RAT + " runs in front in the center; right behind him " + PIG + ", with a broken small violin hanging around his neck; and last " + AXO + ", jogging slowly and out of breath. All three run in the same direction, straight toward the camera, across the wooden bridge, their whole bodies in the frame. No one speaks. Running footsteps on wood, birds and water.")
t("U23", 6, ["CATRINA", "MX-CANAL-PUENTE-AMANECER"], "720p", PUE +
  "Medium shot ON the wooden bridge deck, the camera moves backwards in front of her: " + CAT + " walks fast and elegantly along the bridge straight toward the camera, her whole body in the frame, fanning herself, never running, and calls out sweetly " + VOZ_CAT + ': "¡Almitas, no se vayan sin despedirse!" Her mouth moves with the words. The bridge railing and the misty canal behind her. Church bells far away, birds waking up and soft wind.')
t("U24", 6, ["DIZZY", "TOCINO", "CHUY", "MX-CALLE-AMANECER"], "360p", CAL +
  "Low front shot in the middle of the street, the camera moves backwards fast in front of them. Exactly three characters, only one of each, all running in the same direction straight toward the camera, whole bodies in the frame, feet on the cobblestones: " + RAT + " in front, " + PIG + " behind him, and " + AXO + " last, out of breath; they kick up marigold petals. No one speaks. " + SON_AMA)
t("U25", 6, ["DIZZY", "TOCINO", "CHUY", "MX-ALCANTARILLA-AMANECER"], "720p", ALC +
  "Medium-wide shot, static camera, all three whole bodies in the frame, feet on the cobblestones: " + RAT + " and " + PIG + " stand on the left next to the glowing manhole cover, breathing hard; " + AXO + " stands on the right, smiles lazily, raises one hand to say goodbye and says " + VOZ_AXO + ': "Ahí nos vidrios, carnales." Only the axolotl speaks; the cigarette stays in his mouth. ' + SON_AMA)
t("U26", 6, ["DIZZY", "TOCINO", "MX-ALCANTARILLA-AMANECER"], "360p", ALC +
  "Medium shot, static camera. The manhole cover slides aside by itself and bright green light shoots up; " + RAT + " and " + PIG + " hold hands and hoof, close their eyes and jump together into the glowing hole, disappearing in a soft green flash with sparkles; the cover slides back. No one speaks, no screaming. A magical whoosh.")
t("U27", 5, ["DIZZY", "TOCINO", "ZARZO-AMANECER"], "720p", ZAR +
  "Wide shot, static camera. A small swirling ring of green magic light opens on the wooden ceiling above the mattress; " + RAT + " and then " + PIG + " drop out of it and land softly on the mattress with a puff of dust; the green light closes. No one speaks. " + SON_ZAR)
t("U28", 6, ["GERTRUDIS", "ZARZO-AMANECER"], "720p", ZAR +
  "Medium shot, static camera: the wooden door on the left opens and " + GER + " stands in the doorway, her whole body in the frame, frowning, tapping her foot. She says " + VOZ_GER + ': "¿Y ustedes de dónde vienen a esta hora?" Her mouth moves with the words. ' + SON_ZAR)
t("U29", 5, ["DIZZY", "ZARZO-AMANECER"], "720p", ZAR +
  "Medium close-up, static camera: " + RAT + ", sitting on the mattress on the right side of the frame, his whole head, cap and camera in the frame, both eyes looking the same way, with a guilty nervous smile. He looks to the left and says " + VOZ_RAT + ': "Del más allá, abuela… literal." His mouth moves with the words. ' + SON_ZAR)
t("U30", 4, ["GERTRUDIS", "DIZZY", "ZARZO-AMANECER"], "720p", ZAR +
  "Medium-wide shot, static camera, both whole bodies in the frame: on the left " + GER + "; on the right " + RAT + " sitting on the mattress. She throws the rubber slipper with her wing and it bounces off the rat's cap; his cap flies off and he falls back on the mattress. No one speaks. A funny slap sound.")
t("U31", 8, ["DIZZY", "ZARZO-AMANECER"], "720p", ZAR +
  "Medium close-up, static camera: " + RAT + ", sitting on the mattress in the center of the frame, rubbing his head, his cap back on with the camera fully in the frame, both eyes looking straight into the lens. He smiles at the camera and says " + VOZ_RAT + ': "Sígueme pa\' no perderte el próximo episodio, mi llave." His mouth moves with the words. ' + SON_ZAR)
t("U32", 4, ["DIZZY", "ZARZO-AMANECER"], "720p", ZAR +
  "Extreme close-up, static camera, of the small action camera on top of the rat's cap: its little red light turns on by itself and a soft green glow pulses from its lens, lighting the rat's surprised face from above. No one speaks. A soft electronic beep and a magical hum.")
t("FIN", 10, ["AEREA-FINCA"], "360p",
  "Horizontal 16:9, 10 seconds. Cinematic aerial drone shot of the lonely two-story coffee farmhouse on the green mountain at sunrise, as in the reference photo, golden light, mist in the valleys, birds flying. The drone slowly pulls back and rises. No characters, no text. Soft wind, birds and a rooster far away.")

# --- Escena de convivencia en la trajinera (idea de Jay, 12-nov): plano general + primeros planos alternados (plano/contraplano)
# Posiciones fijas como en U06: Tocino a la IZQUIERDA, Dizzy en el MEDIO, Chuy a la DERECHA con la vara; la trajinera de Lupe al fondo.
FONDO_LUPE = "Far behind them, out of focus, another flower-covered boat with a small chihuahua musician playing the violin. "
t("V1", 6, ["DIZZY", "TOCINO", "CHUY", "MX-TRAJINERA-CHUY"], "720p", TRA +
  "Wide shot, slow push-in, all three whole bodies on the boat: on the left " + PIG + ", staring dreamily to the back with his sunglasses down; in the middle " + RAT + ", sitting on the bench; on the right " + AXO + ", standing with the long pole. The rat notices the pig staring, rolls his eyes and nudges him with his elbow. " + FONDO_LUPE + "No one speaks. " + SON_CAN)
t("V2", 5, ["DIZZY", "MX-TRAJINERA-CHUY"], "720p", TRA +
  "Over-the-shoulder close-up: the camera is behind the pig's pink ear on the left edge of the frame, looking at " + RAT + ", who sits in the center, his whole head, cap and camera in the frame, both eyes looking the same way, angry, pointing his finger at the pig. He scolds him " + VOZ_RAT + ': "¡Ey, Gringo! ¿Usted es bobo o qué? ¡Esa mariachi lo va a matar!" His mouth moves with the words; only the rat speaks. ' + SON_CAN)
t("V3", 5, ["TOCINO", "MX-TRAJINERA-CHUY-CONTRA"], "720p", TRA +
  "Close-up, static camera: " + PIG + ", on the left side of the frame, his four hooves down, a silly in-love smile, his ears up, looking to the right at the rat. He answers " + VOZ_PIG + ': "Bro, relax… es amor a primera vista." His mouth moves with the words; only the pig speaks. ' + FONDO_LUPE + SON_CAN)
t("V4", 4, ["CHUY", "MX-TRAJINERA-CHUY"], "720p", TRA +
  "Close-up, static camera: " + AXO + ", on the right side of the frame, holding the long pole, smiles lazily, giggles and says " + VOZ_AXO + ': "Ay, el amor, carnal…" His mouth moves with the words; the cigarette stays in his mouth. ' + SON_CAN)
t("V5", 4, ["DIZZY", "MX-TRAJINERA-CHUY-CONTRA"], "720p", TRA +
  "Close-up, static camera: " + RAT + ", in the center of the frame, his whole head, cap and camera in the frame, both eyes looking straight into the lens, fed up, and he says to the camera " + VOZ_RAT + ': "¡Amor mis chanclas!" His mouth moves with the words. ' + SON_CAN)
t("V0", 10, ["DIZZY", "TOCINO", "CHUY", "MX-TRAJINERA-CHUY"], "720p", TRA +
  "One continuous 10-second shot with a moving camera, like a TV series. Positions never change: on the left " + PIG + "; in the middle " + RAT + ", sitting on the bench; on the right " + AXO + ", standing with the long pole. "
  "0 to 2 seconds: wide shot of all three; the pig stares dreamily to the back with his sunglasses down and the rat nudges him with his elbow. "
  "2 to 5 seconds: the camera pushes in fast to a close-up of the rat's face (cap and camera fully in the frame, both eyes looking the same way); angry, he scolds the pig " + VOZ_RAT + ': "¡Ey, Gringo! ¿Usted es bobo o qué?" '
  "5 to 8 seconds: the camera pans left to a close-up of the pig, who smiles in love and answers " + VOZ_PIG + ': "Bro, relax… es amor a primera vista." '
  "8 to 10 seconds: the camera pans right to a close-up of the axolotl, who giggles lazily, the cigarette in his mouth. "
  "Each character's mouth moves only when he speaks. " + FONDO_LUPE + SON_CAN)
ORDEN = ["U02","U03","U04","U05","A-CANALES","U06","U07","U08","U09","U11","U12","U13","V1","V2","V3","V4","V5","U14","U15","U16","U17","U18","U19",
         "U20","U21","U22","U23","U24","U25","U26","U27","U28","U29","U30","U31","U32","FIN"]
if __name__ == "__main__":
    c = 0
    for k in ORDEN:
        d, f, r, p = U[k]; c += d * (3 if r == "720p" else 1); print(k, d, r, len(p), f)
    print("créditos aprox.", c)

# --- 12-nov (Jay): «nunca el fondo vacío»: detrás del que habla siempre se ven los otros reaccionando (muecas), con la boca cerrada.
def atras(k, extra, cast_add):
    d, f, r, p = U[k]
    for c in cast_add:
        if c not in f: f = [c] + f
    U[k] = (d, f, r, p.replace(" His mouth moves with the words", " " + extra + " His mouth moves with the words", 1).replace(" Her mouth moves with the words", " " + extra + " Her mouth moves with the words", 1))
atras("V5", "Behind him, slightly out of focus, " + PIG + " still stares dreamily to the back with his sunglasses down, and " + AXO + " giggles at the pig; both keep their mouths closed.", ["TOCINO", "CHUY"])
atras("U21", "Behind him, slightly out of focus, " + RAT + " and " + PIG + " (a broken small violin hanging around his neck) sit on the bench and slowly look up at the sky, worried, mouths closed.", ["DIZZY", "TOCINO"])
atras("U28", "In the foreground on the right, slightly out of focus, " + RAT + " and " + PIG + " sit frozen on the mattress with guilty faces, mouths closed.", ["DIZZY", "TOCINO"])
atras("U29", "Behind him, " + PIG + " hides under the blanket on the mattress and peeks out with one eye, scared, mouth closed.", ["TOCINO"])
atras("U31", "Behind him, " + PIG + " lies on the mattress with a big bump on his head, snoring with his mouth closed.", ["TOCINO"])
ORDEN = [k for k in ORDEN if k not in ("V1", "V2", "V3", "V4", "U14")]
ORDEN.insert(ORDEN.index("V5"), "V0")

# 12-nov: Jay pide tomas de 4 s para cerrar créditos
for k in ("U27", "U29"):
    d, f, r, p_ = U[k]; U[k] = (4, f, r, p_.replace(f"Horizontal 16:9, {d} seconds.", "Horizontal 16:9, 4 seconds.", 1))
# 12-nov: el encabezado decía «night lighting» también en las escenas del amanecer
for k, (d, f, r, p_) in list(U.items()):
    if "sunrise" in p_ and "night lighting" in p_:
        U[k] = (d, f, r, p_.replace("cinematic night lighting", "cinematic soft dawn lighting" if "blue hour" in p_ else "cinematic warm morning lighting", 1))
atras("U30", "Behind them on the mattress, " + PIG + " covers his eyes with the blanket, mouth closed.", ["TOCINO"])
d_, f_, r_, p_ = U["U30"]
U["U30"] = (d_, f_, r_, p_.replace("No one speaks. A funny slap sound.", "Behind them on the mattress, a skinny pink pig with a black mohawk, cracked sunglasses and a torn leather vest, on all four legs, hides under the blanket, mouth closed. No one speaks. A funny slap sound."))

# ===== 12-nov (Jay): NO vuelven a casa todavía: «sacarle más jugo a México». Nuevo final =====
TUERTO = "a small black-and-white cat with a black eye patch over one eye (always visible), a toothpick in his mouth, a gray tracksuit jacket and gold bracelets"
CUCA = "a brown cockroach standing on her back legs, with a red bikini and gold hoop earrings on her antennae"
BART = "an old brown mule wearing a black-and-white striped Colombian sombrero vueltiao, a leather bag and two plain sacks on his back"
VOZ_TUE = "in Colombian Spanish with a low, calm, husky male voice"
HUE = "A rough hidden street market in a Colombian alley at the first light of dawn, brick walls with graffiti, old car seats, fire barrels with dying flames, string lights, as in the reference photo. "
HUE_E = "The entrance of a rough hidden street market in a Colombian alley at the first light of dawn, brick walls, string lights, as in the reference photo. "
t("U25", 6, ["DIZZY", "TOCINO", "CHUY", "MX-ALCANTARILLA-AMANECER"], "720p", ALC +
  "Medium-wide shot, static camera, exactly three characters, only one of each, whole bodies in the frame, feet on the cobblestones, out of breath: " + RAT + " in front of the manhole cover in the center, " + PIG + " on the left and " + AXO + " on the right. The first golden rays of the sun hit the alley and the faint green glow of the cover flickers and goes out completely. The rat stares at it in panic and says " + VOZ_RAT + ': "No, no, no… ¡se apagó!" Only the rat speaks; the pig and the axolotl keep their mouths open in shock without speaking. ' + SON_AMA)
t("U26", 5, ["CHUY", "TOCINO", "MX-ALCANTARILLA-AMANECER"], "720p", ALC.replace("glowing faint magical green", "no longer glowing") +
  "Close-up, static camera: " + AXO + ", on the right side of the frame, scratches his head, smiles lazily and says " + VOZ_AXO + ': "Uy… ya valió, carnales." Behind him, ' + PIG + " faints dramatically and falls on his side onto the cobblestones, mouth closed. His mouth moves with the words; the cigarette stays in his mouth. " + SON_AMA)
t("U26b", 5, ["CATRINA", "MX-ALCANTARILLA-AMANECER"], "720p", ALC.replace("glowing faint magical green", "no longer glowing") +
  "Wide shot, slow push-in: at the far end of the alley, backlit by the sunrise, " + CAT + " appears and walks slowly toward the camera, fanning herself, smiling, and says " + VOZ_CAT + ': "Ahora sí, almitas… no se me escapan." Her mouth moves with the words. ' + SON_AMA)
t("H1", 8, ["TUERTO", "CUCA", "VENDEDORES-HUECO", "HUECO-DENTRO"], "720p", HUE +
  "Wide shot, slow push-in. " + P(CUCA) + " and a few animal vendors warm up around a fire barrel. " + P(TUERTO) + " walks in from the left dragging a huge old flat TV screen on a rope, proud, and says " + VOZ_TUE + ': "¡Miren esta pantallota que me encontré, parceros!" Only the cat speaks; the others turn to look, surprised, mouths closed. Crackling fire and distant roosters.')
t("H2", 6, ["GERTRUDIS", "BARTOLO", "HUECO-ENTRADA"], "720p", HUE_E +
  "Medium-wide shot, static camera, both whole bodies in the frame: " + GER.replace("holding one rubber slipper in her wing", "holding a basket full of arepas in her wings") + " walks in on the left, and " + BART + " walks in behind her on the right, chewing slowly. She looks around worried and says " + VOZ_GER + ': "¿Alguien ha visto a mi nieto? Le traje arepitas." Her mouth moves with the words; only the hen speaks. Crackling fire and distant roosters.')
t("H3", 4, ["HUECO-DENTRO"], "360p",
  "Horizontal 16:9, 4 seconds. Stylized 3D animation, cinematic light. A huge old flat TV screen hangs on the graffiti brick wall of the rough street market at dawn, as in the reference photo, string lights around it. The screen flickers with static and then lights up completely in plain solid bright green, with no image and no text. No characters. An electric buzz and a beep.")
t("H4", 10, ["TUERTO", "CUCA", "GERTRUDIS", "BARTOLO", "HUECO-DENTRO"], "720p", HUE +
  "One continuous 10-second shot with a moving camera, like a TV series. Exactly these characters, only one of each, standing together in front of a huge screen on the wall, their faces lit by its green glow: " + TUERTO + "; " + CUCA + "; " + GER.replace("holding one rubber slipper in her wing", "holding a basket of arepas") + "; and " + BART + ". The camera glides from face to face: the cat smirks, the cockroach covers her mouth in surprise, the hen's eyes go wide and she drops her basket, the mule keeps chewing calmly. Nobody speaks; all mouths closed. Crackling fire and distant roosters.")
t("H5", 5, ["GERTRUDIS", "BARTOLO", "HUECO-DENTRO"], "720p", HUE +
  "Close-up, static camera: " + GER.replace("holding one rubber slipper in her wing", "with both wings on her cheeks") + ", on the left side of the frame, her face lit by a green glow, shocked, and she says " + VOZ_GER + ': "¿Y mi nieto qué hace en México?" Behind her, slightly out of focus, ' + BART + " keeps chewing calmly, mouth closed. Her mouth moves with the words. Crackling fire.")
t("H6", 4, ["TUERTO", "HUECO-DENTRO"], "720p", HUE +
  "Close-up, static camera: " + TUERTO + ", on the right side of the frame, his face lit by a green glow, moves the toothpick to the other side of his mouth, smirks and says " + VOZ_TUE + ': "Ese pelado no aprende." His mouth moves with the words. Crackling fire.')
t("W2", 8, ["DIZZY", "TOCINO", "CHUY", "MX-ALCANTARILLA-AMANECER"], "720p", ALC.replace("glowing faint magical green", "no longer glowing") +
  "Medium close-up, static camera: " + RAT + ", in the center of the frame, his whole head, cap and camera in the frame, both eyes looking straight into the lens, with a crooked brave smile. He says to the camera " + VOZ_RAT + ': "Mis ratas… nos quedamos en México. Sígueme pa\' no perderte el próximo episodio, mi llave." Behind him, ' + AXO + " waves lazily at the camera and " + PIG + " lies on the cobblestones, both with mouths closed. His mouth moves with the words. " + SON_AMA)
ORDEN = [k for k in ORDEN if k not in ("U27", "U28", "U29", "U30", "U31", "U32", "FIN")]
ORDEN = ORDEN[:ORDEN.index("U26") + 1] + ["U26b", "H1", "H2", "H3", "H4", "H5", "H6", "W2"]
for k, (d, f, r, p_) in list(U.items()):
    if ("dawn" in p_ or "sunrise" in p_) and "cinematic night lighting" in p_:
        U[k] = (d, f, r, p_.replace("cinematic night lighting", "cinematic soft dawn lighting", 1))
# 12-nov (Jay): las de 5 s pasan a 4 s; más tomas de cine (aéreas, enfoque/desenfoque, acercamientos a objetos y caras)
for k in ("U26", "U26b", "H5"):
    d, f, r, p_ = U[k]; U[k] = (4, f, r, p_.replace(f"Horizontal 16:9, {d} seconds.", "Horizontal 16:9, 4 seconds.", 1))
t("A-MX-AMANECER", 6, ["AEREA-CDMX-NOCHE"], "360p",
  "Horizontal 16:9, 6 seconds. Cinematic aerial drone shot of the old Mexican city with the two-tower cathedral and the two volcanoes, as in the reference photo, at the exact moment of sunrise: the first golden sun appears behind the volcanoes and its light sweeps over the rooftops, candles going out, morning mist. The drone flies fast forward and down toward the narrow streets. No characters, no text. Church bells and wind.")
t("I-TAPA", 4, ["MX-ALCANTARILLA-AMANECER"], "360p",
  "Horizontal 16:9, 4 seconds. Stylized 3D animation, cinematic soft dawn lighting. Extreme close-up at ground level of the round iron manhole cover from the reference photo, its faint green glow pulsing; a golden sunbeam slowly slides across the cobblestones and touches it, and the green glow fades out completely; then the focus racks to the background, where a small gray rat's black slides in white socks stop running in front of it. No faces, no text. A dying magical hum and birds.")
t("A-HUECO", 6, ["AEREA-OLLA"], "360p",
  "Horizontal 16:9, 6 seconds. Cinematic aerial drone shot at the first light of dawn over the crowded Colombian hillside neighborhood from the reference photo, brick houses, tangled cables, smoke from a few chimneys, pink sky. The drone dives fast down into one narrow alley. No characters, no text. Distant roosters, dogs and wind.")
i = ORDEN.index("U24"); ORDEN.insert(i, "A-MX-AMANECER")
i = ORDEN.index("U25"); ORDEN.insert(i + 1, "I-TAPA")
i = ORDEN.index("H1"); ORDEN.insert(i, "A-HUECO")

# ===== 12-nov (Jay): en vez de la pantalla, un PROYECTOR robado que proyecta a Dizzy sobre una VACA que se le escapa al Gallinazo =====
VACA = "a realistic black-and-white Holstein cow with a big clean white middle side with no spots, small horns and a brass bell on a leather collar"
GALL = "a black vulture with a bald wrinkled reddish head, a white fluffy neck ruff and a stained white butcher apron, from the reference image"
CAR = "The meat stall of a rough hidden street market in a Colombian alley at the first light of dawn, hanging string lights, crates and fire barrels, as in the reference photo. "
t("H0", 6, ["VACA", "VENDEDORES-HUECO", "HUECO-PUESTO-CARNE"], "720p", CAR +
  "Wide shot, the camera pans fast following the action: " + VACA + " escapes from the meat stall and runs through the market from right to left, knocking over crates and scattering vendors; behind her " + GALL + " chases her, flapping his wings, and shouts in Colombian Spanish with a very deep, croaky male voice: \"¡Vuelva acá, mi almuerzo!\" Only the vulture speaks. Crates crashing, a cow bell ringing, chickens squawking.")
t("H1", 6, ["TUERTO", "CUCA", "VENDEDORES-HUECO", "HUECO-DENTRO"], "720p", HUE +
  "Medium-wide shot, slow push-in. " + P(CUCA) + " and a few animal vendors warm up around a fire barrel. " + P(TUERTO) + " walks in from the left proudly carrying a big old movie projector in his arms, and says " + VOZ_TUE + ': "¡Miren lo que me conseguí, parceros!" Only the cat speaks; the others turn to look, mouths closed. Crackling fire and distant roosters.')
t("H3", 4, ["TUERTO", "HUECO-DENTRO"], "360p",
  "Horizontal 16:9, 4 seconds. Stylized 3D animation, cinematic soft dawn lighting, shallow depth of field. Extreme close-up of an old movie projector held by the paws of a black-and-white cat in a gray tracksuit sleeve, in a rough street market at dawn, as in the reference photo: his paw presses a button by accident, the lens lights up and a strong beam of light shoots out toward the right; the focus racks along the beam. No faces, no text. A click and a mechanical whirr.")
t("H3b", 6, ["VACA", "HUECO-DENTRO"], "720p", HUE +
  "Medium shot, static camera: " + VACA + " runs in from the left and stops in the middle of the frame, panting, right in front of a strong beam of projector light coming from the left. The beam paints a big bright rectangle of plain solid green light on the white side of her body. She slowly turns her head to the camera with a confused face and moos: \"Muuuu…\" Her mouth moves with the moo. Projector whirr and a cow bell.")
t("H4", 10, ["TUERTO", "CUCA", "GERTRUDIS", "BARTOLO", "HUECO-DENTRO"], "720p", HUE +
  "One continuous 10-second shot with a moving camera, like a TV series. Exactly these characters, only one of each, standing together and staring at something bright on the right, their faces lit by flickering projector light: " + TUERTO + "; " + CUCA + "; " + GER.replace("holding one rubber slipper in her wing", "holding a basket of arepas") + "; and " + BART + ". The camera glides from face to face: the cat smirks, the cockroach covers her mouth in surprise, the hen's eyes go wide and she drops her basket, the mule keeps chewing calmly. Nobody speaks; all mouths closed. Crackling fire and a projector whirr.")
for k in ("H5", "H6"):
    d, f, r, p_ = U[k]; U[k] = (d, f, r, p_.replace("her face lit by a green glow", "her face lit by flickering projector light").replace("his face lit by a green glow", "his face lit by flickering projector light"))
ORDEN = [k for k in ORDEN if k not in ("H1", "H2", "H3", "H4")]
i = ORDEN.index("A-HUECO") + 1
ORDEN[i:i] = ["H0", "H1", "H2", "H3", "H3b", "H4"]
for k, (d, f, r, p_) in list(U.items()):
    if ("dawn" in p_ or "sunrise" in p_) and "cinematic night lighting" in p_:
        U[k] = (d, f, r, p_.replace("cinematic night lighting", "cinematic soft dawn lighting", 1))

# 12-nov (Jay): el Gallinazo NO persigue; zoom rápido a su cara mientras la vaca se va. Más ángulos.
t("H0", 6, ["VACA", "GALLINAZO-FRENTE", "HUECO-PUESTO-CARNE"], "720p", CAR +
  "Medium shot of the meat stall, then a fast zoom-in: " + VACA + " bursts out from behind the stall and runs away to the left, knocking over a crate; the camera quickly zooms in to a close-up of " + GALL + ", who stays behind the counter, frozen, his beak open in shock, while out of focus behind him the cow runs away down the alley. He shouts in Colombian Spanish with a very deep, croaky male voice: \"¡Vuelva acá, mi almuerzo!\" Only the vulture speaks. A crate crashing, a cow bell ringing away.")
t("H0b", 4, ["VACA", "HUECO-DENTRO"], "360p",
  "Horizontal 16:9, 4 seconds. Stylized 3D animation, cinematic soft dawn lighting, shallow depth of field. Low shot at ground level in a rough street market at dawn, as in the reference photo: the hooves of a black-and-white cow gallop fast past the camera from right to left, kicking up dust and bottle caps, a brass bell ringing; motion blur. No faces, no text. Galloping hooves and a cow bell.")
i = ORDEN.index("H0"); ORDEN.insert(i + 1, "H0b")
for k, (d, f, r, p_) in list(U.items()):
    if ("dawn" in p_ or "sunrise" in p_) and "cinematic night lighting" in p_:
        U[k] = (d, f, r, p_.replace("cinematic night lighting", "cinematic soft dawn lighting", 1))
# 12-nov (Jay): transición: la cámara se acerca a la proyección en el lomo de la vaca y entramos a México «como si grabara la cámara de Dizzy» (visor REC en la edición)
t("H3c", 4, ["VACA", "HUECO-DENTRO"], "360p",
  "Horizontal 16:9, 4 seconds. Stylized 3D animation, cinematic soft dawn lighting. In a rough street market at dawn, as in the reference photo, a realistic black-and-white Holstein cow stands still with a big bright rectangle of plain solid green projector light on the clean white middle side of her body. The camera slowly pushes in straight toward the green rectangle until the green light fills the whole frame. No faces, no text. Projector whirr getting louder.")
mex = ["A-MX-AMANECER", "U24", "U25", "I-TAPA", "U26", "U26b"]
hue = ["A-HUECO", "H0", "H0b", "H1", "H2", "H3", "H3b", "H3c"]
ORDEN = [k for k in ORDEN if k not in mex + hue + ["H3c"]]
i = ORDEN.index("U23") + 1
ORDEN[i:i] = hue + mex   # después de la persecución: corte a El Hueco → proyección → México por la cámara de Dizzy → vuelta a las reacciones (H4, H5, H6) → W2

# 13-nov-2026 · U26b versión SOMBRA: la Catrina completa se bloqueó 3 veces (limpia, larga y muda).
# Solo su sombra, sin cara ni cuerpo, sin voz en Flow (la frase va con ElevenLabs encima). Solo la foto del lugar.
t("U26b", 4, ["MX-ALCANTARILLA-AMANECER"], "720p", ALC +
  "Low wide shot, static camera, no characters visible in the frame. The rising sun shines from the far end of the alley. "
  "A long dark shadow slowly stretches across the cobblestones toward the camera: the shadow of a tall slim lady with a huge wide hat decorated with flowers, "
  "a long flowing dress and a folding fan that opens and moves slowly. Only the shadow is seen, never the person. Marigold petals drift in the wind. "
  "No one speaks. Church bells far away, a soft eerie wind.")
_d, _f, _r, _x = U["U26b"]
U["U26b"] = (_d, _f, _r, _x.replace("cinematic night lighting", "cinematic soft dawn lighting").replace("a round iron manhole cover glowing faint magical green", "a round iron manhole cover no longer glowing"))

# 13-nov-2026 · W2 v2: Tocino salió de pie (venía desmayado de U26). Estado explícito y posición fija.
t("W2", 8, ["DIZZY", "TOCINO", "CHUY", "MX-ALCANTARILLA-AMANECER"], "720p", ALC.replace("a round iron manhole cover glowing faint magical green", "a round iron manhole cover no longer glowing") +
  "Medium close-up, static camera, exactly three characters, only one of each. In the center: " + RAT + ", his whole head, cap and camera in the frame, both eyes looking straight into the lens, never cross-eyed, with a crooked brave smile. "
  "He says to the camera in Colombian Spanish with a raspy, hoarse young male street voice: \"Mis ratas… nos quedamos en México. Sígueme pa' no perderte el próximo episodio, mi llave.\" His mouth moves with the words; only he speaks. "
  "Behind him on the left: " + AXO + ", standing, waving lazily at the camera with his mouth closed. "
  "Behind him on the right, on the ground: " + PIG + ", lying flat on his side on the cobblestones, fainted, with his eyes closed and his tongue out; he never stands up and never moves. "
  "Church bells far away, birds waking up and soft wind.")
_d, _f, _r, _x = U["W2"]
U["W2"] = (_d, _f, _r, _x.replace("cinematic night lighting", "cinematic soft dawn lighting"))
_d, _f, _r, _x = U["W2"]
U["W2"] = (_d, _f, _r, _x.replace("on his back, always on all four legs, lying flat", "on his back, lying flat"))

# 13-nov-2026 · W2 v3 MUDA: la v2 dio «No se pudo generar el audio». Modo vídeos silenciosos, sin frase entre comillas;
# Dizzy habla con ventana de tiempo y la voz de ElevenLabs se pega en la edición.
_x = U["W2"][3]
_x = _x.replace('He says to the camera in Colombian Spanish with a raspy, hoarse young male street voice: "Mis ratas… nos quedamos en México. Sígueme pa\' no perderte el próximo episodio, mi llave." His mouth moves with the words; only he speaks. ',
                "From second 0.5 to second 7 he talks to the camera with lively, clear mouth movements and small head nods, then he stops talking and smiles; only he moves his mouth. ")
_x = _x.replace(" Church bells far away, birds waking up and soft wind.", " Silent video, no voices.")
U["W2"] = (8, U["W2"][1], "720p", _x)

# ======================================================================================================
# 13-nov-2026 · ARREGLOS DE CONTINUIDAD tras el armado (Jay: «que parezca una película; la continuidad es lo más importante»)
# ======================================================================================================
AMA = lambda s: s.replace("cinematic night lighting", "cinematic soft dawn lighting")
R = {}
def r(i, d, fotos, res, txt, dawn=False):
    full = H.format(d=d) + txt
    R[i] = U[i] = (d, fotos, res, AMA(full) if dawn else full)

# 1. Chuy jala la cuerda (inserto de la mano) — antes no se entendía quién tiraba el toldo
r("U03b", 4, ["MX-MERCADO-ESCONDITE"], "720p", ESC +
  "Close-up insert, static camera, no faces: from the left side of the frame, one chubby pink four-fingered hand grabs a thick rope that hangs from the roof "
  "and pulls it down hard and fast; the rope runs up out of the frame. Dust falls from above. No one speaks. A loud rope creak. " + SON_ESC)
# 2. El toldo le cae a la Catrina — plano más cerrado para que se entienda
r("U04", 4, ["CATRINA", "MX-MERCADO-ESCONDITE"], "720p", ESC +
  "Medium shot, static camera: " + CAT + ", on the right side of the frame, bends down toward the camera with a sly smile, her whole body in the frame. "
  "Suddenly a huge heavy colorful striped fabric awning drops from the top of the frame straight onto her and covers her completely from head to toe, "
  "so her face and body disappear; she turns into a big wiggling lump of cloth that waves its arms under the fabric. No one speaks. A heavy cloth thump. " + SON_ESC)
# 3. Se suben a la trajinera — antes aparecían a bordo de un momento a otro
r("U05b", 6, ["DIZZY", "TOCINO", "CHUY", "MX-MERCADO-MUELLE"], "720p", MUE +
  "Medium-wide shot, static camera from the water, the colorful flower-covered boat tied to the small wooden dock in the foreground. Exactly three characters, only one of each: "
  "first " + RAT + " jumps from the dock into the boat; then " + PIG + " jumps in on his four legs; last " + AXO + " steps in calmly, "
  "picks up a long wooden pole and pushes the boat away from the dock. The boat starts to glide away. No one speaks. " + SON_CAN)
# 4. Más conversación antes de que Chuy cambie de tema
r("U10a", 4, ["DIZZY", "MX-TRAJINERA-CHUY-CONTRA"], "720p", TRA +
  "Medium close-up, static camera: " + RAT + ", sitting on the boat bench on the left side of the frame, his whole head, cap and camera in the frame, both eyes looking the same way, worried. "
  "He leans toward someone on the right and asks " + VOZ_RAT + ': "Chuy… ¿y cuánto falta pa\' que salga el sol?" His mouth moves with the words. ' + SON_CAN)
r("U10b", 6, ["CHUY", "MX-TRAJINERA-CHUY"], "720p", TRA +
  "Medium close-up, static camera: " + AXO + ", standing at the back of the boat on the right side of the frame, holding the long pole with one hand. "
  "Very slowly he looks up at the night sky, counts on the fingers of his free hand with his lips moving silently, then freezes with a totally blank face, "
  "eyes crossed for a second, the cigarette still in his mouth. No one speaks. " + SON_CAN)
# 5. La trajinera de los mariachis llega al lado (antes Lupe aparecía en otro barco y luego atrás de ellos)
r("U12b", 6, ["DIZZY", "TOCINO", "CHUY", "LUPE", "MX-CANAL-TRAJINERAS"], "720p",
  "Calm dark canal at night with floating marigolds, lanterns and string lights, as in the reference photo. Wide shot from the water, static camera, exactly four characters, only one of each. "
  "Two flower-covered canal boats glide slowly side by side, very close, with a narrow gap of dark water between them. "
  "On the boat on the right: " + RAT + " sits on the bench, " + PIG + " stands next to him on his four legs, and " + AXO + " stands at the back pushing with a long pole. "
  "On the boat on the left, standing on its small wooden stage: " + LUPE + ", who plays a sweet melody on her violin. "
  "The pig slowly turns his head and stares at her. No one speaks. Sweet violin music and water lapping.")
# 6. Tocino salta de una trajinera a la otra, claro y de lado
r("U15", 4, ["TOCINO", "DIZZY", "CHUY", "MX-TRAJINERA-MARIACHI"], "720p", MAR +
  "Wide side shot, static camera from the water: two flower-covered boats side by side with a narrow gap of dark water between them, the mariachi boat with its small stage on the left. "
  "Exactly three characters, only one of each. On the edge of the boat on the right, " + PIG + " takes a short run and leaps across the gap, flies over the water "
  "and lands on his four hooves on the small stage of the boat on the left, wobbling. On the boat on the right, " + RAT + " covers his eyes and " + AXO + " watches calmly. "
  "No one speaks. A splash of water and wood creaks.")
# 7. El violinazo: el violín se rompe en pedazos (ya no queda colgado del cuello)
r("U18", 4, ["LUPE", "TOCINO", "MX-TRAJINERA-MARIACHI"], "720p", MAR +
  "Medium two-shot, static camera, both whole bodies on the small stage: on the left " + LUPE + "; on the right " + PIG + ". "
  "She swings her small violin and smashes it on top of the pig's head; the violin shatters into small wooden pieces and strings that fall to the floor, nothing stays on him. "
  "He blinks, dizzy, his eyes spinning, and wobbles on his four legs. No one speaks. A wooden crack and water lapping.")
# 8. Se bajan de la trajinera al pie del puente (antes estaban en la barca y de pronto corriendo en el puente)
r("U21b", 6, ["DIZZY", "TOCINO", "CHUY", "MX-CANAL-PUENTE-AMANECER"], "720p", PUE +
  "Medium-wide shot, static camera from the stone steps at the foot of the wooden arched bridge. Exactly three characters, only one of each. "
  "Their flower-covered boat bumps into the steps; " + RAT + " jumps off first and runs up the steps toward the camera, " + PIG + " jumps off on his four legs right behind him, "
  "and " + AXO + " drops his pole and follows them, jogging slowly and out of breath. No one speaks. Wood bump, running steps and birds waking up.", dawn=True)
# 9. La Catrina los persigue en el MISMO puente (antes salía en otro muelle)
r("U23", 6, ["CATRINA", "MX-CANAL-PUENTE-AMANECER"], "720p", PUE +
  "Medium-wide shot, static camera low on a wooden walkway with wooden railings that passes under a big wooden arched bridge. "
  "Under the arch, far away, " + CAT + " appears and walks fast and elegantly straight toward the camera along the same walkway, her whole body in the frame, fanning herself, never running, "
  "and calls out sweetly " + VOZ_CAT + ': "¡Almitas, no se vayan sin despedirse!" Her mouth moves with the words. Church bells far away, birds waking up and soft wind.', dawn=True)
# U05b v2 (13-nov): la v1 salió con DOS ratas, el marrano «volando» y Dizzy y Tocino se quedaron en el muelle.
# Más simple: Chuy YA está en la trajinera con la vara; solo saltan dos, de lado, y U06 sigue con Chuy empujando.
r("U05b", 4, ["DIZZY", "TOCINO", "CHUY", "MX-MERCADO-MUELLE"], "720p", MUE +
  "Medium side shot, static camera, the flower-covered boat in the foreground across the frame, the small wooden dock on the left. Exactly three characters, only one of each. "
  + P(AXO) + " already stands at the back of the boat on the right, holding a long wooden pole. "
  "From the dock on the left, " + RAT + " jumps into the boat and lands sitting on the bench; right behind him " + PIG + " jumps in on his four legs and lands next to the rat. "
  "Both end inside the boat; nobody stays on the dock. The boat rocks and water splashes. No one speaks. " + SON_CAN)
# U12b v2 (13-nov): la trajinera de ellos salió como un bote azul sin arco (no es la de Chuy) y Tocino no volteó.
# Se suben las DOS fotos de barcas (la de Chuy y la de los mariachis) en vez de la del canal, y cada barca se describe.
r("U12b", 6, ["DIZZY", "TOCINO", "CHUY", "LUPE", "MX-TRAJINERA-CHUY", "MX-TRAJINERA-MARIACHI"], "720p",
  "Calm dark canal at night with floating marigolds, lanterns and string lights. Wide shot from the water, static camera, exactly four characters, only one of each, and exactly two boats. "
  "On the right: THEIR boat, exactly the red wooden boat with the green painted arch, paper lanterns and a hammock from the first boat reference photo; on it "
  + RAT + " sits on the bench, " + PIG + " stands next to him on his four legs, and " + AXO + " stands at the back pushing with a long pole. "
  "On the left, gliding side by side very close to it, with a narrow gap of dark water between them: the mariachi boat with the small wooden stage and the arch covered with flowers "
  "from the second boat reference photo; on its stage " + LUPE + " plays a sweet melody on her violin. "
  "At second 2 the pig slowly turns his whole head to the left toward her, his sunglasses slide down and he stares at her in love. No one speaks. Sweet violin music and water lapping.")
# U12b v3 (13-nov): v2 acertó las barcas pero TOCINO NO SALIÓ (en su lugar, una rata café). Con 6 fotos Flow suelta un personaje.
# Máximo 5 fotos: la barca de los mariachis va solo descrita. Tocino en el borde más cercano a Lupe, bien visible y primero en la lista.
r("U12b", 6, ["TOCINO", "DIZZY", "CHUY", "LUPE", "MX-TRAJINERA-CHUY"], "720p",
  "Calm dark canal at night with floating marigolds, lanterns and string lights. Wide shot from the water, static camera, exactly four characters, only one of each, and exactly two boats. "
  "On the right: THEIR boat, exactly the red wooden boat with the green painted arch, paper lanterns and a hammock from the boat reference photo. On it, from left to right: "
  + PIG + ", pink skin, clearly visible on the left edge of their boat, standing on his four legs; then " + RAT + ", gray fur, sitting on the bench; then " + AXO + ", at the back pushing with a long pole. "
  "On the left, gliding side by side very close to them, with a narrow gap of dark water between them: a mariachi boat with a small wooden stage and a tall orange arch covered with marigolds; on its stage "
  + LUPE + " plays a sweet melody on her violin. "
  "At second 2 the pink pig slowly turns his whole head to the left toward her, his sunglasses slide down and he stares at her in love. No one speaks. Sweet violin music and water lapping.")

# ======================================================================================================
# 13-nov-2026 (tarde) · CANALES EN TOMAS LARGAS DE 10 s (Jay: «la continuidad es lo más importante»; cada toma corta parecía otra barca)
# Regla: misma trajinera SIEMPRE (foto MX-TRAJINERA-CHUY), mismas posiciones, cámara que se mueve dentro de la toma,
# modo «vídeos silenciosos» con ventanas de tiempo para las bocas (varios hablan en la misma toma); voces de ElevenLabs en la edición.
# ======================================================================================================
BOTE = ("All the action happens on THEIR boat: exactly the red wooden canal boat with the green painted arch, paper lanterns and a hammock from the boat reference photo; "
        "it is always this same boat. Positions never change: the pig stands on the left side of the boat on his four legs, the rat sits on the bench in the middle, "
        "the axolotl stands at the back on the right holding the long wooden pole. ")
CANAL = "A calm dark canal at night with floating marigolds, lanterns and string lights, other lit boats far away. "
MUDO = " Silent video, no voices, no music."
def L(i, d, fotos, txt, dawn=False):
    full = H.format(d=d) + txt + MUDO
    R[i] = U[i] = (d, fotos, "720p", AMA(full) if dawn else full)
F3 = ["TOCINO", "DIZZY", "CHUY", "MX-TRAJINERA-CHUY"]
TRES = "Exactly three characters, only one of each: " + PIG + "; " + RAT + "; " + AXO + ". "

L("L1", 10, F3, CANAL + BOTE + TRES +
  "One continuous 10-second shot, the camera floats slowly alongside the boat as it glides away from the dock. "
  "0 to 3 seconds: the pig looks around amazed and talks with lively mouth movements. "
  "3 to 6 seconds: the camera drifts closer to the rat, who turns to the axolotl and talks with lively mouth movements, both eyes looking the same way. "
  "6 to 10 seconds: the camera pushes in to the axolotl, who answers very slowly with lazy mouth movements, the cigarette in his mouth. "
  "Only the one who talks moves his mouth; the others keep their mouths closed.")
L("L2", 10, F3, CANAL + BOTE + TRES +
  "One continuous 10-second shot with a slow moving camera. "
  "0 to 4 seconds: close on the axolotl, who keeps talking very slowly with lazy mouth movements and points up at the night sky. "
  "4 to 7 seconds: the camera pans left to the pig, scared, ears flat, who talks fast with nervous mouth movements. "
  "7 to 10 seconds: the camera pans to the rat, worried, who leans toward the axolotl and asks something with lively mouth movements, both eyes looking the same way. "
  "Only the one who talks moves his mouth; the others keep their mouths closed.")
L("L3", 10, F3, CANAL + BOTE + TRES +
  "One continuous 10-second shot, medium shot of the axolotl with the rat in the foreground on the left, out of focus. "
  "0 to 6 seconds: the axolotl looks up at the sky, counts slowly on the fingers of his free hand with silent lips, then freezes with a totally blank face. "
  "6 to 8 seconds: he blinks, giggles lazily and talks with slow mouth movements. "
  "8 to 10 seconds: the rat slaps his own forehead with his paw in frustration, mouth closed.")
L("L4", 10, ["TOCINO", "DIZZY", "CHUY", "LUPE", "MX-TRAJINERA-CHUY"], CANAL + BOTE +
  "Exactly four characters, only one of each: " + PIG + "; " + RAT + "; " + AXO + "; and " + LUPE + ". "
  "One continuous 10-second cinematic shot. 0 to 2 seconds: on their boat, the axolotl lazily points ahead and talks with slow mouth movements. "
  "2 to 6 seconds: the camera turns toward the canal ahead: in the thick mist, a dark silhouette of another boat with a tall arch and a small figure with a big sombrero appears, backlit by warm lanterns, and slowly comes closer. "
  "6 to 10 seconds: it comes out of the mist and glides right next to their boat on the left side: a mariachi boat with a small wooden stage and a tall orange arch covered with marigolds, "
  "where the chihuahua stands on the stage playing her violin with her eyes closed; on their boat, the pig turns his head toward her and his sunglasses slide down.")
L("L5", 10, ["TOCINO", "DIZZY", "CHUY", "LUPE", "MX-TRAJINERA-CHUY"], CANAL + BOTE +
  "Exactly four characters, only one of each: " + PIG + "; " + RAT + "; " + AXO + "; and " + LUPE + ", who plays the violin on the small stage of a mariachi boat with an orange arch of marigolds, gliding right next to their boat on the left, always visible in the background. "
  "One continuous 10-second shot with a moving camera, like a TV series. "
  "0 to 2 seconds: wide shot; the pig stares dreamily at the chihuahua and the rat nudges him with his elbow. "
  "2 to 5 seconds: the camera pushes in to the rat's face (cap and camera fully in the frame, both eyes looking the same way); angry, he scolds the pig with lively mouth movements. "
  "5 to 8 seconds: the camera pans left to the pig, who smiles in love and answers with lively mouth movements. "
  "8 to 10 seconds: the camera pans right to the axolotl, who giggles lazily. Only the one who talks moves his mouth.")
L("L6", 10, ["TOCINO", "LUPE", "DIZZY", "CHUY", "MX-TRAJINERA-MARIACHI"],
  "A mariachi canal boat at night with a small wooden stage, string lights and a tall arch covered with marigolds, as in the reference photo, gliding side by side with a red boat with a green arch on the right. "
  "Exactly four characters, only one of each: " + PIG + "; " + LUPE + "; and, on the red boat on the right in the background, " + RAT + " and " + AXO + ". "
  "One continuous 10-second shot, the camera on the side. 0 to 3 seconds: the pig takes a short run on the edge of the red boat and leaps across the narrow gap of water, landing on his four hooves on the small stage next to the chihuahua, wobbling. "
  "3 to 8 seconds: the camera pushes in; the pig stands in front of her on his four legs, sways his head and sings to her with big romantic mouth movements, eyes closed. "
  "8 to 10 seconds: the chihuahua stops playing and stares at him, offended, mouth closed. In the background the rat covers his eyes.")
L("L7", 10, ["LUPE", "TOCINO", "DIZZY", "CHUY", "MX-TRAJINERA-MARIACHI"],
  "A mariachi canal boat at night with a small wooden stage, string lights and a tall arch covered with marigolds, as in the reference photo, gliding side by side with a red boat with a green arch on the right. "
  "Exactly four characters, only one of each: " + LUPE + "; " + PIG + "; and, on the red boat on the right, " + RAT + " and " + AXO + ". "
  "One continuous 10-second shot. 0 to 3 seconds: two-shot on the stage, the chihuahua yells at the pig with angry, fast mouth movements. "
  "3 to 5 seconds: she swings her small violin and smashes it on top of his head; the violin shatters into small wooden pieces and strings that fall to the floor, nothing stays on him; he wobbles, dizzy, eyes spinning. "
  "5 to 7 seconds: the pig jumps back across the gap onto the red boat. "
  "7 to 10 seconds: the camera pans to the rat on the red boat, who looks into the lens, tired, and talks with lively mouth movements, both eyes looking the same way.")
L("L8", 10, F3, "A calm canal at the blue hour just before sunrise, the sky turning pink and orange, soft mist on the water, a wooden arched bridge ahead with stone steps at its foot. " + BOTE + TRES +
  "One continuous 10-second shot. 0 to 3 seconds: the axolotl looks up at the pink sky and talks with slow mouth movements. "
  "3 to 6 seconds: the camera pans forward: the boat bumps into the stone steps at the foot of the bridge. "
  "6 to 10 seconds: the rat jumps off first and runs up the steps, the pig follows on his four legs, and the axolotl drops the pole and follows them, out of breath. Nobody stays on the boat.", dawn=True)
L("L9", 10, ["DIZZY", "TOCINO", "CHUY", "CATRINA", "MX-CANAL-PUENTE-AMANECER"], PUE +
  "Exactly four characters, only one of each: " + RAT + "; " + PIG + "; " + AXO + "; and " + CAT + ". "
  "One continuous 10-second shot ON the wooden bridge, the camera moves backwards in front of them. "
  "0 to 6 seconds: the rat, the pig on his four legs and the axolotl run straight toward the camera across the bridge, whole bodies in the frame. "
  "From second 4, far behind them at the other end of the SAME bridge, the skeleton cat lady appears and walks fast and elegantly after them, fanning herself. "
  "6 to 10 seconds: the focus racks to her as she comes closer and calls out to them with sweet, theatrical mouth movements.", dawn=True)
L("U26", 6, ["CHUY", "TOCINO", "MX-ALCANTARILLA-AMANECER"],
  "A narrow Mexican colonial alley at blue dawn, a round iron manhole cover no longer glowing, marigold petals and burnt-out candles on the cobblestones, pink sky, as in the reference photo. "
  "Close-up, static camera: " + AXO + ", on the right side of the frame. 0 to 1 second: he scratches his head. 1 to 5 seconds: he talks very slowly with lazy mouth movements, smiling. "
  "Behind him, " + PIG + " faints dramatically and falls on his side onto the cobblestones, mouth closed, and stays lying there.", dawn=True)
# L5 v2 (13-nov): tras L4, aclarar que nadie cambia de barco (en L4 apareció un 2.º Tocino en el barco de Lupe).
_d, _f, _r, _x = U["L5"]
U["L5"] = R["L5"] = (_d, _f, _r, _x.replace(" Silent video, no voices, no music.",
    " The pig, the rat and the axolotl stay on THEIR red boat the whole time and the chihuahua stays alone on her stage; nobody changes boats. Silent video, no voices, no music."))
