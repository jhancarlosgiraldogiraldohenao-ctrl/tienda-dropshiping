# Genera la página web (Artifact) con el mismo contenido del PDF de la sección 1 v2.1
import re, os, sys, html
here = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, here)
import build_v2
raw = build_v2.build()
body = raw.split('<body>', 1)[1].rsplit('</body>', 1)[0]
toc = []
def add_id(m):
    t = re.sub('<[^>]+>', '', m.group(1)); slug = re.sub(r'[^a-z0-9]+', '-', html.unescape(t).lower().encode('ascii', 'ignore').decode()).strip('-')[:40]
    toc.append((slug, html.unescape(t))); return f'<h2 id="{slug}">{m.group(1)}</h2>'
body = re.sub(r'<h2>(.*?)</h2>', add_id, body)
nav = '<nav class="toc" aria-label="Contenido"><details><summary>Ir a…</summary><ul>' + ''.join(f'<li><a href="#{s}">{html.escape(t)}</a></li>' for s, t in toc) + '</ul></details></nav>'
head = '''<title>El viaje de Toffee</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600;9..144,800&family=DM+Sans:wght@400;600;700&family=JetBrains+Mono:wght@400&display=swap">
<style>
/* Libreta de producción: columna de lectura, tomas como fichas con botón Copiar; colores de la marca (marino, caramelo, crema) */
:root{--bg:#FBF6EE;--paper:#FFFFFF;--ink:#2B211C;--muted:#6E5F56;--line:#E7D9CC;--navy:#16213E;--caramel:#C9762F;--code:#F4EEE6;--box:#FFF3E4;
 --display:"Fraunces",Georgia,serif;--body:"DM Sans",system-ui,sans-serif;--mono:"JetBrains Mono",ui-monospace,monospace}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--bg:#11182C;--paper:#18213A;--ink:#EDE4D8;--muted:#A99C90;--line:#2C3756;--navy:#E9DCCB;--caramel:#E8A066;--code:#0E1426;--box:#1F2944;color-scheme:dark}}
:root[data-theme="dark"]{--bg:#11182C;--paper:#18213A;--ink:#EDE4D8;--muted:#A99C90;--line:#2C3756;--navy:#E9DCCB;--caramel:#E8A066;--code:#0E1426;--box:#1F2944;color-scheme:dark}
body{background:var(--bg);color:var(--ink);font:16px/1.55 var(--body);padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));padding-block:20px 60px}
main{max-width:760px;margin:0 auto}
h1{font-family:var(--display);font-weight:800;font-size:clamp(28px,6vw,40px);line-height:1.1;color:var(--navy);text-wrap:balance;margin:8px 0 6px}
h2{font-family:var(--display);font-weight:800;font-size:24px;color:var(--navy);margin:44px 0 10px;padding-top:10px;border-top:2px solid var(--caramel);text-wrap:balance;scroll-margin-top:12px}
h3{font-family:var(--display);font-weight:600;font-size:18px;color:var(--navy);margin:22px 0 6px}
h4{font-size:15px;color:var(--caramel);margin:14px 0 4px}
.sub{color:var(--muted);font-size:14px}
.box{background:var(--box);border-radius:10px;padding:12px 14px;margin:12px 0;font-size:15px}
.toma{background:var(--paper);border:1px solid var(--line);border-radius:10px;padding:12px 14px;margin:12px 0}
.meta{font-weight:700;color:var(--navy)}
.chip,.fn{display:inline-block;border-radius:999px;padding:2px 9px;font-size:12px;font-weight:600;margin:2px 4px 2px 0;color:#fff}
.chip{background:#16213E}
.cont{color:var(--caramel);font-weight:600}
.voz{margin-top:6px;font-size:15px}
pre{font:12.5px/1.5 var(--mono);white-space:pre-wrap;word-break:break-word;background:var(--code);border-radius:8px;padding:10px 12px;margin:8px 0;position:relative}
.copiar{display:block;margin:4px 0 0 auto;font:600 13px var(--body);background:var(--caramel);color:#fff;border:0;border-radius:999px;padding:7px 14px;cursor:pointer}
.copiar:focus-visible{outline:3px solid var(--navy);outline-offset:2px}
.tabla{overflow-x:auto;margin:10px 0}
table{border-collapse:collapse;width:100%;font-size:14px}
td,th{border:1px solid var(--line);padding:6px 8px;vertical-align:top;text-align:left}
th{background:#16213E;color:#fff}
code{font-family:var(--mono);font-size:12.5px}
ol,ul{padding-left:22px}
.toc details{background:var(--paper);border:1px solid var(--line);border-radius:10px;padding:8px 12px;margin:14px 0}
.toc summary{cursor:pointer;font-weight:700;color:var(--navy)}
.toc ul{columns:2 240px;margin:8px 0 0;font-size:14px}
.toc a{color:var(--ink)}
a{color:var(--caramel)}
@media (prefers-reduced-motion:reduce){*{scroll-behavior:auto}}
</style>
'''
body = re.sub(r'(<table>.*?</table>)', r'<div class="tabla">\1</div>', body, flags=re.S)
body = body.replace('</h1>', '</h1>', 1)
i = body.index('</p>') + 4  # tras el subtítulo
page = head + '<main>' + body[:i] + nav + body[i:] + '''</main>
<script>
document.querySelectorAll('pre').forEach(function(p,i){
  var b=document.createElement('button'); b.className='copiar'; b.type='button'; b.id='copiar-'+i; b.textContent='Copiar';
  b.addEventListener('click',function(){
    var t=p.innerText;
    function ok(){b.textContent='Copiado ✓';setTimeout(function(){b.textContent='Copiar'},1600)}
    function sel(){var r=document.createRange();r.selectNodeContents(p);var s=getSelection();s.removeAllRanges();s.addRange(r);b.textContent='Seleccionado: copia con el menú'}
    try{navigator.clipboard.writeText(t).then(ok,sel)}catch(e){sel()}
  });
  p.insertAdjacentElement('afterend',b);
});
</script>'''
os.makedirs(os.path.join(here, 'web'), exist_ok=True)
open(os.path.join(here, 'web', 'el-viaje-de-toffee.html'), 'w').write(page)
print('ok', len(page))
