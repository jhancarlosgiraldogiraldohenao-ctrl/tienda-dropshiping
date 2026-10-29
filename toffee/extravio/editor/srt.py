# Subtítulos .srt (español) del capítulo editado, con los tiempos reales de cada frase en la línea de tiempo.
# Uso: python3 srt.py <carpeta de trabajo> <salida.srt>   (lee voz.json, _placed.json y _timeline.json que deja ed01.py)
import json, os, sys
W = sys.argv[1]
VZ = json.load(open(os.path.join(W, 'voz.json')))
PL = json.load(open(os.path.join(W, '_placed.json')))
CUTS = json.load(open(os.path.join(W, '_timeline.json')))['cuts']
FIX = {'¡Galletta!': '¡Galleta!', 'Galletta,': 'Galleta,', '¡Galletta,': '¡Galleta,', '¿Galletta?': '¿Galleta?', 'Galletta': 'Galleta', 'Psst.': 'Psst…', 'Gato,': 'gato.', 'bienvenidos': 'Bienvenidos'}  # Whisper escribe mal el nombre
FILE = {'T': 'voz_toffee_1.mp3', 'L': 'voz_lucho_1.mp3'}

words = []
for key, (v, st, en) in PL.items():
    if '@' not in key: continue
    k = key.split('@')[0]; _, cs, ce = CUTS[k]
    for a, b, w in VZ[FILE[v]]['words']:
        if cs <= (a + b) / 2 < ce:   # la palabra es de la frase si su centro cae dentro del corte
            words.append((st + max(a, cs) - cs, st + b - cs, FIX.get(w, w), key))
words.sort()

cues, cur = [], []
for w in words:
    if cur and (w[3] != cur[-1][3] or w[0] - cur[-1][1] > 0.6 or len(' '.join(x[2] for x in cur + [w])) > 84
                or (cur[-1][2][-1] in '.?!' and len(' '.join(x[2] for x in cur)) > 12)):
        cues.append(cur); cur = []
    cur.append(w)
if cur: cues.append(cur)

def ts(t):
    ms = int(round(t * 1000)); return f'{ms//3600000:02d}:{ms//60000%60:02d}:{ms//1000%60:02d},{ms%1000:03d}'
out = []
for i, c in enumerate(cues):
    a, b = c[0][0], max(c[-1][1] + 0.3, c[0][0] + 1.0)
    if i + 1 < len(cues): b = min(b, cues[i + 1][0][0] - 0.05)
    t = ' '.join(x[2] for x in c)
    if len(t) > 42:   # dos líneas, partidas en la palabra más cercana a la mitad
        sp_ = [j for j, ch in enumerate(t) if ch == ' ']; m = min(sp_, key=lambda j: abs(j - len(t) / 2)); t = t[:m] + '\n' + t[m + 1:]
    out.append(f'{i+1}\n{ts(a)} --> {ts(b)}\n{t}\n')
open(sys.argv[2], 'w').write('\n'.join(out))
print(len(out), 'subtítulos')

# Inglés: mismos tiempos, texto traducido a mano (un renglón por subtítulo; \n = salto de línea)
if len(sys.argv) > 4 and os.path.exists(sys.argv[3]):
    en = [l.rstrip('\n').replace('\\n', '\n') for l in open(sys.argv[3]) if l.strip()]
    assert len(en) == len(out), f'{len(en)} traducciones para {len(out)} subtítulos'
    open(sys.argv[4], 'w').write('\n'.join(o.split('\n')[0] + '\n' + o.split('\n')[1] + '\n' + e + '\n' for o, e in zip(out, en)))
    print('inglés listo')
