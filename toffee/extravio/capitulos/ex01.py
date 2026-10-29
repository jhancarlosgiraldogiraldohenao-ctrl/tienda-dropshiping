# EXTRAVÍO · Capítulo 1 «Me caí a otro mundo persiguiendo a mi perro» (escrito el 30-oct-2026)
# python3 toffee/extravio/capitulos/ex01.py → web/capitulo-01.html (Artifact)
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base import Cap, ST, T, G, TR, END, GX, LU, BALL, HT, HLU

C = Cap(1, verticales={11, 13, 16, 17, 21, 22, 28, 31})
CG = "one cat and one dog"
CGL = "one cat, one dog and one mouse"
HOME = ("Cozy small apartment living room in the late afternoon, warm window light, a gray sofa, "
        "the red plush sleigh-shaped pet bed on the rug, the front door on the right side.")
STREET = ("A quiet residential street of a Latin American city on a rainy late afternoon, wet asphalt, colorful houses, "
          "a sidewalk curb with a metal storm drain grate.")
SEA = ("An endless sea made of millions of colorful balls (tennis balls, rubber balls, soccer balls) stretching to the horizon under a huge warm "
       "sunset, a small beach of lost toys, the silhouette of a city of lost things far away (like the reference).")
HILL = ("On top of a hill of lost objects (suitcases, umbrellas, socks, keys, old toys) at dusk, looking at a fantastical city built from stacked "
        "suitcases with glowing turquoise windows, lost objects slowly raining down from an amber sky (like the city reference).")

# ---------------- 1 · La vida de un influencer ----------------
C.esc("La vida de un «influencer»", "INICIO · quién es Toffee y qué quiere")
C.tk(8, "TS", f"{ST(8)} {HOME} {T} sits proudly on {TR} like a king on a throne and looks straight into the lens. {HT('A ver, mis desgraciados… bienvenidos a otro día en la vida del gato más famoso de internet.')} {END('one cat', 'the cat', 'quiet room')}",
     voz="[proud, dramatic] A ver, mis desgraciados… bienvenidos a otro día en la vida del gato más famoso de internet.", quien="TOFFEE (a cámara)")
C.tk(6, "TS", f"{ST(6)} {HOME} Same framing: {T} on the sleigh bed, his proud face slowly drops into a flat, annoyed look; he glances away from the lens. {HT('Bueno… casi famoso. Tengo doce seguidores. Y tres son bots.')} {END('one cat', 'the cat', 'quiet room')}",
     voz="[deflated] Bueno… casi famoso. … Tengo doce seguidores. [annoyed] Y tres son bots.", quien="TOFFEE (a cámara)", cont="Usar el último cuadro de la toma 1 como primer cuadro.")
C.tk(6, "G", f"{ST(6)} {HOME} Low camera on the rug. {G} lies happily chewing {BALL}; he squeaks it twice, then looks up at the camera and tilts his head. {END('one dog', None, 'squeaky toy sounds')}",
     voz="[unimpressed] Él es Galleta. Mi asistente. No sabe hacer nada… [shrugs] pero es gratis.", quien="TOFFEE (voz en off)")
C.tk(8, "T", f"{ST(8)} {HOME} Near the front door: an empty key hook on the wall and the front door left slightly open, a strip of rainy daylight coming in. {T} sits by the door and looks at the camera with a judging face. {END('one cat', None, 'light rain outside')}",
     voz="[sarcastic] Mi humana perdió las llaves de la casa hace tres meses. Desde entonces deja la puerta… así.", quien="TOFFEE (voz en off)")

# ---------------- 2 · La pelota ----------------
C.esc("La pelota", "DESARROLLO · Galleta lo empieza todo")
C.tk(6, "G", f"{ST(6)} {HOME} {G} drops {BALL} on the floor; it bounces twice and rolls straight out through the slightly open front door. The dog {GX['desastre']}. {END('one dog', None, 'bouncing ball')}",
     voz=None, quien="(sin voz: la pelota rebota y sale)")
C.tk(6, "TG", f"{ST(6)} {HOME} On the right, {G} runs out through the open front door after the ball. On the left, {T} jumps up from the sleigh bed with wide eyes. {HT('Galleta. No. ¡GALLETA!', voice='in a loud, alarmed male voice', verb='shouts')} {END(CG, 'the cat', 'rain outside')}",
     voz="[warning] Galleta. No. [shouting] ¡GALLETA!", quien="TOFFEE")
C.tk(8, "G", f"{ST(8)} {STREET} {BALL} rolls along the wet curb and falls into the storm drain opening. {G} runs after it and pushes his head into the drain opening, tail wagging. {END('one dog', None, 'rain and a hollow echo')}",
     voz=None, quien="(sin voz)")
C.tk(6, "T", f"{ST(6)} Doorway of the apartment, rainy street outside. {T} stands on the doorstep, refusing to step out, looks at the camera, sighs, closes his eyes for a second, then steps out into the rain. {HT('Yo no salgo. Yo nunca salgo.')} {END('one cat', 'the cat', 'rain')}",
     voz="[firm] Yo no salgo. Yo nunca salgo. [long sigh] …[muttering] Puta madre.", quien="TOFFEE", nota="«Puta madre» va en voz baja, casi entre dientes; es la grosería fuerte del capítulo (más de 10 s después del inicio).")
C.tk(6, "TG", f"{ST(6)} {STREET} On the left, {T}, wet from the rain, arrives next to the storm drain; on the right, {G} with his head in the drain. A soft turquoise light starts glowing from inside the drain, lighting their faces. {HT('¿Por qué está brillando la alcantarilla?', voice='in a worried male voice')} {END(CG, 'the cat', 'rain and a magical hum')}",
     voz="[suspicious] ¿Por qué está brillando la alcantarilla?", quien="TOFFEE")
C.tk(6, "TG", f"{ST(6)} {STREET} The turquoise glow from the storm drain grows bright; the cat and the dog slide into the glowing opening and disappear down into the light, the cat screaming. {END(CG, None, 'rain, a magical whoosh and a scream fading down')}",
     voz="[screaming, falling] ¡¡AAAAH!!", quien="TOFFEE")

# ---------------- 3 · El Remolino ----------------
C.esc("El Remolino", "OBSTÁCULO · caen a otro mundo")
C.tk(8, "TGR", f"{ST(8)} Inside a huge swirling vortex tunnel of lost objects (socks, remote controls, keys, toys, balls, umbrellas, letters) lit by turquoise magical light (like the reference). {T} falls tumbling through the vortex screaming with huge eyes; next to him {G} falls happily, trying to catch {BALL} floating in the air. {HT('¡¡GALLETAAA!!', voice='in a loud, terrified male voice', verb='screams')} {END(CG, 'the cat', 'rushing wind and clattering objects')}",
     voz="[screaming, terrified] ¡¡GALLETAAA!!", quien="TOFFEE", gancho=True, nota="GANCHO: los primeros 5 s de esta toma abren el capítulo, antes del logo.")
C.tk(6, "TR", f"{ST(6)} Inside the swirling turquoise vortex of lost objects. Close shot of {T} falling, holding on to a floating TV remote control with both paws, looking into the lens with a resigned, dramatic face. {END('one cat', None, 'rushing wind')}",
     voz="[dramatic, resigned] Si me muero, quiero que sepan que fue culpa del perro.", quien="TOFFEE (voz en off)")

# ---------------- 4 · El Mar de Pelotas ----------------
C.esc("El Mar de Pelotas", "OBSTÁCULO + CORAZÓN · Galleta se hunde y Toffee lo salva")
C.tk(6, "TGM", f"{ST(6)} {SEA} The cat and the dog fall from the sky and splash into the sea of balls, and hundreds of colorful balls burst up into the air and rain back down. {END(CG, None, 'a huge bouncy crash and rattling balls')}",
     voz=None, quien="(sin voz: el golpe en las pelotas)")
C.tk(6, "TM", f"{ST(6)} {SEA} {T} pops his head out of the balls, spits out a small ball, and looks around amazed at the endless sea of balls and the sunset. {HT('¿Qué… es… esto?', voice='in an amazed, breathless male voice', verb='whispers')} {END('one cat', 'the cat', 'gentle rattling of balls')}",
     voz="[amazed, breathless] ¿Qué… es… esto?", quien="TOFFEE (a cámara)")
C.tk(6, "GM", f"{ST(6)} {SEA} {G} dives happily among the balls looking for his yellow ball, then slowly sinks until only the tip of his tail is visible, and disappears under the balls. {END('one dog', None, 'rattling balls')}",
     voz="[worried] ¿Galleta?", quien="TOFFEE (voz en off)")
C.tk(8, "TM", f"{ST(8)} {SEA} {T} swims desperately through the balls, pushing them aside with his front paws and digging down, very worried. {HT('¡Galleta! ¡No te mueras, que tú eres el que carga todo!', voice='in a loud, desperate male voice', verb='shouts')} {END('one cat', 'the cat', 'rattling balls')}",
     voz="[shouting, desperate] ¡Galleta! ¡No te mueras, que tú eres el que carga todo!", quien="TOFFEE")
C.tk(6, "TGM", f"{ST(6)} {SEA} On the left, {T} pulls {G} up out of the balls by his bandana; the dog comes up happy with {BALL} in his mouth and licks the cat. The cat looks into the lens, embarrassed. {HT('Casi me da algo. Por la pelota. Me preocupaba la pelota.')} {END(CG, 'the cat', 'rattling balls')}",
     voz="[relieved, then defensive] Casi me da algo. … Por la pelota. Me preocupaba la pelota.", quien="TOFFEE (a cámara)")

# ---------------- 5 · Lucho ----------------
C.esc("Lucho", "DESARROLLO · las reglas de Extravío")
C.tk(6, "LM", f"{ST(6)} {SEA} On a small beach of lost toys, {LU} peeks out from behind a broken toy car, looks left and right, nervous, and leans toward the camera. {HLU('Psst… gato.', verb='whispers')} {END('one mouse', 'the mouse', 'distant waves of balls')}",
     voz=None, quien="LUCHO: «Psst… gato.»")
C.tk(8, "LM", f"{ST(8)} {SEA} Close-up of {LU} on the beach of lost toys, nibbling his cheese, twitchy, talking secretly to the camera. {HLU('Bienvenidos a Extravío. Aquí cae todo lo que se pierde. Medias, controles, llaves… y mascotas.')} {END('one mouse', 'the mouse', 'distant waves of balls')}",
     voz=None, quien="LUCHO: «Bienvenidos a Extravío. Aquí cae todo lo que se pierde. Medias, controles, llaves… y mascotas.»", cont="Usar el último cuadro de la toma 18 como primer cuadro.")
C.tk(6, "TGM", f"{ST(6)} {SEA} On the beach of lost toys: on the left, {T}, wet and offended, sits up straight and talks proudly; on the right, {G} chews his ball. {HT('Nosotros no estamos perdidos. Yo soy famoso.')} {END(CG, 'the cat', 'distant waves of balls')}",
     voz="[offended, proud] Nosotros no estamos perdidos. Yo soy famoso.", quien="TOFFEE")
C.tk(8, "TLM", f"{ST(8)} {SEA} On the beach of lost toys: on the right, {LU} squints at the cat, then his face lights up as if he recognizes a celebrity; on the left, {T} smiles, flattered. {HLU('¿Famoso? ¡Ah, claro! Tú eres el Gato con Botas, ¿cierto?')} {END(CGL, 'the mouse', 'distant waves of balls')}",
     voz=None, quien="LUCHO: «¿Famoso? ¡Ah, claro! Tú eres el Gato con Botas, ¿cierto?»", nota="En la edición: burbuja con la ilustración clásica del Gato con Botas (imagen aparte, abajo).")
C.tk(6, "T", f"{ST(6)} {SEA} Close-up of {T}, furious, ears back, eyes narrowed, shouting at someone off-screen to the right. {HT('¿¡Me ves botas, desgraciado!?', voice='in a loud, furious male voice', verb='shouts')} {END('one cat', 'the cat', 'distant waves of balls')}",
     voz="[furious, shouting] ¿¡Me ves botas, desgraciado!?", quien="TOFFEE")
C.tk(8, "L", f"{ST(8)} {SEA} Close-up of {LU}, calm now, lowering his voice and leaning toward the camera, serious and mysterious. {HLU('Tranquilo, Botas. Aquí hay una regla: solo vuelves a casa si alguien allá arriba todavía te está buscando.', verb='whispers')} {END('one mouse', 'the mouse', 'distant waves of balls')}",
     voz=None, quien="LUCHO (susurro): «Tranquilo, Botas. Aquí hay una regla: solo vuelves a casa si alguien allá arriba todavía te está buscando.»")
C.tk(6, "T", f"{ST(6)} {SEA} Close-up of {T}, his confidence slowly breaking, eyes looking down, unsure. {HT('Mi humana me está buscando. Seguro. Creo.')} {END('one cat', 'the cat', 'distant waves of balls')}",
     voz="[confident] Mi humana me está buscando. [unsure] Seguro. [small voice] …Creo.", quien="TOFFEE")
C.tk(8, "TL", f"{ST(8)} {SEA} On the beach of lost toys: on the right, {LU} taps his backpack of old keys, which jingle; on the left, {T} listens. {HLU('¿Y la llave de tu casa? Para volver, necesitas la llave.')} {END('one cat and one mouse', 'the mouse', 'jingling keys')}",
     voz=None, quien="LUCHO: «¿Y la llave de tu casa? Para volver, necesitas la llave.»")
C.tk(6, "TL", f"{ST(6)} On the beach of lost toys: on the left, {T} answers flatly; on the right, {LU} grins slowly with his crooked tooth and giggles. {HT('Mi humana la perdió hace tres meses.')} {END('one cat and one mouse', 'the cat', 'distant waves of balls')}",
     voz="[flat] Mi humana la perdió hace tres meses.", quien="TOFFEE · y después LUCHO: «Entonces está aquí. En algún lado. Je, je.»",
     nota="La respuesta de Lucho («Entonces está aquí. En algún lado. Je, je.») va en voz en off sobre su sonrisa.")

# ---------------- 6 · La ciudad ----------------
C.esc("La ciudad de Extravío", "RECOMPENSA · el mundo que nadie ha grabado")
C.tk(8, "TGC", f"{ST(8)} {HILL} Wide shot from behind: on the left {T}, on the right {G}, sitting small on top of the hill, looking at the glowing city. {END(CG, None, 'soft magical wind and distant clinking')}",
     voz="[amazed, quiet] Un mundo entero… que nadie ha grabado nunca.", quien="TOFFEE (voz en off)", nota="Toma de «wow»: miniatura y shorts.")
C.tk(6, "TC", f"{ST(6)} {HILL} Close-up of {T}, the turquoise city lights reflected in his big eyes, slowly smiling with ambition, looking into the lens. {HT('Voy a ser el gato más famoso del multiverso.', verb='whispers')} {END('one cat', 'the cat', 'soft magical wind')}",
     voz="[whispers, ambitious] Voy a ser el gato más famoso del multiverso.", quien="TOFFEE (a cámara)")
C.tk(6, "LC", f"{ST(6)} {HILL} Close-up of {LU} sitting on a suitcase on the hill, nibbling cheese, looking at the camera with a tired sarcastic face. {HLU('Primero sobrevive a esta noche, Botas.')} {END('one mouse', 'the mouse', 'soft magical wind')}",
     voz=None, quien="LUCHO: «Primero sobrevive a esta noche, Botas.»")

# ---------------- 7 · La Polilla y Max ----------------
C.esc("La sombra y la placa", "CONTINUACIÓN · el misterio que deja ganas del capítulo 2")
C.tk(6, "C", f"{ST(6)} The fantastical city of lost things at dusk (like the reference). A gigantic shadow shaped like a moth with huge wings slowly passes over the city, and the turquoise windows go dark one by one under it. {END('no animals visible on the ground', None, 'deep slow wing flaps')}".replace("Exactly no animals visible on the ground for the whole video, identical to the references; no other animals appear.", "No animals visible on the ground."),
     voz=None, quien="LUCHO (voz en off, susurro): «Escóndanse. Ella no puede saber que llegaron.»", nota="La Polilla NO se ve todavía: solo su sombra.")
C.tk(6, "L", f"{ST(6)} {HILL} {LU} dives under an old suitcase and hides, only his trembling nose and whiskers peeking out, nervously nibbling his cheese. {END('one mouse', None, 'deep slow wing flaps far away')}",
     voz=None, quien="(sin voz: Lucho tiembla y come queso)")
C.tk(6, "GX", f"{ST(6)} {HILL} Close-up of {G} looking up at the dark sky; the gold bone tag on his bandana starts glowing softly; the tag has the name MAX engraved on it (like the tag reference). {END('one dog', None, 'a soft magical hum')}",
     voz=None, quien="(sin voz: la placa brilla)")
C.tk(6, "TG", f"{ST(6)} {HILL} On the left, {T} leans close to the glowing tag on {G}'s bandana, reads it, frowns and looks into the lens, confused. {HT('¿Max? ¿Quién carajos es Max?')} {END(CG, 'the cat', 'soft magical hum')}",
     voz="[confused] ¿Max? [frowning] ¿Quién carajos es Max?", quien="TOFFEE (a cámara)")
C.tk(10, "TGF", f"{ST(10)} {HILL} Calm wide shot from behind: on the left {T}, on the right {G}, sitting small on the hill looking at the glowing city at night, lost objects slowly falling like snow (like the reference). Lots of empty sky. {END(CG, None, 'soft magical wind')}",
     voz="[cheeky] ¿Ustedes saben quién es Max? Los leo. [proud] Sígueme para no perderte el próximo episodio.", quien="TOFFEE (voz en off)",
     nota="Pantalla final: aquí YouTube pone sus botones (últimos 15–20 s; alargo el final congelando el cuadro si hace falta).")

# ---------------- Textos ----------------
TOFFEE = "\n\n".join(t['voz'] for t in C.todas() if t['voz'])
LUCHO = "\n\n".join([
 "[hoarse whisper] Psst… gato.",
 "[raspy, secretive] Bienvenidos a Extravío. Aquí cae todo lo que se pierde. [wheezing] Medias, controles, llaves… y mascotas.",
 "[surprised, excited] ¿Famoso? ¡Ah, claro! Tú eres el Gato con Botas, ¿cierto?",
 "[calm, mysterious whisper] Tranquilo, Botas. Aquí hay una regla: solo vuelves a casa si alguien allá arriba todavía te está buscando.",
 "[raspy] ¿Y la llave de tu casa? Para volver, necesitas la llave.",
 "[sly] Entonces está aquí. En algún lado. [nervous giggle] Je, je.",
 "[tired, sarcastic] Primero sobrevive a esta noche, Botas.",
 "[terrified whisper] Escóndanse. Ella no puede saber que llegaron."])
GATO_BOTAS = ("Antique 19th-century book engraving illustration in black ink on aged yellowed paper, in the style of classic fairy-tale book illustrations: "
              "the fairy-tale Puss in Boots, a slim gray tabby cat standing on two legs wearing tall floppy leather musketeer boots, a wide cavalier hat with a long feather "
              "and a short cape, bowing elegantly. Fine cross-hatching, vintage storybook look. Plain paper background. No color, no text.")
MINI = ("YouTube thumbnail, 16:9, photorealistic cinematic, high contrast: inside a huge swirling turquoise vortex of lost objects (socks, keys, remote controls, balls), "
        "the cream-caramel British Shorthair cat from the reference (navy knitted nightcap with cream pompom and small black action camera on top) falling toward the camera, "
        "screaming with a huge open mouth and huge eyes, filling the left half; on the right, the scruffy golden-brown dog from the reference (navy bandana with gold bone tag) "
        "falling happily with a yellow ball in his mouth. Bright warm light at the bottom of the vortex. No text.")
D = dict(
 titulo="Me caí a otro mundo persiguiendo a mi perro",
 secciones=[
  ("La historia en 30 segundos", '<div class="box">'
   '<p><b>Qué quiere Toffee:</b> ser famoso (tiene 12 seguidores… y 3 son bots).</p>'
   '<p><b>Qué se lo impide:</b> Galleta persigue su pelota por una alcantarilla que brilla y los dos caen a <b>Extravío</b>, el mundo donde termina todo lo que se pierde. Para volver necesitan que alguien los esté buscando… y la llave de casa, que la humana perdió hace tres meses.</p>'
   '<p><b>Qué cambia al final:</b> tienen una misión (encontrar la llave), un guía dudoso (Lucho, que lo llama «Botas»), un mundo que nadie ha grabado (Toffee quiere hacerse famoso grabándolo) y dos misterios: la sombra de una polilla gigante y la placa de Galleta que dice <b>MAX</b>.</p>'
   '<p><b>Corazón:</b> Toffee se lanza al Mar de Pelotas a sacar a Galleta… y después dice que se preocupaba por la pelota.</p></div>'),
  ("Por qué está escrito así", '<ul>'
   '<li><b>Gancho:</b> la caída por el Remolino con el «¡¡GALLETAAA!!» abre el capítulo; luego el logo de EXTRAVÍO (2–3 s) y «A ver, mis desgraciados…».</li>'
   '<li><b>Una cosa por culpa de la otra:</b> humana pierde la llave → puerta abierta → la pelota sale → Galleta la sigue → la alcantarilla brilla → caen → Galleta se hunde → Toffee lo salva → Lucho → la regla y la llave → la misión.</li>'
   '<li><b>Tono adulto con límites:</b> «puta madre» entre dientes (lejos de los primeros 10 s), «desgraciado(s)» y «carajos». Parodia del Gato con Botas con la ilustración clásica del cuento (dominio público).</li>'
   '<li><b>Elementos que vuelven:</b> «Botas» (el apodo que Toffee odia), la llave de casa, la pelota amarilla, la regla, la Polilla y MAX.</li>'
   '<li><b>Productos de la Colección Extravío</b> que salen sin forzar: el gorro de Toffee, la pañoleta y la placa de Galleta, la pelotita.</li>'
   '<li><b>Sin texto en pantalla.</b> El cierre lo dice Toffee con su voz.</li></ul>'),
  ("Antes de generar (en este orden)", '<ol>'
   '<li><b>Voces primero:</b> Toffee (todo su texto de abajo en un solo bloque, 2–3 versiones, estabilidad 35–45 %) y Lucho (su bloque). Mándamelas.</li>'
   '<li><b>La imagen del Gato con Botas</b> (Nano Banana, prompt abajo).</li>'
   '<li><b>Prueba de 3 tomas en 16:9:</b> 11 (el Remolino), 18 (Lucho) y 27 (la ciudad). Si salen bien, sigues con el resto.</li>'
   '<li>Me mandas las tomas; respondo «✓» hasta que digas «listo». Al final, las 8 verticales para los shorts.</li></ol>'),
 ],
 voces=[("Toffee · todo su texto en un solo bloque (voz de Toffee)", "Estabilidad 35–45 %, similitud 85 %, Español. Respeta los renglones en blanco: ahí corto.", TOFFEE),
        ("Lucho · todo su texto en un solo bloque (voz «Lucho»)", "Estabilidad 30–40 %. Si alguna etiqueta se lee en voz alta, bórrala.", LUCHO)],
 imagenes=[("Imagen: el Gato con Botas clásico (para la burbuja de la toma 21)", "Nano Banana Pro · 1:1 · sin fotos · guardar como GATO-CON-BOTAS.jpg. Es el del cuento de 1697 (dominio público), NO el de Shrek.", GATO_BOTAS)],
 final=[
  ("Publicación", f'<h3>Título</h3><pre>Me caí a otro mundo persiguiendo a mi perro 🌀 | Extravío · Cap. 1</pre>'
   '<p>Otras opciones: «Mi perro me arrastró al mundo donde termina todo lo que se pierde» · «Encontré el lugar donde van las medias perdidas (y no deberíamos estar aquí)»</p>'
   f'<h3>Miniatura (Nano Banana Pro · 16:9 · fotos de Toffee y Galleta)</h3><pre>{MINI}</pre><p>Texto que pongo yo encima (máx. 2 palabras): «¿OTRO MUNDO?»</p>'
   '<h3>Descripción</h3><pre>Toffee quería ser famoso. Tenía 12 seguidores (3 eran bots). Entonces Galleta persiguió su pelota por una alcantarilla que brillaba… y cayeron a Extravío, el mundo donde termina todo lo que se pierde. 🌀\n\n¿Ustedes saben quién es Max? Los leo 👇\n\n🧢 El gorro de Toffee y la pañoleta de Galleta: soytoffee.store\n\nEXTRAVÍO · Temporada 1 «La llave de casa» · Capítulo 1\nPersonajes y videos hechos con inteligencia artificial; historia, voces y edición propias.\n#Extravío #ToffeeyGalleta #animación</pre>'
   '<h3>Comentario fijado</h3><pre>🔑 Regla de Extravío: solo vuelves a casa si alguien te está buscando. ¿Quién creen que es Max? 👇</pre>'
   '<p><b>Al subir:</b> «No, no es para niños» · marcar «contenido alterado o sintético» · lista «Extravío · Temporada 1» · pantalla final al capítulo 2 · subtítulos .srt en español e inglés (los hago yo).</p>'),
  ("Shorts que salen de este capítulo", '<table><tr><th>Short</th><th>Tomas</th><th>Título</th></tr>'
   '<tr><td>Gancho</td><td>5–11</td><td>Mi perro persiguió su pelota… y caímos a otro mundo 🌀</td></tr>'
   '<tr><td>El Gato con Botas</td><td>20–22</td><td>«¿Tú eres el Gato con Botas?» 😾</td></tr>'
   '<tr><td>Corazón</td><td>15–17</td><td>Dice que no lo quiere… 🐶</td></tr>'
   '<tr><td>La regla</td><td>23–26</td><td>Solo vuelves a casa si alguien te está buscando 🔑</td></tr>'
   '<tr><td>Misterio</td><td>31–34</td><td>¿Quién es Max? 🦴</td></tr></table>'
   '<p>Cada short lo reedito en 9:16 con subtítulos estilo Gnomo Palomo y lo entrego sin marca de agua.</p>'),
 ])

if __name__ == '__main__':
    C.publicar(D, 'capitulo-01.html')
    tot = sum(t['s'] for t in C.todas())
    print('tomas', len(C.todas()), 'segundos', tot)
