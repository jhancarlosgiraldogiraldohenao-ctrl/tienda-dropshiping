# Editor del capítulo 2 de EXTRAVÍO «La Tierra de los Recordados» (base: ed01p.py).
# Uso: python3 ed02.py <carpeta cap02 (tomas/, voces/, audio/)> <carpeta piloto (sfx/, sfx2/)>
# Novedades: canción con la Catrina en cámara lenta para que la mandíbula siga el bolero; silencios vivos (Desencanto):
# ambiente por lugar con capas + música suave en los momentos tiernos; efectos en el cuadro exacto.
import os, sys, json, glob, re, subprocess as sp
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pegar import pegar_suave, load, SR, norm

C, P = [os.path.abspath(x) for x in sys.argv[1:3]]
REFS = '/home/user/tienda-dropshiping/toffee/refs/extravio'
os.chdir(C); os.makedirs('_v', exist_ok=True)
FW = json.load(open('tomas/words.json')); VW = json.load(open('voces/voces_words.json'))
def dur(f): return float(sp.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', f], capture_output=True, text=True).stdout)
def tom(n): return f'{C}/tomas/{n}.mp4'
def voz(stamp): return glob.glob(f'{C}/voces/*T{stamp}_*.mp3')[0]
V = dict(V01='21_51_35', V02='21_52_19', V04='21_54_35', V05='21_55_23', V09='21_55_49', V10='21_56_15', V19='21_56_54', V23='21_57_20',
         V28='21_58_57', V34='21_59_19', V35='21_59_54', V39='22_00_24', V40='22_00_53', L07='22_01_25', L08='22_01_48', L21='22_02_44',
         L38='22_03_05', C20='21_47_51', C22='21_48_33')
VP = {k: voz(s) for k, s in V.items()}
def vwords(k): return VW[os.path.basename(VP[k])]

# ---------------- Montaje ----------------
SEG, ESC = [], []
def esc(n, trans=None, td=0.0): ESC.append(dict(n=n, start=len(SEG), trans=trans, td=td))
def seg(id_, a=None, b=None, boca=None, amb=0.6, speed=1.0, freeze=0.0, src=None):
    f = src or tom(id_); d = dur(f); ws = FW.get(os.path.basename(f), [])
    if a is None: a = max(0.0, ws[0][0] - 0.9) if (boca and ws) else 0.2
    if b is None: b = min(d - 0.05, ws[-1][1] + 1.3) if (boca and ws) else d - 0.1
    SEG.append(dict(id=id_, src=f, a=a, b=b, boca=boca, amb=(0.3 if boca else amb), speed=speed, freeze=freeze, fw=ws))
esc('gancho');  seg('C2-01', 0.0, 5.8, boca='V01', amb=0.3); seg('C2-02', 0.3, 4.0, boca='V02')
esc('logo', 'circleopen', 0.35); SEG.append(dict(id='LOGO', src=None, a=0, b=3.2, boca=None, amb=0, speed=1, freeze=0, fw=[]))
esc('azotea', 'fade', 0.5)
seg('C2-03', 0.2, 5.4); seg('C2-04', 0.0, 6.0, boca='V04'); seg('C2-05', 1.0, 4.0, boca='V05'); seg('C2-06', 0.3, 3.9)
seg('C2-07', 1.6, 8.0, boca='L07'); seg('C2-08', boca='L08'); seg('C2-09', boca='V09'); seg('C2-10', 0.3, 4.0, boca='V10')
esc('puerta', 'fade', 0.3); seg('C2-11', 0.3, 5.9); seg('C2-12', 0.2, 5.9, src=tom('C2-12b'))
esc('cancion', 'fade', 0.6)
seg('C2-13', 0.1, 7.9, amb=0.0)                               # la Catrina a lo lejos abre los brazos
seg('C2-14', 0.8, 7.9, amb=0.0, speed=1.8)                    # «Bienvenidos, forasteros, a la Tierra del Recuerdo» (cámara lenta = ritmo del bolero)
seg('C2-16', 1.0, 8.0, amb=0.0, speed=1.93)                   # «Aquí vive quien te piensa, solo el olvido está muerto»
seg('C2-15', 0.2, 5.9, amb=0.3); seg('C2-17', 0.2, 7.9, amb=0.3); seg('C2-18', 0.2, 5.9, amb=0.4)
esc('precio', 'fade', 0.4)
seg('C2-19', 0.3, 3.9, boca='V19'); seg('C2-20', 0.0, 5.6, boca='C20'); seg('C2-21', 0.5, 3.8, boca='L21'); seg('C2-22', 0.6, 3.6, boca='C22')
seg('C2-23', 0.2, 5.6, boca='V23'); seg('C2-24', 0.2, 5.9)
esc('xolo', 'fade', 0.6)
seg('C2-25', 0.2, 5.9); seg('C2-26', 0.2, 7.9); seg('C2-27', 0.2, 5.9); seg('C2-28', 0.4, 3.8, boca='V28'); seg('C2-29', 0.2, 3.9); seg('C2-30', 0.2, 5.9)
esc('libro', 'fade', 0.3)
seg('C2-31', 0.2, 5.9); seg('C2-32', 0.2, 4.3)              # se corta antes de que aparezcan letras en las páginas
seg('C2-33', 0.2, 3.95); seg('C2-34', 1.6, 5.9, boca='V34'); seg('C2-35', 0.3, 3.95, boca='V35')
esc('max', 'fade', 0.3)
seg('C2-36', 0.2, 5.9, src=tom('C2-36b')); seg('C2-37', 0.2, 3.95); seg('C2-38', 0.0, 5.6, boca='L38')
esc('cierre', 'fade', 0.4)
seg('C2-39', 0.3, 7.9, boca='V39'); seg('C2-40', 0.2, 4.0, boca='V40'); seg('C2-41', 0.2, 9.9, freeze=6.0)

# ---------------- Tiempos ----------------
for s in SEG: s['len'] = (s['b'] - s['a']) * s['speed'] + s['freeze']
XF = 0.25; ESC.append(dict(start=len(SEG))); t = 0.0; T0 = [0.0] * len(SEG)
for e, nx in zip(ESC[:-1], ESC[1:]):
    if e['trans']: t -= e['td']
    for i in range(e['start'], nx['start']):
        if i > e['start']: t -= XF
        T0[i] = t; t += SEG[i]['len']
TOT = t; N = int((TOT + 1) * SR)
def ix(id_): return [s['id'] for s in SEG].index(id_)
def ti(id_): return T0[ix(id_)]
print(f'{len(SEG)} tomas · {TOT // 60:.0f}:{TOT % 60:04.1f}')

# ---------------- Voces pegadas a la boca ----------------
VOX = np.zeros(N, np.float32); AMB = np.zeros(N, np.float32)
def nivel(x):
    e = x[np.abs(x) > 0.02]; r = np.sqrt(np.mean(e ** 2)) if len(e) else 0.1
    return x * (0.12 / r)
def put(buf, x, t):
    i = int(t * SR)
    if i < 0: x = x[-i:]; i = 0
    j = min(N, i + len(x)); buf[i:j] += x[: j - i]
def habla(s):   # zonas donde habla Flow (por palabras), en segundos de la toma
    return [[max(0, a - 0.15), b + 0.25] for a, b, w in s['fw']]
ERR = []
for i, s in enumerate(SEG):
    if not s['boca']: continue
    x = nivel(load(VP[s['boca']])); ew = vwords(s['boca'])
    fw = [[a - s['a'], b - s['a'], w] for a, b, w in s['fw'] if s['a'] - 0.3 <= a < s['b']]
    try: y, err = pegar_suave(x, ew, fw, s['len'] + 2.5, lo=0.8, hi=1.25)
    except Exception as ex:
        print('  sin pegar', s['id'], ex); y = np.zeros(int((s['len'] + 2.5) * SR), np.float32); st = int(max(0, (fw[0][0] - ew[0][0]) if fw and ew else 0.3) * SR); y[st: st + len(x)] = x[: len(y) - st]; err = []
    # ajuste fino: correr la frase entera (±0,3 s) hasta que calce con cuando Flow habla
    fr = int(0.02 * SR); n_ = int(s['len'] / 0.02); M = np.zeros(n_)
    for va, vb in habla(s): M[max(0, int((va - s['a']) / 0.02)): max(0, int((vb - s['a']) / 0.02))] = 1
    if M.sum() > 5:
        m_ = len(y) // fr; ey = 20 * np.log10(np.sqrt(np.mean(y[: m_ * fr].reshape(m_, fr) ** 2, axis=1)) + 1e-9)
        Bv = (ey > -42).astype(float)[:n_]; Bv = np.pad(Bv, (0, max(0, n_ - len(Bv))))
        def ov(k): return np.sum(M[max(0, k): n_ + min(0, k)] * Bv[max(0, -k): n_ - max(0, k)]) / max(1, np.sum(np.maximum(M, Bv)))
        kb = max(range(-15, 16), key=lambda k: ov(k) - 0.002 * abs(k))
        if ov(kb) > ov(0) + 0.03: y = np.roll(y, kb * fr)
    put(VOX, y, T0[i] + 0.08); ERR += [abs(e) for e in err]
if ERR: print(f'boca: {len(ERR)} palabras, desfase medio {np.mean(ERR):.3f} s, 90 % < {np.percentile(ERR, 90):.2f} s')

# ---------------- Ambiente de cada toma (sin la voz de Flow) ----------------
for i, s in enumerate(SEG):
    if not s['src'] or s['amb'] <= 0 or s['speed'] != 1: continue
    X = 0.25; full = load(s['src']); a0 = max(0.0, s['a'] - X); a = full[int(a0 * SR): int((s['b'] + X) * SR)].copy()
    g = np.ones(len(a), np.float32)
    for va, vb in habla(s): g[int(max(0, va - a0) * SR): int(max(0, vb - a0) * SR)] = 0
    k_ = int(0.15 * SR); g = np.convolve(g, np.ones(k_) / k_, mode='same'); a *= g * s['amb']
    f = int(X * SR); a[:f] *= np.linspace(0, 1, f); a[-f:] *= np.linspace(1, 0, f)
    put(AMB, a, T0[i] - (s['a'] - a0))
# camas por lugar (silencios vivos)
AU = f'{C}/audio'
CAMA = dict(gancho=f'{AU}/AMB_PUEBLO.mp4', azotea=f'{AU}/AMANECER.mp3', puerta=f'{AU}/AMANECER.mp3', cancion=f'{AU}/AMB_PUEBLO.mp4',
            precio=f'{AU}/AMB_PUEBLO.mp4', xolo=f'{AU}/NOCHE_ALTAR.mp3', libro=f'{AU}/NOCHE_ALTAR.mp3', max=f'{AU}/NOCHE_ALTAR.mp3', cierre=f'{AU}/NOCHE_ALTAR.mp3')
NIV = dict(cancion=0.25)
for e, nx in zip(ESC[:-1], ESC[1:]):
    if e['n'] not in CAMA: continue
    bed = load(CAMA[e['n']]); bed = bed * (10 ** (-24 / 20) / (np.sqrt(np.mean(bed ** 2)) + 1e-9))
    t0 = T0[e['start']]; t1 = T0[nx['start']] if nx['start'] < len(SEG) else TOT; L = int((t1 - t0 + 0.5) * SR)
    out = bed.copy(); xf = int(1.0 * SR)
    while len(out) < L:
        r = bed.copy(); out[-xf:] = out[-xf:] * np.linspace(1, 0, xf) + r[:xf] * np.linspace(0, 1, xf); out = np.concatenate([out, r[xf:]])
    out = out[:L] * NIV.get(e['n'], 0.55); f = int(0.8 * SR); out[:f] *= np.linspace(0, 1, f); out[-f:] *= np.linspace(1, 0, f)
    put(AMB, out, t0)

# ---------------- Efectos en el cuadro exacto (segundos desde que empieza la toma en pantalla) ----------------
FX = np.zeros(N, np.float32); S2 = f'{P}/sfx2'
def fxf(name): return f'{AU}/{name}' if os.path.exists(f'{AU}/{name}') else f'{S2}/{name}'
def wend(id_, pre):
    s = SEG[ix(id_)]; return next(b for a, b, w in s['fw'] if norm(w).startswith(pre)) - s['a'] + 0.1
def fx(id_, rel, name, g=-10.0, largo=None, trim=True):
    x = load(fxf(name)).copy()
    if trim: on = np.argmax(np.abs(x) > 0.1 * np.max(np.abs(x))); x = x[max(0, on - int(0.01 * SR)):]
    if largo: x = x[: int(largo * SR)]; fo = int(0.6 * SR); x[-fo:] *= np.linspace(1, 0, fo)
    x *= 10 ** (g / 20) / (np.max(np.abs(x)) + 1e-9); put(FX, x, ti(id_) + rel)
fx('C2-01', -0.75, 'MUSICOS.mp3', -9, trim=False)        # los músicos tocan y paran en seco antes de «¡Por fin tengo público!»
fx('C2-02', wend('C2-02', 'literal'), 'GOLPE.mp3', -10)   # → logo
fx('LOGO', -0.25, 'WHOOSH.mp3', -8)
fx('C2-05', wend('C2-05', 'bot'), 'TRISTE.mp3', -9)       # «Es un bot»
fx('C2-07', 0.6, 'BRILLO.mp3', -13)                       # la llave que brilla
fx('C2-11', 3.1, 'PUERTA.mp3', -8)                        # se abre la puerta
fx('C2-12', 3.4, 'WHOOSH.mp3', -8)                        # entran a la luz
fx('C2-18', 0.0, 'RISAS.mp3', -16, largo=6.0)            # esqueletos de fiesta
fx('C2-20', 0.15, 'CAMPANA.mp3', -11)                     # la campanita
fx('C2-22', wend('C2-22', 'no'), 'GOLPE.mp3', -10)        # «No.»
fx('C2-24', 1.4, 'BRILLO.mp3', -11)                       # sale el recuerdo
fx('C2-27', 2.6, 'GRUNIDO.mp3', -12); fx('C2-29', 1.4, 'GRUNIDO.mp3', -8)
fx('C2-32', 1.3, 'LIBRO.mp3', -9)                         # el libro se abre
fx('C2-36', 0.0, 'RISER.mp3', -15, largo=6.0)             # la página arrancada
fx('C2-38', 0.0, 'ALAS.mp3', -8, largo=5.0)               # la Polilla arriba
fx('C2-40', wend('C2-40', 'episod') + 0.1, 'FIN.mp3', -9)

# ---------------- Música por momentos + la canción ----------------
MUS = np.zeros(N, np.float32)
def mus(f, a_id, a_rel, b_id, b_rel, ss=0.0, db=-26.0, fi=1.0, fo=2.0):
    f = fxf(f); t0, t1 = ti(a_id) + a_rel, ti(b_id) + b_rel; L = int((t1 - t0) * SR); src = load(f)[int(ss * SR):]
    while len(src) < L: src = np.concatenate([src, load(f)])
    x = src[:L].copy(); x *= 10 ** (db / 20) / (np.sqrt(np.mean(x ** 2)) + 1e-9)
    a_, b_ = int(min(fi, L / SR / 3) * SR), int(min(fo, L / SR / 3) * SR); x[:a_] *= np.linspace(0, 1, a_); x[-b_:] *= np.linspace(1, 0, b_)
    put(MUS, x, t0)
mus('M_TEMA.mp4', 'C2-03', 0.0, 'C2-07', 0.5, db=-27, fi=1.5)
mus('M_DIALOGO.mp4', 'C2-07', 0.0, 'C2-11', 0.5, db=-27, fo=1.0)
mus('M_MISTERIO.mp4', 'C2-11', 0.0, 'C2-12', 5.0, ss=2.0, db=-25, fo=1.5)
mus('M_MUERTOS.mp4', 'C2-19', 0.0, 'C2-25', 0.3, db=-28, fi=1.5)
mus('M_TIERNO.mp4', 'C2-25', 0.0, 'C2-27', 0.8, db=-25, fo=1.0)
mus('M_DIALOGO.mp4', 'C2-27', 0.5, 'C2-30', 0.5, ss=20, db=-27, fo=1.0)
mus('M_TIERNO.mp4', 'C2-30', 0.0, 'C2-31', 1.0, ss=12, db=-25, fo=1.0)
mus('M_MISTERIO.mp4', 'C2-31', 0.0, 'C2-33', 0.3, ss=8, db=-25, fo=0.8)
mus('M_TIERNO.mp4', 'C2-33', 0.0, 'C2-36', 0.3, ss=24, db=-25, fo=1.0)
mus('M_SUSPENSO.mp4', 'C2-36', 0.0, 'C2-39', 0.5, ss=10, db=-25, fo=1.5)
mus('M_MISTERIO.mp4', 'C2-39', 0.0, 'C2-40', 0.5, ss=16, db=-28, fo=1.0)
mus('M_TIERNO.mp4', 'C2-40', 0.3, 'C2-41', 15.4, ss=30, db=-25, fi=1.5, fo=5.0)
# la canción: «Bienvenidos» (14,9 s de la canción) cae cuando la Catrina lo canta en C2-14 (1,23 s de la toma, en cámara lenta ×1,8)
SONG = np.zeros(N, np.float32); s14 = SEG[ix('C2-14')]
t_song0 = ti('C2-14') + (1.23 - s14['a']) * s14['speed'] - 14.9
song = load(f'{AU}/cancion1.mp4').copy(); song *= 10 ** (-19 / 20) / (np.sqrt(np.mean(song[int(15 * SR): int(55 * SR)] ** 2)) + 1e-9)
a_s = int(4.0 * SR); song = song[a_s: int(60.0 * SR)]; fi = int(1.5 * SR); song[:fi] *= np.linspace(0, 1, fi); fo = int(3.0 * SR); song[-fo:] *= np.linspace(1, 0, fo)
put(SONG, song, t_song0 + 4.0)
print('canción: «Aquí vive» cae a', round(t_song0 + 27.4 - ti('C2-16'), 2), 's de C2-16 (la boca dice «Aquí» a', round((1.42 - 1.0) * 1.93, 2), ')')

envv = np.convolve(np.abs(VOX), np.ones(int(0.3 * SR)) / int(0.3 * SR), mode='same'); duck = np.clip(envv / 0.015, 0, 1)
duck = np.convolve(duck, np.ones(int(0.25 * SR)) / int(0.25 * SR), mode='same')
LOGOMUS = np.zeros(N, np.float32); lm = glob.glob(f'{P}/sfx/*Key_of_the_Veil*')
if lm:
    m_ = load(lm[0])[: int(4.2 * SR)].copy(); m_ *= 10 ** (-18 / 20) / (np.sqrt(np.mean(m_ ** 2)) + 1e-9)
    fo = int(1.2 * SR); m_[-fo:] *= np.linspace(1, 0, fo); put(LOGOMUS, m_, ti('LOGO') - 0.5)
MIX = np.clip(VOX * 1.15 + AMB * (0.45 - 0.33 * duck) + MUS * (1 - 0.68 * duck) + FX * (1 - 0.4 * duck) + SONG + LOGOMUS, -1, 1)
MIX.astype(np.float32).tofile('_mix.f32')
if os.environ.get('DUMP'): np.save('_vox.npy', VOX); np.save('_amb.npy', AMB)
json.dump(dict(T0=T0, segs=[(s['id'], s['a'], s['b'], s['len']) for s in SEG]), open('_timeline.json', 'w'))
if os.environ.get('SOLO_AUDIO'): sys.exit()

# ---------------- Video ----------------
BASE = 'scale=1920:1080:flags=lanczos,setsar=1,fps=24,format=yuv420p'
def stats(s):
    fr = []
    for t in np.linspace(s['a'] + 0.3, s['b'] - 0.3, 3):
        r = sp.run(['ffmpeg', '-v', 'error', '-ss', f'{t:.2f}', '-i', s['src'], '-frames:v', '1', '-vf', 'scale=96:54', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], capture_output=True).stdout
        if r: fr.append(np.frombuffer(r, np.uint8).reshape(-1, 3).astype(float))
    x = np.concatenate(fr); return x.mean(0), x.std(0)
GRADE = {}
for e, nx in zip(ESC[:-1], ESC[1:]):
    ids = [i for i in range(e['start'], nx['start']) if SEG[i]['src'] and SEG[i]['id'] not in ('C2-33', 'C2-37', 'C2-32')]
    if len(ids) < 2: continue
    st_ = {i: stats(SEG[i]) for i in ids}; mT = np.median([st_[i][0] for i in ids], 0); sT = np.median([st_[i][1] for i in ids], 0)
    for i in ids:
        m, sd = st_[i]; k = 1 + 0.5 * (sT / np.maximum(sd, 1) - 1); tt = m + 0.5 * (mT - m)
        GRADE[i] = 'lutrgb=' + ':'.join(f"{c}='clip((val-{m[j]:.1f})*{k[j]:.3f}+{tt[j]:.1f},0,255)'" for j, c in enumerate('rgb'))
def clip(i, s, out):
    n = int(round(s['len'] * 24))
    if s['id'] == 'LOGO':
        sp.run(['ffmpeg', '-v', 'error', '-y', '-i', f'{REFS}/marca/LOGO-EXTRAVIO.jpg', '-vf',
                f"crop=iw:iw*9/16:0:(ih-iw*9/16)/2,scale=1920:1080,zoompan=z='1+0.0006*on':x='iw/2-iw/zoom/2':y='ih/2-ih/zoom/2':d={n}:s=1920x1080:fps=24,{BASE}",
                '-frames:v', str(n), '-c:v', 'libx264', '-crf', '16', out], check=True); return
    vf = []
    if s['speed'] != 1: vf += [f"setpts={s['speed']}*PTS", "minterpolate=fps=24:mi_mode=blend"]
    if i in GRADE: vf.append(GRADE[i])
    vf.append(BASE)
    if s['freeze']: vf.append(f"tpad=stop_mode=clone:stop_duration={s['freeze']}")
    sp.run(['ffmpeg', '-v', 'error', '-y', '-ss', str(s['a']), '-t', str(s['b'] - s['a']), '-i', s['src'], '-vf', ','.join(vf),
            '-an', '-frames:v', str(n), '-c:v', 'libx264', '-crf', '16', out], check=True)
for i, s in enumerate(SEG):
    if not (os.environ.get('REUSAR') and os.path.exists(f'_v/{i:02d}.mp4')): clip(i, s, f'_v/{i:02d}.mp4')
escenas = []
for k, (e, nx) in enumerate(zip(ESC[:-1], ESC[1:])):
    out = f'_v/esc{k:02d}.mp4'; idx = list(range(e['start'], nx['start']))
    if len(idx) == 1: sp.run(['ffmpeg', '-v', 'error', '-y', '-i', f'_v/{idx[0]:02d}.mp4', '-c', 'copy', out], check=True)
    else:
        inp, fc_, lst, acc_ = [], [], '[a0]', SEG[idx[0]]['len']
        for j, i in enumerate(idx):
            inp += ['-i', f'_v/{i:02d}.mp4']; fc_.append(f'[{j}:v]setpts=PTS-STARTPTS,fps=24,settb=1/24,format=yuv420p[a{j}]')
            if j == 0: continue
            fc_.append(f"{lst}[a{j}]xfade=transition=fade:duration={XF}:offset={acc_ - XF:.3f},settb=1/24[y{j}]"); acc_ += SEG[i]['len'] - XF; lst = f'[y{j}]'
        sp.run(['ffmpeg', '-v', 'error', '-y'] + inp + ['-filter_complex', ';'.join(fc_), '-map', lst, '-c:v', 'libx264', '-crf', '16', '-pix_fmt', 'yuv420p', out], check=True)
    escenas.append((out, sum(SEG[i]['len'] for i in idx) - XF * (len(idx) - 1), e.get('trans'), e.get('td', 0)))
inputs, fc, acc, last = [], [], 0.0, '[v0]'
for k, (f, L, tr, td) in enumerate(escenas):
    inputs += ['-i', f]; fc.append(f'[{k}:v]setpts=PTS-STARTPTS,fps=24,settb=1/24,format=yuv420p[v{k}]')
    if k == 0: acc = L; continue
    if tr: fc.append(f"{last}[v{k}]xfade=transition={tr}:duration={td}:offset={acc - td:.3f},settb=1/24[x{k}]"); acc += L - td
    else: fc.append(f"{last}[v{k}]concat=n=2:v=1:a=0,settb=1/24[x{k}]"); acc += L
    last = f'[x{k}]'
sp.run(['ffmpeg', '-v', 'error', '-y'] + inputs + ['-filter_complex', ';'.join(fc), '-map', last, '-c:v', 'libx264', '-crf', '17', '-pix_fmt', 'yuv420p', '_video.mp4'], check=True)
sp.run(['ffmpeg', '-v', 'error', '-y', '-i', '_video.mp4', '-f', 'f32le', '-ar', str(SR), '-ac', '1', '-i', '_mix.f32', '-map', '0:v', '-map', '1:a',
        '-c:v', 'copy', '-c:a', 'aac', '-b:a', '256k', '-shortest', '_mux.mp4'], check=True)
def lufs(f):
    o = sp.run(['ffmpeg', '-hide_banner', '-i', f, '-af', 'ebur128', '-f', 'null', '-'], capture_output=True, text=True).stderr
    return float(re.findall(r'I:\s+(-?[\d.]+) LUFS', o)[-1])
g = -14 - lufs('_mux.mp4') + 2.4
sp.run(['ffmpeg', '-v', 'error', '-y', '-i', '_mux.mp4', '-c:v', 'copy', '-af', f'aresample=192000,volume={g:.2f}dB,alimiter=limit=0.82:attack=1:release=60:level=disabled,aresample=48000',
        '-c:a', 'aac', '-b:a', '256k', '-movflags', '+faststart', 'EXTRAVIO-CAP02.mp4'], check=True)
print('listo', round(TOT, 1), 's · volumen', lufs('EXTRAVIO-CAP02.mp4'), 'LUFS')
