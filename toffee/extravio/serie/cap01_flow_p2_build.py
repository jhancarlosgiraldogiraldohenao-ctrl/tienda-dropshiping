"""Arma CAP01-FLOW-P2.md, .html (con botones de Copiar) y cap01_flow_p2.json desde P2 de cap01_flow.py."""
import sys, json, html, os
AQ = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, AQ)
import cap01_flow as F
REUSO = [("81", "G37 (de la parte 1): todos se quedan quietos; encima va «¡MIJITO!» de la abuela en off"),
         ("90", "G12 (toma aérea del camino) con color de atardecer"),
         ("103", "Pantallas finales: G103 nueva (la finca de noche desde el aire) + el inicio de G98 (Dizzy dormido)")]
NUEVOS = "Antes de las tomas de la mesa, del zarzo de noche y del camino al atardecer: las 3 fotos nuevas de lugares (HUECO-MESA-DOMINO, ZARZO-NOCHE, CAMINO-ATARDECER)."
tot = sum(F.CRED[g[1]] for g in F.P2)
md = ["# Capítulo 1 · PARTE 2 del video: prompts de Flow (tomas 54 a 103)\n",
      f"Google Flow, **Omni 1.1 Flash**, **vertical 9:16**. **{len(F.P2)} generaciones · ≈ {tot} créditos** (720p, x1). Hechos con todo lo aprendido (`memoria/`).\n",
      f"**{NUEVOS}**\n", "**Tomas que NO hay que generar (se reusan, 0 créditos):**\n"] + [f"- Toma {a}: {b}" for a, b in REUSO] + ["",
      "**Orden nuevo:** primero estas tomas; después Claude mide la boca de cada una y manda los textos de las voces con el ritmo exacto.\n"]
for g in F.P2:
    md.append(f"\n## {g[0]} · {g[1]} s · toma {g[2]}\n\n**Fotos:** {' + '.join(F.refs(g))}\n\n```\n{F.prompt(g)}\n```\n")
open(os.path.join(AQ, 'CAP01-FLOW-P2.md'), 'w').write('\n'.join(md))
json.dump([{"id": g[0], "d": g[1], "tomas": g[2], "refs": F.refs(g), "p": F.prompt(g)} for g in F.P2], open(os.path.join(AQ, 'cap01_flow_p2.json'), 'w'), ensure_ascii=False)
cards = [f'''<section class="card"><div class="hd"><h2>{g[0]}</h2><span class="pill">{g[1]} s</span><span class="sub">toma {html.escape(g[2])}</span></div>
<p class="refs"><b>Fotos:</b> {' · '.join(html.escape(r) for r in F.refs(g))}</p>
<div class="pr"><button class="cp" aria-label="Copiar prompt {g[0]}">Copiar</button><pre>{html.escape(F.prompt(g))}</pre></div></section>''' for g in F.P2]
reuso = ''.join(f'<li><b>Toma {a}:</b> {html.escape(b)}</li>' for a, b in REUSO)
css = open(os.path.join(AQ, 'CAP01-FLOW-P2.html')).read().split('<style>')[1].split('</style>')[0] if os.path.exists(os.path.join(AQ, 'CAP01-FLOW-P2.html')) else ''
page = f'''<title>Prompts Parte 2</title>
<style>{css}</style>
<main><h1>Capítulo 1 · Parte 2 · prompts de Flow</h1>
<p class="lead">{len(F.P2)} generaciones · ≈ {tot} créditos · vertical 9:16 · Omni 1.1 Flash. Las voces van DESPUÉS: cuando tengas las tomas, Claude mide cada boca y te manda los textos con el ritmo exacto.</p>
<div class="box"><b>Primero:</b> {html.escape(NUEVOS)}</div>
<div class="box"><b>No hay que generar (se reusan):</b><ul>{reuso}</ul></div>
{''.join(cards)}</main>
<script>document.querySelectorAll('.cp').forEach(b=>b.onclick=async()=>{{const t=b.nextElementSibling.textContent;try{{await navigator.clipboard.writeText(t);}}catch(e){{const r=document.createRange();r.selectNodeContents(b.nextElementSibling);const s=getSelection();s.removeAllRanges();s.addRange(r);document.execCommand('copy');}}b.textContent='¡Copiado!';setTimeout(()=>b.textContent='Copiar',1500);}});</script>'''
open(os.path.join(AQ, 'CAP01-FLOW-P2.html'), 'w').write(page)
print(len(F.P2), tot)
