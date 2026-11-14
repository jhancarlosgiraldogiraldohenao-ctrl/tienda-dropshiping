# -*- coding: utf-8 -*-
"""Capítulo 2 · PARTE 2 · EDICIÓN FINAL (14-nov-2026).
Imagen = el armado aprobado (armado_cap02p2.py, mismo orden E y mismos fundidos de 0,3 s).
Encima: voces de ElevenLabs pegadas a la boca (sin estirar), audio de Flow solo como ambiente (Lupe y la vaca se dejan de Flow,
decisión de Jay), música SIEMPRE sonando por escenas con una bajada suave bajo los diálogos, ambientes, efectos y subtítulos estilo Gnomo.
TMPED=<carpeta> python3 toffee/extravio/editor/ed_dizzy02p2.py -> toffee/videos-editados/EXTRAVIO-DIZZY-CAP02-P2.mp4
"""
import os, sys, json, subprocess as sp
import numpy as np
AQ = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, AQ)
import armado_cap02p2 as A          # noqa: E402  (orden, cortes y video del armado)
import ed_dizzy02p1h as P           # noqa: E402  (sincronizar(), palabras(), ROJO)
from pegar import load, SR          # noqa: E402
RAIZ = A.RAIZ
VZ2 = os.path.join(RAIZ, 'serie', 'voces-cap02', 'p2'); VZ1 = os.path.join(RAIZ, 'serie', 'voces-cap02', 'p1')
SN = os.path.join(RAIZ, 'sonidos'); FONTS = os.path.join(AQ, 'datos-dizzy01', 'fonts')
TMP = os.environ.get('TMPED', '/tmp/ed_dizzy02p2'); os.makedirs(TMP, exist_ok=True)
OUT = os.path.abspath(os.path.join(RAIZ, '..', 'videos-editados', 'EXTRAVIO-DIZZY-CAP02-P2.mp4'))
VIDEO = os.path.abspath(os.path.join(RAIZ, '..', 'videos-editados', 'EXTRAVIO-DIZZY-CAP02-P2-ARMADO.mp4'))
XF = A.XF
B1 = json.load(open(os.path.join(RAIZ, 'serie', 'cap02', 'cap02_bocas_p1h.json')))
B2 = json.load(open(os.path.join(RAIZ, 'serie', 'cap02', 'cap02_bocas_p2.json')))
P.BOC = {**B1, **B2}; P.TMP = TMP

# Voces por segmento (índice de A.E): ('sync', voz) = a la boca de Flow; ('at', voz, s) = arranca s segundos después del inicio del segmento.
def V(t, *items, a=None):
    for i, e in enumerate(A.E):
        if e['t'] == t and (a is None or e['a'] == a): return i, list(items)
    raise KeyError(t)
VOCES = dict([
    V('T35', ('sync', 'T35', 'p1')),
    V('U02', ('sync', 'U02')), V('U03', ('sync', 'U03')),
    V('U05b', ('at', 'U05b', 0.3)),
    V('L1', ('at', 'L1-tocino', 0.3), ('at', 'L1-dizzy', 3.3), ('at', 'L1-chuy', 6.6)),
    V('L2', ('at', 'L2-chuy', 0.2), ('at', 'L2-tocino', 4.6), ('at', 'L2-dizzy', 8.5)),
    V('L3', ('at', 'L3-chuy', 5.6), ('at', 'L3-dizzy', 8.0)),
    V('L4', ('at', 'L4-chuy', 0.6)),
    V('L5', ('at', 'L5-dizzy', 2.0), ('at', 'L5-tocino', 4.6), ('at', 'L5-chuy', 8.4)),
    V('U16', ('sync', 'U16')), V('U19', ('sync', 'U19')), V('U21', ('sync', 'U21')),
    V('L9', ('at', 'L9', 2.3)),
    V('H0', ('sync', 'H0')), V('H1', ('sync', 'H1')), V('H2', ('sync', 'H2')),
    V('U25', ('sync', 'U25')), V('U26-v2', ('sync', 'U26')), V('U26b', ('at', 'U26b', 0.6)),
    V('H5', ('sync', 'H5')), V('H6', ('sync', 'H6')),
    V('H3b', ('at', 'W2', 0.5), a=3.0),        # Dizzy habla desde la vaca y sigue a pantalla completa
])
FLOW_LLENO = {'U17', 'H3b'}                    # Lupe y el «Muuu» de la vaca: audio de Flow (Jay, 14-nov)
FIX = {'U16': ['Mi amor…', '(eres mi', 'tamalito…)'], 'L1-tocino': ['Bro…', '¿esto es un', 'Uber de agua?'],
       'L5-tocino': ['Bro, relax…', 'es amor a', 'primera vista.'], 'L2-tocino': ['¿Pa\' siempre?', 'Bro, yo amo México…', 'pero no tanto.']}
ROJO = P.ROJO | {'gringo!', 'gringo', 'mariachis.', 'sol?', 'sol.', 'almuerzo!', 'gonorreas!', 'nieto?', 'méxico?', 'apagó!', 'valió,', 'tamalito…)',
                 'almitas…', 'almitas,', 'colombia?', 'siempre.', 'chanclas!', 'güevón', 'huevón'}

# Música y ambiente por escena (índices de A.E, del primero al último de cada escena)
def idx(t, a=None): return V(t, a=a)[0]
ESC = [  # (desde, hasta, música, volumen, ambiente)
    (0, 0, 'M12b-mariachi-muertos-metales', 0.32, 'E27-ambiente-canal'),
    (1, idx('U05b'), 'M16-vals-catrina', 0.40, 'E25-ambiente-muertos-noche'),
    (idx('A-CANALES'), idx('L3'), 'M15-tema-chuy', 0.30, 'E27-ambiente-canal'),
    (idx('L4'), idx('L5'), 'M12-mariachi-muertos', 0.26, 'E27-ambiente-canal'),
    (idx('U15'), idx('U19'), 'M14-bolero-tocino', 0.30, 'E27-ambiente-canal'),
    (idx('U21'), idx('U20'), 'M15b-tema-chuy-suave', 0.28, 'E27-ambiente-canal'),
    (idx('L9'), idx('L9'), 'M13-persecucion-cumbia', 0.34, 'E25-ambiente-muertos-noche'),
    (idx('A-HUECO'), idx('H3'), 'M4-cancion-el-hueco', 0.28, 'E14-ambiente-olla'),
    (idx('H3b', 0.0), idx('U26b'), 'M10-misterio-camara', 0.28, 'E25-ambiente-muertos-noche'),
    (idx('H4'), len(A.E) - 1, 'M11-tema-extravio', 0.30, 'E14-ambiente-olla'),
]
FX = [  # (índice, segundo dentro del segmento, efecto, volumen)
    (0, 1.6, 'efectos/E30-violin-roto', 0.9), (idx('U18', 0.0) if False else 0, 0, None, 0),
    (idx('U21'), 0.2, 'efectos/E32-campanas-amanecer', 0.6),
    (idx('H3'), 1.3, 'efectos/E35-proyector', 0.8),
    (idx('U26b'), 0.2, 'efectos/E29-huesos-catrina', 0.7),
    (idx('U25'), 1.0, 'efectos/E33-viaje-magico', 0.35),
]
for i, e in enumerate(A.E):   # el violinazo de la serenata (segunda aparición de U18)
    if e['t'] == 'U18' and i > 0: FX.append((i, 1.6, 'efectos/E30-violin-roto', 0.9))

def recorta(x, db=-45):
    """Quita el silencio del principio y del final de la voz (para que el «at» caiga justo en la primera sílaba)."""
    fr = int(0.01 * SR); n = len(x) // fr
    e = 20 * np.log10(np.sqrt(np.mean(x[:n * fr].reshape(n, fr) ** 2, axis=1)) + 1e-9); on = np.where(e > db)[0]
    if not len(on): return x, 0.0
    a = max(0, on[0] * fr - int(0.02 * SR)); b = min(len(x), (on[-1] + 1) * fr + int(0.08 * SR))
    return x[a:b], a / SR

def main():
    plan = []; t0 = 0.0
    for i, e in enumerate(A.E):
        d = e['b'] - e['a']; plan.append(dict(e, i=i, t0=t0, d=d)); t0 += d - XF
    TOT = t0 + XF; N = int(TOT * SR) + SR * 4
    flow = np.zeros(N); voz = np.zeros(N); fx = np.zeros(N); subs = []; hab = np.zeros(N); SYNC = []

    def subtitulos(v, ws, mapa, base):
        if not ws: return
        if v in FIX:
            ch = FIX[v]; a0, a1 = mapa(ws[0][0]), mapa(ws[-1][1]); st = (a1 - a0) / len(ch)
            for j, c in enumerate(ch): subs.append((base + a0 + j * st, base + a0 + (j + 1) * st + 0.15, c))
            return
        grp, cur = [], []
        for w_ in ws:
            cur.append(w_)
            if len(cur) == 3 or len(' '.join(z[2] for z in cur)) > 13 or w_[2][-1:] in '.,?!…': grp.append(cur); cur = []
        if cur: grp.append(cur)
        for j, g in enumerate(grp):
            s0 = base + mapa(g[0][0]); s1 = base + (mapa(grp[j + 1][0][0]) if j + 1 < len(grp) else mapa(g[-1][1]) + 0.35)
            subs.append((s0, min(s1, s0 + 1.6), ' '.join(z[2] for z in g)))

    for p in plan:
        src = os.path.join(p.get('src', A.TK), p['t'] + '.mp4')
        x = load(src)[int(p['a'] * SR): int(p['b'] * SR)]
        items = VOCES.get(p['i'], [])
        env = np.ones(len(x)) * (1.0 if p['t'] in FLOW_LLENO else 0.6)
        if p.get('proy'): env *= 0.5
        base = p['t0']
        for it in items:
            if it[0] == 'sync':
                v = it[1]; P.VZ = VZ1 if len(it) > 2 else VZ2
                y, mapa, err = P.sincronizar(p['t'], p['a'], p['b'], v, 'es'); SYNC.append((v, round(err, 2)))
                Wd = [w for w in P.BOC[p['t']]['palabras'] if w[1] > p['a'] and w[0] < p['b']]
                if Wd:   # se tapa la voz de Flow mientras habla
                    env[max(0, int((Wd[0][0] - p['a'] - 0.25) * SR)): int((Wd[-1][1] - p['a'] + 0.2) * SR)] = 0.0
                k = int(base * SR); voz[k:k + len(y)] += y[:N - k]
                ws = P.palabras(v, 'es'); subtitulos(v, ws, mapa, base)
                nz = np.nonzero(np.abs(y) > 0.01)[0]
                if len(nz): hab[k + nz[0]: k + nz[-1]] = 1
            else:
                v, s = it[1], it[2]; P.VZ = VZ2
                raw = load(os.path.join(VZ2, v + '.mp3')); y, cut = recorta(raw)
                k = int((base + s) * SR); voz[k:k + len(y)] += y[:N - k]; hab[k:k + len(y)] = 1
                ws = P.palabras(v, 'es'); subtitulos(v, ws, (lambda tv, s=s, cut=cut: s + tv - cut), base)
        if p['t'] == 'U17':   # Lupe con la voz de Flow: subtítulos con las palabras medidas en la toma
            ws = [[w[0] - p['a'], w[1] - p['a'], w[2]] for w in P.BOC['U17']['palabras'] if w[0] >= p['a']]
            subs.append((base + ws[0][0], base + ws[1][1] + 0.1, '¿Tamalito?')); subs.append((base + ws[1][1] + 0.1, base + ws[-1][1] + 0.3, '¡Tamalito su abuela!'))
            hab[int((base + ws[0][0]) * SR): int((base + ws[-1][1]) * SR)] = 1
        f_ = int(XF * SR)
        if len(x) > 2 * f_: env[:f_] *= np.linspace(0, 1, f_); env[-f_:] *= np.linspace(1, 0, f_)
        env = np.convolve(env, np.ones(480) / 480, 'same')
        k = int(base * SR); flow[k:k + len(x)] += x * env[:len(x)]
    for i, at, f, g in FX:
        if not f: continue
        z = load(os.path.join(SN, f + '.mp3')) * g; k = int((plan[i]['t0'] + at) * SR); fx[k:k + len(z)] += z[:N - k]
    # música SIEMPRE sonando (fundido cruzado de 1 s entre escenas) y ambiente
    mus = np.zeros(N); amb = np.zeros(N)
    def bed(path, a, b, g, arr, fade):
        z = load(path); L = int((b - a) * SR); z = np.tile(z, L // len(z) + 1)[:L] * g
        f = min(int(fade * SR), L // 2); z[:f] *= np.linspace(0, 1, f); z[-f:] *= np.linspace(1, 0, f)
        k = int(a * SR); arr[k:k + L] += z[:N - k]
    for a_, b_, m, g, am in ESC:
        a = plan[a_]['t0'] - (0.5 if a_ else 0); b = plan[b_]['t0'] + plan[b_]['d'] + 0.5
        bed(os.path.join(SN, 'musica', m + '.mp3'), max(0, a), b, g, mus, 1.0)
        bed(os.path.join(SN, 'ambientes', am + '.mp3'), max(0, a), b, 0.20, amb, 0.8)
    w_ = int(1.0 * SR); duck = 1 - 0.30 * np.convolve(hab, np.ones(w_) / w_, 'same')   # baja suave bajo los diálogos
    mix = (flow + voz + fx + mus * duck + amb)[:int(TOT * SR)]
    raw = np.clip(mix, -1, 1).astype(np.float32).tobytes()
    r = sp.run(['ffmpeg', '-hide_banner', '-f', 'f32le', '-ar', str(SR), '-ac', '1', '-i', '-', '-af', 'loudnorm=I=-14:TP=-1.5:print_format=json', '-f', 'null', '-'], input=raw, capture_output=True)
    js = json.loads(r.stderr.decode()[r.stderr.decode().rfind('{'):])
    ln = (f"loudnorm=I=-14:TP=-1.5:linear=true:measured_I={js['input_i']}:measured_TP={js['input_tp']}:"
          f"measured_LRA={js['input_lra']}:measured_thresh={js['input_thresh']}:offset={js['target_offset']}")
    wav = os.path.join(TMP, 'mix.wav')
    sp.run(['ffmpeg', '-v', 'error', '-y', '-f', 'f32le', '-ar', str(SR), '-ac', '1', '-i', '-', '-af', ln, '-ar', '48000', '-ac', '2', wav], input=raw, check=True)
    # subtítulos estilo Gnomo (Montserrat negrita blanca, borde, palabras clave en rojo, centro del cuadro)
    def tt(s): return f'{int(s // 3600)}:{int(s % 3600 // 60):02d}:{s % 60:05.2f}'
    ass = ('[Script Info]\nScriptType: v4.00+\nPlayResX: 1920\nPlayResY: 1080\n\n[V4+ Styles]\n'
           'Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding\n'
           'Style: Sub,Montserrat,54,&H00FFFFFF,&H00FFFFFF,&H00000000,&H80000000,-1,0,0,0,100,100,0,0,1,4,3,5,60,60,0,1\n\n'
           '[Events]\nFormat: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n')
    subs.sort()
    for j, (a, b, x) in enumerate(subs):
        if j + 1 < len(subs): b = min(b, subs[j + 1][0])
        if b - a < 0.15: continue
        x = ' '.join(('{\\c&H3B3BFF&}' + w_ + '{\\c&HFFFFFF&}') if w_.lower().strip('¿¡') in ROJO else w_ for w_ in x.split())
        ass += f'Dialogue: 0,{tt(a)},{tt(b)},Sub,,0,0,0,,{{\\pos(960,880)}}{x}\n'
    sa = os.path.join(TMP, 'subs.ass'); open(sa, 'w').write(ass)
    sp.run(['ffmpeg', '-v', 'error', '-y', '-i', VIDEO, '-i', wav, '-vf', f'ass={sa}:fontsdir={FONTS}', '-map', '0:v', '-map', '1:a',
            '-c:v', 'libx264', '-crf', '18', '-preset', 'medium', '-c:a', 'aac', '-b:a', '192k', '-shortest', '-movflags', '+faststart', OUT], check=True)
    print('sincronía (error máx. por voz):', SYNC)
    print('listo:', OUT, round(TOT, 1), 's')

if __name__ == '__main__': main()
