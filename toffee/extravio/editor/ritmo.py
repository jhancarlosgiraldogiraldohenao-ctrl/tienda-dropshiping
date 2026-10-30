# Guion de ritmo para ElevenLabs: copia cómo habló Flow en cada toma (pausas, palabras estiradas, gritos)
# para que la voz de ElevenLabs salga con el mismo ritmo que la boca. Uso: python3 ritmo.py <carpeta de trabajo>
import json, os, sys, re, subprocess as sp
import numpy as np
os.chdir(sys.argv[1]); SR = 16000
T = json.load(open('takes.json'))
TOMAS = [(11, 'in_11', 'T'), (1, 'in_02', 'T'), (2, 'in_01', 'T'), (6, 'in_03', 'T'), (8, 'in_09', 'T'), (9, 'in_08', 'T'), (14, 'in_14', 'T'),
         (16, 'in_20', 'T'), (17, 'r_17', 'T'), (19, 'in_19', 'L'), (20, 'in_18', 'T'), (21, 'in_17', 'L'), (22, 'in_24', 'T'), (23, 'in_23', 'L'),
         (24, 'in_22', 'T'), (25, 'in_21', 'L'), (26, 'r_26', 'T'), (28, 'in_27', 'T'), (29, 'in_26', 'L'), (33, 'in_29', 'T')]
VOC = 'aeiouáéíóú'
def stretch_word(w, k):
    # repite la última vocal fuerte para alargar la palabra (Vooooy)
    m = list(re.finditer(f'[{VOC}{VOC.upper()}]', w))
    if not m: return w
    i = m[-1].start() if len(m) == 1 or w[-1] in VOC else m[-1].start()
    return w[:i + 1] + w[i].lower() * k + w[i + 1:]
out = []
for n, f, who in sorted(TOMAS):
    ws = T[f + '.mp4']['words']
    a = np.frombuffer(sp.run(['ffmpeg', '-v', 'error', '-i', f + '.mp4', '-ac', '1', '-ar', str(SR), '-f', 'f32le', '-'], capture_output=True).stdout, np.float32)
    rms = [20 * np.log10(np.sqrt(np.mean(a[int(s * SR):int(e * SR)] ** 2)) + 1e-9) for s, e, _ in ws]
    ref = np.median(rms)
    txt = []
    for j, (s, e, w) in enumerate(ws):
        letters = len(re.sub(r'[^\wáéíóúñ]', '', w)); dur = e - s
        if letters and dur > 0.13 * letters + 0.25 and j < len(ws) - 1: w = stretch_word(w, min(4, int(dur / (0.09 * letters))))
        if rms[j] > ref + 5 and letters > 2: w = w.upper()
        txt.append(w)
        if j < len(ws) - 1:
            g = ws[j + 1][0] - e
            if g > 0.7: txt.append('… [long pause]')
            elif g > 0.35: txt.append('… [short pause]')
            elif g > 0.15 and not w[-1] in ',.?!…': txt[-1] += ','
    line = ' '.join(txt).replace(' …', '…')
    speech = sum(e - s for s, e, _ in ws); total = ws[-1][1] - ws[0][0]
    out.append(dict(toma=n, quien='TOFFEE' if who == 'T' else 'LUCHO', texto=line, dur=round(total, 1)))
json.dump(out, open('_ritmo.json', 'w'), ensure_ascii=False, indent=1)
for o in out: print(o['toma'], o['quien'], o['dur'], '|', o['texto'])
