import html, sys, subprocess, os
sys.path.insert(0, os.path.dirname(__file__))
import datos as D, re
cap = lambda p: re.sub(r'([.!?] )the ', lambda m: m.group(1)+'The ', p)
E = html.escape

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&family=JetBrains+Mono:wght@400&display=swap');
body{font-family:Inter,sans-serif;color:#2B211C;font-size:10.5pt;line-height:1.45;margin:0}
h1{font-size:26pt;color:#16213E;margin:0 0 6px}
h2{font-size:17pt;color:#16213E;border-bottom:3px solid #E0954F;padding-bottom:4px;margin:22px 0 8px;page-break-before:always}
h4{font-size:11pt;color:#B2541A;margin:10px 0 3px}
h3{font-size:12pt;color:#16213E;margin:14px 0 4px}
.sub{color:#6E5F56}
.box{background:#FFF6EC;border-left:4px solid #E0954F;padding:8px 12px;margin:8px 0;border-radius:4px}
.toma{border:1px solid #E7D9CC;border-radius:6px;padding:8px 10px;margin:10px 0;page-break-inside:avoid}
.meta{font-weight:600;color:#16213E}
.chip{display:inline-block;background:#16213E;color:#fff;border-radius:10px;padding:1px 8px;font-size:8.5pt;margin-right:4px}
.cont{color:#B2541A;font-weight:600}
pre{font-family:'JetBrains Mono',monospace;font-size:8.3pt;white-space:pre-wrap;background:#F4F1EE;padding:7px 9px;border-radius:4px;margin:6px 0}
.voz{color:#16213E}
table{border-collapse:collapse;width:100%;font-size:9.5pt}td,th{border:1px solid #E7D9CC;padding:4px 6px;vertical-align:top}th{background:#16213E;color:#fff;text-align:left}
"""

def build():
    o = [f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body>"]
    o.append("<h1>El viaje de Toffee · Estudio + Sección 1</h1><p class='sub'>Vlogs 2 al 15 · 26 de octubre al 8 de noviembre de 2026 · Halloween → Día de Muertos → América</p>")
    o.append("""<div class='box'><b>Cómo usar este PDF (igual que el vlog 1)</b><ol>
<li><b>Antes de cada vlog</b>, si tiene un personaje nuevo, haz primero su ficha en Nano Banana Pro (página «Personajes nuevos») y guárdala.</li>
<li>Cada toma: <b>Omni 1.1 Flash · 9:16 · los segundos que dice</b>. Sube las fotos que dice (TOFFEE = TOFFEE-viajero.jpg, GALLETA = GALLETA-viajero.jpg, TRINEO = REF-trineo-rojo.jpg, OREJERAS = REF-orejeras-gris.jpg, DISFRAZ = REF-disfraz-verde.jpg).</li>
<li>Si dice <b>Primer cuadro</b>, mándame la toma anterior y yo te saco el último cuadro.</li>
<li>Copia el prompt completo. Si la toma no sale como dice, <b>se repite</b> (mándamela y te digo qué falló).</li>
<li>Voces: genera en ElevenLabs <b>todas las frases de Toffee de un vlog juntas</b> (cuadro «Voces de Toffee» al final de cada vlog) y aparte las de cada personaje con su voz fija.</li>
<li>Me mandas las tomas aprobadas + las voces y yo edito: subtítulos en español, título arriba, cortes, boca sincronizada.</li></ol></div>""")
    import markdown
    est = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'ESTUDIO-GNOMO-Y-LOCO-BLANCO.md')).read()
    import re
    L = est.split('\n'); F = []
    for ln in L:
        isl = bool(re.match(r'\s*([-*]|\d+\.) ', ln))
        if isl and F and F[-1].strip() and not re.match(r'\s*([-*]|\d+\.) ', F[-1]) and not F[-1].startswith('  '): F.append('')
        F.append(re.sub(r'^  (?=[-*] )', '    ', ln))
    est = '\n'.join(F)
    o.append("<div class='estudio'>" + markdown.markdown(est, extensions=['tables']).replace('h3>', 'h4>').replace('h2>', 'h3>').replace('h1>', 'h2>') + "</div>")
    o.append("<h2>Personajes nuevos (fichas para Nano Banana Pro · formato 1:1)</h2>")
    for nom, arch, desc, p in D.FICHAS:
        o.append(f"<div class='toma'><span class='meta'>{E(nom)}</span> → guárdala como <b>{E(arch)}</b><br><span class='sub'>{E(desc)}</span><pre>{E(p)}</pre></div>")
    o.append("<h3>Voces fijas en ElevenLabs</h3><table><tr><th>Personaje</th><th>Qué voz usar</th></tr>")
    for a, b in D.VOCES: o.append(f"<tr><td>{E(a)}</td><td>{E(b)}</td></tr>")
    o.append("</table><p class='sub'>Galleta, el Chupacabras, el alebrije, Paca y el chihuahua no hablan (así hay menos voces que cuidar).</p>")
    for v in D.VLOGS:
        o.append(f"<h2>Vlog {v['n']} · {E(v['titulo'])}</h2><p><span class='chip'>{E(v['fecha'])}</span><span class='chip'>{len(v['tomas'])} tomas</span>"
                 + (f"<span class='chip'>Ficha nueva: {E(', '.join(v['fichas']))}</span>" if v['fichas'] else "") + "</p>")
        o.append(f"<div class='box'><b>La historia:</b> {E(v['resumen'])}<br><b>Texto arriba (lo pongo yo):</b> {E(v['arriba'][0])} <b style='color:#E0954F'>{E(v['arriba'][1])}</b></div>")
        toff = []
        for i, (s, fotos, cont, p, vt, vo) in enumerate(v['tomas'], 1):
            gz = " <span class='chip' style='background:#E0954F'>⭐ GANCHO: va primero en la edición</span>" if i == v['gancho'] else ""
            o.append(f"<div class='toma'><span class='meta'>Toma {i} · Omni 1.1 Flash · {s} s</span>{gz} · Fotos: <b>{E(fotos)}</b>"
                     + (f"<br><span class='cont'>Primer cuadro: {E(cont)}</span>" if cont else "") + f"<pre>{E(cap(p))}</pre>")
            if vt: o.append(f"<div class='voz'>🎙️ Toffee: {E(vt)}</div>")
            if vo: o.append(f"<div class='voz'>🎙️ {E(vo)}</div>")
            o.append("</div>")
            if vt and vt.startswith('«'):
                toff.append(vt.split('»')[0].strip('«'))
        o.append("<div class='box'><b>Voces de Toffee de este vlog (copiar todo junto en ElevenLabs):</b><pre>" + E("\n\n".join(toff)) + "</pre></div>")
    import musica as M
    o.append("<h2>Ruta del viaje hasta el 31 de diciembre</h2><table><tr><th>Sección</th><th>Fechas</th><th>Lugares y temas</th><th>Canciones</th></tr>")
    for a, b_, c, d in M.RUTA: o.append(f"<tr><td>{E(a)}</td><td>{E(b_)}</td><td>{E(c)}</td><td>{E(d)}</td></tr>")
    o.append(f"</table><div class='box'>{E(M.MICKEY)}</div>")
    o.append("<h2>Música y sonidos para hacer en ElevenLabs</h2>")
    o.append(f"<div class='box'><b>Cómo hacer cada canción:</b> {E(M.AJUSTES_MUSICA)}</div>")
    for c in M.CANCIONES:
        o.append(f"<div class='toma'><span class='meta'>🎵 {E(c['titulo'])}</span> <span class='chip'>{E(c['estado'])}</span><br><b>Para:</b> {E(c['uso'])}<br><span class='sub'>{E(c['porque'])}</span>")
        if c['estilo']:
            o.append(f"<pre>{E(c['estilo'])} Use these exact lyrics:\n\n{E(c['letra'])}</pre>")
        o.append("</div>")
    o.append("<h3>Jingles</h3><table><tr><th>Nombre del archivo</th><th>Qué escribir (Efectos de sonido o Música)</th></tr>")
    for n, f, p in M.JINGLES: o.append(f"<tr><td>{E(n)}<br><b>{E(f)}</b></td><td><code>{E(p)}</code></td></tr>")
    o.append("</table><h3>Efectos de sonido (ElevenLabs › Efectos de sonido)</h3><p class='sub'>Genera cada uno, descárgalo con el nombre de la izquierda y mándamelos todos juntos. Cuestan muy poco.</p><table><tr><th>Archivo</th><th>Qué escribir</th></tr>")
    for f, p in M.SFX: o.append(f"<tr><td><b>{E(f)}</b></td><td><code>{E(p)}</code></td></tr>")
    o.append("</table><h3>Más cosas de ElevenLabs para aprovechar</h3><table>")
    for n, d in M.EXTRAS: o.append(f"<tr><td><b>{E(n)}</b></td><td>{E(d)}</td></tr>")
    o.append("</table>")
    o.append("</body></html>")
    return "\n".join(o)

if __name__ == '__main__':
    here = os.path.dirname(os.path.abspath(__file__))
    open(os.path.join(here, 'plan.html'), 'w').write(build())
    out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(here, '..', '..', 'VIAJE-SECCION-1-PROMPTS.pdf')
    subprocess.run(['node', os.path.join(here, 'pdf.js'), os.path.abspath(out)], cwd=here, check=True)
    print('ok', out)
