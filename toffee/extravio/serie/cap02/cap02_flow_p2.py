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
GALL = "a black vulture meat seller with a white butcher apron and a red cap, from the reference image"
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
