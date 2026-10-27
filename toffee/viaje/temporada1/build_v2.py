import html, sys, subprocess, os, re
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, here)
import datos_v2 as D, musica as M
from build import CSS
E = html.escape
cap = lambda p: re.sub(r'([.!?] )the ', lambda m: m.group(1) + 'The ', p)
COLOR = {"INICIO": "#16213E", "DESARROLLO": "#3E6B8A", "OBSTÁCULO": "#B2541A", "RECOMPENSA": "#2E7D4F", "CONTINUACIÓN": "#7A4FA0"}

def tabla(cab, filas):
    o = ["<table><tr>" + "".join(f"<th>{E(c)}</th>" for c in cab) + "</tr>"]
    for f in filas: o.append("<tr>" + "".join(f"<td>{E(str(x))}</td>" for x in f) + "</tr>")
    return "".join(o) + "</table>"

def build():
    o = [f"<html><head><meta charset='utf-8'><style>{CSS} .fn{{display:inline-block;color:#fff;border-radius:10px;padding:1px 8px;font-size:8.5pt;margin-right:4px}}</style></head><body>"]
    o.append("<h1>El viaje de Toffee · Sección 1 (versión 2)</h1><p class='sub'>14 episodios · 27 de octubre al 19 de noviembre de 2026 · 4 episodios por semana + cortos, comerciales y fotos</p>")
    o.append("""<div class='box'><b>Qué cambió frente a la versión 1</b><ol>
<li><b>Primeros segundos:</b> cada episodio empieza con su toma GANCHO ⭐ y una promesa clara arriba.</li>
<li><b>Historias más simples:</b> un conflicto entendible y una recompensa por episodio. Cada toma tiene una sola función (inicio, desarrollo, obstáculo, recompensa, continuación).</li>
<li><b>Personalidades definidas:</b> Toffee antihéroe sarcástico con buen corazón; Galleta impulsivo, curioso y a veces el más listo, con 7 expresiones fijas.</li>
<li><b>Ritmo:</b> 4 episodios por semana (lun, mié, vie, dom), 3 cortos para gente nueva y 2 comerciales. Halloween se resume en 3 cascabeles y 4 episodios; se quitaron el mercado de las brujas y las escenas que no aportaban.</li>
<li><b>Productos con transparencia</b> y sin promesas que no podamos probar.</li>
<li><b>Medición semanal con datos</b> y propósito social verificable.</li></ol>
<b>Si ya generaste tomas del vlog 2 viejo:</b> sirven la lechuza aterrizando, la de los cinco cascabeles NO (ahora son tres), la del trineo que no arranca y la del camino de calabazas.</div>""")

    o.append("<h2>1 · Toffee y Galleta: quiénes son</h2>")
    for nom, k in (("🐱 Toffee", "toffee"), ("🐶 Galleta", "galleta")):
        o.append(f"<h3>{nom}</h3>" + tabla(["", ""], D.PERSONALIDAD[k]))
    o.append(f"<h3>Saludo de Toffee</h3><p>{E(D.SALUDO)}. Va en la primera frase que dice en cámara (no en todos los episodios: cuando hay un lugar nuevo).</p>")
    o.append("<h3>Frases de Toffee (se repiten para que se vuelvan suyas)</h3>" + tabla(["Momento", "Frases"], D.FRASES))
    o.append(f"<div class='box'>{E(D.GROSERIAS)}</div>")
    o.append("<h3>Las 7 expresiones de Galleta (así van en los prompts)</h3>" + tabla(["Expresión", "Texto en inglés que va en el prompt"], [(k, v) for k, v in D.GX.items()]))
    o.append("<h3>La relación</h3>" + tabla(["Situación", "Toffee", "Galleta"], [
        ("Aparece un problema", "Se queja y arma un plan complicado", "Intenta resolverlo ya"),
        ("Algo sale mal", "Busca a quién culpar", "Lo reconoce (aunque él lo causó)"),
        ("Un animal necesita ayuda", "Finge que no le importa… y ayuda", "Quiere ayudar desde el inicio"),
        ("Hay peligro", "«Estoy evaluando la situación»", "Tiene miedo, pero no abandona a Toffee"),
        ("Ganan", "Se queda con el mérito", "Celebra sin importar quién se lleva el crédito")]))

    o.append("<h2>2 · Cómo se arma cada episodio</h2><ol>" + "".join(f"<li>{E(r)}</li>" for r in D.GANCHO_REGLAS) + "</ol>")
    o.append("<p>" + " ".join(f"<span class='fn' style='background:{c}'>{f}</span>" for f, c in COLOR.items()) + "</p>")
    o.append("<h3>Elenco fijo del universo</h3>" + tabla(["Personaje", "Quién es"], D.ELENCO_FUTURO))

    o.append("<h2>3 · Calendario semanal</h2>" + tabla(["Día", "Publicación principal", "Segunda (solo si está buena)"], D.CALENDARIO))
    o.append("<p class='sub'>Es una guía, no una obligación. Si un segundo video no está bueno, no se publica. Cada publicación debe ofrecer algo distinto (no subir el mismo fragmento tres veces).</p>")
    for t, filas in D.SEMANAS: o.append(f"<h3>{E(t)}</h3>" + tabla(["Día", "Principal", "Segunda"], filas))

    o.append("<h2>4 · Personajes nuevos de esta versión</h2>")
    for nom, arch, desc, p in D.FICHAS_NUEVAS:
        o.append(f"<div class='toma'><span class='meta'>{E(nom)}</span> → guárdalo como <b>{E(arch)}</b><br><span class='sub'>{E(desc)}</span><pre>{E(p)}</pre></div>")
    o.append("<h3>Voces nuevas</h3>" + tabla(["Personaje", "Cómo crearla"], D.VOCES_NUEVAS))
    o.append("<p class='sub'>Ya aprobados: Doña Lechuza, Calabacín, Chupacabras, Alebrije, Paca y Chihuahua Enmascarado. Conde Murciélago: falta la medalla lisa.</p>")

    for e in D.EP:
        o.append(f"<h2>Episodio {e['n']} · {E(e['titulo'])}</h2><p><span class='chip'>{E(e['fecha'])}</span><span class='chip'>{len(e['tomas'])} tomas · {sum(t['s'] for t in e['tomas'])} s</span>"
                 + (f"<span class='chip'>Ficha nueva: {E(', '.join(e['fichas']))}</span>" if e.get('fichas') else "") + "</p>")
        o.append(f"<div class='box'><b>Conflicto:</b> {E(e['conflicto'])}<br><b>Recompensa:</b> {E(e['recompensa'])}<br><b>La historia:</b> {E(e['resumen'])}<br>"
                 f"<b>Texto arriba:</b> {E(e['arriba'][0])} <b style='color:#E0954F'>{E(e['arriba'][1])}</b>"
                 + (f"<br><b>Pregunta al público:</b> {E(e['pregunta'])}" if e.get('pregunta') else "")
                 + (f"<br><b>Producto:</b> {E(e['producto'])}" if e.get('producto') else "") + "</div>")
        toff = []
        for i, t in enumerate(e['tomas'], 1):
            gz = " <span class='chip' style='background:#E0954F'>⭐ GANCHO: va primero en la edición</span>" if t['gancho'] else ""
            o.append(f"<div class='toma'><span class='fn' style='background:{COLOR[t['f']]}'>{t['f']}</span><span class='meta'>Toma {i} · Omni 1.1 Flash · {t['s']} s</span>{gz} · Fotos: <b>{E(t['fotos'])}</b>"
                     + (f"<br><span class='cont'>Primer cuadro: {E(t['cont'])}</span>" if t['cont'] else "") + f"<pre>{E(cap(t['p']))}</pre>")
            if t['toffee']: o.append(f"<div class='voz'>🎙️ Toffee: {E(t['toffee'])}</div>")
            if t['otro']: o.append(f"<div class='voz'>🎙️ {E(t['otro'])}</div>")
            o.append("</div>")
            if t['toffee'] and t['toffee'].startswith('«'): toff.append(t['toffee'].split('»')[0].strip('«'))
        o.append("<div class='box'><b>Voces de Toffee de este episodio (todo junto en ElevenLabs):</b><pre>" + E("\n\n".join(toff)) + "</pre></div>")

    o.append("<h2>5 · Formato B: cortos para llegar a gente nueva (3 por semana)</h2>")
    o.append("<div class='box'>Antes de publicar: «Si alguien descubre a Toffee por este video, ¿entiende por qué es gracioso o especial y tiene una razón para seguirlo?». Si no, no aporta a la marca. Un baile de moda solo sirve si encaja con su personalidad.</div>")
    for c in D.CORTOS:
        o.append(f"<div class='toma'><span class='chip'>{E(c['tipo'])}</span><span class='meta'>{E(c['titulo'])} · {c['seg']} s</span> · Fotos: <b>{E(c['fotos'])}</b><br><span class='sub'>{E(c['idea'])}</span><pre>{E(cap(c['p']))}</pre><div class='voz'>🎙️ Toffee: {E(c['voz'])}</div><div class='sub'>{E(c['texto'])}</div></div>")

    o.append("<h2>6 · Formato C: comerciales integrados (2 por semana)</h2><ol>" + "".join(f"<li>{E(r)}</li>" for r in D.REGLAS_COMERCIAL) + "</ol>")
    for c in D.COMERCIALES:
        o.append(f"<div class='toma'><span class='chip'>{E(c['producto'])}</span><span class='meta'>{E(c['titulo'])}</span><br><span class='sub'>{E(c['situacion'])}</span>")
        for i, p in enumerate(c['tomas'], 1): o.append(f"<b>Toma {i}</b><pre>{E(cap(p))}</pre>")
        o.append(f"<div class='voz'>🎙️ Toffee: {E(c['voz'])}</div><div><b>Cierre:</b> {E(c['cierre'])}</div><div><b>Descripción:</b> {E(c['descripcion'])}</div></div>")

    o.append("<h2>7 · Fotos para Instagram (2 por semana)</h2><p class='sub'>En Nano Banana Pro, con las fichas de referencia. Alternar foto sola y carrusel. No volver todas un catálogo.</p>")
    for f in D.FOTOS:
        o.append(f"<div class='toma'><span class='chip'>{E(f['tipo'])}</span><span class='meta'>{E(f['formato'])}</span> · Fotos: <b>{E(f['fotos'])}</b><pre>{E(f['p'])}</pre><div><b>Texto:</b> {E(f['texto'])}</div></div>")

    o.append("<h2>8 · Cómo medir y decidir con datos</h2>" + tabla(["Tipo", "Pregunta", "Qué mirar"], D.METRICAS))
    o.append("<ol>" + "".join(f"<li>{E(r)}</li>" for r in D.REGLAS_MEDICION) + "</ol>")
    o.append("<h3>Cómo leer los resultados</h3>" + tabla(["Si pasa esto", "Revisa esto"], D.CASOS))

    o.append("<h2>9 · Propósito social y donaciones verificables</h2><ol>" + "".join(f"<li>{E(r)}</li>" for r in D.DONACIONES) + "</ol>")

    o.append("<h2>10 · Ruta hasta el 31 de diciembre</h2>" + tabla(["Sección", "Fechas", "Lugares y temas", "Canciones"], M.RUTA))
    o.append(f"<div class='box'>{E(M.MICKEY)}</div>")
    o.append("<h2>11 · Música y sonidos (ElevenLabs)</h2>")
    o.append(f"<div class='box'><b>Cómo hacer cada canción:</b> {E(M.AJUSTES_MUSICA)}</div>")
    for c in M.CANCIONES:
        o.append(f"<div class='toma'><span class='meta'>🎵 {E(c['titulo'])}</span> <span class='chip'>{E(c['estado'])}</span><br><b>Para:</b> {E(c['uso'])}<br><span class='sub'>{E(c['porque'])}</span>")
        if c['estilo']: o.append(f"<pre>{E(c['estilo'])} Use these exact lyrics:\n\n{E(c['letra'])}</pre>")
        o.append("</div>")
    o.append("<h3>Jingles y efectos de sonido</h3>" + tabla(["Archivo", "Qué escribir"], [(f, p) for n, f, p in M.JINGLES] + list(M.SFX)))
    o.append("</body></html>")
    return "\n".join(o)

if __name__ == '__main__':
    open(os.path.join(here, 'plan.html'), 'w').write(build())
    out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(here, '..', '..', 'VIAJE-SECCION-1-v2.pdf')
    subprocess.run(['node', os.path.join(here, 'pdf.js'), os.path.abspath(out)], cwd=here, check=True)
    os.remove(os.path.join(here, 'plan.html'))
    print('ok', out)
