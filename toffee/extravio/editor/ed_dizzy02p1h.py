# -*- coding: utf-8 -*-
"""Editor del capítulo 2 de Dizzy (México), PARTE 1, HORIZONTAL 16:9 (9-nov-2026).
Reusa el pegado de voces del cap. 1 (alinear() de ed_dizzy01p2: frases de ElevenLabs sobre la boca medida de Flow).
Lugares sin personajes = fotos animadas (cámara lenta, grano; el mapa con la raya verde).
TMPED=<carpeta> python3 toffee/extravio/editor/ed_dizzy02p1.py -> toffee/videos-editados/EXTRAVIO-DIZZY-CAP02-P1.mp4
"""
import os, sys, json, subprocess as sp
import numpy as np, cv2
AQ = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, AQ)
import ed_dizzy01p2 as M  # noqa: E402
from pegar import load, SR  # noqa: E402
RAIZ = os.path.abspath(os.path.join(AQ, '..'))
TK = os.path.join(RAIZ, 'serie', 'tomas-cap02', 'horizontal'); TK1 = os.path.join(RAIZ, 'serie', 'tomas-cap01')
VZ = os.path.join(RAIZ, 'serie', 'voces-cap02', 'p1'); SN = os.path.join(RAIZ, 'sonidos')
LUG = os.path.abspath(os.path.join(RAIZ, '..', 'refs', 'extravio', 'lugares'))
FONTS = os.path.join(AQ, 'datos-dizzy01', 'fonts')
TMP = os.environ.get('TMPED', '/tmp/ed_dizzy02p1h'); os.makedirs(TMP, exist_ok=True)
OUT = os.path.abspath(os.path.join(RAIZ, '..', 'videos-editados', 'EXTRAVIO-DIZZY-CAP02-P1-H.mp4'))
W, H, FPS = 1920, 1080, 30
XF = 0.3  # fundido entre tomas
M.TK = TK; M.TMP = TMP

# t = toma (o foto), a/b = corte, v = voz, sc = escena (música/ambiente)
E = [
 # GANCHO (sin la alcantarilla, pedido de Jay): la Catrina llega y lo ve
 dict(t='T11', a=0.3, b=2.9, v='T11', mute=1, sc='hook'),
 dict(t='T19', a=0.4, b=5.2, v='T19', sc='hook'),
 # TÍTULO sobre la finca a medianoche
 dict(t='A-FINCA', a=0.0, b=4.6, sc='finca', titulo='EXTRAVÍO · VLOG 02'),
 dict(t='T01', a=0.6, b=7.7, v='T01', sc='finca'),
 dict(t='T02', a=0.2, b=3.8, sc='finca'),
 dict(t='A-PUEBLO', a=0.0, b=4.2, sc='pueblo'),
 dict(t='T03', a=0.5, b=7.2, v='T03', sc='pueblo'),
 # el callejón de la visión
 dict(t='T06', a=1.6, b=5.2, v='T06', sc='callejon'),
 dict(t='T07', a=2.6, b=5.9, v='T07', sc='callejon'),
 dict(t='G99', src=TK1, a=0.0, b=2.4, sc='callejon', vision=1),
 dict(t='T07b', a=0.0, b=4.0, sc='callejon'),
 dict(t='T08', a=0.0, b=4.0, sc='callejon'),
 dict(t='T09', a=0.5, b=5.0, v='T09', mute=1, sc='callejon'),
 dict(t='T10', a=0.5, b=5.6, v='T10', sc='callejon'),
 dict(t='T11', a=0.0, b=4.0, v='T11', mute=1, sc='tunel'),
 # el viaje
 dict(foto='AEREA-AMERICA-NOCHE.jpg', d=5.0, mov='mapa', sc='mapa'),
 dict(t='A-CDMX', a=0.0, b=4.5, sc='mx'),
 dict(t='T14', a=0.5, b=5.5, sc='mx'),
 dict(t='T15', a=0.0, b=4.0, sc='mx'),
 dict(t='T16', a=0.6, b=4.6, v='T16', sc='mx'),
 dict(t='T17', a=0.3, b=3.9, v='T17h', sc='mx'),
 dict(t='H-PRUEBA', a=0.6, b=4.2, v='H-PRUEBA', vcut=1, sc='mx'),
 # la Catrina
 dict(t='T18', a=0.0, b=8.0, sc='catrina', fx=[('efectos/E29-huesos-catrina', 1.0, 0.8)]),
 dict(t='T19', a=0.4, b=5.2, v='T19', sc='catrina'),
 dict(t='T20', a=0.6, b=5.6, v='T20', sc='catrina'),
 dict(t='T21', a=0.9, b=5.7, v='T21', sc='catrina'),
 dict(t='T22', a=0.2, b=3.2, v='T22', sc='flirt'),
 dict(t='T23', a=0.0, b=8.0, v='T23', sc='flirt'),
 dict(t='T24', a=0.0, b=4.0, v='T24', sc='flirt', fx=[('efectos/E29-huesos-catrina', 0.1, 0.7)]),
 dict(t='T25', a=0.0, b=4.5, v='T25', sc='flirt'),
 # persecución
 dict(t='A-BARRIO', a=0.0, b=4.2, sc='chase'),
 dict(t='T26', a=0.0, b=6.0, sc='chase'),
 dict(t='T27', a=2.0, b=6.0, v='T27', sc='chase'),
 dict(t='T28', a=0.0, b=4.0, sc='chase'),
 # Chuy
 dict(t='T29', a=2.0, b=7.5, v='T29', sc='chuy'),
 dict(t='T30', a=0.5, b=2.6, v='T30', sc='chuy'),
 dict(t='T31', a=0.0, b=6.8, v='T31', sc='chuy'),
 # suspenso
 dict(t='T33', a=0.0, b=4.0, sc='susp', fx=[('efectos/E17-bajo-amenaza', 0.3, 1.0)]),
 dict(t='T34', a=1.5, b=4.5, v='T34', mute=1, sc='susp'),
 dict(t='T35', a=0.8, b=4.0, v='T35', sc='susp'),
]
MUS = {'hook': ('M12b-mariachi-muertos-metales', 0.30), 'finca': ('M10-misterio-camara', 0.22), 'pueblo': ('M10-misterio-camara', 0.22),
       'callejon': ('M10-misterio-camara', 0.26), 'mx': ('M12-mariachi-muertos', 0.30), 'catrina': ('M16-vals-catrina', 0.55),
       'flirt': ('M6-cuca-saxofon', 0.28), 'chase': ('M13-persecucion-cumbia', 0.32), 'chuy': ('M15-tema-chuy', 0.28), 'susp': ('M10-misterio-camara', 0.25)}
AMB = {'callejon': 'E26-ambiente-alcantarilla', 'tunel': 'E26-ambiente-alcantarilla', 'mx': 'E25-ambiente-muertos-noche', 'catrina': 'E25-ambiente-muertos-noche',
       'flirt': 'E25-ambiente-muertos-noche', 'chase': 'E25-ambiente-muertos-noche', 'hook': 'E25-ambiente-muertos-noche'}
TRAD = {'T03': ['Bro,', 'es medianoche.', 'Esta es', 'una pésima idea.'], 'T06': ['Bro…', '¡está brillando!'], 'T10': ['¡Espérenme!'],
        'T22': ['Uff…', '¡qué mamacita!'],
        'T23': ['¡Mamacita!', 'No me importa', 'que seas puro hueso…', 'me gustan flaquitas.']}
FIX = {'T17h': ['Bro…', '¡estamos en', 'México!']}  # subtítulo fijo (Whisper oye «Brother»)
ROJO = {'ratas', 'doce', 'gringo', 'visión', 'méxico', 'méxico!', 'alma', 'perdida', 'panteón', 'chuy', 'muertos', 'marrano', 'flaquitas',
        'hueso…', 'flaca', 'youtube', 'méxico,', 'tacos!', 'medianoche.', 'brillando!', 'mamacita!', 'encontré'}

def run(a): sp.run(a, check=True)
def ffdur(f): return float(sp.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', f], capture_output=True, text=True).stdout)

# ---------- fotos animadas ----------
def foto(e, out):
    im = cv2.imread(os.path.join(LUG, e['foto'])).astype(np.float32) / 255
    im = cv2.resize(im, (W * 2, int(W * 2 * im.shape[0] / im.shape[1])), interpolation=cv2.INTER_CUBIC)
    h, w = im.shape[:2]; n = int(e['d'] * FPS); rng = np.random.default_rng(1)
    ease = lambda t: t * t * (3 - 2 * t)
    p = sp.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                  '-c:v', 'libx264', '-crf', '17', '-preset', 'fast', '-pix_fmt', 'yuv420p', out], stdin=sp.PIPE)
    if e['mov'] == 'mapa':
        sx, sy = w / 1116, h / 2000
        P0 = np.array([870 * sx, 1235 * sy]); P1 = np.array([560 * sx, 930 * sy]); P2 = np.array([95 * sx, 690 * sy])
        pts = np.array([(1 - t) ** 2 * P0 + 2 * (1 - t) * t * P1 + t ** 2 * P2 for t in np.linspace(0, 1, 500)]); spark = []
    for i in range(n):
        t = i / max(1, n - 1); img = im
        if e['mov'] == 'mapa':
            pr = ease(np.clip((t - 0.1) / 0.65, 0, 1)); k = int(pr * 499); lay = np.zeros_like(im)
            if k > 1:
                pl = pts[:k + 1].astype(np.int32).reshape(-1, 1, 2)
                cv2.polylines(lay, [pl], False, (0.35, 1.0, 0.45), 10, cv2.LINE_AA); glow = cv2.GaussianBlur(lay, (0, 0), 26) * 2.2
                core = np.zeros_like(im); cv2.polylines(core, [pl], False, (0.85, 1, 0.9), 3, cv2.LINE_AA)
                hx, hy = pts[k]
                if pr < 1:
                    for _ in range(3): spark.append([hx + rng.normal(0, 9), hy + rng.normal(0, 9), rng.normal(0, 2), rng.normal(-1, 2), 1.0])
                    cv2.circle(core, (int(hx), int(hy)), 13, (0.9, 1, 0.95), -1, cv2.LINE_AA)
                fl = np.zeros_like(im)
                if pr >= 1:
                    a2 = max(0, 1 - (t - 0.75) / 0.2); cv2.circle(fl, tuple(P2.astype(int)), 60, (0.5, 1, 0.6), -1); fl = cv2.GaussianBlur(fl, (0, 0), 45) * 3 * a2
                sp_ = np.zeros_like(im)
                for s in spark:
                    s[0] += s[2]; s[1] += s[3]; s[4] *= 0.95
                    cv2.circle(sp_, (int(s[0]), int(s[1])), 3, (0.6 * s[4], s[4], 0.7 * s[4]), -1, cv2.LINE_AA)
                spark[:] = [s for s in spark if s[4] > 0.05]
                lay = glow + core + cv2.GaussianBlur(sp_, (0, 0), 2) * 1.5 + fl
            img = im + lay; z = 1.05 + 0.2 * ease(t); cx = 0.5 - 0.1 * ease(t); cy = 0.52 - 0.1 * ease(t)
        elif e['mov'] == 'baja':
            z = 1.0 + 0.16 * ease(t); cx = 0.5; cy = 0.45 + 0.08 * ease(t)
        else:
            z = 1.04 + 0.14 * ease(t); cx = 0.5; cy = 0.5
        s = (W / w) * z
        Mx = np.float32([[s, 0, W / 2 - s * cx * w], [0, s, H / 2 - s * cy * h]])
        f = cv2.warpAffine(img, Mx, (W, H), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)
        g = cv2.resize(rng.normal(0, 0.012, (H // 2, W // 2)).astype(np.float32), (W, H))[..., None]
        p.stdin.write((np.clip(f + g, 0, 1) * 255).astype(np.uint8).tobytes())
    p.stdin.close(); p.wait()

def toma_video(e, out):
    src = os.path.join(e.get('src', TK), e['t'] + '.mp4')
    vf = 'scale=1920:1080:flags=lanczos,fps=30,format=yuv420p'
    if e.get('vision'):
        vf = ('split[x][y];[x]scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,gblur=sigma=30,eq=brightness=-0.15[bg];'
              '[y]scale=-2:1080[fg];[bg][fg]overlay=(W-w)/2:0,fps=30,colorchannelmixer=rr=0.7:gg=1.15:bb=0.7,noise=alls=14:allf=t,'
              'drawbox=x=60:y=50:w=140:h=8:c=white:t=fill,drawbox=x=60:y=50:w=8:h=110:c=white:t=fill,'
              'drawbox=x=1720:y=50:w=140:h=8:c=white:t=fill,drawbox=x=1852:y=50:w=8:h=110:c=white:t=fill,'
              'drawbox=x=60:y=1022:w=140:h=8:c=white:t=fill,drawbox=x=60:y=920:w=8:h=110:c=white:t=fill,'
              'drawbox=x=1720:y=1022:w=140:h=8:c=white:t=fill,drawbox=x=1852:y=920:w=8:h=110:c=white:t=fill,'
              "drawbox=x=1620:y=96:w=26:h=26:c=red:t=fill:enable='lt(mod(t,1),0.6)',"
              f"drawtext=fontfile={FONTS}/Montserrat.ttf:text=REC:x=1660:y=90:fontsize=40:fontcolor=white,format=yuv420p")
    run(['ffmpeg', '-v', 'error', '-y', '-ss', str(e['a']), '-to', str(e['b']), '-i', src, '-an', '-vf' if not e.get('vision') else '-filter_complex', vf,
         '-c:v', 'libx264', '-crf', '16', '-preset', 'fast', out])


BOC = json.load(open(os.path.join(RAIZ, 'serie', 'cap02', 'cap02_bocas_p1h.json')))
BOC['T23'] = {'tramos': [[1.2, 5.0]], 'habla': 3.8, 'palabras': []}  # toma G sin voz: la frase va en off mientras camina
GRITO = {'T09', 'T11', 'T23'}
def _n(w):
    import unicodedata, re
    w = unicodedata.normalize('NFD', w.lower()); w = ''.join(c for c in w if unicodedata.category(c) != 'Mn')
    return re.sub(r'[^a-z0-9]', '', w)
def _tramos_voz(x):
    fr = int(0.01 * SR); n = len(x) // fr
    e = 20 * np.log10(np.sqrt(np.mean(x[:n * fr].reshape(n, fr) ** 2, axis=1)) + 1e-9); on = e > -38; out = []; i = 0
    while i < n:
        if on[i]:
            j = i
            while j < n and (on[j] or on[j:j + 6].any()): j += 1
            if j - i >= 5: out.append([i * 0.01, j * 0.01])
            i = j
        else: i += 1
    return out
def sincronizar(t, a, b, v, lang):
    """Anclas palabra por palabra: palabras de Flow (Whisper) ajustadas al arranque real de cada tramo de boca, y
    palabras de ElevenLabs ajustadas al arranque real de cada tramo de voz. Devuelve (señal desde a, mapa voz→clip, error)."""
    import difflib
    vx = load(os.path.join(VZ, v + '.mp3'))
    S = [[q[0] - a, q[1] - a] for q in BOC[t]['tramos'] if q[1] > a and q[0] < b]
    S = [q for q in S if q[1] - q[0] >= 0.2] or S
    if t in GRITO or not BOC[t]['palabras']:
        st = S[0][0] if S else 0.2; tv = _tramos_voz(vx); v0 = tv[0][0] if tv else 0.0
        y = np.zeros(int((b - a + 3) * SR)); s0 = int(max(0, st - v0 + 0.03) * SR); y[s0:s0 + len(vx)] = vx[:len(y) - s0]
        return y, (lambda tv_: tv_ - v0 + st + 0.03), 0.0
    FW = [[w[0] - a, w[1] - a, w[2]] for w in BOC[t]['palabras'] if w[1] - a > 0.05 and w[0] - a < b - a]
    def snap(words, segs):
        out = []; usados = set()
        for w in words:
            best = None; ov = 0
            for j, q in enumerate(segs):
                o = min(w[1], q[1]) - max(w[0], q[0])
                if o > ov: ov, best = o, j
            if best is None:
                best = int(np.argmin([abs(q[0] - w[0]) for q in segs])) if segs else None
            s0 = w[0]
            if best is not None:
                q = segs[best]
                s0 = q[0] if best not in usados else min(max(w[0], q[0]), q[1] - 0.05)
                usados.add(best)
            out.append([s0, w[1], w[2]])
        for k in range(1, len(out)): out[k][0] = max(out[k][0], out[k - 1][0] + 0.06)
        return out
    FW = snap(FW, S)
    VW = snap([list(w) for w in palabras(v, lang)], _tramos_voz(vx))
    sm = difflib.SequenceMatcher(None, [_n(w[2]) for w in VW], [_n(w[2]) for w in FW], autojunk=False)
    pares = []
    for blk in sm.get_matching_blocks():
        for k in range(blk.size): pares.append((VW[blk.a + k][0], FW[blk.b + k][0]))
    if not pares: pares = [(VW[0][0], FW[0][0])] if VW and FW else [(0.0, S[0][0] if S else 0.2)]
    toks = ['k' + chr(97 + (i % 26)) * 3 + str(i) for i in range(len(pares))]
    ew = [[pv, pv + 0.1, k] for (pv, _), k in zip(pares, toks)]; fw = [[pf + 0.03, pf + 0.13, k] for (_, pf), k in zip(pares, toks)]
    # 9-nov-2026 (Jay: «las voces suenan ralentizadas»): NADA de estirar. La voz se parte solo en silencios reales
    # (>= 0,18 s bajo -40 dB) y cada frase entera se mueve para que su primera palabra caiga en la boca de Flow.
    fr = int(0.01 * SR); n_ = len(vx) // fr
    db = 20 * np.log10(np.sqrt(np.mean(vx[:n_ * fr].reshape(n_, fr) ** 2, axis=1)) + 1e-9); on = db > -40
    fr_ = []; i = 0
    while i < n_:
        if on[i]:
            j = i
            while j < n_ and (on[j] or on[j:j + 18].any()): j += 1
            fr_.append([max(0, i * 0.01 - 0.03), min(len(vx) / SR, j * 0.01 + 0.05)]); i = j
        else: i += 1
    if not fr_: fr_ = [[0.0, len(vx) / SR]]
    vmap = {pv: pf for pv, pf in pares}
    L = int((b - a + 3) * SR); y = np.zeros(L); offs = []; prev_end = -1.0; errs = []
    for k, (f0, f1) in enumerate(fr_):
        dentro = [pv for pv in vmap if f0 - 0.05 <= pv <= f1]
        if dentro:
            pv = min(dentro); st = vmap[pv] - (pv - f0)
        else:
            st = (prev_end + (f0 - fr_[k - 1][1])) if k else (S[0][0] if S else 0.2)
        st = max(st, prev_end + 0.08, 0.0)
        if dentro: errs.append(abs(st + (pv - f0) - vmap[pv]))
        seg = vx[int(f0 * SR): int(f1 * SR)].copy(); g = min(len(seg) // 2, int(0.01 * SR))
        if g: seg[:g] *= np.linspace(0, 1, g); seg[-g:] *= np.linspace(1, 0, g)
        k0 = int(st * SR); m = min(len(seg), L - k0)
        if m > 0: y[k0:k0 + m] += seg[:m]
        offs.append((f0, f1, st - f0)); prev_end = st + (f1 - f0)
    def mapa_(tv_, o_=offs):
        for f0, f1, d in o_:
            if tv_ <= f1 + 0.02: return tv_ + d
        return tv_ + o_[-1][2]
    return y, mapa_, (max(errs) if errs else 0.0)

# ---------- palabras de cada voz (para subtítulos) ----------
_WH = None
def palabras(v, lang):
    cache = os.path.join(TMP, f'w_{v}.json')
    if os.path.exists(cache): return json.load(open(cache))
    global _WH
    if _WH is None:
        from faster_whisper import WhisperModel; _WH = WhisperModel('small', compute_type='int8')
    a = sp.run(['ffmpeg', '-v', 'error', '-i', os.path.join(VZ, v + '.mp3'), '-ac', '1', '-ar', '16000', '-f', 'f32le', '-'], capture_output=True).stdout
    s, _ = _WH.transcribe(np.frombuffer(a, np.float32), language=lang, word_timestamps=True)
    w = [[z.start, z.end, z.word.strip()] for g in s for z in g.words]; json.dump(w, open(cache, 'w')); return w

SYNC = []
def main():
    plan = []; t0 = 0.0
    for i, e in enumerate(E):
        vf = os.path.join(TMP, f'seg{i:02d}.mp4')
        if 'foto' in e:
            if not os.path.exists(vf): foto(e, vf)
            d = e['d']
        else:
            toma_video(e, vf); d = e['b'] - e['a']
        plan.append(dict(e, vf=vf, t0=t0, d=d)); t0 += d - XF
    TOT = t0 + XF; N = int(TOT * SR) + SR * 3
    flow = np.zeros(N); voz = np.zeros(N); fx = np.zeros(N); subs = []
    for p in plan:
        if 'foto' in p: continue
        src = os.path.join(p.get('src', TK), p['t'] + '.mp4')
        x = load(src)[int(p['a'] * SR): int(p['b'] * SR)]
        env = np.ones(len(x)) * (0.55 if p.get('v') else (1.0 if p.get('grito') else 0.75))
        if p.get('vision'): env *= 0.5
        if p.get('mute'): env *= 0.0  # voz de Flow fuera: solo la de ElevenLabs (pedido de Jay)
        if p.get('v'):
            Q = [[q[0] - p['a'], q[1] - p['a']] for q in BOC[p['t']]['tramos'] if q[1] > p['a'] and q[0] < p['b']]
            Wd = [w for w in BOC[p['t']]['palabras'] if w[1] > p['a'] and w[0] < p['b']]
            fin = (Wd[-1][1] - p['a'] + 0.15) if Wd else (Q[-1][1] + 0.35 if Q else 0)
            if Q: env[max(0, int((Q[0][0] - 0.25) * SR)): int(fin * SR)] = 0.0
            env[int(fin * SR):] = 0.9
            env = np.convolve(env, np.ones(480) / 480, 'same')
            lang = 'en' if p['v'] in TRAD else 'es'
            y, mapa, err = sincronizar(p['t'], p['a'], p['b'], p['v'], lang)
            if p.get('vcut'):
                L_ = int(p['d'] * SR); y = y[:L_].copy(); f_ = int(0.15 * SR); y[-f_:] *= np.linspace(1, 0, f_)
            SYNC.append((p['t'], round(err, 2)))
            k = int(p['t0'] * SR); voz[k:k + len(y)] += y[:N - k]
            lang = 'en' if p['v'] in TRAD else 'es'
            ws = palabras(p['v'], lang)
            if (p['v'] in TRAD or p['v'] in FIX) and ws:
                a0 = mapa(ws[0][0]); a1 = mapa(ws[-1][1]); ch = TRAD.get(p['v']) or FIX[p['v']]; step = (a1 - a0) / len(ch)
                for j, c in enumerate(ch): subs.append((p['t0'] + a0 + j * step, p['t0'] + a0 + (j + 1) * step + 0.15, c))
            elif ws and p['t'] not in ('T09', 'T11'):
                grp = []; cur = []
                for w_ in ws:
                    cur.append(w_)
                    if len(cur) == 3 or len(' '.join(z[2] for z in cur)) > 13 or w_[2][-1:] in '.,?!…': grp.append(cur); cur = []
                if cur: grp.append(cur)
                for j, g in enumerate(grp):
                    if p.get('vcut') and mapa(g[0][0]) > p['d'] - 0.3: break
                    s0 = p['t0'] + mapa(g[0][0]); s1 = p['t0'] + (mapa(grp[j + 1][0][0]) if j + 1 < len(grp) else mapa(g[-1][1]) + 0.35)
                    subs.append((s0, min(s1, s0 + 1.6), ' '.join(g_[2] for g_ in g)))
        f_ = int(XF * SR)
        if len(x) > 2 * f_: env = env.copy(); env[:f_] *= np.linspace(0, 1, f_); env[-f_:] *= np.linspace(1, 0, f_)
        k = int(p['t0'] * SR); flow[k:k + len(x)] += x * env[:len(x)]
        for f, at, g in p.get('fx', []):
            z = load(os.path.join(SN, f + '.mp3')) * g; k2 = int((p['t0'] + at) * SR); fx[k2:k2 + len(z)] += z[:N - k2]
    # viaje mágico en el mapa
    for p in plan:
        if p.get('mov') == 'mapa':
            z = load(os.path.join(SN, 'efectos', 'E33-viaje-magico.mp3')) * 0.8; k2 = int((p['t0'] + 0.4) * SR); fx[k2:k2 + len(z)] += z[:N - k2]
    # música y ambiente por bloques de escena
    mus = np.zeros(N); amb = np.zeros(N)
    blocks = []
    for p in plan:
        if blocks and blocks[-1][0] == p['sc']: blocks[-1][2] = p['t0'] + p['d']
        else: blocks.append([p['sc'], p['t0'], p['t0'] + p['d']])
    def bed(name, a, b, g, arr, fade=0.4):
        z = load(os.path.join(SN, ('musica' if name.startswith('M') else 'ambientes'), name + '.mp3'))
        L = int((b - a) * SR); z = np.tile(z, L // len(z) + 1)[:L] * g
        f = int(fade * SR); z[:f] *= np.linspace(0, 1, f); z[-f:] *= np.linspace(1, 0, f)
        k = int(a * SR); arr[k:k + L] += z[:N - k]
    for sc, a, b in blocks:
        if sc in MUS: bed(MUS[sc][0], a, b, MUS[sc][1], mus)
        if sc in AMB: bed(AMB[sc], a, b, 0.22, amb, 0.6)
    hab = np.zeros(N)
    for p in plan:
        if p.get('v'): hab[int(p['t0'] * SR): int((p['t0'] + p['d']) * SR)] = 1
    w_ = int(1.2 * SR); duck = 1 - 0.35 * np.convolve(hab, np.ones(w_) / w_, 'same')  # baja 3-4 dB en toda la toma con diálogo, sin subir y bajar a cada palabra
    mix = flow + voz + fx + mus * duck + amb
    mix = mix[:int(TOT * SR)]
    wav = os.path.join(TMP, 'mix.wav')
    sp.run(['ffmpeg', '-v', 'error', '-y', '-f', 'f32le', '-ar', str(SR), '-ac', '1', '-i', '-', '-af', 'loudnorm=I=-14:TP=-1.5', '-ar', '48000', '-ac', '2', wav],
           input=np.clip(mix, -1, 1).astype(np.float32).tobytes(), check=True)
    # video
    vid = os.path.join(TMP, 'video.mp4'); inp = []; fc = []
    for p in plan: inp += ['-i', p['vf']]
    last = '0:v'
    for k in range(1, len(plan)):
        fc.append(f"[{last}][{k}:v]xfade=transition=fade:duration={XF}:offset={plan[k]['t0']:.3f}[x{k}]"); last = f'x{k}'
    run(['ffmpeg', '-v', 'error', '-y'] + inp + ['-filter_complex', ';'.join(fc), '-map', f'[{last}]', '-c:v', 'libx264', '-crf', '17', '-preset', 'fast', '-pix_fmt', 'yuv420p', vid])
    # subtítulos
    def tt(s): return f'{int(s // 3600)}:{int(s % 3600 // 60):02d}:{s % 60:05.2f}'
    ass = ('[Script Info]\nScriptType: v4.00+\nPlayResX: 1920\nPlayResY: 1080\n\n[V4+ Styles]\n'
           'Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding\n'
           'Style: Sub,Montserrat,54,&H00FFFFFF,&H00FFFFFF,&H00000000,&H80000000,-1,0,0,0,100,100,0,0,1,4,3,5,60,60,0,1\n'
           'Style: Tit,Montserrat,50,&H00FFFFFF,&H00FFFFFF,&H00000000,&H80000000,-1,0,0,0,100,100,6,0,1,4,2,5,60,60,0,1\n\n'
           '[Events]\nFormat: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n')
    subs.sort()
    for j, (a, b, x) in enumerate(subs):
        if j + 1 < len(subs): b = min(b, subs[j + 1][0])
        x = ' '.join(('{\\c&H3B3BFF&}' + w_ + '{\\c&HFFFFFF&}') if w_.lower().strip('¿¡,') in ROJO else w_ for w_ in x.split())
        ass += f'Dialogue: 0,{tt(a)},{tt(b)},Sub,,0,0,0,,{{\\pos(960,880)}}{x}\n'
    for p in plan:
        if p.get('titulo'): ass += f"Dialogue: 1,{tt(p['t0'] + 0.3)},{tt(p['t0'] + p['d'] - 0.2)},Tit,,0,0,0,,{{\\pos(960,300)\\fad(250,350)}}{p['titulo']}\n"
    sa = os.path.join(TMP, 'subs.ass'); open(sa, 'w').write(ass)
    run(['ffmpeg', '-v', 'error', '-y', '-i', vid, '-i', wav, '-vf', f'ass={sa}:fontsdir={FONTS}', '-map', '0:v', '-map', '1:a',
         '-c:v', 'libx264', '-crf', '18', '-preset', 'medium', '-c:a', 'aac', '-b:a', '192k', '-shortest', '-movflags', '+faststart', OUT])
    print('sincronía (error máx. por toma):', SYNC)
    print('listo:', OUT, round(TOT, 1), 's')

if __name__ == '__main__': main()
