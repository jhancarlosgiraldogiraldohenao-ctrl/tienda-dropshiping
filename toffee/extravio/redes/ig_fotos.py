# Fotos para el perfil de Instagram de Dizzy (6-nov-2026). python3 toffee/extravio/redes/ig_fotos.py
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "serie", "cap02"))
import cap02_recursos as R
AQUI = os.path.dirname(os.path.abspath(__file__))
FIN = (" Photorealistic 3D animated film style, cinematic light, sharp details, expressive faces, funny and flashy,"
       " no humans, no text, no letters, no logos, no readable printing on money or signs. Vertical 3:4.")
R.SECC = [
 ("Carrusel «Así se ve mi 2027» (Nano Banana Pro, vertical 3:4)",
  "Adjunta la foto del personaje (DIZZY-FRENTE, TOCINO-FRENTE, CUCA-FRENTE, GERTRUDIS-FRENTE) como referencia. La última foto es el chiste: la realidad.", [
  ("FOTO 1 · DIZZY-PLATA", "Adjunta DIZZY-FRENTE.",
   "Using the attached image as the exact same character (same rat, same flat cap with the little camera on top, same chain, socks and sandals), the rat sits like a king on a huge pile of shiny colorful soda bottle caps mixed with thick stacks of green paper money, throwing bills into the air with one hand, money raining around him, a cocky smirk, gold sunglasses, inside a dark room with purple and orange neon lights." + FIN),
  ("FOTO 2 · DIZZY-CADENAS", "Adjunta DIZZY-FRENTE.",
   "Using the attached image as the exact same character (same rat, same flat cap with the little camera on top, socks and sandals), the rat poses low-angle at night, leaning on the hood of a shiny red sports car his size, wearing five thick gold chains and a big gold chain with a bottle cap pendant, a shiny gold tooth in his cocky smile, arms crossed, a Colombian city street with neon lights and wet asphalt behind him." + FIN),
  ("FOTO 3 · TOCINO-JACUZZI", "Adjunta TOCINO-FRENTE y CUCA-FRENTE.",
   "Using the attached images as the exact same characters: the pig sits in a bubbling hot tub on a rooftop at night with city lights behind, wearing sunglasses and a gold chain, one arm around each of two flirty cockroach ladies (the attached cockroach and a second similar cockroach with pink hoop earrings), both laughing and holding glasses of soda with straws, the pig winking and blowing a kiss to the camera, his guitar resting on the edge of the tub, balloons and confetti, party mood, playful and funny, not sexual." + FIN),
  ("FOTO 4 · YATE", "Adjunta DIZZY-FRENTE y TOCINO-FRENTE.",
   "Using the attached images as the exact same characters: the rat (left) and the pig (right) stand on the deck of a small white luxury yacht on a turquoise Caribbean sea at sunset, old colonial city walls and colorful houses in the distance, the rat shaking a big soda bottle that sprays foam everywhere, the pig playing his guitar with sunglasses, both wearing gold chains, soda bottle caps scattered on the deck, golden hour light." + FIN),
  ("FOTO 5 · LA REALIDAD (el chiste)", "Adjunta DIZZY-FRENTE y GERTRUDIS-FRENTE.",
   "Using the attached images as the exact same characters: inside a humble old Colombian farmhouse kitchen with a wood-fired clay stove, the rat stands in the center holding a broom and sweeping, looking tired and annoyed, while the grandma hen stands behind him on the right with one wing on her hip and a sandal raised in the other wing, giving him a strict look, morning light through a small window, funny contrast." + FIN),
 ]),
]
if __name__ == "__main__":
    md = R.md().replace(R.md().split("\n## ")[0], "# Instagram de Dizzy · carrusel «Así se ve mi 2027» (6-nov-2026)\n")
    open(os.path.join(AQUI, "IG-FOTOS-2027.md"), "w").write(md)
    h = R.web().replace("<title>Capítulo 2 México</title>", "<title>Fotos Instagram Dizzy</title>").replace(
        "Extravío · Capítulo 2 · México 💀🌼", "Instagram de Dizzy · «Así se ve mi 2027» 💸").replace(
        "Personajes, lugares, música, sonidos y voces.", "5 fotos para el primer carrusel.")
    os.makedirs(os.path.join(AQUI, "web"), exist_ok=True)
    open(os.path.join(AQUI, "web", "ig-fotos-2027.html"), "w").write(h)
    print("ok")
