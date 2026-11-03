# Base común de los capítulos de EXTRAVÍO: piezas de los prompts (Omni 1.1 Flash, 16:9) y el armado de la página web.
import os, sys, html
here = os.path.dirname(os.path.abspath(__file__))
TEMP1 = os.path.join(here, '..', '..', 'viaje', 'temporada1')
sys.path.insert(0, TEMP1)
from datos import T, G, TR, END, VL  # noqa: E402
from datos_v2 import GX  # noqa: E402

ST = lambda s: (f"Horizontal 16:9 widescreen, {s} seconds. Photorealistic cinematic video, normal lens "
                "(no fisheye, no vignette, no dark corners), sharp, natural colors, realistic physics. One continuous shot with no cuts. Full 16:9 frame from edge to edge, no black bars, no letterbox. "
                "Keep the main character near the center of the frame.")
VERT = lambda p: p.replace("Horizontal 16:9 widescreen", "Vertical 9:16").replace(" Full 16:9 frame from edge to edge, no black bars, no letterbox.", " Full vertical frame, no black bars.").replace(" Keep the main character near the center of the frame.", "")

LU = ("Lucho, the skinny scruffy gray street mouse from the reference standing on two legs (huge dark eye bags, big round tired eyes, "
      "one crooked front tooth, torn black hoodie, small worn backpack full of old keys), holding a chunk of yellow cheese,")
BALL = "a small yellow rubber squeaky ball"
VTO = "in a deep, slow, sleepy male voice"
# Voz de Toffee para que la haga Flow (prueba aprobada por Jay el 29-oct-2026; sale de su descripción de ElevenLabs)
VOZ_TOFFEE = ("with a light, soft and sweet young adult male voice (a 20-year-old young man, light tenor): warm, round and cozy, sleepy and lazy, "
              "slow pace with soft sighs, clear and slightly formal diction, subtle smug charm and dry humor, effortless and sincere. "
              "Clearly an adult young man, not a child, not a woman, not falsetto, not squeaky, not cartoonish")
VLU = "in a hoarse, raspy, quiet male voice, slightly short of breath"

def HT(line, voice=VTO, verb="says"):
    return f'The cat {verb} in Latin American Spanish, {voice}: "{line}" His lips move in sync with every word.'
def HLU(line, verb="says"):
    return f'The mouse {verb} in Latin American Spanish, {VLU}: "{line}" His mouth moves in sync with every word.'

REF = dict(T="TOFFEE-viajero.jpg", G="GALLETA-viajero.jpg", S="REF-trineo-rojo.jpg", L="LUCHO.jpg", R="REMOLINO.jpg",
           M="MAR-DE-PELOTAS.jpg", C="EXTRAVIO-CIUDAD.jpg", X="PLACA-MAX.jpg", P="POLILLA.jpg", F="FONDO-PANTALLA-FINAL.jpg",
           K="MERCADO-DE-LLAVES.jpg", O="RECUERDO.jpg", Q="CALLE-EXTRAVIO.jpg")

class Cap:
    def __init__(self, n, verticales=()):
        self.n, self.ESC, self.N, self.V = n, [], 0, set(verticales)
    def esc(self, t, f): self.ESC.append(dict(t=t, f=f, tomas=[]))
    def tk(self, s, fotos, p, voz=None, quien=None, cont=None, gancho=False, nota=None):
        self.N += 1
        import re
        p = re.sub(r'([.!?)] )the ', lambda m: m.group(1) + 'The ', p).replace(',,', ',')
        self.ESC[-1]['tomas'].append(dict(n=self.N, s=s, fotos=[REF[x] for x in fotos], p=p, voz=voz, quien=quien,
                                          cont=cont, gancho=gancho, nota=nota, v=self.N in self.V))
    def todas(self): return [t for e in self.ESC for t in e['tomas']]
    def toma(self, n): return next(t for t in self.todas() if t['n'] == n)

    def page(self, d):
        e_ = html.escape
        tot = sum(t['s'] for t in self.todas())
        h = [f'<h1>Extravío · Capítulo {self.n}: {e_(d["titulo"])}</h1>',
             f'<p class="sub">Toffee y Galleta · Temporada 1 «La llave de casa» · {len(self.todas())} tomas ({tot//60}:{tot%60:02d} sin recortar) · Omni 1.1 Flash · <b>16:9 horizontal</b> (+ {len(self.V)} tomas también en 9:16 para shorts)</p>']
        for titulo, cuerpo in d['secciones']:
            h.append(f'<h2>{e_(titulo)}</h2>{cuerpo}')
        h.append('<h2>Voces (primero las voces, después las tomas)</h2>')
        for nombre, nota, texto in d['voces']:
            h.append(f'<h3>{e_(nombre)}</h3><p class="sub">{e_(nota)}</p><pre>{e_(texto)}</pre>')
        for titulo, nota, pr in d.get('imagenes', []):
            h.append(f'<h3>{e_(titulo)}</h3><p class="sub">{e_(nota)}</p><pre>{e_(pr)}</pre>')
        h.append('<h2>Las tomas</h2>')
        for es in self.ESC:
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
        for titulo, cuerpo in d['final']:
            h.append(f'<h2>{e_(titulo)}</h2>{cuerpo}')
        return "\n".join(h)

    def publicar(self, d, nombre):
        src = open(os.path.join(TEMP1, 'build_web.py')).read()
        head = src[src.index("head = '''") + 10: src.index("'''", src.index("head = '''") + 10)]
        head = head.replace('<title>El viaje de Toffee</title>', f'<title>Extravío · Capítulo {self.n}</title>')
        script = src[src.index("<script>"): src.index("</script>") + 9]
        os.makedirs(os.path.join(here, 'web'), exist_ok=True)
        page = self.page(d).replace('<table>', '<div class="tabla"><table>').replace('</table>', '</table></div>')
        open(os.path.join(here, 'web', nombre), 'w').write(head + '<main>' + page + '</main>\n' + script)
