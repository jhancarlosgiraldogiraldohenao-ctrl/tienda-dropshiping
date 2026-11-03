# Editor del capítulo 1 de EXTRAVÍO (16:9, serie de TV: sin texto en pantalla).
# Uso: python3 ed01.py <carpeta de trabajo con in_*.mp4, r_*.mp4, voz_*.mp3, audio/a_0*.mp4, takes.json, voz.json>
# - Voces de ElevenLabs cortadas SOLO en silencios (se elige el punto más bajo entre frases y se verifica el nivel).
# - Cada frase se coloca alineando una palabra ancla con la misma palabra que dice la boca en la toma de Flow.
# - El audio de Flow se usa como ambiente en las tomas sin diálogo; donde Flow habla, se silencia.
import os, sys, json, subprocess as sp
import numpy as np

W = sys.argv[1] if len(sys.argv) > 1 else '.'
os.chdir(W)
SR = 48000
REFS = '/home/user/tienda-dropshiping/toffee/refs/extravio'
FPS = 24

def load(f, sr=SR, ch=1, ss=None, t=None):
    cmd = ['ffmpeg', '-v', 'error']
    if ss is not None: cmd += ['-ss', str(ss)]
    if t is not None: cmd += ['-t', str(t)]
    cmd += ['-i', f, '-f', 'f32le', '-ac', str(ch), '-ar', str(sr), '-']
    a = np.frombuffer(sp.run(cmd, capture_output=True).stdout, np.float32)
    return a.reshape(-1, ch) if ch > 1 else a

VZ = json.load(open('voz.json'))
TK = json.load(open('takes.json'))
VOICE = {'T': load('voz_toffee_1.mp3'), 'L': load('voz_lucho_1.mp3')}
VWORDS = {'T': VZ['voz_toffee_1.mp3']['words'], 'L': VZ['voz_lucho_1.mp3']['words']}

def db_at(x, t, w=0.02):
    i = int(t * SR); s = x[max(0, i - int(w * SR / 2)): i + int(w * SR / 2)]
    return 20 * np.log10(np.sqrt(np.mean(s ** 2)) + 1e-9) if len(s) else -120

def cut_point(x, a, b):
    """Punto de menor energía entre a y b (segundos)."""
    best, bt = 1e9, a
    for t in np.arange(a, b, 0.01):
        d = db_at(x, t)
        if d < best: best, bt = d, t
    assert best < -38, f'corte con sonido en {a:.2f}-{b:.2f}: {best:.0f} dB'
    return bt

# Frases: (voz, inicio aprox, fin aprox) → los bordes se ajustan al silencio más bajo cercano
FR = {
 'T1': ('T', 0.00, 6.6), 'T2': ('T', 6.6, 12.3), 'T3': ('T', 12.3, 17.1), 'T4': ('T', 17.1, 22.9),
 'T5': ('T', 22.9, 25.5), 'T6': ('T', 25.5, 30.6), 'T7': ('T', 30.6, 32.6), 'T7b': ('T', 32.6, 33.65),
 'T8': ('T', 33.65, 35.3), 'T9': ('T', 35.3, 38.9), 'T10': ('T', 38.9, 41.2), 'T11': ('T', 41.2, 42.2),
 'T12': ('T', 42.2, 45.4), 'T13': ('T', 45.4, 49.9), 'T14': ('T', 49.9, 53.2), 'T15': ('T', 53.2, 55.1),
 'T16': ('T', 55.1, 58.5), 'T17': ('T', 58.5, 60.7), 'T18': ('T', 60.7, 64.6), 'T19': ('T', 64.6, 67.9),
 'T20': ('T', 67.9, 70.4), 'T21': ('T', 70.4, 75.7),
 'L1a': ('L', 0.00, 1.6), 'L1b': ('L', 1.6, 10.5), 'L2': ('L', 10.5, 14.5), 'L3': ('L', 14.5, 21.3),
 'L4': ('L', 21.3, 25.2), 'L5': ('L', 25.2, 28.6), 'L6': ('L', 28.6, 31.5), 'L7': ('L', 31.5, 34.4),
}
CUTS = {}
def frase(k):
    if k in CUTS: return CUTS[k]
    v, a, b = FR[k]; x = VOICE[v]; dur = len(x) / SR
    def edge(t):
        if t <= 0.05: return 0.0
        if t >= dur - 0.05: return dur
        return cut_point(x, t - 0.35, min(dur, t + 0.35))
    s, e = edge(a), edge(b)
    CUTS[k] = (v, s, e); return CUTS[k]

def word_t(v, prefix, after):
    for st, en, w in VWORDS[v]:
        if st >= after - 0.05 and w.lower().strip('¡!¿?.,').startswith(prefix.lower()):
            return st
    raise KeyError((v, prefix, after))

# ---------------- Montaje ----------------
# Segmento: dict(src, a, b, crop, amb (volumen del audio de Flow), mute (regiones a silenciar, en tiempo de clip), img/dur para imágenes)
SEG = []
VO = []  # (frase, índice de segmento, modo, valor): modo 'boca' = (palabra en voz, tiempo de la boca en el clip); 'en' = segundo del clip donde empieza la frase
def seg(src=None, a=0, b=None, crop=False, amb=0.0, img=None, dur=None, freeze=0, pre=0, zoom=1.0):
    SEG.append(dict(src=src, a=a, b=b, crop=crop, amb=amb, img=img, dur=dur, freeze=freeze, pre=pre, zoom=zoom)); return len(SEG) - 1
def vo(k, i, modo, val): VO.append((k, i, modo, val))

def vad_mute(src):
    return TK[src]['vad']

g = seg('in_11.mp4', 0, 4.5);                         vo('T8', g, 'boca', ('gall', 0.91))          # GANCHO
LOGO = seg(img='LOGO', dur=3.0)
s = seg('in_02.mp4', 0, 8.04);                        vo('T1', s, 'boca', ('a', 0.21))
s = seg('in_06.mp4', 4.8, 6.0, amb=0.5)                                                              # Galleta (tapa el cambio de cama)
s = seg('in_01.mp4', 0.6, 6.04);                      vo('T2', s, 'boca', ('bueno', 1.1))
s = seg('in_06.mp4', 0, 4.8, amb=0.5);                vo('T3', s, 'en', 0.3)
s = seg('in_05.mp4', 0, 8.04, amb=0.5);               vo('T4', s, 'en', 0.8)
s = seg('in_04.mp4', 0, 6.0, amb=0.6)
s = seg('in_03.mp4', 0.7, 5.6);                       vo('T5', s, 'boca', ('gall', 1.2))
s = seg('in_10.mp4', 0, 7.0, amb=0.7)
s = seg('in_09.mp4', 0, 6.0, crop=True);              vo('T6', s, 'boca', ('yo', 0.05))
TENSION = s + 1
s = seg('in_08.mp4', 0.5, 6.0, amb=0.4);              vo('T7', s, 'boca', ('por', 2.74))
s = seg('in_07.mp4', 3.4, 6.0, amb=0.6);              vo('T7b', s, 'en', 3.8)
s = seg('in_11.mp4', 0, 8.0, amb=0.5);                vo('T8', s, 'boca', ('gall', 0.91))
s = seg('in_16.mp4', 0, 6.0, amb=0.6);                vo('T9', s, 'en', 0.6)
s = seg('in_15.mp4', 0, 6.0, amb=0.8)
s = seg('in_14.mp4', 1.5, 6.0, amb=0.4);              vo('T10', s, 'boca', ('qu', 3.09))
s = seg('in_13.mp4', 0, 6.0, amb=0.6);                vo('T11', s, 'en', 4.2)
s = seg('in_20.mp4', 0.8, 8.0, amb=0.3);              vo('T12', s, 'boca', ('gall', 2.24))
s = seg('r_17.mp4', 0.5, 6.0, crop=True, amb=0.3);    vo('T13', s, 'boca', ('casi', 1.58))
LUCHO = len(SEG)
s = seg('in_17.mp4', 0, 1.7, amb=0.4);                vo('L1a', s, 'en', 0.1)
s = seg('in_19.mp4', 0, 8.0, amb=0.3);                vo('L1b', s, 'boca', ('bienv', 0.14))
s = seg('in_18.mp4', 0, 5.5, amb=0.3, pre=1.0);                vo('T14', s, 'boca', ('nosotros', 0.18))
s = seg('in_17.mp4', 2.0, 8.0, amb=0.3);              vo('L2', s, 'boca', ('famoso', 2.89))
s = seg(img='GATO', dur=2.2)
s = seg('in_24.mp4', 1.0, 5.6, amb=0.3);              vo('T15', s, 'boca', ('me', 1.84))
s = seg('in_23.mp4', 1.0, 8.0, amb=0.3);              vo('L3', s, 'boca', ('aquí', 3.24))
s = seg('in_22.mp4', 0.3, 5.6, amb=0.3);              vo('T16', s, 'boca', ('mi', 0.75))
s = seg('in_21.mp4', 1.8, 8.0, amb=0.3);              vo('L4', s, 'boca', ('y', 2.74))
s = seg('r_26.mp4', 0.4, 6.0, crop=True, amb=0.3);    vo('T17', s, 'boca', ('mi', 0.88)); vo('L5', s, 'tras', 'T17')
s = seg('in_28.mp4', 0, 8.0, amb=0.5);                vo('T18', s, 'en', 1.0)
s = seg('in_27.mp4', 0.5, 6.0, crop=True, amb=0.3);   vo('T19', s, 'boca', ('voy', 1.07))
s = seg('in_26.mp4', 1.5, 6.0, amb=0.3);              vo('L6', s, 'boca', ('primero', 2.29))
MISTERIO = len(SEG)
s = seg('in_25.mp4', 0, 6.0, amb=0.8);                vo('L7', s, 'en', 2.2)
s = seg('in_31.mp4', 0, 6.0, crop=True, amb=0.6)
s = seg('in_30.mp4', 0, 6.0, amb=0.6)
s = seg(img='MAX', dur=1.8)
s = seg('in_29.mp4', 1.5, 6.0, amb=0.3);              vo('T20', s, 'boca', ('max', 2.45))
FIN = seg('in_33.mp4', 0, 10.0, amb=0.6, freeze=8.0); vo('T21', FIN, 'en', 1.2)

# ---------------- Tiempos ----------------
T0 = []; t = 0
for s_ in SEG:
    d = s_['dur'] if s_['img'] else (s_['b'] - s_['a']) + s_['freeze'] + s_['pre']
    s_['len'] = d; T0.append(t); t += d
TOT = t

def clip_t(i, x):  # tiempo de línea para el segundo x del clip del segmento i
    return T0[i] + SEG[i]['pre'] + (x - SEG[i]['a'])

PLACED = {}
for k, i, modo, val in VO:
    v, cs, ce = frase(k)
    if modo == 'boca':
        pref, boca = val
        wt = word_t(v, pref, cs)
        start = clip_t(i, boca) - (wt - cs)
    elif modo == 'en':
        start = clip_t(i, val)
    elif modo == 'tras':
        pv, ps, pe = PLACED[val]
        start = pe + 0.25
    PLACED[k + '@' + str(i)] = (v, start, start + (ce - cs))
    PLACED[k] = (v, start, start + (ce - cs))
items = [(k, i) for k, i, _, _ in VO]
# ---- Sincronía fina con la boca (pedido de Jay, 29-oct-2026: la sincronía manda) ----
# Cada palabra de ElevenLabs que se reconoce en la boca de Flow es un ancla. Entre dos anclas la voz se acelera o se
# frena un poco (rubberband, sin cambiar el tono, entre 0,8 y 1,25) para que cada palabra caiga donde la boca la dice.
import re, unicodedata
def norm(w):
    w = unicodedata.normalize('NFD', w.lower()); w = ''.join(c for c in w if unicodedata.category(c) != 'Mn')
    return re.sub(r'[^a-z0-9]', '', w)
def stretch(x, dur):
    if abs(len(x) / SR - dur) < 0.01: return x
    tempo = (len(x) / SR) / dur
    r = sp.run(['ffmpeg', '-v', 'error', '-f', 'f32le', '-ar', str(SR), '-ac', '1', '-i', '-', '-af',
                f'rubberband=tempo={tempo:.4f}:pitchq=quality:formant=preserved:transients=smooth', '-f', 'f32le', '-'],
               input=x.astype(np.float32).tobytes(), capture_output=True, check=True)
    return np.frombuffer(r.stdout, np.float32)
def fit(x, dur):
    """Lleva el pedazo x a dur segundos: primero alargando o acortando sus silencios, después (si falta) la voz."""
    fr = int(0.01 * SR); n = len(x) // fr
    if n < 3: return stretch(x, dur)
    db = np.array([20 * np.log10(np.sqrt(np.mean(x[q * fr:(q + 1) * fr] ** 2)) + 1e-9) for q in range(n)])
    sil = db < -40; runs, q = [], 0
    while q < n:
        r = q
        while r < n and sil[r] == sil[q]: r += 1
        runs.append((bool(sil[q]) and 0 < q and r < n, q * fr, r * fr if r < n else len(x))); q = r
    S = sum(b - a for s_, a, b in runs if s_) / SR; P = len(x) / SR - S
    if S > 0 and dur - P >= 0.35 * S: al, be = (dur - P) / S, 1.0
    else:
        al = 0.35 if S > 0 else 1.0; be = min(1.35, max(0.8, (dur - al * S) / P)); RAT.append(be)
    parts = []
    for s_, a, b in runs:
        seg_ = x[a:b]
        if s_:
            m = int(len(seg_) * al); seg_ = seg_[:m] if m <= len(seg_) else np.concatenate([seg_, np.zeros(m - len(seg_), np.float32)])
        parts.append(seg_)
    y = np.concatenate(parts)
    return stretch(y, len(y) / SR * be) if abs(be - 1) > 0.01 else y
CHUNKS = {}; ERR = []; RAT = [1.0]; BAD = []
for k, i, modo, val in VO:
    if modo != 'boca': continue
    v, cs, ce = frase(k); x = VOICE[v]; s_ = SEG[i]
    ew = [w for w in VWORDS[v] if cs <= (w[0] + w[1]) / 2 < ce]
    fw = [w for w in TK[s_['src']]['words'] if s_['a'] - 0.1 <= w[0] < s_['b']]
    anc, j = [], 0
    for w in ew:
        a_ = norm(w[2])[:4]
        for jj in range(j, min(j + 4, len(fw))):
            b_ = norm(fw[jj][2])[:4]
            if a_ and b_ and (a_.startswith(b_[:3]) or b_.startswith(a_[:3])):
                t_ = clip_t(i, fw[jj][0])
                if not anc or (w[0] - anc[-1][0] > 0.08 and t_ - anc[-1][1] > 0.08): anc.append((max(w[0] - 0.02, cs), t_ - 0.02))
                j = jj + 1; break
    if not anc: continue
    pts = [cs] + [e for e, _ in anc] + [ce]
    st = anc[0][1] - (anc[0][0] - cs)
    y, f = np.zeros(0, np.float32), int(0.01 * SR)
    for n in range(len(pts) - 1):
        a_, b_ = pts[n], pts[n + 1]; cur = st + len(y) / SR
        if n >= 1: ERR.append(abs(cur - anc[n - 1][1])); BAD.append((k, round(cur - anc[n - 1][1], 2), round(anc[n-1][0], 2)))
        L = max(0.05, anc[n][1] - cur) if 1 <= n < len(anc) else b_ - a_
        z = fit(x[int(a_ * SR): int(b_ * SR)], L + (0.01 if len(y) else 0))
        # si la boca hace una pausa que la voz no tiene: pausa justo antes de la palabra (solo si ahí la voz está casi en silencio)
        if len(y) and len(z) / SR < L - 0.05 and db_at(x, a_ - 0.01, 0.02) < -30:
            pad = int((L - len(z) / SR) * SR); fo = int(0.008 * SR)
            y = y.copy(); y[-fo:] *= np.linspace(1, 0, fo); y = np.concatenate([y, np.zeros(pad, np.float32)])
        if len(y) >= f and len(z) >= f:
            z = z.copy(); z[:f] = z[:f] * np.linspace(0, 1, f) + y[-f:] * np.linspace(1, 0, f); y = y[:-f]
        y = np.concatenate([y, z])
    CHUNKS[(k, i)] = [st, y]
    PLACED[k + '@' + str(i)] = PLACED[k] = (v, st, st + len(y) / SR)
if ERR: print(f'sincronía: {len(ERR)} palabras, desfase medio {np.mean(ERR):.2f} s, 90 % por debajo de {np.percentile(ERR, 90):.2f} s; velocidad {min(RAT):.2f}–{max(RAT):.2f}')
if os.environ.get('SOLO_SYNC'): print([b for b in BAD if abs(b[1]) > 0.15])
MODO = {(k, i): m for k, i, m, _ in VO}
# si dos frases se pisan (contando solo donde hay voz, no el silencio de las puntas):
# una frase en la boca nunca se mueve; se corre la otra (la de voz en off va antes, o la siguiente va después)
def habla(k, i):
    if (k, i) in CHUNKS:
        y = CHUNKS[(k, i)][1]; fr = int(0.01 * SR)
        e = np.array([np.sqrt(np.mean(y[q:q + fr] ** 2)) for q in range(0, len(y) - fr, fr)]); on = np.where(e > 0.01)[0]
        return on[0] * 0.01, (on[-1] + 1) * 0.01
    v, cs, ce = frase(k); ws = [w for w in VWORDS[v] if cs <= (w[0] + w[1]) / 2 < ce]
    return (ws[0][0] - cs, ws[-1][1] - cs + 0.05) if ws else (0.0, ce - cs)
def mover(k, i, sh):
    v, st, en = PLACED[k + '@' + str(i)]; PLACED[k + '@' + str(i)] = PLACED[k] = (v, st + sh, en + sh)
    if (k, i) in CHUNKS: CHUNKS[(k, i)][0] += sh
prev = None
for k, i in sorted(items, key=lambda ki: PLACED[ki[0] + '@' + str(ki[1])][1]):
    if prev:
        pk, pi = prev; p_end = PLACED[pk + '@' + str(pi)][1] + habla(pk, pi)[1]
        s_ini = PLACED[k + '@' + str(i)][1] + habla(k, i)[0]
        if s_ini < p_end + 0.1:
            sh = p_end + 0.1 - s_ini
            if MODO[(k, i)] == 'boca' and MODO[(pk, pi)] != 'boca':
                print(f'adelanto {pk} {sh:.2f} s (para no mover la boca de {k})'); mover(pk, pi, -sh)
            else:
                print(f'corro {k} {sh:.2f} s' + ('  ⚠ boca' if MODO[(k, i)] == 'boca' else '')); mover(k, i, sh)
    prev = (k, i)
if os.environ.get('SOLO_SYNC'): sys.exit()
# ---------------- Audio ----------------
N = int((TOT + 0.5) * SR)
VOX = np.zeros(N, np.float32); AMB = np.zeros(N, np.float32)
for k, i in items:
    if (k, i) in CHUNKS:
        st_, x = CHUNKS[(k, i)]; x = x.copy(); f = int(0.005 * SR)
        x[:f] *= np.linspace(0, 1, f); x[-f:] *= np.linspace(1, 0, f)
        st = int(st_ * SR); VOX[st: st + len(x)] += x
        continue
    v, cs, ce = frase(k); x = VOICE[v][int(cs * SR): int(ce * SR)].copy()
    f = int(0.005 * SR); x[:f] *= np.linspace(0, 1, f); x[-f:] *= np.linspace(1, 0, f)
    st = int(PLACED[k + '@' + str(i)][1] * SR); VOX[st: st + len(x)] += x
for i, s_ in enumerate(SEG):
    if s_['img'] or s_['amb'] <= 0: continue
    a = load(s_['src'], ss=s_['a'], t=s_['b'] - s_['a'])
    for (va, vb) in TK[s_['src']]['vad']:   # donde Flow habla, silencio
        ia, ib = int(max(0, va - s_['a'] - 0.1) * SR), int(max(0, vb - s_['a'] + 0.1) * SR)
        a = a.copy(); a[ia:ib] = 0
    a = a * s_['amb']; f = int(0.04 * SR)
    if len(a) > 2 * f: a[:f] *= np.linspace(0, 1, f); a[-f:] *= np.linspace(1, 0, f)
    st = int((T0[i] + s_['pre']) * SR); AMB[st: st + len(a)] += a[: N - st]

def music(f, start, end, ss=0.0, gain=1.0, fade=1.5):
    L = end - start; src = load(f, ss=ss)
    while len(src) < L * SR: src = np.concatenate([src, load(f)])
    x = src[: int(L * SR)].copy(); fi = int(min(fade, L / 3) * SR)
    x[:fi] *= np.linspace(0, 1, fi); x[-fi:] *= np.linspace(1, 0, fi)
    out = np.zeros(N, np.float32); st = int(start * SR); out[st: st + len(x)] = x[: N - st] * gain; return out

MUS = (music('audio/a_03.mp4', 0, T0[LOGO], ss=0, fade=0.3)
       + music('audio/a_01.mp4', T0[LOGO], T0[LOGO] + 3.0, ss=0.6, fade=0.4) * 1.3
       + music('audio/a_02.mp4', T0[LOGO] + 3.0, T0[TENSION], ss=0)
       + music('audio/a_03.mp4', T0[TENSION], T0[LUCHO], ss=0)
       + music('audio/a_02.mp4', T0[LUCHO], T0[MISTERIO], ss=20)
       + music('audio/a_01.mp4', T0[MISTERIO], TOT, ss=3, fade=3.0))
# bajar la música cuando hay voz (ducking)
env = np.abs(VOX); k = int(0.25 * SR); env = np.convolve(env, np.ones(k) / k, mode='same')
duck = np.clip(env / 0.02, 0, 1)
MUS *= (0.42 - 0.30 * duck)
MIX = VOX * 1.0 + AMB * 0.8 + MUS
MIX = np.clip(MIX, -1, 1)
MIX.astype(np.float32).tofile('_mix.f32')

# ---------------- Video ----------------
os.makedirs('_v', exist_ok=True)
def crop_filter(src):
    y0, y1 = min(b[0] for b in TK[src]['bars'] if b), max(b[1] for b in TK[src]['bars'] if b)
    ys = [b for b in TK[src]['bars'] if b and b[0] > 5]
    y0, y1 = (max(b[0] for b in ys), min(b[1] for b in ys)) if ys else (0, 719)
    h = y1 - y0 + 1; w = int(h * 16 / 9) // 2 * 2; x = (1280 - w) // 2
    return f'crop={w}:{h - h % 2}:{x}:{y0},'
parts = []
for i, s_ in enumerate(SEG):
    out = f'_v/{i:02d}.mp4'
    base = 'scale=1920:1080:flags=lanczos,setsar=1,fps=24'
    if s_['img'] == 'LOGO':
        cmd = ['ffmpeg', '-v', 'error', '-y', '-loop', '1', '-t', str(s_['dur']), '-i', f'{REFS}/marca/LOGO-EXTRAVIO.jpg', '-vf',
               "scale=1080:1080,pad=1920:1080:420:0:color=0x0B1530,format=yuv420p,fade=t=in:st=0:d=0.5,fade=t=out:st=2.5:d=0.5,fps=24", '-c:v', 'libx264', '-crf', '17', '-pix_fmt', 'yuv420p', out]
    elif s_['img'] in ('GATO', 'MAX'):
        img = f'{REFS}/objetos/GATO-CON-BOTAS.jpg' if s_['img'] == 'GATO' else f'{REFS}/objetos/PLACA-MAX.jpg'
        pre = '' if s_['img'] == 'GATO' else 'crop=iw/2:ih/2:0:0,'
        n = int(s_['dur'] * FPS)
        cmd = ['ffmpeg', '-v', 'error', '-y', '-loop', '1', '-i', img, '-vf',
               f"{pre}scale=2160:2160,zoompan=z='1+0.0015*on':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={n}:s=1080x1080:fps=24,pad=1920:1080:420:0:color=0x0B1530,format=yuv420p",
               '-frames:v', str(n), '-c:v', 'libx264', '-crf', '17', '-pix_fmt', 'yuv420p', out]
    else:
        vf = (crop_filter(s_['src']) if s_['crop'] else '') + base
        if s_['freeze']: vf += f',tpad=stop_mode=clone:stop_duration={s_["freeze"]}'
        if s_['pre']: vf += f',tpad=start_mode=clone:start_duration={s_["pre"]}'
        n = int(round(s_['len'] * FPS))
        cmd = ['ffmpeg', '-v', 'error', '-y', '-ss', str(s_['a']), '-t', str(s_['b'] - s_['a']), '-i', s_['src'], '-vf', vf,
               '-frames:v', str(n), '-an', '-c:v', 'libx264', '-crf', '17', '-pix_fmt', 'yuv420p', out]
    sp.run(cmd, check=True); parts.append(out)
open('_v/list.txt', 'w').write(''.join(f"file '{os.path.basename(p)}'\n" for p in parts))
sp.run(['ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', '_v/list.txt', '-c', 'copy', '_video.mp4'], check=True)
sp.run(['ffmpeg', '-v', 'error', '-y', '-i', '_video.mp4', '-f', 'f32le', '-ar', str(SR), '-ac', '1', '-i', '_mix.f32',
        '-map', '0:v', '-map', '1:a', '-af', 'loudnorm=I=-14:TP=-1.5:LRA=11', '-ar', '48000', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k',
        '-shortest', '_mux.mp4'], check=True)
# loudnorm de una pasada se queda corto (−15.9): se mide y se sube con ganancia + limitador hasta −14 LUFS
import re
def lufs(f):
    o = sp.run(['ffmpeg', '-hide_banner', '-i', f, '-af', 'ebur128', '-f', 'null', '-'], capture_output=True, text=True).stderr
    return float(re.findall(r'I:\s+(-?[\d.]+) LUFS', o)[-1])
g = -14 - lufs('_mux.mp4') + 0.7
sp.run(['ffmpeg', '-v', 'error', '-y', '-i', '_mux.mp4', '-c:v', 'copy', '-af',
        f'aresample=192000,volume={g:.2f}dB,alimiter=limit=0.82:attack=1:release=60:level=disabled,aresample=48000',
        '-c:a', 'aac', '-b:a', '256k', 'EXTRAVIO-CAP01.mp4'], check=True)
print('volumen final:', lufs('EXTRAVIO-CAP01.mp4'), 'LUFS')
json.dump(PLACED, open('_placed.json', 'w')); json.dump({'T0': T0, 'segs': [(s_['src'] or s_['img'], s_['a'], s_['len']) for s_ in SEG], 'cuts': CUTS}, open('_timeline.json', 'w'))
print('total', round(TOT, 2), 's ·', len(SEG), 'segmentos')
