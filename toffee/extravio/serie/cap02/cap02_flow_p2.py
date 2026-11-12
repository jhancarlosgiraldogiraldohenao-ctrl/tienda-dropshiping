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
  "Wide shot, side tracking camera, all three whole bodies small in the frame, feet on the bridge: " + RAT + " runs in front, " + PIG + " runs behind him with a broken small violin hanging around his neck, and " + AXO + " jogs slowly last; all running from left to right across the bridge. No one speaks. Fast cumbia-like footsteps rhythm, birds and water.")
t("U23", 6, ["CATRINA", "MX-CANAL-PUENTE-AMANECER"], "720p", PUE +
  "Medium shot, the camera moves backwards in front of her: " + CAT + " walks fast and elegantly across the bridge from left to right, fanning herself, never running, and calls out sweetly " + VOZ_CAT + ': "¡Almitas, no se vayan sin despedirse!" Her mouth moves with the words. ' + SON_AMA)
t("U24", 6, ["DIZZY", "TOCINO", "CHUY", "MX-CALLE-AMANECER"], "360p", CAL +
  "Low side tracking camera moving fast, all three whole bodies in the frame, feet on the cobblestones: " + RAT + ", " + PIG + " and " + AXO + " run from left to right down the street, kicking up marigold petals. No one speaks. " + SON_AMA)
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
ORDEN = ["U02","U03","U04","U05","A-CANALES","U06","U07","U08","U09","U11","U12","U13","U14","U15","U16","U17","U18","U19",
         "U20","U21","U22","U23","U24","U25","U26","U27","U28","U29","U30","U31","U32","FIN"]
if __name__ == "__main__":
    c = 0
    for k in ORDEN:
        d, f, r, p = U[k]; c += d * (3 if r == "720p" else 1); print(k, d, r, len(p), f)
    print("créditos aprox.", c)
