# -*- coding: utf-8 -*-
import html, sys
sys.path.insert(0, '.')
from datos import DIAS, FOTOS

e = html.escape
RED_COLOR = {'TikTok': '#16213E', 'Instagram': '#9C5A1B', 'YouTube': '#4F6E43'}
RED_TIPO = {'TikTok': 'El chiste', 'Instagram': 'El consejo', 'YouTube': 'La historia'}


def chips(cast):
    out = []
    for c in cast:
        f, n = FOTOS[c]
        out.append(f'<span class="chip"><img src="img/{f}.jpg">{e(f)}.jpg</span>')
    return ''.join(out)


def video_html(dia, v, primero=False):
    total = sum(t['dur'] for t in v['tomas'])
    ntomas = len(v['tomas'])
    con_voz = any(t['voz'] for t in v['tomas'])
    col = RED_COLOR[v['red']]
    h = [f'<section class="video">']
    if primero:
        h.append(f'<h2>Día {dia["n"]} · {e(dia["fecha"])}</h2>')
    h.append(f'<div class="vhead" style="background:{col}"><span>Día {dia["n"]} · Video {v["letra"]}</span>'
             f'<span>Pensado para {v["red"]} · {RED_TIPO[v["red"]]}</span></div>')
    h.append(f'<h3>{e(v["titulo"])}</h3>')
    tomas_txt = '1 toma' if ntomas == 1 else f'{ntomas} tomas de 8 s que se unen'
    h.append(f'<p class="meta"><b>{total} s</b> · {tomas_txt} · Voz de Toffee: <b>{"SÍ" if con_voz else "NO"}</b> · '
             f'Palabra: <b>{e(v["palabra"])}</b></p>')
    h.append(f'<p class="porque"><b>Por qué funciona:</b> {e(v["porque"])}</p>')
    for i, t in enumerate(v['tomas'], 1):
        h.append('<div class="toma">')
        h.append('<div class="izq">')
        h.append(f'<div class="tomah">Toma {i} de {ntomas} · <b>{t["dur"]} segundos</b></div>')
        h.append(f'<div class="fotos"><span class="lbl">Fotos para añadir:</span>{chips(t["cast"])}</div>')
        h.append(f'<pre class="prompt">{e(t["prompt"])}</pre>')
        h.append('</div><div class="der">')
        h.append('<div class="gh">Guion</div>')
        if t['voz']:
            h.append(f'<p class="voz"><span>🎙️ Voz de Toffee</span>{e(t["voz"])}</p>')
        else:
            h.append('<p class="voz nov"><span>🎙️ Voz</span>No lleva voz.</p>')
        if t['texto']:
            h.append(f'<p class="txt"><span>🔤 Texto en pantalla (lo pongo yo)</span>{e(t["texto"])}</p>')
        h.append('</div></div>')
    h.append(f'<p class="edic"><b>✂️ Edición (yo):</b> {e(v["edicion"])}</p>')
    h.append('<div class="pub">')
    h.append(f'<div><span>Descripción (TikTok e Instagram)</span><p>{e(v["desc"]).replace(chr(10), "<br>")}</p></div>')
    h.append(f'<div><span>Título (YouTube Shorts)</span><p>{e(v["yt"])}</p></div>')
    h.append(f'<div><span>Hashtags (en las 3 redes)</span><p class="tags">{e(v["tags"])}</p></div>')
    h.append('</div></section>')
    return '\n'.join(h)


def calendario():
    filas = []
    for d in DIAS:
        cel = [f'<td class="d"><b>Día {d["n"]}</b><br>{e(d["fecha"])}</td>']
        for v in d['videos']:
            total = sum(t['dur'] for t in v['tomas'])
            cel.append(f'<td>{e(v["titulo"])}<br><small>{total} s · {e(v["palabra"])}</small></td>')
        filas.append('<tr>' + ''.join(cel) + '</tr>')
    return ('<table class="cal"><tr><th></th><th style="background:#16213E">A · El chiste<br><small>pensado para TikTok</small></th>'
            '<th style="background:#9C5A1B">B · El consejo<br><small>pensado para Instagram</small></th>'
            '<th style="background:#4F6E43">C · La historia<br><small>pensado para YouTube</small></th></tr>' + ''.join(filas) + '</table>')


def refs():
    out = ['<div class="refs">']
    for k, (f, n) in FOTOS.items():
        out.append(f'<div><img src="img/{f}.jpg"><b>{e(n)}</b><small>{e(f)}.jpg</small></div>')
    out.append('</div>')
    return ''.join(out)


tomas_total = sum(len(v['tomas']) for d in DIAS for v in d['videos'])

HTML = f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Plan de videos Toffee · 7 días</title>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600;9..144,700&family=DM+Sans:wght@400;500;700&display=swap" rel="stylesheet">
<style>
@page {{ size: A4; margin: 14mm 13mm 16mm; }}
* {{ box-sizing: border-box; }}
body {{ font-family: 'DM Sans', sans-serif; color: #2B2118; font-size: 10pt; line-height: 1.45; margin: 0; }}
h1, h2, h3 {{ font-family: 'Fraunces', serif; color: #16213E; margin: 0 0 6px; }}
h1 {{ font-size: 28pt; line-height: 1.1; }}
h2 {{ font-size: 17pt; margin-top: 4px; border-bottom: 3px solid #E0954F; padding-bottom: 4px; }}
h3 {{ font-size: 14pt; margin-top: 6px; }}
h4 {{ font-family: 'Fraunces', serif; color: #9C5A1B; font-size: 12pt; margin: 12px 0 4px; }}
p {{ margin: 0 0 6px; }}
ul, ol {{ margin: 0 0 6px 18px; padding: 0; }} li {{ margin-bottom: 2px; }}
.salto {{ break-before: page; }}
.portada {{ background: #16213E; color: #FBF6EE; padding: 26px 26px 22px; border-radius: 14px; margin-bottom: 14px; }}
.portada h1 {{ color: #FBF6EE; }} .portada h1 em {{ color: #E0954F; font-style: italic; }}
.portada p {{ color: #F3E9D8; font-size: 11pt; }}
.tres {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px; margin: 10px 0; }}
.tres div {{ border-radius: 10px; padding: 10px; color: #FBF6EE; }}
.tres b {{ display: block; font-family: 'Fraunces', serif; font-size: 12pt; }}
.caja {{ background: #FBF6EE; border: 1px solid #E8DCC6; border-radius: 10px; padding: 10px 12px; margin: 8px 0; break-inside: avoid; }}
.caja.salvia {{ background: #E3EBDC; border-color: #C9D6BD; }}
.refs {{ display: grid; grid-template-columns: repeat(6, 1fr); gap: 6px; margin: 6px 0; }}
.refs div {{ text-align: center; font-size: 8pt; }} .refs img {{ width: 100%; aspect-ratio: 1; object-fit: cover; border-radius: 8px; display: block; margin-bottom: 3px; }}
.refs b, .refs small {{ display: block; }}
table {{ border-collapse: collapse; width: 100%; font-size: 9pt; }}
th {{ color: #FBF6EE; text-align: left; padding: 6px; background: #16213E; }}
td {{ border-bottom: 1px solid #E8DCC6; padding: 5px 6px; vertical-align: top; }}
.cal td.d {{ white-space: nowrap; background: #FBF6EE; }}
.video {{ break-before: page; }}
.vhead {{ color: #FBF6EE; display: flex; justify-content: space-between; padding: 6px 10px; border-radius: 8px; font-weight: 700; font-size: 9.5pt; }}
.meta {{ color: #6E5F56; font-size: 9.5pt; }}
.porque {{ background: #E3EBDC; border-radius: 8px; padding: 6px 9px; font-size: 9.3pt; }}
.toma {{ display: grid; grid-template-columns: 63% 37%; border: 1px solid #E8DCC6; border-radius: 10px; margin: 8px 0; break-inside: avoid; overflow: hidden; }}
.izq {{ padding: 8px 10px; }} .der {{ background: #FBF6EE; padding: 8px 10px; border-left: 1px solid #E8DCC6; }}
.tomah {{ font-size: 9.5pt; color: #16213E; margin-bottom: 4px; }}
.fotos {{ display: flex; flex-wrap: wrap; gap: 4px; align-items: center; margin-bottom: 5px; }}
.lbl {{ font-size: 8.5pt; font-weight: 700; color: #9C5A1B; margin-right: 2px; }}
.chip {{ display: inline-flex; align-items: center; gap: 4px; background: #F3E9D8; border-radius: 99px; padding: 2px 8px 2px 2px; font-size: 8pt; }}
.chip img {{ width: 20px; height: 20px; border-radius: 50%; object-fit: cover; }}
pre.prompt {{ white-space: pre-wrap; word-wrap: break-word; font-family: 'DejaVu Sans Mono', monospace; font-size: 7.6pt; line-height: 1.38; background: #F6F1E7; border-radius: 6px; padding: 7px 8px; margin: 0; color: #2B2118; }}
.gh {{ font-family: 'Fraunces', serif; color: #16213E; font-size: 11pt; margin-bottom: 4px; }}
.voz, .txt {{ font-size: 9.4pt; margin-bottom: 8px; }}
.voz span, .txt span {{ display: block; font-size: 8pt; font-weight: 700; color: #9C5A1B; text-transform: uppercase; letter-spacing: .04em; margin-bottom: 2px; }}
.voz {{ font-size: 10.5pt; color: #16213E; }} .voz.nov {{ color: #6E5F56; font-size: 9.4pt; }}
.edic {{ font-size: 9.3pt; }}
.pub {{ border: 2px solid #E0954F; border-radius: 10px; padding: 8px 10px; break-inside: avoid; }}
.pub span {{ display: block; font-size: 8pt; font-weight: 700; color: #9C5A1B; text-transform: uppercase; letter-spacing: .04em; }}
.pub p {{ margin-bottom: 6px; }} .tags {{ color: #16213E; font-weight: 700; }}
.chonk img {{ width: 100%; border-radius: 8px; margin: 4px 0; }}
.dato {{ display: inline-block; background: #16213E; color: #FBF6EE; border-radius: 8px; padding: 6px 10px; margin: 0 6px 6px 0; font-size: 9pt; }}
.dato b {{ display: block; font-family: 'Fraunces', serif; font-size: 13pt; color: #FFD27A; }}
.resp {{ font-size: 9pt; background: #fff; border-left: 3px solid #E0954F; padding: 4px 8px; margin: 4px 0; }}
</style></head><body>

<div class="portada">
<p style="letter-spacing:.12em;text-transform:uppercase;font-size:9pt;color:#E0954F;font-weight:700">Soy Toffee · Plan de videos</p>
<h1>7 días, <em>3 videos diarios</em></h1>
<p>Del sábado 24 al viernes 30 de octubre de 2026. Son 21 videos ({tomas_total} tomas para generar en Google Flow con Omni Flash 1.1, a 720p y en vertical 9:16). Cada video está pensado para una red, pero <b>los 3 se suben en las 3 redes</b>, para ver qué funciona dónde.</p>
<p>Lo hice con tu estudio (Víctor Heras, los 27 videos virales y los que venden, y tus números), con lo que funciona en cada red y con el análisis de la cuenta de Chonk.</p>
</div>

<div class="tres">
<div style="background:#16213E"><b>A · El chiste</b>Pensado para TikTok. Humor, una situación absurda, un giro. Corto (6–10 s), una sola toma, el final empalma con el inicio. Casi siempre sin voz.</div>
<div style="background:#9C5A1B"><b>B · El consejo</b>Pensado para Instagram. Soluciona un problema o es «esto es mi perro». Texto en pantalla. 16 s (2 tomas de 8 s), con voz.</div>
<div style="background:#4F6E43"><b>C · La historia</b>Pensado para YouTube. «El diario de Galleta», por capítulos: inicio, problema, final. 24–32 s (3–4 tomas de 8 s), con voz. Título que la gente busca.</div>
</div>

<h2>El calendario</h2>
{calendario()}

<h2 class="salto">Antes de empezar (léelo una vez)</h2>
<h4>Las fotos que vas a añadir en Flow (Ingredientes, máximo 3 por toma)</h4>
<p>Cada toma te dice cuáles. Son tus fotos oficiales, las mismas de siempre:</p>
{refs()}
<div class="caja"><b>Cómo generar en Flow</b>
<ol>
<li>Modelo <b>Omni Flash 1.1</b>, 720p, vertical 9:16, con la <b>duración que dice cada toma</b> (6, 8 o 10 s).</li>
<li>Añade las fotos de la toma como Ingredientes y pega el prompt <b>completo</b> (está en inglés porque Flow lo entiende mejor).</li>
<li>Genera 2 versiones de cada toma y quédate con la que tenga a Toffee y a Galleta más parecidos a las fotos.</li>
<li>Si una toma sale con el gorro raro, con dos gatos o con el perro cambiando de color, se repite: no la arregla la edición.</li>
</ol></div>
<div class="caja"><b>La voz de Toffee</b>
<ul>
<li>La pones tú, con tu voz de siempre. Flow solo pone el sonido del ambiente; todos los prompts le piden «sin voces» y que los animales tengan la boca cerrada (es <b>voz en off</b>, como la de Jake el perro).</li>
<li>El guion de cada toma dura lo que la toma (unos 8 s). Si al leerlo no cabe, súbele un poquito la velocidad (1,1×) o mándamelo y lo ajusto.</li>
<li>Los videos A no llevan voz: el sonido lo pone el <b>audio en tendencia que eliges en TikTok el día que publicas</b> (regla 6 de tu estudio).</li>
</ul></div>
<div class="caja"><b>Al publicar (de tu estudio)</b>
<ul>
<li>Sube el <b>archivo limpio que yo te devuelvo</b> en las 3 redes. Nunca bajes el de TikTok para subirlo a otra red: lleva marca de agua y lo castigan.</li>
<li>Instagram: cuenta de creador; publica tú a mano (el programador de Instagram le quita alcance) o con Metricool.</li>
<li>Activa siempre la etiqueta de <b>contenido creado con IA</b>.</li>
<li>Nada de fechas límite ni «últimas unidades». Las orejeras <b>amortiguan</b>: nunca decir que eliminan el ruido o curan el miedo.</li>
<li>No compartas tus videos en grupos ni pidas likes; no pongas anuncios.</li>
</ul></div>
<div class="caja salvia"><b>Respuestas a las palabras clave (cópialas como Toffee)</b>
<p class="resp"><b>CALMA:</b> ¡Humano! Aquí Toffee 😼 Las orejeras de Galleta están en soytoffee.store (el enlace está en mi perfil). Envío gratis y pagas con PSE, Nequi o tarjeta en cuotas. Y el 3 % va a mi marrano para perritos de la calle 🐷 ¿Desde qué país me escribes?</p>
<p class="resp"><b>ÁRBOL:</b> ¡Humano! Aquí Toffee 😼 El disfraz de árbol está en soytoffee.store (el enlace está en mi perfil). Es para mascotas de 1,5 a 7,5 kg. Envío gratis y pagas con PSE, Nequi o en cuotas 🎄 ¿Desde qué país me escribes?</p>
<p class="resp"><b>TRINEO:</b> ¡Humano! Aquí Toffee 😼 Mi cama trineo está en soytoffee.store (el enlace está en mi perfil). Mide 50 × 38 × 26 cm y tiene bordes altos, como me gusta. Envío gratis y pagas con PSE, Nequi o en cuotas 🛷 ¿Desde qué país me escribes?</p>
<p class="resp"><b>FONDO:</b> ¡Humano! Aquí Toffee 😼 Te mandé tu fondo de pantalla por mensaje 🐾 Si no te llega, sígueme y escríbeme «FONDO» por mensaje.</p>
</div>

<h2 class="salto">Lo que aprendí de Chonk (@fatchonkywizardcat)</h2>
<p>Revisé el perfil y sus 2 videos más vistos cuadro por cuadro, con sus números reales (sacados de TikTok el 23-oct). <b>Ojo:</b> TikTok no deja ver la lista de sus 93 videos sin iniciar sesión, así que no pude revisarlos todos. Lo que sí se ve en las búsquedas públicas de TikTok: hace bailes («chonk dance», «wiggle») y una serie por capítulos, «Tales of Chonk» (<a href="https://www.tiktok.com/discover/wizard-cat">TikTok · wizard cat</a>).</p>
<div>
<span class="dato"><b>159.500</b>seguidores</span><span class="dato"><b>6,9 M</b>likes</span><span class="dato"><b>93</b>videos</span><span class="dato"><b>1-oct-2026</b>creó la cuenta (≈ 4 videos al día)</span><span class="dato"><b>Tienda propia</b>chonkwizardcat.com</span>
</div>
<div class="caja chonk"><b>Video 1 · «my owner loves playing with me 😸» · 3-oct (a los 2 días de abrir la cuenta)</b>
<p>12,5 M vistas · 3,1 M likes (25 de cada 100) · <b>2 M compartidos (16 de cada 100)</b> · 290 mil guardados · 6 segundos.</p>
<img src="img/chonk-7692436985079680269.jpg">
<p>La cámara está abajo mirando hacia arriba; el dueño le toma las patitas y la cara se acerca al lente; la cámara gira. Una sola toma, sin texto y sin voz.</p></div>
<div class="caja chonk"><b>Video 2 · «hiii friends! My name is CHONK👋» · 5-oct</b>
<p>5 M vistas · 756 mil likes · 429 mil compartidos · 87 mil guardados · 8 segundos.</p>
<img src="img/chonk-7693230825734720782.jpg">
<p>Cámara en el piso: el gato saluda con la pata al lente, con un sticker «hallo👋» que gira con la cámara; el teléfono «se cae», la cara queda al revés («hiii👋») y termina en la misma cara del inicio. Se repite solo.</p></div>
<h4>Lo que tomamos para Toffee</h4>
<ol>
<li><b>Su look es casi el de Toffee</b> (gato crema, redondo, con gorro azul oscuro) y llegó a 159 mil en 3 semanas. Eso confirma que el look de Toffee gusta. Pero <b>no lo copiamos</b>: Toffee usa gorro de dormir (no de mago), habla español, vive en Colombia, tiene a Galleta y una causa. Eso es lo que Chonk no tiene.</li>
<li><b>Cámara al ras del piso o pegada a la cara</b>, y el gato que toca el lente: se siente como si fuera tu gato. Lo usan los videos A del día 1 y del día 3.</li>
<li><b>6 a 8 segundos, una toma, el final igual al inicio.</b> Todos los videos A son así.</li>
<li><b>Sin voz y con una palabra en pantalla</b> como sticker («hola, humano 👋», «lunes.»).</li>
<li><b>Descripción corta en primera persona y pocos hashtags.</b> Chonk escribe como si el gato hablara y usa 3 hashtags. Tu estudio dice tercera persona; por eso probamos las dos: los A van en primera persona (como Chonk) y los B y C en tercera (como dice tu estudio). En una semana vemos cuál gana.</li>
<li><b>Ternura que se comparte:</b> cachetes contra el lente, patitas, ojos grandes. Su mejor video tiene 16 de cada 100 compartiendo: es lo que más empuja.</li>
<li><b>Publica mucho:</b> unos 4 videos al día. Tu plan de 3 diarios va en la misma línea.</li>
</ol>

{''.join(video_html(d, v, i == 0) for d in DIAS for i, v in enumerate(d['videos']))}

<h2 class="salto">Cómo me mandas los clips para editar</h2>
<div class="caja"><b>Ponles este nombre</b> (así sé cuál es cuál):
<ul>
<li>Video A: <b>D1-A.mp4</b> (una sola toma).</li>
<li>Videos B y C: <b>D1-B-1.mp4, D1-B-2.mp4</b>… y <b>D1-C-1.mp4</b> hasta <b>D1-C-4.mp4</b>.</li>
<li>La voz: <b>D1-B-voz.mp3</b> y <b>D1-C-voz.mp3</b> (puede ser un solo audio por video, leyendo todo el guion seguido).</li>
</ul></div>
<div class="caja"><b>Lo que hago yo con cada video</b>
<ol>
<li>Uno las tomas y recorto lo que sobra (el inicio lento, los cuadros raros del final).</li>
<li>Pongo la voz encima y bajo el sonido de Flow para que se entienda.</li>
<li>Subtítulos grandes y legibles, y el texto en pantalla que dice cada toma, con los colores de Toffee.</li>
<li>Mejoro la calidad: lo paso de 720p a <b>1080 × 1920</b> (lo que piden las redes), con más nitidez y menos ruido. Ojo: mejora lo que hay, no inventa detalles que Flow no generó.</li>
<li>Te devuelvo <b>D1-A-final.mp4</b>, <b>D1-B-final.mp4</b> y <b>D1-C-final.mp4</b>, listos para subir a las 3 redes.</li>
</ol></div>
<div class="caja salvia"><b>Cómo vamos a medir (cada noche, 2 minutos; el día 7 decidimos)</b>
<table>
<tr><th>Red</th><th>Número clave</th><th>Dónde lo ves</th></tr>
<tr><td>TikTok</td><td>% que lo vio completo y tiempo promedio</td><td>Video → Estadísticas</td></tr>
<tr><td>Instagram</td><td>Veces compartido y guardados</td><td>Reel → Ver estadísticas</td></tr>
<tr><td>YouTube</td><td>«Lo vieron» contra «Lo deslizaron»</td><td>YouTube Studio → Contenido → el Short</td></tr>
<tr><td>Las 3</td><td>Comentarios con CALMA, ÁRBOL, TRINEO o FONDO</td><td>Comentarios</td></tr>
</table>
<p style="margin-top:6px">Anota cuál de los 3 videos (A, B o C) ganó en cada red. Con eso, la semana 2 hacemos más del que ganó (tu estudio: el 80 % no funciona; se repite el 20 % que sí, con otro gancho).</p></div>
</body></html>'''

open('plan.html', 'w').write(HTML)
print('ok', tomas_total)
