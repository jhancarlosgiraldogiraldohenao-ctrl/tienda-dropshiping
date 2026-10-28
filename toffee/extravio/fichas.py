# Fichas técnicas de todo lo que Jay tiene que generar para Extravío → toffee/EXTRAVIO-FICHAS.pdf
# Imágenes: Nano Banana Pro. Voces y sonidos: ElevenLabs. Las aprobadas se guardan en toffee/refs/extravio/.
import os, sys, html, subprocess
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(here, '..', 'viaje', 'temporada1'))
from build import CSS

def SHEET(bg, desc, same):
    return (f"Character reference sheet, 2x2 grid, 1:1, photorealistic, same character in all 4 views (front, 3/4 left, side, back), "
            f"plain {bg} background: {desc} {same} No text.")
LOOK = ("Photorealistic cinematic establishing shot, 16:9, like a frame from a high-budget live-action fantasy film, "
        "natural light, rich detail, deep perspective. No characters, no animals, no people, no text, no logos.")
def WORLD(desc): return f"{desc} {LOOK}"
def PROP(bg, desc): return (f"Prop reference sheet, 2x2 grid, 1:1, photorealistic, the same object in all 4 views (front, 3/4, side, close-up detail), "
                            f"plain {bg} background: {desc} No hands, no people. No text unless written below.")

# (prioridad, carpeta, archivo, nombre, para qué, fotos que adjuntar, prompt)
A, B, C = "A · antes del capítulo 1", "B · noviembre", "C · diciembre"
PERSONAJES = [
 (A, "personajes", "LUCHO.jpg", "Lucho, el ratón", "La voz de las malas ideas. Vende llaves y recuerdos. Sale en casi todos los capítulos.", "—",
  SHEET("dark gray alley", "a skinny, scruffy gray street mouse standing on two legs, messy patchy fur, HUGE dark eye bags, slightly red-rimmed tired eyes, twitchy whiskers, one crooked front tooth in a nervous grin, wearing a small torn black hoodie with the hood down and a tiny ragged backpack full of old keys hanging out, holding a small chunk of yellow cheese close to his chest, paws slightly shaky. Shifty, paranoid, funny, a little pathetic but lovable. NOT cute cartoon: realistic mouse anatomy. No gloves, no shorts, no round black ears.",
        "Same hoodie, backpack, cheese and eye bags in ALL views.")),
 (A, "personajes", "POLILLA.jpg", "La Gran Polilla (villana)", "Se come los recuerdos. Aparece poco, pero tiene que impresionar.", "—",
  SHEET("deep black", "a gigantic moth, as big as a horse, elegant and terrifying: huge wings like cathedral stained-glass windows in deep purple, gold and teal with two giant eye-shaped patterns, a thick furry silver-white body, long feathery antennae, huge glowing pale-blue eyes, and a faint glowing dust falling from her wings like sparkles. Beautiful, regal, menacing, not gory.",
        "Same wing pattern and glowing eyes in ALL views.")),
 (A, "personajes", "TOFFEE-EXPRESIONES.jpg", "Toffee · hoja de expresiones", "Para que Toffee sea siempre el mismo y actúe mejor en Flow.", "TOFFEE-viajero.jpg",
  "Character expression sheet, 3x2 grid, 3:2, photorealistic, the cream-caramel British Shorthair cat from the reference (chubby, very round face, big green eyes) wearing his navy knitted nightcap with a cream pompom and a small black action camera on top of the nightcap, head and shoulders, plain soft gray background, six expressions: proud and smug, terrified and screaming, sarcastic eye-roll, sleepy, tender and moved, sneaky whispering. Same cat, same nightcap and camera in all six. No text."),
 (A, "personajes", "GALLETA-EXPRESIONES.jpg", "Galleta · hoja de expresiones", "Sus 7 caras fijas (no habla: actúa con la cara).", "GALLETA-viajero.jpg",
  "Character expression sheet, 4x2 grid, 2:1, photorealistic, the scruffy golden-brown criollo dog from the reference (thin, wiry fur, bushy eyebrows, white chest and paws) wearing his navy bandana with a gold bone tag, head and shoulders, plain soft gray background, seven expressions plus one neutral: innocent (big round eyes, head tilted), mischievous (slow smile, eyebrows raised), complicit look straight at camera, hiding scared with ears back, begging puppy eyes, celebrating with tongue out, tender leaning head, neutral. Same dog and bandana in all eight. No text."),
 (B, "personajes", "GUARDIAN-SIESTA.jpg", "El Guardián de la Siesta (Mundo Siesta)", "Perezoso gigante que no deja salir a nadie que se duerma.", "—",
  SHEET("warm afternoon beige", "a giant three-toed sloth standing on two legs, wearing faded striped pajamas and a long droopy nightcap, holding a huge fluffy pillow like a shield, half-closed eyes, very slow and gentle but slightly creepy smile.", "Same pajamas, nightcap and pillow in ALL views.")),
 (B, "personajes", "ALCALDESA-LIKES.jpg", "La Alcaldesa Likes (Ciudad Algoritmo)", "Pavo real influencer que gobierna con likes.", "—",
  SHEET("bright white studio", "a white peacock with its tail fully open, the eye spots on the tail feathers glowing softly pink like little heart lights, a tiny golden crown, a glamorous fake smile and confident pose like a celebrity. No phone, no screen.", "Same crown and glowing tail in ALL views.")),
 (B, "personajes", "LLORONA.jpg", "La Llorona (Tierra de los Espantos)", "Leyenda latina: dramática, llorona y con problemas de vecinos. Comedia, no terror.", "—",
  SHEET("misty night river", "a ghostly woman in a long flowing white dress and white veil, pale glowing skin, long dark hair, holding a crumpled tissue, floating slightly above the ground, tearful but comically dramatic expression, soft blue ghost glow. Spooky but funny, not gory.", "Same dress, veil and tissue in ALL views.")),
 (B, "personajes", "SILBON.jpg", "El Silbón (Tierra de los Espantos)", "Leyenda llanera: flaco altísimo que silba. Vecino gruñón de la Llorona.", "—",
  SHEET("dark plains at night", "an extremely tall and thin ghostly man, 3 meters tall, wearing an old wide-brimmed straw sombrero llanero, worn shirt and trousers, carrying an old burlap sack over his shoulder, long thin arms, grumpy tired face, faint gray ghost glow. Spooky but comedic, not gory, no bones.", "Same hat and sack in ALL views.")),
 (B, "personajes", "GALLETAS-MULTIVERSO.jpg", "Galletas del multiverso (Dimensión Galleta)", "Versiones de Galleta de otros universos.", "GALLETA-viajero.jpg",
  "Character lineup sheet, 4x1 grid, 2:1, photorealistic, four versions of the same scruffy golden-brown criollo dog from the reference (thin wiry fur, bushy eyebrows, white chest and paws), full body, plain gray background: 1) King Galleta with a small gold crown and red velvet cape, 2) Pirate Galleta with an eye patch and a striped bandana, 3) Giant Galleta three times bigger, 4) Elegant Galleta with a tiny bow tie and monocle. Same dog face in all four. No text."),
 (B, "personajes", "DONA-MULA.jpg", "Doña Mula (Pueblo en las Nubes)", "Mula cafetera que maneja el pueblo flotante. Guiño a Colombia.", "—",
  SHEET("soft clouds", "a friendly brown mule wearing a white-and-black sombrero aguadeño hat and a leather carriel bag across her body, carrying two small sacks of coffee on her back, wise and sassy expression. No humans.", "Same hat, carriel and sacks in ALL views.")),
 (B, "personajes", "CARTERO-CARACOL.jpg", "El Cartero Caracol (Oficina de Cartas Perdidas)", "El cartero más lento del multiverso.", "—",
  SHEET("old post office wood", "a big garden snail with a tiny blue postman cap and a small leather mail bag hanging from his shell, the shell covered with old stamps, sleepy patient eyes.", "Same cap, bag and stamps in ALL views.")),
 (B, "personajes", "TRUENITO.jpg", "Truenito (Mundo Trueno)", "Criatura del trueno: nube pequeña y gruñona que retumba.", "—",
  SHEET("stormy purple sky", "a small round dark-gray storm cloud creature the size of a dog, with two big glowing yellow eyes, tiny crackling blue lightning sparks around it (only around the cloud), grumpy face.", "Same eyes and size in ALL views.")),
]

OBJETOS = [
 (A, "objetos", "LLAVE-DE-CASA.jpg", "La llave de casa", "La misión de la temporada: la llave que perdió la humana de Toffee.", "—",
  PROP("dark navy", "an ordinary brass house key on a small ring with a red pompom keychain and a tiny silver paw-shaped charm, softly glowing with a warm golden magic light from inside.")),
 (A, "objetos", "PLACA-MAX.jpg", "La placa de Galleta: «MAX»", "El misterio de Galleta. Primer plano en el final del capítulo 1.", "GALLETA-viajero.jpg",
  PROP("dark navy", "a small gold bone-shaped pet ID tag, slightly scratched and old, hanging from a navy bandana, with the name MAX engraved on it in simple capital letters.") + " The only text allowed is the engraved word MAX."),
 (A, "objetos", "RECUERDO.jpg", "Un recuerdo", "La magia y la moneda de Extravío.", "—",
  PROP("black", "a glowing turquoise orb of light the size of a tennis ball, like a soap bubble made of light, with a tiny blurry happy memory moving inside it (a dog playing with a ball in a garden), soft sparkles around it.")),
 (A, "objetos", "PUERTA-PORTAL.jpg", "La puerta-portal", "Cómo se ve cada puerta cuando una llave la abre.", "—",
  PROP("misty field", "an old wooden door standing alone with no wall around it, its keyhole glowing, bright colored light leaking from the edges, half open showing a different glowing world on the other side.")),
 (B, "objetos", "TELE-PERDIDA.jpg", "La tele perdida (Zapping de Extravío)", "Capta canales de otros mundos: comerciales y noticieros absurdos para shorts.", "—",
  PROP("dusty attic", "an old retro CRT television with a wooden case and two bent rabbit-ear antennas, a crack on one corner, the screen showing glowing static.")),
 (C, "objetos", "CARTEL-SE-BUSCA.jpg", "Cartel «Se busca gato»", "Posible cierre de temporada: la humana nunca dejó de buscarlo.", "TOFFEE-viajero.jpg",
  PROP("wooden lamppost", "a paper lost-cat poster taped to a lamppost, slightly wet from rain, with a photo of the cream-caramel British Shorthair cat from the reference wearing his navy nightcap.") + " Text on the poster: SE BUSCA · TOFFEE."),
]

MUNDOS = [
 (A, "mundos", "EXTRAVIO-CIUDAD.jpg", "La ciudad de Extravío", "El «hogar» de la serie. Plano de presentación de cada capítulo en Extravío.", "—",
  WORLD("A vast fantastical city built entirely from lost things: towers made of stacked suitcases, umbrellas and old lamps, bridges made of giant keys, houses made of lost shoes, small floating islands of junk with glowing turquoise lights in their windows; a warm amber dusk sky where lost objects (socks, keys, balls, letters) slowly rain down like snow.")),
 (A, "mundos", "REMOLINO.jpg", "El Remolino", "Por donde se cae a Extravío (la toma de «wow» del capítulo 1).", "—",
  WORLD("A huge swirling vortex tunnel seen from inside, falling downward, made of spinning lost objects (socks, remote controls, keys, toys, balls, umbrellas, letters) lit by turquoise magical light, with a bright warm glow at the bottom.")),
 (A, "mundos", "MAR-DE-PELOTAS.jpg", "El Mar de Pelotas", "Donde caen Toffee y Galleta.", "—",
  WORLD("An endless ocean made of millions of colorful balls (tennis balls, rubber balls, soccer balls) stretching to the horizon with gentle waves, a huge warm sunset, a small beach made of lost toys, the silhouette of the city of lost things far away.")),
 (A, "mundos", "MERCADO-DE-LLAVES.jpg", "El Mercado de las Llaves", "La casa de Lucho. Aquí se venden llaves (portales) y recuerdos.", "—",
  WORLD("A narrow night bazaar alley where thousands of old keys hang from strings like wind chimes, glowing paper lanterns, wooden stalls full of lost objects, jars filled with glowing turquoise orbs of light, warm and mysterious atmosphere.")),
 (A, "mundos", "PLAZA-MIL-PUERTAS.jpg", "La Plaza de las Mil Puertas", "Todas las puertas a otros mundos.", "—",
  WORLD("A huge circular plaza filled with hundreds of free-standing doors of every style (castle doors, fridge doors, car doors, tiny mouse doors, giant cathedral doors), some slightly open leaking colored light from other worlds, mist on the ground, twilight.")),
 (A, "mundos", "MONTANA-MEDIAS.jpg", "La Montaña de las Medias Sin Par", "Lugar icónico de Extravío.", "—",
  WORLD("A giant mountain range made entirely of single lost socks of every color and pattern, with sock avalanches, a winding path up the slope, clear blue sky.")),
 (A, "mundos", "VALLE-DE-OCTUBRE.jpg", "El Valle de Octubre", "Halloween eterno (especial del 31-oct). Casa de Doña Lechuza y Calabacín.", "—",
  WORLD("A misty valley where it is always Halloween night: rolling hills covered with glowing carved jack-o'-lanterns, crooked bare trees, a giant orange full moon, lost Halloween costumes hanging from branches like flags, a small crooked witch house with warm windows.")),
 (A, "mundos", "TIERRA-RECORDADOS.jpg", "La Tierra de los Recordados", "Día de Muertos (especial del 2-nov): aquí viven los que alguien recuerda.", "—",
  WORLD("A magical night world inspired by Mexican Día de Muertos: bridges made of orange cempasúchil marigold petals floating over a dark river, thousands of floating candles, colorful papel picado strung across the sky, a glowing town of colorful houses, warm orange and purple light.")),
 (B, "mundos", "BOSQUE-PARAGUAS.jpg", "El Bosque de los Paraguas Olvidados", "Paraguas que flotan como medusas.", "—",
  WORLD("A forest where hundreds of open lost umbrellas float slowly in the air like jellyfish, gentle rain, soft gray-blue light, puddles reflecting the colorful umbrellas.")),
 (B, "mundos", "CIUDAD-CONTROL-REMOTO.jpg", "Ciudad Control Remoto", "Rascacielos de controles; los botones cambian el clima.", "—",
  WORLD("A city skyline where every skyscraper is a giant TV remote control standing upright, glowing rubber buttons as windows, giant buttons on the ground, a sky changing between sunny and stormy in different halves.")),
 (B, "mundos", "MUNDO-SIESTA.jpg", "Mundo Siesta", "Siempre domingo, 3 p. m. Si te duermes, te quedas.", "—",
  WORLD("A drowsy world where it is always a warm Sunday 3 p.m.: endless hammocks, giant soft pillows as hills, huge sleeping sunflowers bending down, a lazy golden haze, clocks melting softly and stopped at 3:00.")),
 (B, "mundos", "CIUDAD-ALGORITMO.jpg", "Ciudad Algoritmo", "Los likes son dinero y gravedad. Sátira de influencers.", "—",
  WORLD("A glossy futuristic city with giant glowing heart-shaped like symbols floating in the air, buildings shaped like ring lights, pink and white neon, a stage with a red carpet, and in the distance some buildings slowly floating away into the sky. No readable text, no phones.")),
 (B, "mundos", "MUNDO-AL-REVES.jpg", "El Mundo al Revés", "Los perros son los dueños; Galleta es el jefe.", "—",
  WORLD("A cozy suburban street where everything is built for dogs: giant dog houses as mansions, fire hydrants as fountains, a bone-shaped swimming pool, a park full of dog-sized benches, a giant stick monument in a plaza, sunny day.")),
 (B, "mundos", "TIERRA-ESPANTOS.jpg", "La Tierra de los Espantos", "Leyendas latinas con problemas de vecinos.", "—",
  WORLD("A spooky but charming Latin American village at night: colonial houses with colorful facades, a misty river, a lone bus stop with a flickering lamp, a ghostly white glow near the river, crooked palm trees, a full moon. Funny and spooky, not gory.")),
 (B, "mundos", "DIMENSION-GALLETA.jpg", "La Dimensión Galleta", "Donde viven Galletas de otros universos (pistas de Max).", "—",
  WORLD("A surreal world made of dog things: hills of golden kibble, a river of water from a dog bowl, giant chew toys as trees, a castle shaped like a dog house with a crown, a pink sky with a bone-shaped moon.")),
 (B, "mundos", "PUEBLO-NUBES.jpg", "El Pueblo en las Nubes", "Pueblo cafetero flotante. Guiño a Colombia.", "—",
  WORLD("A colorful Colombian coffee-region village (bright painted balconies, wooden doors in red, blue and yellow) floating on top of big white clouds, coffee plants growing on the cloud edges, very tall wax palm trees rising out of the clouds, warm morning light.")),
 (B, "mundos", "MUNDO-TRUENO.jpg", "El Mundo Trueno", "Truenos y pólvora son criaturas; aquí las orejeras salvan el día.", "—",
  WORLD("A dramatic world of purple storm clouds where small round cloud creatures with glowing eyes float around, lightning bolts frozen in the air like glass sculptures, colorful fireworks blooming far away on the horizon, a rocky plateau with a cozy cave glowing warm inside.")),
 (B, "mundos", "OFICINA-CARTAS.jpg", "La Oficina de Cartas Perdidas", "Cartas a Santa que nunca llegaron; camino al final de temporada.", "—",
  WORLD("A gigantic cathedral-like old post office hall with mountains of lost letters and envelopes reaching the ceiling, brass pneumatic tubes, wooden sorting shelves, warm dusty light rays, a few letters floating in the air.")),
 (C, "mundos", "POLO-NORTE.jpg", "El Polo Norte", "Final de la temporada 1.", "—",
  WORLD("A magical North Pole at night under green and purple aurora borealis: a cozy giant workshop made of wood and ice with warm windows, snowy pine trees with lights, a frozen lake reflecting the aurora.")),
]

VOCES = [
 (A, "Lucho", "Lucho",
  "Studio-quality recording, recorded up close on a professional condenser microphone: clean, crisp, full and present audio, no phone or radio filter, no distortion, no background noise, no echo. A thin middle-aged Latin American man with a naturally hoarse, raspy, gravelly voice who speaks quietly and secretively (a raspy low voice, not a full whisper), slightly short of breath with a soft wheezy inhale between phrases and a quick nervous giggle; paranoid and fast like a street dealer of strange objects; Latin American Spanish.",
  "Psst… gato. ¿Buscas una llave? Tengo de todo. Original… casi. Je, je."),
 (A, "La Gran Polilla", "Polilla",
  "An ancient, elegant female voice, deep and very slow, calm and hypnotic, soft whisper with a light echo as if spoken in a huge empty cathedral, beautiful and menacing at the same time, Latin American Spanish.",
  "Nadie te está buscando, gatito. Quédate. Aquí… nadie recuerda nada."),
 (B, "Guardián de la Siesta", "Siesta",
  "A very slow, very sleepy deep male voice that yawns between words, gentle and soft but slightly creepy, Latin American Spanish.",
  "Shhh… Aquí siempre es domingo. Acuéstate… solo cinco minutos."),
 (B, "Alcaldesa Likes", "Likes",
  "A glamorous young female influencer voice, fake-sweet and over-excited, fast, with forced laughs, Latin American Spanish.",
  "¡Hola, mis amores! ¿Cero seguidores? ¡Ay, qué ternura! Aquí eso es ilegal."),
 (B, "La Llorona", "Llorona",
  "A dramatic female voice that sobs and wails theatrically between words, like a telenovela actress, echoing, Latin American Spanish.",
  "¡Ay, mis hijos! … No, no he perdido a nadie. Lloro porque el Silbón no me deja dormir."),
 (B, "El Silbón", "Silbon",
  "A deep, grumpy, tired old male voice from the Colombian-Venezuelan plains, slow, with long whistles between phrases, Latin American Spanish.",
  "(silbido largo) Vecina… son las tres de la mañana. Deje de llorar."),
 (B, "Doña Mula", "Mula",
  "A warm, sassy middle-aged female voice with a Colombian paisa accent, friendly and quick-witted, Spanish.",
  "¿Usted es el gato famoso? Pues aquí manda el tinto, mijo."),
 (B, "El Cartero Caracol", "Caracol",
  "An extremely slow, calm old male voice, every word stretched, patient and kind, Latin American Spanish.",
  "Su… carta… llegó. Hace… cuarenta… años."),
]

CANCIONES = [
 (A, "TEMA-EXTRAVIO.mp3", "«Extravío» · la canción de la serie (1 min)",
  "Para los shorts y como sonido propio en TikTok e Instagram (si otros la usan, nos hacen publicidad). En los capítulos solo suena la firma de 3 s.",
  "Catchy whimsical Latin indie-pop with a light electronic cumbia beat, music box and marimba melody, warm male vocal with a playful sly tone, a sing-along chorus, mysterious but fun, 1 minute, Spanish lyrics.",
  "[Verso]\nSe me perdió la media, se me perdió el control,\nlas llaves de la casa y hasta el corazón.\nY todo lo que pierdes no se va pa'l olvido:\nse cae, se cae, se cae… ¡a Extravío!\n\n[Coro]\nExtravío, Extravío, donde todo va a parar,\nlo que nadie está buscando no lo vuelves a encontrar.\nExtravío, Extravío, si te pierdes por aquí,\nque alguien te esté buscando… o te quedas aquí."),
 (B, "JINGLE-LUCHO.mp3", "Jingle del Mercado de Lucho (15 s)",
  "Comercial absurdo para el «Zapping de Extravío» y para shorts.",
  "Cheesy fast late-night TV commercial jingle, cheap synth and accordion, raspy whispering male voice that sounds short of breath, funny and suspicious, 15 seconds, Spanish lyrics.",
  "¿Perdiste algo? ¡Lucho lo tiene!\nLlaves, recuerdos y algo que no conviene.\nOriginal… casi. Garantía… ninguna.\n¡Mercado de Lucho! Se paga con queso… o con tu fortuna."),
]
MUSICA = [
 (A, "FIRMA-EXTRAVIO.mp3", "Firma sonora (3 s)", "Suena con el logo, al inicio de cada capítulo.",
  "A 3-second magical sonic logo: a single shimmering music-box melody that falls downward and ends with a soft whoosh and a deep warm bass hit. Mysterious, whimsical, cinematic. No vocals."),
 (A, "FONDO-CIUDAD.mp3", "Fondo de la ciudad de Extravío (1 min)", "Escenas en la ciudad y en el Mercado.",
  "Whimsical mysterious instrumental for a fantasy city made of lost things: music box, pizzicato strings, soft marimba, light percussion, curious and slightly melancholic, loopable, 1 minute. No vocals."),
 (A, "FONDO-MAR-PELOTAS.mp3", "Fondo del Mar de Pelotas (1 min)", "Capítulo 1: la llegada.",
  "Bright playful adventure instrumental, bouncy pizzicato, light ukulele and glockenspiel, sense of wonder and fun, loopable, 1 minute. No vocals."),
 (A, "FONDO-LUCHO.mp3", "Tema de Lucho (45 s)", "Cada vez que Lucho aparece con una mala idea.",
  "Sneaky comedic instrumental: tiptoeing pizzicato bass, muted trumpet, finger snaps, a little nervous and shady, loopable, 45 seconds. No vocals."),
 (A, "FONDO-POLILLA.mp3", "Tema de La Gran Polilla (45 s)", "Cuando aparece la villana.",
  "Dark elegant villain theme: slow choir pads, low cello, a soft harp, hypnotic and menacing, 45 seconds. No lyrics."),
 (A, "FONDO-TENSION.mp3", "Persecución / peligro (45 s)", "Momentos de acción y escapes.",
  "Fast tense adventure chase instrumental, driving strings and percussion, brass hits, playful but urgent, 45 seconds. No vocals."),
 (A, "FONDO-CORAZON.mp3", "Momento de corazón (45 s)", "Rescates y finales emotivos.",
  "Tender emotional instrumental: soft piano and warm strings, a little music box, hopeful and moving, 45 seconds. No vocals."),
 (A, "FONDO-VALLE-OCTUBRE.mp3", "Valle de Octubre (1 min)", "El mundo de Halloween eterno.",
  "Spooky-fun Halloween instrumental: harpsichord, theremin, pizzicato, light bells, mischievous and cozy, loopable, 1 minute. No vocals."),
 (A, "FONDO-RECORDADOS.mp3", "Tierra de los Recordados (1 min)", "El mundo del Día de Muertos.",
  "Warm magical Mexican-inspired instrumental: soft guitarra, marimba, gentle strings, nostalgic and beautiful, loopable, 1 minute. No vocals."),
 (B, "FONDO-SIESTA.mp3", "Mundo Siesta (1 min)", "", "Very slow dreamy lullaby instrumental, soft vibraphone and warm pads, sleepy Sunday afternoon, loopable, 1 minute. No vocals."),
 (B, "FONDO-ALGORITMO.mp3", "Ciudad Algoritmo (1 min)", "", "Glossy upbeat synth-pop instrumental, sparkly and fake-happy like a social media ad, loopable, 1 minute. No vocals."),
 (B, "FONDO-ESPANTOS.mp3", "Tierra de los Espantos (1 min)", "", "Spooky Latin folk instrumental: llanero harp, maracas, ghostly whistles, funny and eerie, loopable, 1 minute. No vocals."),
 (B, "FONDO-NUBES.mp3", "Pueblo en las Nubes (1 min)", "", "Cheerful Colombian-inspired instrumental: tiple and guitar, light percussion, airy and warm, loopable, 1 minute. No vocals."),
 (B, "FONDO-TRUENO.mp3", "Mundo Trueno (1 min)", "", "Epic stormy instrumental with booming taiko drums, low brass and rising strings, dramatic but not scary, 1 minute. No vocals."),
 (B, "FONDO-ZAPPING.mp3", "Zapping de Extravío (30 s)", "", "Retro TV channel-surfing music bed: cheesy 80s synth, short and loopable, 30 seconds. No vocals."),
]
SONIDOS = [
 (A, "SFX-PORTAL.mp3", "Portal que se abre", "An old wooden door unlocking with a magical key turn, then a deep whoosh of wind and a shimmering bright opening portal sound."),
 (A, "SFX-REMOLINO.mp3", "Caída por el Remolino", "Falling down a swirling vortex: rushing wind, spinning objects clattering, distant echoes, building to a soft landing."),
 (A, "SFX-PELOTAS.mp3", "Aterrizaje en el Mar de Pelotas", "Two bodies landing in a huge pool of rubber balls: a loud bouncy crash and hundreds of balls rattling and rolling."),
 (A, "SFX-RECUERDO.mp3", "Aparece un recuerdo", "A soft crystal chime with a gentle glowing hum, like a memory appearing, magical and warm."),
 (A, "SFX-POLILLA.mp3", "Alas de la Polilla", "Giant moth wings flapping slowly: deep soft fluttering whooshes with a faint dusty shimmer."),
 (A, "SFX-LLAVES.mp3", "Llaves del Mercado", "Hundreds of old keys hanging like wind chimes, clinking softly in a breeze."),
 (A, "SFX-RISITA-LUCHO.mp3", "Risita de Lucho", "A small wheezy nervous mouse giggle, quick and squeaky."),
 (A, "SFX-QUESO.mp3", "Lucho huele el queso", "A long deep ecstatic sniff followed by a tiny wheezy happy sigh."),
 (A, "SFX-WHOOSH.mp3", "Transición rápida", "A fast clean cinematic whoosh transition, short and airy."),
 (A, "SFX-GOLPE-COMICO.mp3", "Golpe cómico", "A cartoonish soft thud with a tiny boing at the end."),
 (A, "SFX-ALCANTARILLA.mp3", "La alcantarilla", "A metal storm drain grate rattling, echoing water dripping, and a hollow echo below."),
 (A, "SFX-GALLETA.mp3", "Galleta (sin palabras)", "A happy small dog: two excited short barks, a curious sniff and a soft whine."),
 (B, "SFX-ZAPPING.mp3", "Zapping", "An old CRT TV switching channels: click, burst of static, short buzz."),
 (B, "SFX-TRUENITO.mp3", "Truenito", "A small grumpy thunder rumble, cute but booming, with a crackle."),
 (B, "SFX-BOSTEZO.mp3", "Bostezo del Mundo Siesta", "A huge slow sleepy yawn echoing in a quiet afternoon."),
]

LOGOS = [
 (A, "marca", "LOGO-EXTRAVIO.png", "Logo de la serie", "Para el inicio de cada capítulo (1 s), miniaturas y el canal.",
  "Logo design for an animated fantasy series, transparent-looking plain dark background, 3:2: the word EXTRAVÍO in big hand-crafted letters made of lost objects (a sock, a key, a ball, a remote control, a letter) glowing with turquoise magic light, with a small cream cat nightcap with a pompom hanging from the letter V. Whimsical, cinematic, readable. Only the text EXTRAVÍO."),
 (A, "marca", "BANNER-CANAL.jpg", "Banner del canal de YouTube", "Portada del canal (2560×1440; lo importante en el centro).", "TOFFEE-viajero.jpg · GALLETA-viajero.jpg",
  ),
]
LOGOS[1] = (A, "marca", "BANNER-CANAL.jpg", "Banner del canal de YouTube", "Portada del canal (2560×1440; lo importante en el centro). Adjunta las fotos de Toffee y Galleta.",
  "YouTube channel banner, 16:9, photorealistic cinematic: the cream-caramel British Shorthair cat from the reference (navy knitted nightcap with cream pompom and small black action camera on top) and the scruffy golden-brown dog from the reference (navy bandana with gold bone tag) standing in the center on top of a hill of lost objects, looking at the fantastical city of lost things at dusk with lost objects slowly raining down and turquoise glowing lights. Characters small and centered in the middle third. No text.")

LOGOS += [
 (A, "marca", "AVATAR-CANAL.jpg", "Foto de perfil del canal", "Se ve en círculo y muy pequeña: solo la cara de Toffee, clara y reconocible. Adjunta la foto de Toffee.",
  "Square 1:1 profile picture, photorealistic: close-up of the face of the cream-caramel British Shorthair cat from the reference (chubby, very round face, big green eyes) wearing his navy knitted nightcap with a cream pompom and the small black action camera on top, smug confident expression, looking at the camera, centered so it fits inside a circle, soft turquoise magical glow behind him on a dark amber background. No text."),
 (A, "marca", "FONDO-PANTALLA-FINAL.jpg", "Fondo de los últimos 20 s de cada capítulo", "Escena tranquila donde YouTube pone sus botones de «siguiente video» y «suscribirse». Adjunta Toffee y Galleta.",
  "Photorealistic cinematic wide shot, 16:9: the cream-caramel British Shorthair cat from the reference (navy knitted nightcap with cream pompom and small black action camera on top) and the scruffy golden-brown dog from the reference (navy bandana with gold bone tag) sitting small on the lower center, seen from behind, on a hill of lost objects looking at the glowing city of lost things at night, turquoise lights, lost objects slowly falling like snow. Lots of calm empty sky in the upper and side areas. No text."),
]

def build_img():
    e = html.escape
    def tabla(cab, filas):
        return '<table><tr>' + ''.join(f'<th>{c}</th>' for c in cab) + '</tr>' + ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in f) + '</tr>' for f in filas) + '</table>'
    allimg = PERSONAJES + OBJETOS + MUNDOS
    h = ['<h1>EXTRAVÍO · 1 · todas las imágenes</h1>',
         '<p class="sub">Toffee y Galleta · 29-oct-2026 · Imágenes en Nano Banana Pro · Voces y sonidos en ElevenLabs · La biblia del mundo está en la carpeta toffee/extravio/</p>',
         '<div class="box"><b>Cómo usar este PDF</b><ol>'
         '<li>Empieza por la <b>prioridad A</b> (lo que necesita el capítulo 1). Después la B (mundos de noviembre) y la C (diciembre).</li>'
         '<li>Copia el prompt, adjunta las fotos que dice «Adjuntar» y genera 2–4 opciones. Mándame la mejor de cada una; si algo no cuadra con la descripción, se repite.</li>'
         '<li>Ponle a cada imagen el nombre de archivo que dice la ficha (por ejemplo LUCHO.jpg).</li>'
         '<li><b>Personajes y objetos</b> en 1:1 (hoja 2×2). <b>Mundos</b> en 16:9: son la referencia de cada lugar para Flow.</li>'
         '<li>Las voces, canciones y efectos están en el otro PDF: <b>EXTRAVIO-2-AUDIO.pdf</b>.</li></ol></div>',
         '<h3>El look de Extravío</h3><p>Todo fotorrealista y de cine, como las tomas de Flow que ya hacemos. La ciudad de Extravío: atardecer ámbar con luces mágicas <b>turquesa</b> (el color de los recuerdos). Cada mundo tiene su propia paleta, para que el público sepa en un segundo dónde está. Nada de personajes con dueño. Comedia y misterio, nunca sangre.</p>']
    resumen = [(p, n, f'refs/extravio/{c}/{a}') for (p, c, a, n, *_ ) in allimg] + [(p, n, f'refs/extravio/{c}/{a}') for (p, c, a, n, *_ ) in LOGOS]
    cuenta = {k: sum(1 for r in resumen if r[0] == k) for k in (A, B, C)}
    h.append('<h3>Resumen</h3>' + tabla(['Prioridad', 'Imágenes'], [[k, cuenta[k]] for k in (A, B, C)]) +
             f'<p>Lo que ya existe y se reutiliza: TOFFEE-viajero.jpg, GALLETA-viajero.jpg, LECHUZA, CALABACÍN, CHUPACABRAS, ALEBRIJE, PACA, CHIHUAHUA Pendiente de antes: el Conde Murciélago con el medallón liso.</p>')
    h.append('<h3>Lista de archivos</h3>' + tabla(['Prioridad', 'Qué', 'Guardar como'], [[e(p), e(n), f'<code>{e(r)}</code>'] for p, n, r in sorted(resumen, key=lambda x: x[0])]))
    def bloque(titulo, items):
        h.append(f'<h2>{titulo}</h2>')
        for p, c, a, n, para, fotos, pr in items:
            h.append(f'<div class="toma"><div class="meta">{e(n)} · <span class="chip">{e(p)}</span></div>'
                     f'<div><b>Guardar como:</b> <code>refs/extravio/{c}/{e(a)}</code> · <b>Adjuntar:</b> {e(fotos)}</div>'
                     f'<div class="voz">{e(para)}</div><pre>{e(pr)}</pre></div>')
    bloque('1 · Personajes', PERSONAJES)
    bloque('2 · Objetos mágicos', OBJETOS)
    bloque('3 · Mundos (16:9)', MUNDOS)
    bloque('4 · Logo y canal', [(p, c, a, n, para, '—' if i == 0 else 'TOFFEE-viajero.jpg · GALLETA-viajero.jpg', pr) for i, (p, c, a, n, para, pr) in enumerate(LOGOS)])
    return '<!doctype html><html><head><meta charset="utf-8"><style>' + CSS + 'code{font-size:8.3pt}</style></head><body>' + '\n'.join(h) + '</body></html>'

def build_audio():
    e = html.escape
    def tabla(cab, filas):
        return '<table><tr>' + ''.join(f'<th>{c}</th>' for c in cab) + '</tr>' + ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in f) + '</tr>' for f in filas) + '</table>'
    h = ['<h1>EXTRAVÍO · 2 · voces, canciones, música y efectos</h1>',
         '<p class="sub">Toffee y Galleta · 29-oct-2026 · Todo en ElevenLabs · Guarda cada archivo con el nombre que dice la ficha y mándamelos.</p>',
         '<div class="box"><b>Cómo usar este PDF</b><ol>'
         '<li><b>Voces</b> → ElevenLabs › Voices › Voice Design: pega la descripción, prueba con la frase de prueba, genera varias y guarda la mejor con el nombre indicado. Estabilidad 30–45 % para que actúen.</li>'
         '<li><b>Canciones y música</b> → Eleven Music: pega el estilo (y la letra si tiene). Duración la que dice la ficha.</li>'
         '<li><b>Efectos</b> → Sound Effects: pega la descripción; genera 2–3 y quédate con el mejor.</li>'
         '<li>Empieza por la <b>prioridad A</b>. Las voces que ya existen (Toffee, Lechuza, Calabacín, Murciélago) se siguen usando.</li>'
         '<li>En los capítulos no hay texto en pantalla: la música y los efectos hacen el trabajo. Por eso piden tanto sonido.</li></ol></div>']
    cnt = lambda L, k: sum(1 for x in L if x[0] == k)
    h.append('<h3>Resumen</h3>' + tabla(['Prioridad', 'Voces', 'Canciones', 'Música de fondo', 'Efectos'],
             [[k, cnt(VOCES, k), cnt(CANCIONES, k), cnt(MUSICA, k), cnt(SONIDOS, k)] for k in (A, B)]))
    h.append('<h2>1 · Voces (Voice Design)</h2>')
    for p, n, nombre, d, prueba in VOCES:
        h.append(f'<div class="toma"><div class="meta">{e(n)} · <span class="chip">{e(p)}</span> · guardar como «{e(nombre)}»</div><pre>{e(d)}</pre><div class="voz"><b>Frase de prueba:</b> {e(prueba)}</div></div>')
    h.append('<h2>2 · Canciones (Eleven Music)</h2><p>Con letra. Para que la canción sea tuya y se pueda usar en videos que ganan dinero, revisa que tu plan de ElevenLabs incluya uso comercial.</p>')
    for p, a, n, para, estilo, letra in CANCIONES:
        h.append(f'<div class="toma"><div class="meta">{e(n)} · <span class="chip">{e(p)}</span> · <code>{e(a)}</code></div><div class="voz">{e(para)}</div><h4>Estilo</h4><pre>{e(estilo)}</pre><h4>Letra</h4><pre>{e(letra)}</pre></div>')
    h.append('<h2>3 · Música de fondo (Eleven Music, sin voz)</h2>')
    for p, a, n, para, pr in MUSICA:
        h.append(f'<div class="toma"><div class="meta">{e(n)} · <span class="chip">{e(p)}</span> · <code>{e(a)}</code></div>' + (f'<div class="voz">{e(para)}</div>' if para else '') + f'<pre>{e(pr)}</pre></div>')
    h.append('<h2>4 · Efectos de sonido (Sound Effects)</h2>')
    for p, a, n, pr in SONIDOS:
        h.append(f'<div class="toma"><div class="meta">{e(n)} · <span class="chip">{e(p)}</span> · <code>{e(a)}</code></div><pre>{e(pr)}</pre></div>')
    return '<!doctype html><html><head><meta charset="utf-8"><style>' + CSS + 'code{font-size:8.3pt}</style></head><body>' + '\n'.join(h) + '</body></html>'

if __name__ == '__main__':
    js = open(os.path.join(here, '..', 'viaje', 'temporada1', 'pdf.js')).read()
    for nombre, fn, pie in (('EXTRAVIO-1-IMAGENES.pdf', build_img, 'Extravío · 1 · imágenes'), ('EXTRAVIO-2-AUDIO.pdf', build_audio, 'Extravío · 2 · audio')):
        open(os.path.join(here, 'plan.html'), 'w').write(fn())
        open(os.path.join(here, 'pdf.js'), 'w').write(js.replace('Soy Toffee · El viaje de Toffee · Sección 1', pie))
        out = os.path.abspath(os.path.join(here, '..', nombre))
        subprocess.run(['node', os.path.join(here, 'pdf.js'), out], cwd=here, check=True)
        print('ok', out)
    os.remove(os.path.join(here, 'pdf.js')); os.remove(os.path.join(here, 'plan.html'))

def web():
    """Las mismas fichas como páginas web (Artifact) con botón Copiar: Jay pidió links en vez de PDF (29-oct-2026)."""
    src = open(os.path.join(here, '..', 'viaje', 'temporada1', 'build_web.py')).read()
    head = src[src.index("head = '''") + 10: src.index("'''", src.index("head = '''") + 10)]
    script = src[src.index("<script>"): src.index("</script>") + 9]
    os.makedirs(os.path.join(here, 'web'), exist_ok=True)
    for nombre, titulo, fn in (('extravio-imagenes.html', 'Extravío · imágenes', build_img), ('extravio-audio.html', 'Extravío · audio', build_audio)):
        body = fn().split('<body>', 1)[1].rsplit('</body>', 1)[0]
        body = body.replace('<table>', '<div class="tabla"><table>').replace('</table>', '</table></div>')
        page = head.replace('<title>El viaje de Toffee</title>', f'<title>{titulo}</title>') + '<main>' + body + '</main>\n' + script
        open(os.path.join(here, 'web', nombre), 'w').write(page)

if __name__ == '__main__':
    web()
