# EXTRAVÍO · Capítulo 1, versión 2 (pedido de Jay, 29-oct-2026): voces sincronizadas con Voice Changer,
# mundo vivo (ciudad y Mercado de las Llaves), una aventura de verdad en el medio (la noche de la Polilla) y la placa MAX en acercamiento.
# python3 toffee/extravio/capitulos/ex01_v2.py → web/capitulo-01-v2.html (Artifact)
import os, sys, html
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base import Cap, ST, T, G, END, GX, LU, BALL, HT, HLU

C = Cap(1, verticales={37, 40, 45, 49, 50})
C.N = 34   # las tomas 1–34 ya están hechas; las nuevas siguen desde la 35
CG, CGL = "one cat and one dog", "one cat, one dog and one mouse"
SEA = ("An endless sea made of millions of colorful balls stretching to the horizon under a huge warm sunset, a small beach of lost toys, "
       "the silhouette of a city of lost things far away (like the reference).")
CITY = ("A busy street of the fantastical city of lost things at dusk (like the street reference): crooked buildings made of stacked old suitcases with glowing "
        "turquoise windows, lost objects (socks, keys, letters, umbrellas) slowly raining down from an amber sky like snow.")
LIFE = ("The world is alive in the background: a small one-eyed teddy bear walks by pushing a little cart full of single socks, three mismatched socks crawl up "
        "a wall like caterpillars, an old tiny TV with little legs walks past showing static, paper letters flutter through the air like birds.")
MKT = ("Inside the Market of Keys at dusk (like the market reference): a narrow cobblestone alley, thousands of old keys hanging from strings like glittering curtains, "
       "wooden stalls, paper lanterns, glass jars with glowing turquoise orbs.")
HILL = ("On top of a hill of lost objects (suitcases, umbrellas, socks, keys, old toys) at night, the fantastical city of lost things glowing turquoise below, "
        "lost objects slowly falling like snow (like the city reference).")
NIGHT = "It is night: the lanterns are off and the market is dark blue, lit only by the dim turquoise jars."
MKTN = MKT.replace("at dusk", "at night")
BEAM = "a wide beam of soft turquoise light coming down from the dark sky above, sweeping slowly across the cobblestones, with the huge shadow of moth wings moving over the ground"

C.esc("Camino a la ciudad (va después de la toma 26)", "DESARROLLO · el mundo está vivo; Lucho los lleva")
C.tk(8, "TGLM", f"{ST(8)} {SEA} Slow tracking shot from behind: the three walk along the beach of lost toys toward the far city: in front on the left {LU} leading the way, in the middle {T}, on the right {G} sniffing the toys. A flock of lost umbrellas flies across the sky like birds, balls roll in the waves, lost objects slowly rain down. {END(CGL, None, 'waves of rattling balls and soft wind')}",
     voz=None, quien="LUCHO y TOFFEE (voces en off, de espaldas: no se ven las bocas)",
     nota="Voces en off (ElevenLabs): LUCHO «Todo lo que se pierde allá arriba cae aquí. Y todo lo que cae aquí… se vende.» · TOFFEE «¿Y quién compra basura?» · LUCHO «Todo el mundo, Botas.» Después siguen las tomas 27, 28 y 29 de la colina.")

C.esc("La ciudad viva (va después de la toma 29)", "DESARROLLO · entran a la ciudad: personajes caminando dentro del mundo")
C.tk(8, "TGLQ", f"{ST(8)} {CITY} Tracking shot from behind, the camera follows the three walking down the middle of the street: on the left {LU}, in the middle {T}, turning his head everywhere, on the right {G}. {LIFE} {END(CGL, None, 'a lively murmur, footsteps and clinking')}".replace("no other animals appear", "no other animals appear (the teddy bear, socks and little TV are objects, not animals)"),
     voz=None, quien="(sin voz: el mundo vivo)")
C.tk(6, "TQ", f"{ST(6)} {CITY} Side tracking shot: {T} walks along the street, amazed, looking around and then talking into the lens like a vlogger, excited. Behind him the little teddy bear with the sock cart and the walking TV pass by. {HT('Esto es contenido. Esto es puro contenido.', voice='in an excited, fast male voice')} {END('one cat', 'the cat', 'a lively murmur and footsteps')}",
     voz=None, quien="TOFFEE (a cámara): «Esto es contenido. Esto es puro contenido.»", cont="Usar el último cuadro de la toma 36 como primer cuadro.")
C.tk(6, "GQ", f"{ST(6)} {CITY} {G} trots along the street; a paper letter flutters past his nose like a bird; he jumps and snaps at it playfully, misses, and lands happily, tail wagging. {END('one dog', None, 'fluttering paper and a lively murmur')}",
     voz=None, quien="(sin voz: Galleta juega con una carta que vuela)")

C.esc("El Mercado de las Llaves", "DESARROLLO · la meta: encontrar la llave de casa entre millones")
C.tk(8, "TLK", f"{ST(8)} {MKT} On the right, {LU} walks into the market and turns around, spreading his arms proudly like a salesman; on the left, {T} follows, looking up at the keys. {HLU('Mercado de las Llaves. Aquí están todas las llaves que se han perdido en la historia.')} {END('one cat and one mouse', 'the mouse', 'jingling keys and a quiet market murmur')}",
     voz=None, quien="LUCHO (a cámara): «Mercado de las Llaves. Aquí están todas las llaves que se han perdido en la historia.»")
C.tk(6, "TK", f"{ST(6)} {MKT} Close-up of {T} looking up at the endless glittering curtains of hanging keys, the camera slowly tilting up with his gaze; his face falls, then he looks into the lens. {HT('¿Y cuál es la mía?', voice='in a flat, defeated male voice')} {END('one cat', 'the cat', 'jingling keys')}",
     voz=None, quien="TOFFEE (a cámara): «¿Y cuál es la mía?»")
C.tk(6, "LK", f"{ST(6)} {MKT} Close-up of {LU} behind his stall, shrugging, nibbling his cheese, then a nervous little giggle. {HLU('Ni idea. Por eso es negocio. Je, je.')} {END('one mouse', 'the mouse', 'jingling keys')}",
     voz=None, quien="LUCHO (a cámara): «Ni idea. Por eso es negocio. Je, je.»")

C.esc("La noche de la Polilla", "OBSTÁCULO · Galleta persigue un recuerdo y Toffee lo salva (va después de la toma 30, la sombra sobre la ciudad)")
C.tk(6, "K", f"{ST(6)} {MKT} The paper lanterns flicker and go out one by one; the market becomes dark blue. The little one-eyed teddy bear, the walking socks and the little TV with legs stop, look up at the sky and run to hide under the stalls. {END('no animals visible', None, 'lanterns going out and deep slow wing flaps far away')}".replace("Exactly no animals visible for the whole video, identical to the references; no other animals appear.", "No animals visible."),
     voz=None, quien="LUCHO (voz en off, susurro): «Escóndanse. Ella no puede saber que llegaron.» (ya está grabada)")
C.tk(6, "TGLK", f"{ST(6)} {MKTN} {NIGHT} Low camera under a wooden market stall: on the left {T} and {G} hiding, pressed together; on the right {LU}, trembling and hugging his cheese. Outside on the cobblestones, {BEAM}. They hold their breath. {END(CGL, None, 'deep slow wing flaps and a low magical hum')}",
     voz=None, quien="(sin voz: escondidos)", cont="Usar el último cuadro de la toma 42 como primer cuadro si se puede.")
C.tk(6, "GOK", f"{ST(6)} {MKTN} {NIGHT} Close-up of {G} under the stall: a glowing turquoise memory sphere (like the sphere reference) rolls slowly across the cobblestones in front of him, like a ball. The dog's ears go up, {GX['desastre']}, and he crawls out after it. {END('one dog', None, 'a soft magical hum')}",
     voz=None, quien="(sin voz: Galleta ve el recuerdo rodar como una pelota)")
C.tk(6, "TK", f"{ST(6)} {MKTN} {NIGHT} Close-up of {T} hiding under the stall, watching the dog leave, eyes wide, whispering in panic; then he sighs, closes his eyes for a second and crawls out. {HT('Galleta… no. Yo no corro. Yo nunca corro.', voice='in a panicked male whisper', verb='whispers')} {END('one cat', 'the cat', 'deep slow wing flaps')}",
     voz=None, quien="TOFFEE (susurro, a cámara): «Galleta… no. Yo no corro. Yo nunca corro.»", nota="Repite el chiste de «Yo no salgo. Yo nunca salgo.» del principio: el público ya sabe que sí va a ir.")
C.tk(6, "TGOK", f"{ST(6)} {MKTN} {NIGHT} Wide shot of the empty market alley: in the middle, {G} happily pushes the glowing turquoise memory sphere with his nose; {BEAM}, getting closer to him. From the left, {T} sprints across the cobblestones toward the dog as fast as he can. {END(CG, None, 'wing flaps getting louder and running paws')}",
     voz=None, quien="(sin voz: la carrera)")
C.tk(6, "TGOK", f"{ST(6)} {MKTN} {NIGHT} {T} grabs {G} by the navy bandana and pulls him into an old brown suitcase lying open on its side at the edge of the alley. A moment later the turquoise light beam passes over the spot where the dog was, and the glowing memory sphere floats up into the light and disappears in the sky. The cat wears NO bandana and NO tag; only the dog wears the navy bandana with the gold bone tag. {END(CG, None, 'a loud whoosh and deep wing flaps')}",
     voz=None, quien="(sin voz: el rescate)", cont="Usar el último cuadro de la toma 46 como primer cuadro.")
C.tk(6, "TGK", f"{ST(6)} Inside a dark old suitcase lying on its side, close shot: on the left {T} holds one front paw over the mouth of {G}, on the right; both have huge eyes, frozen. Turquoise light passes slowly through the gaps of the suitcase over their faces, then everything goes dark and quiet. The cat wears NO bandana and NO tag. {END(CG, None, 'deep wing flaps fading away')}",
     voz=None, quien="(sin voz: el silencio)")
C.tk(6, "TGK", f"{ST(6)} Inside the dark old suitcase, same framing, dim turquoise light: on the left {T}, still shaking, looks at {G} and whispers furiously; the dog licks the cat's face. The cat wears NO bandana and NO tag. {HT('Si me vuelves a hacer eso, te vendo. A Lucho.', voice='in an angry male whisper', verb='whispers')} {END(CG, 'the cat', 'quiet night')}",
     voz=None, quien="TOFFEE (susurro, a cámara): «Si me vuelves a hacer eso, te vendo. A Lucho.»", cont="Usar el último cuadro de la toma 48 como primer cuadro.")
C.tk(6, "LK", f"{ST(6)} {MKTN} {NIGHT} {LU} peeks into the opening of the suitcase from outside, looking in at the camera, surprised, then forces a big fake smile with his crooked tooth. {HLU('¿Siguen vivos? Qué decepción… digo, ¡qué alegría! Je, je.')} {END('one mouse', 'the mouse', 'quiet night')}",
     voz=None, quien="LUCHO (a cámara): «¿Siguen vivos? Qué decepción… digo, ¡qué alegría! Je, je.»")

C.esc("De vuelta a la colina", "RECOMPENSA + CONTINUACIÓN · a salvo… y la placa MAX (después siguen las tomas 33 y 34)")
C.tk(8, "TGLC", f"{ST(8)} {HILL} Wide shot from behind: the three climb slowly up the hill of lost objects in the night: in front {LU}, then {T}, then {G}; tired, quiet. {END(CGL, None, 'soft magical wind')}",
     voz=None, quien="LUCHO (voz en off, de espaldas): «Aquí arriba no sube. Por ahora.»")
C.tk(6, "GX", f"{ST(6)} {HILL} Medium shot of {G} sitting calmly on the hill at night. The camera slowly and smoothly pushes in toward his neck until the gold bone tag on his navy bandana fills the frame; the tag starts glowing softly, and the name MAX engraved on it becomes clear (like the tag reference). One slow continuous dolly-in, no cuts. {END('one dog', None, 'a soft magical hum')}",
     voz=None, quien="(sin voz: acercamiento a la placa)", nota="Reemplaza la toma 32. Si las letras no dicen MAX bien legible, se repite.")

TOFFEE = "[annoyed] ¿Y quién compra basura?"
LUCHO = "\n\n".join([
 "[raspy, proud salesman] Todo lo que se pierde allá arriba cae aquí. [sly] Y todo lo que cae aquí… se vende.",
 "[tired] Todo el mundo, Botas.",
 "[hoarse whisper, relieved] Aquí arriba no sube. [ominous] Por ahora."])
CALLE = ("Photorealistic cinematic 16:9 wide shot, street level, normal lens: a busy street inside a fantastical city built entirely from lost things, at dusk. "
         "Crooked tall buildings made of stacked old suitcases, shoes and books, with glowing turquoise windows; bridges made of giant keys between buildings; "
         "lost objects (socks, keys, letters, small umbrellas) slowly raining down from a warm amber sky like snow. On the cobblestone street: a small one-eyed teddy bear "
         "pushing a little cart full of single socks, an old tiny TV with little legs walking, paper letters fluttering like birds, paper lanterns hanging across the street. "
         "Same style and colors as the reference. Center of the street empty for the characters. No people, no animals, no text.")

def bloque(t):
    e = html.escape
    return f'<pre>{e(t)}</pre>'
D = dict(
 titulo="Me caí a otro mundo persiguiendo a mi perro (versión 2)",
 secciones=[
  ("1 · Voces sincronizadas (lo más importante)",
   "<p>Por qué se ven desincronizadas: la voz de ElevenLabs va a otro ritmo que la boca que hizo Flow. Medí cada toma: la voz va entre 0,2 y 1,8 s adelante o atrás de la boca. Moviendo frases no se arregla.</p>"
   "<p><b>Solución: Voice Changer de ElevenLabs.</b> Flow ya dijo bien todas las frases y la boca va con ESE audio. El Voice Changer le cambia la voz a la de Toffee o Lucho sin cambiar el ritmo, así que la boca queda perfecta.</p>"
   "<ol><li>ElevenLabs → <b>Voice Changer</b>.</li><li>Sube <b>VOZ-PARA-CAMBIAR-TOFFEE.mp3</b>, voz <b>Toffee</b>.</li><li>Ajustes: Stability 50 %, Similarity 85 %, Style 0, <b>Remove background noise: ON</b>.</li>"
   "<li>Generar y descargar. Lo mismo con <b>VOZ-PARA-CAMBIAR-LUCHO.mp3</b> y la voz <b>Lucho</b>.</li><li>Mándame los dos archivos. Yo corto cada frase en su toma.</li></ol>"
   "<p>Las frases en voz en off (sin boca en pantalla) se quedan con las voces que ya hiciste. Las tomas nuevas también: Flow dice la frase y después pasa por el Voice Changer.</p>"),
  ("2 · Lo que hago yo en la edición (no tienes que hacer nada)",
   "<ul><li><b>Logo:</b> sale del remolino del gancho y la cámara «cae» por el ojo de la cerradura de la O hacia la casa. Nada de imagen pegada.</li>"
   "<li><b>Gato con Botas:</b> burbuja de pensamiento que sale de la cabeza de Lucho (tres bolitas que crecen + la burbuja con el dibujo), con sonido de «pop».</li>"
   "<li><b>Transiciones:</b> el sonido de una escena entra antes del corte, fundidos suaves entre lugares, un ambiente continuo por escena (no salta en cada toma).</li>"
   "<li><b>Sonidos:</b> los ambientes de fondo (viento, murmullo de la ciudad, zumbido mágico, remolino) y los «whoosh» los hago yo.</li></ul>"),
  ("3 · Imagen nueva (Nano Banana Pro, 16:9, con EXTRAVIO-CIUDAD de referencia) → CALLE-EXTRAVIO", bloque(CALLE)),
 ],
 voces=[("Toffee · voz en off nueva (ElevenLabs)", "Toma 35.", TOFFEE), ("Lucho · voces en off nuevas (ElevenLabs)", "Tomas 35 y 51.", LUCHO)],
 final=[("Orden del capítulo nuevo",
   "<p>Gancho → logo → tomas 1–26 → <b>35</b> → 27, 28, 29 → <b>36–41</b> → 30 (sombra) → <b>42–50</b> → <b>51</b> → <b>52</b> → 33 → 34. La toma 31 y la 32 salen. Duración estimada: unos 5 minutos.</p>")],
)
if __name__ == '__main__':
    C.publicar(D, 'capitulo-01-v2.html')
    print('tomas nuevas:', len(C.todas()), 'segundos:', sum(t['s'] for t in C.todas()))
