# Editor del capítulo 1 PILOTO de EXTRAVÍO (16:9, serie de TV: sin texto en pantalla).
# Uso: python3 ed01p.py <carpeta piloto> <carpeta ex01 (tomas viejas, voz_*.mp3, takes.json, voz.json, audio/)> <carpeta ritmo (x1-x3.mp3)>
# - Voces de ElevenLabs con el ritmo de Flow, pegadas palabra por palabra a la boca (pegar.py).
# - Ambiente de cada toma de Flow (sin la voz de Flow), música con ducking, transiciones solo entre escenas.
# - Logo que sale del remolino (apertura circular), burbuja de pensamiento del Gato con Botas, pantalla final.
import os, sys, json, glob, subprocess as sp
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pegar import pegar, pegar_suave, por_frases, load, SR, norm

P, E, RT = [os.path.abspath(x) for x in sys.argv[1:4]]
REFS = '/home/user/tienda-dropshiping/toffee/refs/extravio'
os.chdir(P); os.makedirs('_v', exist_ok=True)
W = json.load(open('words.json')); VW = json.load(open('voces_words.json'))
TK = json.load(open(f'{E}/takes.json')); VZ = json.load(open(f'{E}/voz.json'))
RW = json.load(open(f'{RT}/words.json'))
def dur(f): return float(sp.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', f], capture_output=True, text=True).stdout)

# ---------------- Fuentes ----------------
def nf(n): return f'{P}/n{n:02d}.mp4'
def rep(k): return glob.glob(f'{P}/rep/{k}*.mp4')[0]
SRC = dict(P01=nf(5), P02=nf(4), P03=nf(3), P04=rep('d3dde95a'), P05=nf(1), P06=nf(10), P07=nf(9), P08=nf(8), P09=nf(7), P10=nf(6),
           P11=nf(14), P12=nf(13), P13=nf(12), P14=nf(11), P15=nf(17), P16=nf(16), P17=nf(15), P18=nf(21), P19=nf(20), P20=nf(19),
           P21=rep('44746f55'), P22=nf(26), P23=nf(25), P24=nf(24), P25=nf(23), P26=nf(27), P27=nf(31), P28=nf(30), P29=rep('e90f3391'),
           P30=nf(28), P31=nf(36), P32=nf(35), P33=nf(34), P34=nf(33), P35=rep('38ba47d0'), P36=nf(40), P37=nf(37), P38=nf(38), P39=nf(39))
def pte(k): return glob.glob(f'{P}/puentes/{k}*.mp4')[0]
SRC.update(P40=pte('63714319'), P41=pte('c50dc0cc'), P42=pte('2ef86137'), P43=pte('b2df403b'), P44=pte('d846063b'))
def fwords(k):
    s = SRC[k]
    if s.startswith(f'{P}/rep/'): return VW['rep/' + os.path.basename(s)]
    if s.startswith(f'{P}/puentes/'): return []
    return W[os.path.basename(s)]
def voz(stamp): return glob.glob(f'{P}/voces/*T{"18_" + stamp if len(stamp) == 5 else stamp}_*.mp3')[0]
NV = dict(P01='08_40', P10='09_49', P11='10_12', P12='10_43', P13='11_20', P14='11_48', P15='12_50', P18='13_17', P20='13_46', P22='14_10',
          P23='14_44', P26='15_09', P34='15_37', P35='16_02', P38='16_32', T02='18_03', T06='18_27', T08='18_51', T09='19_18', T14='19_46',
          T17='20_10', T20='20_35', T22='21_04', T24='21_27', T28='22_01', L29='22_23', P21='22_40_43', P29='22_41_48')
def vwords(path):
    if path.startswith(RT): return RW[os.path.basename(path)]
    return VW['voces/' + os.path.basename(path)]
VPATH = {k: voz(v) for k, v in NV.items()}
VPATH.update(T01=f'{RT}/x1.mp3', T16=f'{RT}/x3.mp3', L23=f'{RT}/x2.mp3')
OLD = load(f'{E}/voz_toffee_1.mp3')
# voces en off rehechas por Jay el 31-oct-2026 (misma voz de Toffee que el resto)
_v2 = sorted(glob.glob(f'{P}/vo2/*.mp3'), key=lambda f: f.split('T00_')[1])
VO2 = dict(zip(['T3', 'T4', 'PUTA', 'AAH', 'T9', 'T11', 'T18', 'T21'], _v2)) if len(_v2) == 8 else {}
OFF = dict(T3=(12.45, 17.21), T4=(17.21, 23.13), T9=(35.53, 38.97), T11=(41.45, 42.29), T18=(60.85, 64.73), T21=(70.61, 75.65), PUTA=(29.40, 30.75), AAH=(32.77, 33.71))

# ---------------- Montaje ----------------
# seg: id, archivo, desde, hasta; boca = clave de voz pegada a la boca; off = (voz en off, segundo del clip); amb = volumen del ambiente de Flow
SEG = []; ESC = []
def esc(nombre, trans=None, td=0.0): ESC.append(dict(n=nombre, start=len(SEG), trans=trans, td=td))
def seg(id_, src, a, b, boca=None, off=(), amb=0.7, crop=False, pre=0.0, freeze=0.0, fw=None):
    SEG.append(dict(id=id_, src=src, a=a, b=b, boca=boca, off=list(off), amb=amb, crop=crop, pre=pre, freeze=freeze, fw=fw))
def nuevo(k, a=None, b=None, boca=None, off=(), amb=None, freeze=0.0):
    d = dur(SRC[k]); ws = fwords(k)
    if a is None: a = max(0.0, ws[0][0] - 0.9) if (boca and ws) else 0.2
    if b is None: b = min(d - 0.05, ws[-1][1] + 1.5) if (boca and ws) else d - 0.1
    seg(k, SRC[k], a, b, boca=boca, off=off, amb=(0.35 if boca else 0.8) if amb is None else amb, freeze=freeze, fw=ws)
def viejo(k, f, a, b, boca=None, off=(), amb=0.6, crop=False, pre=0.0):
    seg(k, f'{E}/{f}.mp4', a, b, boca=boca, off=off, amb=amb, crop=crop, pre=pre, fw=TK[f + '.mp4']['words'])

esc('gancho');        nuevo('P01', 0.2, 4.2, boca='P01')
esc('logo', 'circleopen', 0.7); seg('LOGO', None, 0, 3.2)
esc('casa', 'fadeblack', 0.5)
nuevo('P02', 0.0, 6.0); nuevo('P03', 0.2, 3.6)
viejo('R01', 'in_02', 0.0, 8.04, boca='T01'); viejo('R02', 'in_01', 0.6, 6.04, boca='T02')
viejo('R03', 'in_06', 0.0, 4.8, off=[('T3', 0.6)], amb=0.6); nuevo('P40', 1.0, 5.95); nuevo('P04', 0.2, 4.0, off=[('T4', 0.3)])
viejo('R04', 'in_05', 0.5, 7.5, amb=0.6)
esc('pelota')
viejo('R05', 'in_04', 0.0, 6.0, amb=0.7); nuevo('P05', 0.3, 5.9)
viejo('R06', 'in_03', 0.3, 6.0, boca='T06'); viejo('R08', 'in_09', 0.0, 6.04, boca='T08', crop=True, off=[('PUTA', 5.0)])
nuevo('P06', 0.3, 5.9); viejo('R09', 'in_08', 0.3, 6.04, boca='T09'); nuevo('P07', 0.2, 5.9, off=[('AAH', 2.4)])
esc('remolino')
viejo('R11', 'in_11', 3.0, 8.0, amb=0.6); viejo('R12', 'in_16', 0.0, 6.0, off=[('T9', 0.6)], amb=0.6); nuevo('P08', 0.0, 4.0)
esc('mar', 'fade', 0.6)
nuevo('P09', 0.2, 5.9); viejo('R13', 'in_15', 0.0, 6.0, amb=0.8); viejo('R14', 'in_14', 1.0, 6.04, boca='T14')
viejo('R15', 'in_13', 0.0, 6.0, off=[('T11', 4.2)], amb=0.6); viejo('R16', 'in_20', 0.5, 8.0, boca='T16'); viejo('R17', 'r_17', 0.3, 6.04, boca='T17', crop=True)
esc('lucho')
nuevo('P10', 1.0, None, boca='P10'); nuevo('P11', boca='P11'); viejo('R20', 'in_18', 0.0, 6.04, boca='T20')
nuevo('P12', None, 8.0, boca='P12', freeze=1.4); viejo('R22', 'in_24', 0.6, 6.04, boca='T22'); viejo('R23', 'in_23', 1.0, 8.0, boca='L23', crop=True)
viejo('R24', 'in_22', 0.0, 6.04, boca='T24'); nuevo('P13', boca='P13'); nuevo('P14', boca='P14'); nuevo('P15', boca='P15'); nuevo('P41', 0.3, 7.9)
esc('ciudad', 'fade', 0.8)
nuevo('P16', 0.2, 7.9, off=[('T18', 3.4)]); viejo('R28', 'in_27', 0.2, 6.04, boca='T28', crop=True); viejo('R29', 'in_26', 1.0, 6.04, boca='L29'); nuevo('P42', 0.3, 7.9)
nuevo('P17', 0.3, 7.9); nuevo('P18', boca='P18'); nuevo('P19', 0.2, 5.95); nuevo('P20', boca='P20'); nuevo('P43', 0.2, 5.9)
esc('local')
nuevo('P21', boca='P21' if 'P21' in NV else None); nuevo('P22', boca='P22'); nuevo('P23', boca='P23'); nuevo('P24', 0.2, 5.9)
esc('noche', 'fadeblack', 0.8)
nuevo('P25', 0.3, 7.9); nuevo('P26', boca='P26'); nuevo('P27', 1.2, 5.95); nuevo('P28', 0.2, 4.8)
nuevo('P29', boca='P29' if 'P29' in NV else None); nuevo('P30', 0.2, 5.9); nuevo('P31', 0.2, 5.95); nuevo('P32', 0.2, 5.0)
nuevo('P33', 0.2, 5.95); nuevo('P34', boca='P34'); nuevo('P35', 1.3, None, boca='P35')
esc('azotea', 'fade', 1.0)
nuevo('P44', 0.2, 5.9)
nuevo('P36', 0.3, 7.9, off=[('L36', 2.0)], amb=0.5); nuevo('P37', 1.9, 5.95); nuevo('P38', boca='P38')
nuevo('P39', 0.2, 9.9, off=[('T21', 1.5)], freeze=8.5)
for k in ('P21', 'P29'):   # mientras llega la voz nueva: queda la de Flow
    if k not in NV: SEG[[s['id'] for s in SEG].index(k)].update(amb=0.9, fw=None)

# ---------------- Tiempos (con los cruces entre escenas) ----------------
for i, s in enumerate(SEG): s['len'] = (s['b'] - s['a']) + s['pre'] + s['freeze']
ESC.append(dict(start=len(SEG)))
t = 0.0; T0 = [0.0] * len(SEG)
for e, nx in zip(ESC[:-1], ESC[1:]):
    if e['trans']: t -= e['td']
    e['t0'] = t
    for i in range(e['start'], nx['start']): T0[i] = t; t += SEG[i]['len']
TOT = t
print(f'{len(SEG)} tomas · {TOT // 60:.0f}:{TOT % 60:04.1f}')

# ---------------- Voces ----------------
N = int((TOT + 1) * SR); VOX = np.zeros(N, np.float32); AMB = np.zeros(N, np.float32)
def nivel(x):  # todas las voces al mismo nivel de habla
    e = x[np.abs(x) > 0.02]; r = np.sqrt(np.mean(e ** 2)) if len(e) else 0.1
    return x * (0.12 / r)
def poner(x, t):
    i = int(t * SR); j = min(N, i + len(x))
    if i < 0: x = x[-i:]; i = 0
    VOX[i:j] += x[:j - i]
ERR = []
for i, s in enumerate(SEG):
    if s['boca']:
        x = nivel(load(VPATH[s['boca']])); ew = vwords(VPATH[s['boca']])
        fw = [[a - s['a'], b - s['a'], w] for a, b, w in s['fw'] if s['a'] - 0.3 <= a < s['b']]
        # pegado suave: solo se ajustan silencios reales y la velocidad entre 0,9 y 1,15 (sin pausas metidas en medio de palabras)
        try:
            y, err = pegar_suave(x, ew, fw, s['len'] + 2.5, lo=0.8, hi=1.25)
        except IndexError:
            y = np.zeros(int((s['len'] + 2.5) * SR), np.float32); st = int(max(0, fw[0][0] - ew[0][0]) * SR); y[st: st + len(x)] = x[: len(y) - st]; err = []
        poner(y, T0[i] + s['pre'])
        ERR += [abs(e) for e in err]
    for k, at in s['off']:
        if k == 'L36': x = nivel(load(voz('17_23')))
        elif k in VO2: x = nivel(load(VO2[k]))
        else: a, b = OFF[k]; x = nivel(OLD[int(a * SR): int(b * SR)])
        t = T0[i] + s['pre'] + at; t0 = t
        while t < t0 + 3 and np.any(np.abs(VOX[int(max(0, t - 0.3) * SR): int((t + 0.6) * SR)]) > 0.01): t += 0.1   # nunca encima de otra voz
        poner(x, t)
if ERR: print(f'boca: {len(ERR)} palabras, desfase medio {np.mean(ERR):.3f} s, 90 % < {np.percentile(ERR, 90):.2f} s')

# ---------------- Ambiente de cada toma (sin la voz de Flow) ----------------
VAD = json.load(open('vad.json'))
def voces_flow(s):
    k = os.path.relpath(s['src'], P) if s['src'].startswith(P) else None
    if k in VAD: return VAD[k]
    if k is None: return TK[os.path.basename(s['src'])]['vad']
    return []
for i, s in enumerate(SEG):
    if not s['src']: continue
    X = 0.25; full = load(s['src']); a0 = max(0.0, s['a'] - X)
    a = full[int(a0 * SR): int((s['b'] + X) * SR)].copy()
    if s['fw'] is not None:   # P21/P29 sin voz nueva todavía: su voz de Flow se queda
        g = np.ones(len(a), np.float32)
        for va, vb in voces_flow(s):
            ia, ib = int(max(0, va - a0 - 0.1) * SR), int(max(0, vb - a0 + 0.1) * SR); g[ia:ib] = 0
        k_ = int(0.15 * SR); g = np.convolve(g, np.ones(k_) / k_, mode='same'); a *= g
    a *= s['amb']; f = int(X * SR)
    if len(a) > 2 * f: a[:f] *= np.linspace(0, 1, f); a[-f:] *= np.linspace(1, 0, f)
    st = int((T0[i] + s['pre'] - (s['a'] - a0)) * SR)
    if st < 0: a = a[-st:]; st = 0
    AMB[st: st + len(a)] += a[: N - st]

# cama de sonido por escena: el ambiente de la toma sin voces más larga, en bucle y bajito, para que no haya huecos
for e, nx in zip(ESC[:-1], ESC[1:]):
    ids = [i for i in range(e['start'], nx['start']) if SEG[i]['src'] and not voces_flow(SEG[i]) and not SEG[i]['boca']]
    if not ids: continue
    b_ = max(ids, key=lambda i: SEG[i]['b'] - SEG[i]['a']); s_ = SEG[b_]
    bed = load(s_['src'])[int(s_['a'] * SR): int(s_['b'] * SR)]
    t0 = T0[e['start']]; t1 = (T0[nx['start']] if nx['start'] < len(SEG) else TOT)
    L = int((t1 - t0) * SR)
    if L <= 0 or len(bed) < SR: continue
    reps = [bed] * (L // len(bed) + 2); xf = int(0.5 * SR); out = reps[0].copy()
    for r in reps[1:]:
        r = r.copy(); out[-xf:] = out[-xf:] * np.linspace(1, 0, xf) + r[:xf] * np.linspace(0, 1, xf); out = np.concatenate([out, r[xf:]])
    out = out[:L] * 0.3; f = int(min(1.0, L / SR / 3) * SR); out[:f] *= np.linspace(0, 1, f); out[-f:] *= np.linspace(1, 0, f)
    st = int(t0 * SR); AMB[st: st + len(out)] += out[: N - st]

# ---------------- Música ----------------
def ti(id_): return T0[[s['id'] for s in SEG].index(id_)]
def music(f, start, end, ss=0.0, gain=1.0, fade=1.5):
    L = end - start; src = load(f)[int(ss * SR):]
    while len(src) < L * SR: src = np.concatenate([src, load(f)])
    x = src[: int(L * SR)].copy(); fi = int(min(fade, L / 3) * SR)
    x[:fi] *= np.linspace(0, 1, fi); x[-fi:] *= np.linspace(1, 0, fi)
    out = np.zeros(N, np.float32); st = int(start * SR); out[st: st + len(x)] = x[: N - st] * gain; return out
A1, A2, A3 = f'{E}/audio/a_01.mp4', f'{E}/audio/a_02.mp4', f'{E}/audio/a_03.mp4'
X2 = 2.5   # cruce entre temas
MUS = (music(A3, 0, ti('LOGO') + 0.3, fade=0.3)
       + music(A1, ti('LOGO'), ti('P02') + 1.0, ss=0.6, gain=1.3, fade=0.6)
       + music(A2, ti('P02'), ti('P07') + X2, fade=X2)
       + music(A3, ti('P07'), ti('P09') + X2, fade=X2)
       + music(A2, ti('P09'), ti('P24') + X2, ss=12, fade=X2)
       + music(A1, ti('P24'), ti('P26') + X2, ss=3, fade=X2)
       + music(A3, ti('P26'), ti('P36') + X2, ss=5, fade=X2)
       + music(A1, ti('P36'), TOT, ss=3, fade=4.0))
env = np.convolve(np.abs(VOX), np.ones(int(0.25 * SR)) / int(0.25 * SR), mode='same')
MUS *= (0.40 - 0.28 * np.clip(env / 0.02, 0, 1))
MIX = np.clip(VOX + AMB * 1.0, -1, 1)   # sin música (pedido de Jay, 30-oct-2026)
MIX.astype(np.float32).tofile('_mix.f32')
if os.environ.get('SOLO_AUDIO'): sys.exit()

# ---------------- Video ----------------
BASE = 'scale=1920:1080:flags=lanczos,setsar=1,fps=24,format=yuv420p'
def logo_clip(out, d):
    n = int(round(d * 24))
    sp.run(['ffmpeg', '-v', 'error', '-y', '-i', f'{REFS}/marca/LOGO-EXTRAVIO.jpg', '-vf',
            f"crop=iw:iw*9/16:0:(ih-iw*9/16)/2,scale=1920:1080,zoompan=z='1+0.0006*on':x='iw/2-iw/zoom/2':y='ih/2-ih/zoom/2':d={n}:s=1920x1080:fps=24,{BASE}",
            '-frames:v', str(n), '-c:v', 'libx264', '-crf', '16', out], check=True)
def burbuja():
    """Burbuja de pensamiento con el Gato con Botas (PNG con transparencia, 3 bolitas + círculo)."""
    W_, H_ = 1920, 1080; img = Image.open(f'{REFS}/objetos/GATO-CON-BOTAS.jpg').convert('RGB')
    D = 330; s_ = min(img.size); img = img.crop(((img.width - s_) // 2, (img.height - s_) // 2, (img.width + s_) // 2, (img.height + s_) // 2)).resize((D, D))
    frames = []
    for f in range(int(2.6 * 24)):
        t = f / 24; c = Image.new('RGBA', (W_, H_), (0, 0, 0, 0)); d = ImageDraw.Draw(c)
        for j, (x, y, r) in enumerate([(1395, 430, 14), (1450, 365, 20), (1515, 295, 27)]):
            if t > 0.12 * j: d.ellipse([x - r, y - r, x + r, y + r], fill=(255, 255, 255, 235))
        if t > 0.4:
            k = min(1.0, (t - 0.4) / 0.18) * (1.06 if t < 0.66 else 1.0); dd = int(D * k)
            if dd > 4:
                cx, cy = 1665, 185; m = Image.new('L', (dd, dd), 0); ImageDraw.Draw(m).ellipse([0, 0, dd, dd], fill=255)
                ring = int(10 * k); d.ellipse([cx - dd // 2 - ring, cy - dd // 2 - ring, cx + dd // 2 + ring, cy + dd // 2 + ring], fill=(255, 255, 255, 240))
                c.paste(img.resize((dd, dd)), (cx - dd // 2, cy - dd // 2), m)
        if t > 2.3: c.putalpha(Image.eval(c.getchannel('A'), lambda v: int(v * max(0, (2.6 - t) / 0.3))))
        frames.append(c)
    os.makedirs('_bur', exist_ok=True)
    for j, fr in enumerate(frames): fr.save(f'_bur/{j:03d}.png')
def stats(s):
    fr = []
    for t in np.linspace(s['a'] + 0.3, s['b'] - 0.3, 3):
        r = sp.run(['ffmpeg', '-v', 'error', '-ss', f'{t:.2f}', '-i', s['src'], '-frames:v', '1', '-vf', 'scale=96:54', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], capture_output=True).stdout
        if r: fr.append(np.frombuffer(r, np.uint8).reshape(-1, 3).astype(float))
    x = np.concatenate(fr); return x.mean(0), x.std(0)
# color parejo dentro de cada escena (lo que da «sintonía»): cada toma se acerca un 60 % al color medio de su escena
GRADE = {}
for e, nx in zip(ESC[:-1], ESC[1:]):
    ids = [i for i in range(e['start'], nx['start']) if SEG[i]['src'] and SEG[i]['id'] not in ('P08',)]   # el ojo es un primerísimo plano: no se toca
    if len(ids) < 2: continue
    st_ = {i: stats(SEG[i]) for i in ids}
    mT = np.median([st_[i][0] for i in ids], 0); sT = np.median([st_[i][1] for i in ids], 0)
    for i in ids:
        m, sd = st_[i]; k = 1 + 0.6 * (sT / np.maximum(sd, 1) - 1); tt = m + 0.6 * (mT - m)
        GRADE[i] = 'lutrgb=' + ':'.join(f"{c}='clip((val-{m[j]:.1f})*{k[j]:.3f}+{tt[j]:.1f},0,255)'" for j, c in enumerate('rgb'))
def clip(i, s, out):
    if s['id'] == 'LOGO': return logo_clip(out, s['len'])
    vf = []
    if s['crop']:
        bars = [b for b in TK[os.path.basename(s['src'])]['bars'] if b and b[0] > 5]
        y0, y1 = (max(b[0] for b in bars), min(b[1] for b in bars)) if bars else (0, 719)
        h = y1 - y0 + 1; w = int(h * 16 / 9) // 2 * 2; vf.append(f'crop={w}:{h - h % 2}:{(1280 - w) // 2}:{y0}')
    if i in GRADE: vf.append(GRADE[i])
    vf.append(BASE)
    if s['pre'] or s['freeze']: vf.append(f"tpad=start_mode=clone:start_duration={s['pre']}:stop_mode=clone:stop_duration={s['freeze']}")
    cmd = ['ffmpeg', '-v', 'error', '-y', '-ss', str(s['a']), '-t', str(s['b'] - s['a']), '-i', s['src']]
    if s['id'] == 'P12':   # burbuja justo después de «botas»
        tb = next(b for a, b, w in s['fw'] if norm(w).startswith('bota')) - s['a'] + 0.15
        burbuja(); cmd += ['-framerate', '24', '-i', '_bur/%03d.png']
        vfs = ','.join(vf)
        cmd += ['-filter_complex', f"[0:v]{vfs}[b];[1:v]setpts=PTS+{tb:.2f}/TB[o];[b][o]overlay=eof_action=pass[v]", '-map', '[v]']
    else:
        cmd += ['-vf', ','.join(vf)]
    cmd += ['-an', '-frames:v', str(int(round(s['len'] * 24))), '-c:v', 'libx264', '-crf', '16', out]
    sp.run(cmd, check=True)
for i, s in enumerate(SEG):
    if not (os.environ.get('REUSAR') and os.path.exists(f'_v/{i:02d}.mp4')): clip(i, s, f'_v/{i:02d}.mp4')
# escenas: cortes secos adentro; entre escenas, transición
escenas = []
for k, (e, nx) in enumerate(zip(ESC[:-1], ESC[1:])):
    out = f'_v/esc{k:02d}.mp4'
    open('_v/l.txt', 'w').write(''.join(f"file '{i:02d}.mp4'\n" for i in range(e['start'], nx['start'])))
    sp.run(['ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', '_v/l.txt', '-c', 'copy', out], check=True)
    escenas.append((out, sum(SEG[i]['len'] for i in range(e['start'], nx['start'])), e.get('trans'), e.get('td', 0)))
inputs, fc, acc, last = [], [], 0.0, '[v0]'
for k, (f, L, tr, td) in enumerate(escenas):
    inputs += ['-i', f]; fc.append(f'[{k}:v]setpts=PTS-STARTPTS,fps=24,settb=1/24,format=yuv420p[v{k}]')
    if k == 0: acc = L; continue
    if tr:
        fc.append(f"{last}[v{k}]xfade=transition={tr}:duration={td}:offset={acc - td:.3f},settb=1/24[x{k}]"); acc += L - td
    else:
        fc.append(f"{last}[v{k}]concat=n=2:v=1:a=0,settb=1/24[x{k}]"); acc += L
    last = f'[x{k}]'
sp.run(['ffmpeg', '-v', 'error', '-y'] + inputs + ['-filter_complex', ';'.join(fc), '-map', last, '-c:v', 'libx264', '-crf', '17', '-pix_fmt', 'yuv420p', '_video.mp4'], check=True)
sp.run(['ffmpeg', '-v', 'error', '-y', '-i', '_video.mp4', '-f', 'f32le', '-ar', str(SR), '-ac', '1', '-i', '_mix.f32', '-map', '0:v', '-map', '1:a',
        '-c:v', 'copy', '-c:a', 'aac', '-b:a', '256k', '-shortest', '_mux.mp4'], check=True)
import re
def lufs(f):
    o = sp.run(['ffmpeg', '-hide_banner', '-i', f, '-af', 'ebur128', '-f', 'null', '-'], capture_output=True, text=True).stderr
    return float(re.findall(r'I:\s+(-?[\d.]+) LUFS', o)[-1])
g = -14 - lufs('_mux.mp4') + 1.0
sp.run(['ffmpeg', '-v', 'error', '-y', '-i', '_mux.mp4', '-c:v', 'copy', '-af',
        f'aresample=192000,volume={g:.2f}dB,alimiter=limit=0.82:attack=1:release=60:level=disabled,aresample=48000',
        '-c:a', 'aac', '-b:a', '256k', '-movflags', '+faststart', 'EXTRAVIO-CAP01-PILOTO.mp4'], check=True)
json.dump(dict(T0=T0, segs=[(s['id'], s['a'], s['b'], s['len']) for s in SEG]), open('_timeline.json', 'w'))
print('listo', round(TOT, 1), 's · volumen', lufs('EXTRAVIO-CAP01-PILOTO.mp4'), 'LUFS')
