# Pega una voz de ElevenLabs a la boca de una toma de Flow (palabra por palabra).
# Primero ajusta los silencios; si hace falta, acelera o frena la voz un poco (0,85–1,2, sin cambiar el tono).
# Uso desde Python: pegar(voz_wav, palabras_voz, palabras_flow, dur_clip) → señal del largo del clip
import re, unicodedata, subprocess as sp
import numpy as np
SR = 48000
def norm(w):
    w = unicodedata.normalize('NFD', w.lower()); w = ''.join(c for c in w if unicodedata.category(c) != 'Mn')
    return re.sub(r'[^a-z0-9]', '', w)
def load(f):
    return np.frombuffer(sp.run(['ffmpeg', '-v', 'error', '-i', f, '-ac', '1', '-ar', str(SR), '-f', 'f32le', '-'], capture_output=True).stdout, np.float32)
def stretch(x, dur):
    if len(x) < 400 or abs(len(x) / SR - dur) < 0.01: return x
    r = sp.run(['ffmpeg', '-v', 'error', '-f', 'f32le', '-ar', str(SR), '-ac', '1', '-i', '-', '-af',
                f'rubberband=tempo={(len(x) / SR) / dur:.4f}:pitchq=quality:formant=preserved:transients=smooth', '-f', 'f32le', '-'],
               input=x.astype(np.float32).tobytes(), capture_output=True, check=True)
    return np.frombuffer(r.stdout, np.float32)
def fit(x, dur, lo=0.85, hi=1.2):
    fr = int(0.01 * SR); n = len(x) // fr
    if n < 3: return stretch(x, dur)
    db = np.array([20 * np.log10(np.sqrt(np.mean(x[q * fr:(q + 1) * fr] ** 2)) + 1e-9) for q in range(n)])
    sil = db < -40; runs, q = [], 0
    while q < n:
        r = q
        while r < n and sil[r] == sil[q]: r += 1
        runs.append((bool(sil[q]) and 0 < q and r < n, q * fr, r * fr if r < n else len(x))); q = r
    S = sum(b - a for s_, a, b in runs if s_) / SR; P = len(x) / SR - S
    if S > 0 and dur - P >= 0.6 * S: al, be = (dur - P) / S, 1.0
    else: al = 0.6 if S > 0 else 1.0; be = min(hi, max(lo, (dur - al * S) / P))
    parts = []
    for s_, a, b in runs:
        seg = x[a:b]
        if s_:
            m = int(len(seg) * al); seg = seg[:m] if m <= len(seg) else np.concatenate([seg, np.zeros(m - len(seg), np.float32)])
        parts.append(seg)
    y = np.concatenate(parts)
    return stretch(y, len(y) / SR * be) if abs(be - 1) > 0.01 else y
def db_at(x, t, w=0.02):
    i = int(t * SR); s = x[max(0, i - int(w * SR / 2)): i + int(w * SR / 2)]
    return 20 * np.log10(np.sqrt(np.mean(s ** 2)) + 1e-9) if len(s) else -120
def pegar(x, ew, fw, dur, lo=0.85, hi=1.2):
    """x: voz; ew/fw: [inicio, fin, palabra] de la voz y de la boca (tiempo del clip). Devuelve (señal, errores)."""
    anc, j = [], 0
    for w in ew:
        a_ = norm(w[2])[:4]
        for jj in range(j, min(j + 4, len(fw))):
            b_ = norm(fw[jj][2])[:4]
            if a_ and b_ and (a_.startswith(b_[:3]) or b_.startswith(a_[:3])):
                if not anc or (w[0] - anc[-1][0] > 0.08 and fw[jj][0] - anc[-1][1] > 0.08): anc.append((max(w[0] - 0.02, 0), fw[jj][0] - 0.02))
                j = jj + 1; break
    cs, ce = 0.0, len(x) / SR
    pts = [cs] + [e for e, _ in anc] + [ce]
    st = anc[0][1] - anc[0][0]
    y, f, err = np.zeros(0, np.float32), int(0.01 * SR), []
    for n in range(len(pts) - 1):
        a_, b_ = pts[n], pts[n + 1]; cur = st + len(y) / SR
        if n >= 1: err.append(cur - anc[n - 1][1])
        L = max(0.05, anc[n][1] - cur) if 1 <= n < len(anc) else b_ - a_
        z = fit(x[int(a_ * SR): int(b_ * SR)], L + (0.01 if len(y) else 0), lo, hi)
        if len(y) and len(z) / SR < L - 0.05 and db_at(x, a_ - 0.01) < -40:
            pad = int((L - len(z) / SR) * SR); fo = int(0.008 * SR)
            y = y.copy(); y[-fo:] *= np.linspace(1, 0, fo); y = np.concatenate([y, np.zeros(pad, np.float32)])
        if len(y) >= f and len(z) >= f:
            z = z.copy(); z[:f] = z[:f] * np.linspace(0, 1, f) + y[-f:] * np.linspace(1, 0, f); y = y[:-f]
        y = np.concatenate([y, z])
    out = np.zeros(int(dur * SR), np.float32); s0 = int(st * SR)
    if s0 < 0: y = y[-s0:]; s0 = 0
    y = y[: len(out) - s0]; out[s0: s0 + len(y)] = y
    return out, err

def por_frases(x, ew, fw, sil_db=-42, sil_min=0.15):
    """Coloca la voz SIN tocarla por dentro: se parte solo en silencios reales (≥ sil_min s) y cada frase entera
    se mueve para que su primera palabra caiga donde la boca la dice. Nada se estira, nada se corta en medio.
    Devuelve [(segundo de inicio relativo al clip, pedazo)], y los desfases de todas las palabras emparejadas."""
    fr = int(0.01 * SR); n = len(x) // fr
    db = np.array([20 * np.log10(np.sqrt(np.mean(x[q * fr:(q + 1) * fr] ** 2)) + 1e-9) for q in range(n)])
    cuts, q = [0], 0
    while q < n:
        if db[q] < sil_db:
            r = q
            while r < n and db[r] < sil_db: r += 1
            if (r - q) * 0.01 >= sil_min and q > 0 and r < n: cuts.append((q + r) // 2 * fr)
            q = r
        else: q += 1
    cuts.append(len(x))
    # pareja de palabras voz → boca (en orden)
    match, j = {}, 0
    for k, w in enumerate(ew):
        a_ = norm(w[2])[:4]
        for jj in range(j, min(j + 4, len(fw))):
            b_ = norm(fw[jj][2])[:4]
            if a_ and b_ and (a_.startswith(b_[:3]) or b_.startswith(a_[:3])):
                match[k] = fw[jj][0]; j = jj + 1; break
    out, err, prev_end = [], [], -9.0
    for c0, c1 in zip(cuts[:-1], cuts[1:]):
        t0, t1 = c0 / SR, c1 / SR
        ks = [k for k, w in enumerate(ew) if t0 <= (w[0] + w[1]) / 2 < t1]
        anc = next((k for k in ks if k in match), None)
        if anc is not None: st = match[anc] - (ew[anc][0] - t0)
        elif out: st = out[-1][0] + (t0 - out[-1][2])
        else: st = (fw[0][0] if fw else 0) - ((ew[ks[0]][0] if ks else 0) - t0)
        st = max(st, prev_end + 0.03)
        out.append((st, x[c0:c1], t0)); prev_end = st + (t1 - t0)
        err += [st + ew[k][0] - t0 - match[k] for k in ks if k in match]
    return [(s, c) for s, c, _ in out], err

def pegar_suave(x, ew, fw, dur, lo=0.85, hi=1.2, tmp='/tmp/_pegar'):
    """Igual que pegar(), pero en UNA sola pasada de rubberband con mapa de tiempos: la voz se acelera o frena de forma
    continua (sin costuras ni pausas metidas), con cada tramo entre 0,85 y 1,2. Devuelve (señal del largo del clip, desfases)."""
    import os
    os.makedirs(tmp, exist_ok=True)
    anc, j = [], 0
    for w in ew:
        a_ = norm(w[2])[:4]
        for jj in range(j, min(j + 4, len(fw))):
            b_ = norm(fw[jj][2])[:4]
            if a_ and b_ and (a_.startswith(b_[:3]) or b_.startswith(a_[:3])):
                if not anc or (w[0] - anc[-1][0] > 0.08 and fw[jj][0] - anc[-1][1] > 0.08): anc.append((max(w[0] - 0.02, 0.0), fw[jj][0] - 0.02))
                j = jj + 1; break
    L = len(x) / SR
    if not anc: raise IndexError
    # tiempos destino con tramos limitados
    src = [0.0] + [a for a, _ in anc] + [L]
    st = anc[0][1] - anc[0][0]
    dst = [st, anc[0][1]]
    for k in range(1, len(anc)):
        d_src = anc[k][0] - anc[k - 1][0]; want = anc[k][1] - dst[-1]
        dst.append(dst[-1] + min(hi * d_src, max(lo * d_src, want)))
    dst.append(dst[-1] + (L - anc[-1][0]))
    err = [dst[k + 1] - anc[k][1] for k in range(len(anc))]
    total = dst[-1] - dst[0]
    with open(f'{tmp}/map.txt', 'w') as fh:
        for a, b in zip(src[1:-1], dst[1:-1]): fh.write(f'{int(a * SR)} {int((b - dst[0]) * SR)}\n')
    sp.run(['ffmpeg', '-v', 'error', '-y', '-f', 'f32le', '-ar', str(SR), '-ac', '1', '-i', '-', f'{tmp}/in.wav'], input=x.astype(np.float32).tobytes(), check=True)
    sp.run(['rubberband', '-q', '-F', '-D', f'{total:.4f}', '-M', f'{tmp}/map.txt', f'{tmp}/in.wav', f'{tmp}/out.wav'], check=True, capture_output=True)
    y = load(f'{tmp}/out.wav')
    out = np.zeros(int(dur * SR), np.float32); s0 = int(st * SR)
    if s0 < 0: y = y[-s0:]; s0 = 0
    y = y[: max(0, len(out) - s0)]; out[s0: s0 + len(y)] = y
    return out, err
