# Toffee y Galleta · Temporada 1 · Capítulo 1 (escrito desde cero el 28-oct-2026)
# Genera web/capitulo-01.html (Artifact) y CAPITULO-01.md. Todo en Omni 1.1 Flash (Google Flow), 16:9 horizontal (capítulo de YouTube); las tomas marcadas se generan también en 9:16 para los shorts.
import os, sys, html, re
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(here, '..', 'temporada1'))
from datos import ST, T, G, TR, LE, CA, END, VL
from datos_v2 import TU, VT_, GX, FICHAS_NUEVAS, VOCES_NUEVAS

# Capítulo de YouTube = horizontal 16:9. El personaje principal cerca del centro, para poder recortar shorts verticales.
ST = lambda s: (f"Horizontal 16:9 widescreen, {s} seconds. Photorealistic video, normal lens "
                "(no fisheye, no vignette, no dark corners), sharp, natural colors, realistic physics. One continuous shot with no cuts. "
                "Keep the main character near the center of the frame.")
VERT = lambda p: p.replace("Horizontal 16:9 widescreen", "Vertical 9:16").replace(" Keep the main character near the center of the frame.", "")
# Tomas con dos personajes o planos abiertos que no se pueden recortar a vertical: se generan también en 9:16 para los shorts.
VERTICALES = {12, 17, 18, 19, 20, 24, 32, 34}

BALL = "a small yellow rubber squeaky ball"
BELLS = "three big shiny golden jingle bells tied together on a red string"
C2 = "one cat and one dog"
VTO = "in a deep, slow, sleepy male voice"

def HT(line, voice=VTO, verb="says"):
    return f'The cat {verb} in Latin American Spanish, {voice}: "{line}" His lips move in sync with every word.'
def HL(line, verb="says"):
    return f'The owl {verb} in Latin American Spanish, {VL}: "{line}" Her beak moves in sync with every word.'
def HR(line, verb="says"):
    return f'The raccoon {verb} in Latin American Spanish, {VT_}: "{line}" His mouth moves in sync with every word.'

F = dict(T="TOFFEE-viajero.jpg", G="GALLETA-viajero.jpg", S="REF-trineo-rojo.jpg", L="LECHUZA.jpg", R="TURBIO.jpg", C="CALABACIN.jpg")

ESC = []   # escenas: (título, función, [tomas])
def esc(t, f): ESC.append(dict(t=t, f=f, tomas=[]))
N = [0]
def tk(s, fotos, p, voz=None, quien=None, cont=None, gancho=False, nota=None):
    N[0] += 1
    ESC[-1]['tomas'].append(dict(v=N[0] in VERTICALES, n=N[0], s=s, fotos=[F[x] for x in fotos], p=p, voz=voz, quien=quien, cont=cont, gancho=gancho, nota=nota))

ROOM = "Cozy bedroom at night, warm Christmas lights on the wall, a window with the city lights outside."
LIVING = "Cozy living room at night with warm Christmas lights, a gray sofa and a big window behind."

# ---------------- ESCENA 1 · El plan ----------------
esc("El plan de Toffee", "INICIO · qué quiere Toffee")
tk(6, "T", f"{ST(6)} {ROOM} Medium close-up at eye level of {T}, sitting on a bed and looking straight into the lens with a proud, dramatic face. {HT('A ver, mis desgraciados… hoy me voy al Polo Norte.')} {END('one cat', 'the cat', 'quiet room')}",
   voz="[sarcastic, dramatic] A ver, mis desgraciados… [proud] hoy me voy al Polo Norte.", quien="TOFFEE (a cámara)")
tk(8, "T", f"{ST(8)} {ROOM} Same framing: {T} sits on the bed, looking into the lens, serious and noble, one ear slightly back. {HT('Santa nunca les trae regalos a los animales de la calle. Voy a pedírselo en persona.')} {END('one cat', 'the cat', 'quiet room')}",
   voz="[serious] Santa nunca les trae regalos a los animales de la calle. [determined] Voy a pedírselo en persona.", quien="TOFFEE (a cámara)", cont="Usar el último cuadro de la toma 1 como primer cuadro.")
tk(6, "T", f"{ST(6)} {ROOM} {T} slowly leans very close to the lens, narrows his eyes and speaks in a low secret voice, like telling a secret. {HT('Y si de paso me vuelvo el gato más famoso del mundo… pues ni modo.', verb='whispers')} {END('one cat', 'the cat', 'quiet room')}",
   voz="[whispers, sly] Y si de paso me vuelvo el gato más famoso del mundo… [smug] pues ni modo.", quien="TOFFEE (secreto, a cámara)", cont="Usar el último cuadro de la toma 2 como primer cuadro.")
tk(6, "G", f"{ST(6)} {ROOM} Low camera on the carpet. {G} lies on the carpet happily chewing {BALL}; he squeaks it twice, then looks up at the camera and tilts his head. {END('one dog', None, 'squeaky toy sounds')}",
   voz="[amused] Él es Galleta. Viene conmigo. … Todavía no lo sabe.", quien="TOFFEE (voz en off)")
tk(8, "TS", f"{ST(8)} {LIVING} Medium-wide shot at eye level: {TR} on the carpet. {T} climbs into the sleigh bed, sits proudly at the front like a captain and looks at the camera. {END('one cat', None, 'quiet room')}",
   voz="[proud] Nuestro vehículo: mi trineo. [embarrassed] Bueno… es mi cama. Pero tiene forma de trineo.", quien="TOFFEE (voz en off)")

# ---------------- ESCENA 2 · Plan A ----------------
esc("Plan A: fracasa", "DESARROLLO · el primer intento")
tk(6, "TGS", f"{ST(6)} {LIVING} Side view: {TR} sits on the edge of the gray sofa seat with {T} inside, leaning forward like a racer. The sleigh bed slowly slides off the sofa and lands flat on the soft carpet with a gentle thump; the cat stays inside, unhurt, with a flat annoyed face. On the right, {G} watches from the carpet. {END(C2, None, 'soft thump')}",
   voz=None, quien="(sin voz: el golpe suave y la cara de Toffee)")
tk(4, "TS", f"{ST(4)} {LIVING} Close-up of {T} lying inside {TR} on the carpet, face flat, staring at the ceiling, completely unimpressed. {END('one cat', None, 'quiet room')}",
   voz="[flat, deadpan] Plan A: fracasó.", quien="TOFFEE (voz en off)")

# ---------------- ESCENA 3 · Don Turbio ----------------
esc("Aparece Don Turbio", "OBSTÁCULO · la tentación")
tk(6, "R", f"{ST(6)} Night, outside view of a living room window with warm Christmas lights inside. {TU} slowly rises into view behind the glass from below, taps the glass twice and opens one side of his trench coat, showing small strange gadgets hanging inside. {HR('Psst… gato.', verb='whispers')} {END('one raccoon', 'the raccoon', 'quiet night')}",
   voz=None, quien="DON TURBIO: «Psst… gato.»")
tk(8, "R", f"{ST(8)} Night, close-up of {TU} at the open window, holding up {BELLS} and shaking them so they jingle. {HR('Cascabeles de reno. Originales. Casi. Hacen volar cualquier cosa.')} {END('one raccoon', 'the raccoon', 'jingle bells')}",
   voz=None, quien="DON TURBIO: «Cascabeles de reno. Originales. Casi. Hacen volar cualquier cosa.»")
tk(6, "T", f"{ST(6)} {LIVING} Close-up of {T} sitting on the windowsill inside, squinting suspiciously toward the window. {HT('¿Y cuánto cuestan?')} {END('one cat', 'the cat', 'quiet room')}",
   voz="[suspicious] ¿Y cuánto cuestan?", quien="TOFFEE (a cámara)")
tk(6, "RG", f"{ST(6)} Night, view from outside through the open window: on the left, {TU} leans in and points with one finger at {BALL} lying on the carpet inside; on the right, {G} lies next to the ball. {HR('Esa pelotita.')} {END('one raccoon and one dog', 'the raccoon', 'quiet night')}",
   voz=None, quien="DON TURBIO: «Esa pelotita.»")
tk(6, "TG", f"{ST(6)} {LIVING} Low camera on the carpet. On the left, {T} pushes {BALL} away with one paw toward the window, without looking at the dog. On the right, {G} {GX['suplica']}. {END(C2, None, 'quiet room')}",
   voz="[avoiding eye contact] Es por una buena causa.", quien="TOFFEE (voz en off)")
tk(6, "R", f"{ST(6)} Night, outside the window: {TU} grabs {BALL} and hands over {BELLS} through the window, then steps back into the darkness and disappears. {HR('Garantía: ninguna.')} {END('one raccoon', 'the raccoon', 'quiet night')}",
   voz=None, quien="DON TURBIO: «Garantía: ninguna.»")

# ---------------- ESCENA 4 · Despegue ----------------
esc("¡Funciona!", "DESARROLLO · el plan parece salir bien")
tk(8, "TGS", f"{ST(8)} {LIVING} {TR} on the carpet. {T} ties {BELLS} to the front tip of the sleigh bed with his paws. {G} sits at the back of the sleigh bed and {GX['desastre']} — staring at the jingling golden bells. {END(C2, None, 'jingle bells')}",
   voz=None, quien="(sin voz: solo cascabeles; Galleta mira los cascabeles)")
tk(6, "TGS", f"{ST(6)} {LIVING} The sleigh bed with {BELLS} at the front begins to glow with a soft golden light and slowly lifts a few centimeters off the carpet, floating. {T} sits at the front with huge surprised eyes; {G} at the back. {HT('Funciona…', verb='whispers')} {END(C2, 'the cat', 'magical shimmer and jingle bells')}",
   voz="[whispers, amazed] Funciona…", quien="TOFFEE (a cámara)", cont="Usar el último cuadro de la toma 14 como primer cuadro.")
tk(8, "TGS", f"{ST(8)} {LIVING} The glowing floating sleigh bed with {T} at the front and {G} at the back flies smoothly out through the big open window into the night sky. {HT('¡Polo Norte, allá vamos!', voice='in a loud, excited male voice', verb='shouts')} {END(C2, 'the cat', 'wind and jingle bells')}",
   voz="[shouting, excited] ¡Polo Norte, allá vamos!", quien="TOFFEE", cont="Usar el último cuadro de la toma 15 como primer cuadro.")

# ---------------- ESCENA 5 · Vuelo y desastre ----------------
esc("El vuelo… y Galleta", "COMPLICACIÓN · Galleta lo empeora todo")
tk(8, "TGS", f"{ST(8)} Night sky over a big city full of lights. Side view from a few meters away, same height: {TR} flies smoothly with a soft golden glow, {BELLS} jingling at the front; {T} sits at the front proudly, {G} at the back with his ears flapping in the wind. Snowflakes fall. {END(C2, None, 'wind and jingle bells')}",
   voz="[proud, epic] Mírenme, humanos. … Esto es historia.", quien="TOFFEE (voz en off)", nota="Toma de «wow»: buena para miniatura y shorts.")
tk(6, "TGS", f"{ST(6)} Night sky, close shot inside the flying sleigh bed. On the left, {T} turns his head back toward the dog with a warning look; on the right, {G} leans slowly forward with his eyes fixed on the jingling golden bells at the front. {HT('Galleta. No. Ni lo pienses.')} {END(C2, 'the cat', 'wind and jingle bells')}",
   voz="[warning, slow] Galleta. No. [firm] Ni lo pienses.", quien="TOFFEE (a cámara)")
tk(6, "TGS", f"{ST(6)} Night sky, close shot of the front of the flying sleigh bed: {G} bites the red string of {BELLS} and pulls playfully; the string snaps and the three golden bells fall away into the dark night below. {T} at the front stares with his mouth open. {END(C2, None, 'wind, a snap, bells falling away')}",
   voz=None, quien="(sin voz: el «snap» y los cascabeles que caen)")
tk(8, "TGS", f"{ST(8)} Night sky above a dark snowy pine forest. Side view: {TR}, without bells and without glow, falls from the sky toward the snowy forest, tilting; {T} at the front holds on with wide eyes and shouts; {G} at the back holds on. {HT('¡¡GALLETAAA!!', voice='in a loud, terrified male voice', verb='screams')} {END(C2, 'the cat', 'wind rushing')}",
   voz="[screaming, terrified] ¡¡GALLETAAA!!", quien="TOFFEE", gancho=True, nota="GANCHO: los primeros 4–5 s de esta toma abren el capítulo.")

# ---------------- ESCENA 6 · Choque y rescate ----------------
esc("El choque y el rescate", "CORAZÓN · Toffee sí quiere a Galleta (aunque lo niegue)")
tk(6, "TS", f"{ST(6)} Dark snowy pine forest at night, wide shot: {TR} lands softly into a deep pile of fresh powder snow, and a big cloud of snow bursts up and slowly falls. Nobody is hurt; nobody is visible in the snow for a moment. No animals are visible in this shot. Only a soft whump and wind. No phone, no selfie stick, no text, no music.",
   voz=None, quien="(sin voz)", nota="En esta toma no se ve a ningún animal: solo el trineo hundido en la nieve.")
tk(6, "T", f"{ST(6)} Dark snowy forest at night, low camera. {T} pops his head out of the deep snow, shakes the snow off his nightcap and camera, and looks around worried. {HT('¿Galleta?', voice='in a worried male voice', verb='calls')} {END('one cat', 'the cat', 'wind')}",
   voz="[worried, quiet] ¿Galleta?", quien="TOFFEE (a cámara)")
tk(6, "T", f"{ST(6)} Dark snowy forest at night. {T} digs fast in the snow with both front paws, snow flying behind him, very worried, looking for someone. {HT('¡GALLETA!', voice='in a loud, desperate male voice', verb='shouts')} {END('one cat', 'the cat', 'wind and digging')}",
   voz="[shouting, desperate] ¡GALLETA!", quien="TOFFEE", cont="Usar el último cuadro de la toma 22 como primer cuadro.")
tk(6, "TG", f"{ST(6)} Dark snowy forest at night. On the right, {G} pops his head out of the snow in front of the cat, happy and unhurt, and licks the cat's face once. On the left, {T} freezes with a disgusted face. {END(C2, None, 'wind')}",
   voz=None, quien="(sin voz: el lengüetazo)", cont="Usar el último cuadro de la toma 23 como primer cuadro.")
tk(6, "T", f"{ST(6)} Dark snowy forest at night. Close-up of {T} with snow on his face, looking into the lens, annoyed and embarrassed. {HT('Asco. Esto no pasó. Y no lo estaba buscando.')} {END('one cat', 'the cat', 'wind')}",
   voz="[annoyed, embarrassed] Asco. … Esto no pasó. [defensive] Y no lo estaba buscando.", quien="TOFFEE (a cámara)")

# ---------------- ESCENA 7 · La lechuza ----------------
esc("Doña Lechuza", "OBSTÁCULO · la misión de verdad")
tk(6, "TG", f"{ST(6)} Dark snowy forest at night. In the darkness between the trees in the background, two big round glowing golden eyes appear and blink. In the foreground, {G} {GX['escondite']}, and {T} stares at the eyes. {END(C2, None, 'wind and a soft hoot')}",
   voz=None, quien="(sin voz: los ojos en la oscuridad)")
tk(6, "L", f"{ST(6)} Snowy forest at night. {LE} lands on a snowy branch close to the camera, wings folding like a real owl, and sets her lantern on the branch. {HL('¡Por fin! Llevo tres siglos esperando visitas.')} {END('one owl', 'the owl', 'wind')}",
   voz=None, quien="DOÑA LECHUZA: «¡Por fin! Llevo tres siglos esperando visitas.»")
tk(8, "L", f"{ST(8)} Snowy forest at night. Close-up of {LE} on the branch, wings folded, lantern beside her, looking into the lens over her tiny glasses. {HL('Vi caer sus cascabeles. No eran de reno. Eran del Valle de Octubre, donde siempre es Halloween.')} {END('one owl', 'the owl', 'wind')}",
   voz=None, quien="DOÑA LECHUZA: «Vi caer sus cascabeles. No eran de reno. Eran del Valle de Octubre, donde siempre es Halloween.»", cont="Usar el último cuadro de la toma 27 como primer cuadro.")
tk(8, "L", f"{ST(8)} Snowy forest at night. {LE} leans toward the camera, golden eyes wide, and lowers her voice. {HL('Sin sus tres cascabeles, ese trineo no vuela. Y cada uno lo guarda un monstruo.', verb='whispers')} {END('one owl', 'the owl', 'wind')}",
   voz=None, quien="DOÑA LECHUZA (susurro): «Sin sus tres cascabeles, ese trineo no vuela. Y cada uno lo guarda un monstruo.»", cont="Usar el último cuadro de la toma 28 como primer cuadro.")
tk(6, "TG", f"{ST(6)} Snowy forest at night. Extreme close-up of {T}, eyes huge, ears back, mouth wide open, shouting in panic; {G} peeks from behind him on the right. {HT('¡¿MONSTRUOS?!', voice='in a loud, high, panicked male voice', verb='shouts')} {END(C2, 'the cat', 'wind')}",
   voz="[shouting, terrified] ¡¡¿¿MONSTRUOS??!!", quien="TOFFEE")
tk(8, "TG", f"{ST(8)} Snowy forest at night. On the left, {T} sits up straight, pretending to be calm, and talks to the camera. On the right, {G} lies flat on the snow covering his eyes with both front paws, shaking slightly with fear (realistic, no drawn lines or cartoon effects). {HT('Yo no tengo miedo. Estoy evaluando la situación.')} {END(C2, 'the cat', 'wind')}",
   voz="[trying to sound brave] Yo no tengo miedo. [whispers] Estoy evaluando la situación.", quien="TOFFEE (a cámara)", cont="Usar el último cuadro de la toma 30 como primer cuadro.")

# ---------------- ESCENA 8 · Recompensa ----------------
esc("Galleta encuentra el camino", "RECOMPENSA · el desastre de Galleta salva el día")
tk(6, "GL", f"{ST(6)} Snowy forest at night. On the left, {LE} stands on the snow and has put her lit lantern down in front of her. On the right, {G}, curious, walks up, sniffs the lantern and bumps it with his nose; the lantern tips over and rolls down a gentle snowy slope, still glowing. {END('one owl and one dog', None, 'wind and a soft clink')}",
   voz=None, quien="(sin voz)")
tk(8, "", f"{ST(8)} Snowy forest at night, wide shot along a winding path: a small glowing old lantern rolls down the path, and as it passes, a long line of carved jack-o'-lantern pumpkins along both sides lights up one by one with warm orange light, deep into the dark forest. No animals appear in this shot. Only a soft magical whoosh as each pumpkin lights. No phone, no selfie stick, no text, no music.",
   voz=None, quien="(sin voz: momento «wow»)", nota="Toma de «wow»: buena para shorts.")
tk(6, "TG", f"{ST(6)} Snowy forest at night, view from behind: on the left {T}, on the right {G}, sitting side by side looking down a long path lit by glowing jack-o'-lantern pumpkins. The dog wags his tail. {END(C2, None, 'wind')}",
   voz="[unimpressed] Galleta encontró el camino. [scoffs] Fue suerte. [smug] Yo lo tenía calculado.", quien="TOFFEE (voz en off)")

# ---------------- ESCENA 9 · Remate y misterio ----------------
esc("Remate y misterio", "CONTINUACIÓN · lo que deja ganas del capítulo 2")
tk(6, "C", f"{ST(6)} Snowy forest at night. At the end of a path of glowing jack-o'-lantern pumpkins, {CA} sits in the dark, trembling nervously and making a tiny scared whimper; his candle light flickers. {END('one pumpkin', None, 'wind and a tiny whimper')}",
   voz="[mysterious, low] ¿Qué monstruo creen que tiene el primer cascabel? [cheeky] Los leo.", quien="TOFFEE (voz en off)")
tk(6, "R", f"{ST(6)} Snowy forest at night. Behind a big pine tree, {TU} peeks out, holding {BALL}; he squeezes it once (squeak), smiles slyly and steps back into the darkness. {END('one raccoon', None, 'wind and one squeak')}",
   voz=None, quien="(sin voz: el «squeak» de la pelota)", nota="Última toma, antes de «Sígueme…». Misterio: ¿qué hace Don Turbio aquí?")

# ---------------- Textos ----------------
TITULO = "Compré cascabeles MÁGICOS… y mi perro nos tumbó del cielo 🛷"
TITULOS_ALT = ["Le vendí la pelota de mi perro a un mapache (y nos estrellamos) 🦝",
               "Me fui al Polo Norte en mi cama… y terminamos en el Valle de los Monstruos 🎃"]
ARRIBA = ("Compré cascabeles", "MÁGICOS 🔔")
MINIATURA = ("YouTube thumbnail, 16:9, photorealistic, cinematic, high contrast: night sky over a snowy pine forest; "
             "the red plush sleigh-shaped pet bed from the reference falling diagonally; in it, the cream-caramel British Shorthair cat "
             "from the reference (navy knitted nightcap with cream pompom and small black action camera on top) screaming with a huge open mouth and huge eyes, "
             "and the scruffy golden-brown dog from the reference behind him holding a golden jingle bell in his mouth with a guilty innocent face. "
             "Big full moon behind them, falling snow. Characters large, filling the right two thirds. No text, no logos.")
TEXTO_MINI = "Texto que pongo yo encima: «¡GALLETA!» en caramelo con borde oscuro, a la izquierda."
DESC = ("Toffee se va al Polo Norte a pedirle a Santa regalos para los animales de la calle… y de paso hacerse famoso. "
        "El problema: su trineo es su cama, compró cascabeles «originales, casi» a un mapache, y Galleta tenía hambre de cascabeles. 🛷🔔\n\n"
        "¿Qué monstruo creen que tiene el primer cascabel? Los leo 👇\n\n"
        "Toffee y Galleta · Temporada 1: Rumbo al Polo Norte · Capítulo 1\n"
        "Personajes y videos hechos con inteligencia artificial; historia, voces y edición propias.\n"
        "#ToffeeyGalleta #gatos #perros #Navidad")
COMENTARIO_FIJADO = "📝 La lista de Toffee empieza hoy: escribe el nombre de un animalito de la calle que merezca un regalo. Los leo todos."

SHORTS = [
 ("Gancho", "Tomas 18–21 + 20", "¿Qué pasa si tu perro se come los cascabeles mágicos? 🔔", "Empieza en la mirada de Galleta a los cascabeles; termina en el «¡¡GALLETAAA!!» y el choque."),
 ("Personaje (Toffee)", "Tomas 10–13", "Cuando tu amigo vende tus cosas «por una buena causa» 🦝", "La cara de súplica de Galleta es el remate."),
 ("Remate", "Tomas 32–34", "Ese amigo que siempre dice «yo lo tenía calculado» 🙄", "Para etiquetar a alguien."),
 ("Corazón", "Tomas 22–25", "Dice que no lo quiere… 🐶❄️", "El «Asco. Esto no pasó.» cierra."),
 ("Wow", "Tomas 17 + 33", "Volando en mi cama sobre la ciudad 🛷✨", "Sin diálogo largo; con el coro de «La Noche del Miau» si encaja."),
 ("Misterio", "Toma 36", "¿Quién es este mapache? 🦝", "Pregunta para comentarios; sirve también para Stories."),
]
ENCUESTA = "Stories: «¿Toffee debió confiar en Don Turbio?» Sí / No"

# ---------------- Salidas ----------------
def todas(): return [t for e in ESC for t in e['tomas']]
def voces_toffee():
    return "\n\n".join(t['voz'] for t in todas() if t['voz'])

def md():
    o = [f"# Toffee y Galleta · Capítulo 1: {TITULO}", ""]
    for e in ESC:
        o.append(f"## {e['t']} · {e['f']}")
        for t in e['tomas']:
            o.append(f"### Toma {t['n']} · {t['s']} s{' · GANCHO' if t['gancho'] else ''}")
            o.append("Fotos: " + (" · ".join(t['fotos']) or "ninguna"))
            if t['cont']: o.append(t['cont'])
            o.append(f"Voz: {t['quien']}" + (f" — {t['voz']}" if t['voz'] else ""))
            o.append("```\n" + t['p'] + "\n```")
            if t['v']: o.append("También en 9:16 para shorts:\n```\n" + VERT(t['p']) + "\n```")
    return "\n".join(o)

def page():
    e_ = html.escape
    tot = sum(t['s'] for t in todas())
    h = [f'<h1>Capítulo 1 · {e_(TITULO)}</h1><p class="sub">Toffee y Galleta · Temporada 1: Rumbo al Polo Norte · {len(todas())} tomas ({tot//60}:{tot%60:02d} sin recortar) · Omni 1.1 Flash · <b>16:9 horizontal</b> (+ 8 tomas también en 9:16 para shorts) · escrito desde cero el 28-oct-2026</p>']
    h.append('<h2>La historia en 30 segundos</h2><div class="box">'
             '<p><b>Qué quiere Toffee:</b> ir al Polo Norte a pedirle a Santa regalos para los animales de la calle… y, en secreto, hacerse famoso.</p>'
             '<p><b>Qué se lo impide:</b> su trineo es su cama y no vuela. Para hacerlo volar le compra cascabeles «originales, casi» a Don Turbio… pagando con la pelota de Galleta. En pleno vuelo, Galleta (que se quedó sin juguete) muerde los cascabeles y se estrellan.</p>'
             '<p><b>Qué cambia al final:</b> están atrapados en el Valle de Octubre, donde siempre es Halloween. Tienen una guía (Doña Lechuza), una misión (3 cascabeles, cada uno con un monstruo) y un misterio: Don Turbio los está siguiendo… con la pelota de Galleta.</p>'
             '<p><b>Corazón:</b> Toffee escarba la nieve desesperado buscando a Galleta y después lo niega («Esto no pasó»).</p></div>')
    h.append('<h2>Por qué está escrito así</h2><ul>'
             '<li><b>Gancho en el segundo 0:</b> el trineo cayendo y el grito «¡¡GALLETAAA!!» (toma 20), después «A ver, mis desgraciados…».</li>'
             '<li><b>Una cosa pasa por culpa de la otra:</b> la cama no vuela → Don Turbio → Toffee paga con la pelota de Galleta → Galleta, sin juguete, muerde los cascabeles → choque → los cascabeles vuelven al valle → la misión.</li>'
             '<li><b>Se entiende solo (80/20):</b> quien no vio nada antes entiende todo. Queda un 20 % de continuidad: los 3 cascabeles y Don Turbio.</li>'
             '<li><b>El trío de Desencanto:</b> Toffee (orgulloso), Galleta (inocente) y Don Turbio (el provocador que causa el caos).</li>'
             '<li><b>Momentos para compartir:</b> «Es por una buena causa», el rescate en la nieve y «Yo lo tenía calculado».</li>'
             '<li><b>Una sola grosería</b> («desgraciados», el saludo). Ningún día ni fecha al final: «Sígueme para no perderte el próximo episodio».</li>'
             '<li><b>Formato:</b> el capítulo va en <b>16:9 horizontal</b> (se ve completo en TV, computador y celular girado). En Flow elige el formato 16:9 antes de generar. Las tomas de un solo personaje las recorto a vertical para los shorts; las 8 tomas con dos personajes o planos abiertos (12, 17, 18, 19, 20, 24, 32 y 34) se generan también en 9:16.</li>'
             '<li><b>Producto dentro de la historia:</b> la cama-trineo roja es el vehículo de toda la temporada.</li></ul>')
    h.append('<h2>Antes de generar (en este orden)</h2><ol>'
             '<li><b>Ficha de Don Turbio</b> en Nano Banana Pro (prompt abajo) → guárdala como TURBIO.jpg.</li>'
             '<li><b>Voz de Don Turbio</b> en ElevenLabs → Voice Design (abajo) → guárdala como «Turbio».</li>'
             '<li><b>Voces primero:</b> genera el texto completo de Toffee (2–3 versiones, estabilidad 35–45 %), las frases de Doña Lechuza (voz «Lechuza») y las de Don Turbio. Mándamelas.</li>'
             '<li><b>Prueba de 3 tomas:</b> en Flow pon el formato <b>16:9</b> y genera primero las tomas 1, 20 y 27. Si salen bien, sigues con el resto. Al final, las 8 versiones verticales (9:16) para los shorts.</li>'
             '<li>Me mandas las tomas; yo respondo «✓» hasta que digas «listo».</li></ol>')
    nm, foto, desc, pr = FICHAS_NUEVAS[0]
    h.append(f'<h3>Ficha de {e_(nm)} · {foto}</h3><p>{e_(desc)}</p><pre>{e_(pr)}</pre>')
    h.append(f'<h3>Voz de Don Turbio</h3><p>{e_(VOCES_NUEVAS[0][1])}</p>')
    h.append('<h2>Voces</h2><h3>Toffee · un solo texto (ElevenLabs, voz de Toffee)</h3>'
             '<p class="sub">Estabilidad 35–45 %, similitud 85 %, Español. Respeta los renglones en blanco: ahí corto. Si lee las etiquetas en voz alta, bórralas y deja los signos.</p>'
             f'<pre>{e_(voces_toffee())}</pre>')
    lech = [re.sub(r'^DOÑA LECHUZA[^:]*: «|»$', '', t['quien']) for t in todas() if t['quien'] and t['quien'].startswith('DOÑA LECHUZA')]
    h.append('<h3>Doña Lechuza (voz «Lechuza»)</h3><pre>' + e_("[warm, excited] " + lech[0] + "\n\n[mysterious] " + lech[1] + "\n\n[whispers] " + lech[2]) + '</pre>')
    tur = [re.sub(r'^DON TURBIO[^:]*: «|»$', '', t['quien']) for t in todas() if t['quien'] and t['quien'].startswith('DON TURBIO')]
    h.append('<h3>Don Turbio (voz «Turbio»)</h3><pre>' + e_("\n\n".join(["[hoarse whisper] " + tur[0], "[wheezing] [raspy whisper, sly] " + tur[1], "[hoarse whisper] " + tur[2], "[wheezy laugh] [raspy whisper] " + tur[3]])) + '</pre>')
    h.append('<h2>Las tomas</h2>')
    for es in ESC:
        h.append(f'<h3>{e_(es["t"])}</h3><p class="sub">{e_(es["f"])}</p>')
        for t in es['tomas']:
            chips = ''.join(f'<span class="chip">{e_(f)}</span>' for f in t['fotos']) or '<span class="chip">sin fotos</span>'
            h.append(f'<div class="toma"><div class="meta">Toma {t["n"]} · {t["s"]} s{" · ⭐ GANCHO" if t["gancho"] else ""}</div>{chips}')
            if t['cont']: h.append(f'<div class="cont">{e_(t["cont"])}</div>')
            h.append(f'<div class="voz"><b>{e_(t["quien"] or "")}</b>' + (f' — {e_(t["voz"])}' if t['voz'] else '') + '</div>')
            if t['nota']: h.append(f'<div class="sub">{e_(t["nota"])}</div>')
            h.append(f'<pre>{e_(t["p"])}</pre>')
            if t['v']: h.append(f'<div class="cont">📱 También en vertical 9:16 (para los shorts): en Flow cambia el formato a 9:16 y usa este prompt.</div><pre>{e_(VERT(t["p"]))}</pre>')
            h.append('</div>')
    h.append(f'<h2>Publicación</h2><h3>Título</h3><pre>{e_(TITULO)}</pre><p>Otras opciones: ' + ' · '.join(e_(x) for x in TITULOS_ALT) + '</p>'
             f'<p><b>Texto arriba (primeros 3 s):</b> {e_(ARRIBA[0])} <b>{e_(ARRIBA[1])}</b></p>'
             f'<h3>Miniatura (Nano Banana Pro, con fotos de Toffee, Galleta y el trineo)</h3><pre>{e_(MINIATURA)}</pre><p>{e_(TEXTO_MINI)}</p>'
             f'<h3>Descripción</h3><pre>{e_(DESC)}</pre><h3>Comentario fijado</h3><pre>{e_(COMENTARIO_FIJADO)}</pre>'
             '<p><b>Al subir:</b> «No, no es para niños» · marcar «contenido alterado o sintético» · lista «Temporada 1: Rumbo al Polo Norte» · pantalla final al capítulo 2. Duración final por encima de 3:15 para que cuente como video largo.</p>')
    h.append('<h2>Shorts que salen de este capítulo</h2><div class="tabla"><table><tr><th>Tipo</th><th>De dónde</th><th>Título</th><th>Nota</th></tr>' +
             ''.join(f'<tr><td>{e_(a)}</td><td>{e_(b)}</td><td>{e_(c)}</td><td>{e_(d)}</td></tr>' for a, b, c, d in SHORTS) + f'</table></div><p>{e_(ENCUESTA)}</p>'
             '<p>Cada short lo reedito con su propio inicio y final, en vertical 9:16 (recortando las tomas de un solo personaje y usando las 8 tomas verticales), y lo entrego limpio (sin marca de agua) para YouTube, TikTok e Instagram.</p>')
    return "\n".join(h)

if __name__ == '__main__':
    sys.path.insert(0, os.path.join(here, '..', 'temporada1'))
    src = open(os.path.join(here, '..', 'temporada1', 'build_web.py')).read()
    head = src[src.index("head = '''") + 10: src.index("'''", src.index("head = '''") + 10)]
    head = head.replace('<title>El viaje de Toffee</title>', '<title>Toffee · Capítulo 1</title>')
    script = src[src.index("<script>"): src.index("</script>") + 9]
    os.makedirs(os.path.join(here, 'web'), exist_ok=True)
    open(os.path.join(here, 'web', 'capitulo-01.html'), 'w').write(head + '<main>' + page() + '</main>\n' + script)
    open(os.path.join(here, 'CAPITULO-01.md'), 'w').write(md())
    tot = sum(t['s'] for t in todas())
    print('tomas', len(todas()), 'segundos', tot)
