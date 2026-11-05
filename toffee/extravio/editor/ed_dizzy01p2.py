# -*- coding: utf-8 -*-
"""Editor del capítulo 1 de Dizzy (vertical 9:16), PARTE 2 del video (copia de ed_dizzy01.py con la lista de la parte 2).
Sigue ESTUDIO-EDICION-GNOMO.md: cortes secos, el sonido nunca se corta, voces en L sobre la toma siguiente,
subtítulos Montserrat blancos en el centro con palabras clave en rojo, música por escena que baja bajo las voces,
golpes de sonido en los chistes. Quita la voz de Flow y pone la de ElevenLabs pegada a la boca.
python3 toffee/extravio/editor/ed_dizzy01.py  ->  toffee/videos-editados/EXTRAVIO-DIZZY-CAP01-P1.mp4
"""
import os, re, sys, json, subprocess as sp
import numpy as np
AQ = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQ)
import pegar as PG  # noqa: E402
from pegar import load, fit, pegar_suave, SR  # noqa: E402
RAIZ = os.path.abspath(os.path.join(AQ, '..'))
TK = os.path.join(RAIZ, 'serie', 'tomas-cap01')
VZ = os.path.join(RAIZ, 'serie', 'voces-cap01', 'p2')
SN = os.path.join(RAIZ, 'sonidos')
DAT = os.path.join(AQ, 'datos-dizzy01')
TMP = os.environ.get('TMPED', '/tmp/ed_dizzy01')
FONTS = os.environ.get('FONTS', os.path.join(DAT, 'fonts'))
OUT = os.path.abspath(os.path.join(RAIZ, '..', 'videos-editados', 'EXTRAVIO-DIZZY-CAP01-P2.mp4'))
W, H, FPS = 1080, 1920, 30
os.makedirs(TMP, exist_ok=True)

VOZ = json.load(open(os.path.join(VZ, 'ELEGIDAS.json')))
FLOW = json.load(open(os.path.join(DAT, 'ritmo-flow.json')))          # palabras de Flow por toma: [ini, fin, palabra]
sys.path.insert(0, os.path.join(RAIZ, 'serie'))
from cap01_voces_p2 import V as VTXT  # noqa: E402
TXT = {c: re.sub(r'\[[^\]]*\]', '', t).replace('  ', ' ').strip() for c, _, _, _, t, _ in VTXT}
# subtítulos con traducción (las frases en inglés de Tocino)
SUBT = {
 'V40': '¡Cállate, man, es arte!',
 'V56': '¡No joda!… Amo a esta mujer.',
 'V62': '…Ay, no.',
 'V52': 'Así se siente, rata.',
}
SUB_Y = 1400  # subtítulos un poco más abajo que al principio (y=1200), lejos de las bocas (Jay, 5-nov-2026; arriba no le gustó)
ROJO = {'dominó', 'crimen', 'arte', 'gordito', 'diciembre', 'alcantarilla', 'comentarios', 'sapa', 'pirobo', 'muchacho', 'cafecito', 'café', 'cucha', 'cámara', 'malparidos', 'hijueputa', 'bartolo', 'perro', 'estúpido', 'tocino', 'perico', 'hueco', 'lucas',
        'cuca', 'tuerto', 'gonorrea', 'abuelita', 'mijito', 'arepaaa', 'tapas', 'talento', 'trampa', 'gringo', 'vlog', 'vlogger', 'cochino'}

# ---------------- lista de tomas (parte 1) ----------------
# t: toma · a: entrada (s) · d: duración (None = lo que pida la voz) · v: voz · vo: voz en off (segundos desde el inicio)
# sc: escena · fx: [(efecto, segundo, ganancia)] · fin: efecto al terminar la voz · tinte · zoom · titulo
E = [
 # 10. El Tuerto (arranca con la respuesta)
 dict(t='G54', a=0.9, v='V35', sc='tuerto', d=None, al=1),
 dict(t='G55', a=0.8, v='V36', sc='tuerto', d=None, al=1),
 dict(t='G56', a=0.5, d=3.0, sc='tuerto'),
 dict(t='G57', a=0.9, v='V37', sc='tuerto', d=None, al=1),
 # 11. El solo de guitarra
 dict(t='G58', a=0.5, v='V38', sc='tuerto', d=None, al=1, cortar_musica=99),
 dict(t='G59', a=0.5, d=3.4, sc='solo', fx=[('E19-solo-guitarra-espantoso', 0.0, 0.9)]),
 dict(t='G60', a=0.5, d=2.0, sc='solo'),
 dict(t='G61', a=0.3, d=1.8, sc='solo'),
 dict(t='G62', a=0.8, v='V39', sc='solo', d=None, al=1),
 dict(t='G63', a=0.8, v='V40', sc='solo', d=None, al=1),
 # 12. Cuca intenta
 dict(t='G64', a=0.5, d=3.2, sc='cuca'),
 dict(t='G65', a=0.8, v='V41', sc='cuca', d=None, al=1),
 dict(t='G66', a=1.2, v='V42', sc='sinmusica', d=None, al=1),
 dict(t='G67', a=1.4, v='V43', sc='sinmusica', d=None, al=1),
 dict(t='G68', a=0.8, v='V44', sc='sinmusica', d=None, al=1),
 dict(t='G69', a=0.4, v='V45', sc='sinmusica', d=None, al=1),
 # 13. La apuesta
 dict(t='G70', a=1.0, v='V46', sc='domino', d=None, al=1),
 dict(t='G71', a=0.6, v='V47', sc='domino', d=None, al=1),
 dict(t='G72', a=1.8, v='V48', sc='domino', d=None, al=1),
 dict(t='G73', a=0.5, d=3.2, sc='domino'),
 dict(t='G74', a=0.3, d=2.4, sc='domino'),
 dict(t='G75', a=0.3, d=2.8, sc='domino'),
 dict(t='G76', a=0.9, v='V49', sc='domino', d=None, al=1),
 dict(t='G77', a=0.8, v='V50', sc='domino', d=None, al=1),
 dict(t='G78', a=0.3, d=2.8, sc='domino'),
 dict(t='G79', a=0.0, v='V51', sc='domino', d=None, al=1, voltear=1),   # se voltea: queda colgado de cabeza
 dict(t='G80', a=0.9, v='V52', sc='domino', d=None, al=1),
 # 14. La abuela
 dict(t='G37', a=0.0, d=2.6, v='V53', vo=0.35, sc='silencio', dmin=2.4),   # todos se congelan: «¡MIJITOOO!» de lejos
 dict(t='G82', a=0.0, d=3.4, sc='abuela'),
 dict(t='G83', a=0.8, v='V54', sc='abuela', d=None, al=1),
 dict(t='G84', a=0.3, d=2.4, sc='abuela'),
 dict(t='G85', a=0.5, d=2.0, sc='abuela'),
 dict(t='G86', a=0.8, d=2.0, sc='abuela', fx=[('E20-chanclazo', 1.15, 1.0)]),
 dict(t='G87', a=1.3, v='V55', sc='abuela', d=None, al=1),
 dict(t='G88', a=1.6, v='V56', sc='abuela', d=None, al=1),
 dict(t='G89', a=0.0, d=3.2, sc='abuela'),
 # 15. El camino de vuelta
 dict(t='G12', a=0.0, d=2.4, sc='regreso', tarde=1),
 dict(t='G91', a=1.2, v='V57', sc='regreso', d=None, al=1),
 dict(t='G92', a=0.6, d=2.2, sc='regreso', fx=[('E20-chanclazo', 1.3, 0.9)]),
 dict(t='G93', a=0.6, v='V58', sc='regreso', d=None, al=1),
 dict(t='G94', a=1.0, v='V59', sc='regreso', d=None, al=1),
 # 16. La comida
 dict(t='G95', a=1.5, v='V60', sc='regreso', d=None, al=1),
 dict(t='G96', a=1.0, v='V61', sc='regreso', d=None, al=1),
 dict(t='G97', a=1.2, v='V62', sc='regreso', d=None, al=1),
 # 17. El misterio
 dict(t='G98', a=1.0, d=4.6, sc='misterio', fx=[('E24-camara-se-prende', 3.0, 1.0)]),
 dict(t='G99', a=1.4, v='V63', sc='misterio', d=None, al=1, tinte_verde=1),
 dict(t='G100', a=1.0, v='V64', sc='misterio', d=None, al=1),
 # 18. Cierre
 dict(t='G101', archivo='G101-v2', a=0.3, v='V65', sc='cierre', d=None, al=1),
 dict(t='G102', a=1.0, v='V66', sc='cierre', d=None, al=1),
]
MUSICA = {'tuerto': ('M5-tuerto-reggaeton', .32), 'cuca': ('M6-cuca-saxofon', .40), 'domino': ('M7-domino-tension', .40),
          'abuela': ('M8-abuela-western', .45), 'regreso': ('M9-regreso-bambuco-tierno', .36), 'misterio': ('M10-misterio-camara', .45),
          'cierre': ('M11-tema-extravio', .40)}
AMB = {'tuerto': ('E14-ambiente-olla', .40), 'solo': ('E14-ambiente-olla', .30), 'cuca': ('E14-ambiente-olla', .35), 'sinmusica': ('E14-ambiente-olla', .40),
       'domino': ('E14-ambiente-olla', .40), 'silencio': ('E14-ambiente-olla', .10), 'abuela': ('E14-ambiente-olla', .30), 'regreso': ('E02-ambiente-finca', .18)}
CANCION = []

def ffdur(f):
    return float(sp.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', f], capture_output=True, text=True).stdout)
def sonido(n):
    for d in ('efectos', 'ambientes', 'musica'):
        f = os.path.join(SN, d, n + '.mp3')
        if os.path.exists(f): return load(f)
    raise FileNotFoundError(n)
def trim_sil(x, db=-45):
    fr = int(0.01 * SR); n = len(x) // fr
    if n == 0: return x
    e = 20 * np.log10(np.sqrt(np.mean(x[:n * fr].reshape(n, fr) ** 2, axis=1)) + 1e-9)
    on = np.where(e > db)[0]
    if len(on) == 0: return x
    return x[max(0, on[0] - 2) * fr: min(n, on[-1] + 4) * fr]

# palabras de las voces (Whisper), cacheadas
VW_F = os.path.join(DAT, 'ritmo-voces.json')
VW = json.load(open(VW_F)) if os.path.exists(VW_F) else {}
# ajustes hechos a mano en Claude Studio: {voz: {mueve: s, gain: x, mute: bool}}
AJ_F = os.path.join(DAT, 'ajustes.json')
AJ = json.load(open(AJ_F)) if os.path.exists(AJ_F) else {}
EXPORTAR = os.environ.get('EXPORTAR') == '1'
def voz(c):
    """Devuelve la señal de la voz (sin silencios a los lados). V30a / V30b = las dos mitades del gallinazo."""
    base = c[:3]
    x = trim_sil(load(os.path.join(VZ, VOZ[base])))
    if c in ('V30a', 'V30b'):
        fr = int(0.01 * SR); n = len(x) // fr
        e = 20 * np.log10(np.sqrt(np.mean(x[:n * fr].reshape(n, fr) ** 2, axis=1)) + 1e-9)
        best, run, st = (0, 0), 0, 0
        for q in range(n):
            if e[q] < -42:
                if run == 0: st = q
                run += 1
                if run > best[1]: best = (st, run)
            else: run = 0
        cut = (best[0] + best[1] // 2) * fr
        x = trim_sil(x[:cut]) if c == 'V30a' else trim_sil(x[cut:])
    return x

def flow_span(t, a, b):
    ws = [w for w in FLOW.get(t, []) if a - 0.05 <= w[0] < b]
    if not ws: return None
    return ws[0][0], max(w[1] for w in ws)

def db_frames(x, fr):
    n = len(x) // fr
    return 20 * np.log10(np.sqrt(np.mean(x[:n * fr].reshape(n, fr) ** 2, axis=1)) + 1e-9) if n else np.zeros(0)
def frases_voz(x, sil=-40, gap=0.15):
    """Frases de la voz de ElevenLabs: se parte solo en silencios reales (≥ gap s)."""
    fr = int(0.01 * SR); e = db_frames(x, fr); on = e > sil; out = []; i = 0; n = len(e); g = int(gap / 0.01)
    while i < n:
        if on[i]:
            j = i
            while j < n and (on[j] or on[j:j + g].any()): j += 1
            if j - i >= 4: out.append([i * 0.01, j * 0.01])
            i = j
        else: i += 1
    return out
_FL = {}
def boca_flow(t, a, b):
    """Tramos donde suena la voz de Flow (= donde se mueve la boca), por el volumen real del audio."""
    k = (t, round(a, 3), round(b, 3))
    if k in _FL: return _FL[k]
    x = load(os.path.join(TK, t + '.mp4'))[int(a * SR): int(b * SR)]
    fr = int(0.01 * SR); e = db_frames(x, fr)
    if not len(e): return []
    piso = float(np.percentile(e, 20)); thr = min(-20.0, max(-28.0, piso + 10))
    on = e > thr; out = []; i = 0; n = len(e)
    while i < n:
        if on[i]:
            j = i
            while j < n and (on[j] or on[j:j + 10].any()): j += 1
            if j - i >= 5: out.append([i * 0.01, j * 0.01])
            i = j
        else: i += 1
    _FL[k] = out; return out
def juntar(lst, n):
    """Une los tramos más pegados hasta que queden n."""
    lst = [list(z) for z in lst]
    while len(lst) > n:
        g = [lst[i + 1][0] - lst[i][1] for i in range(len(lst) - 1)]; i = int(np.argmin(g))
        lst[i][1] = lst[i + 1][1]; del lst[i + 1]
    return lst
def emparejar(P, S):
    """Empareja frases de la voz con tramos de boca (programación dinámica): cada grupo de 1–3 frases va con un grupo
    de 1–4 tramos seguidos; cuesta la diferencia de duración. Se pueden saltar tramos de boca al principio o al final."""
    import functools
    nP, nS = len(P), len(S)
    @functools.lru_cache(None)
    def f(i, j):
        if i == nP: return (0.25 * (nS - j), [])          # tramos de boca sobrantes al final: barato
        if j == nS: return (1e9, [])
        best = (1.6 + (S[j][1] - S[j][0]) + f(i, j + 1)[0], f(i, j + 1)[1]) if i == 0 else (1e9, [])   # saltar un tramo al inicio: caro (la voz debe arrancar con la boca)
        for k in range(1, min(3, nP - i) + 1):
            dv = P[i + k - 1][1] - P[i][0]
            for m in range(1, min(4, nS - j) + 1):
                df = S[j + m - 1][1] - S[j][0]
                c = abs(dv - df) + 0.15 * (k + m - 2)
                r = f(i + k, j + m)
                if c + r[0] < best[0]: best = (c + r[0], [(P[i][0], S[j][0])] + r[1])
        return best
    return f(0, 0)[1]
def alinear(x, t, a, lim, desde=0.0, fijos=None):
    """Pega cada frase de la voz al arranque del tramo de boca de Flow que le toca. Devuelve (señal desde el clip 0, mapa voz→clip, errores)."""
    P = frases_voz(x); S = [q for q in boca_flow(t, a, a + lim) if q[0] >= desde]
    if not P or not S: raise IndexError('sin tramos')
    pares = emparejar(tuple(map(tuple, P)), tuple(map(tuple, S)))
    if fijos:   # arranques de boca puestos a mano (segundos del clip), uno por frase de la voz; None = como salga
        pares = [(P[i][0], q) for i, q in enumerate(fijos) if q is not None and i < len(P)]
    if not pares: raise IndexError('sin pares')
    toks = ['k' + chr(97 + i) * 3 for i in range(len(pares))]
    ew = [[pv, pv + 0.1, k] for (pv, _), k in zip(pares, toks)]; fw = [[pf, pf + 0.1, k] for (_, pf), k in zip(pares, toks)]
    y, err = pegar_suave(x, ew, fw, lim + 2.5, lo=0.8, hi=1.25, tmp=os.path.join(TMP, 'pg'))
    src, dst = PG.ULTIMO
    return y, (lambda tv: float(np.interp(tv, src, dst))), err

SYNC = []
def main():
    total = 0.0; plan = []
    for k, e in enumerate(E):
        f = os.path.join(TK, e.get('archivo', e['t']) + '.mp4')
        if not os.path.exists(f): print('  falta la toma', e['t'], '(se salta)'); continue
        if e.get('si_falta') and os.path.exists(os.path.join(TK, e['si_falta'] + '.mp4')): continue
        L = ffdur(f)
        y = None; vstart = None; mapa = None; corte = 0.0
        if e.get('v') and e['v'][:3] not in VOZ: print('  falta la voz', e['v'], '(se salta)'); e = {k_: v_ for k_, v_ in e.items() if k_ != 'v'}
        if e.get('v'):
            x = voz(e['v'])
            if e.get('quitar'):   # quita las primeras frases de la voz (p. ej. «¡Mía!», «¡Mijito!»)
                P = frases_voz(x); corte = max(0.0, P[e['quitar']][0] - 0.06); x = x[int(corte * SR):]
            if e.get('solo'):     # deja solo las primeras frases
                P = frases_voz(x); x = x[: int(min(len(x) / SR, P[e['solo'] - 1][1] + 0.08) * SR)]
            fw = [[w[0] - e['a'], w[1] - e['a'], w[2]] for w in FLOW.get(e['t'], []) if w[0] >= e['a'] - 0.05]
            if 'vo' in e:
                y = x; vstart = e['vo']; mapa = lambda tv: tv
            elif e.get('al'):
                lim = (e['d'] if e['d'] else L - e['a'])
                try:
                    y, mp_, err = alinear(x, e.get('archivo', e['t']), e['a'], lim, e.get('desde_boca', 0.0), e.get('fijos'))
                    y = np.concatenate([np.zeros(int(0.03 * SR), np.float32), y])   # la voz un pelo después de la boca, nunca antes
                    nz = np.where(np.abs(y) > 1e-4)[0]; y = y[: nz[-1] + 1] if len(nz) else y
                    vstart = 0.0; mapa = (lambda m: (lambda tv: m(tv) + 0.03))(mp_)
                    if err: SYNC.append((e['t'], round(float(np.mean(np.abs(err))), 3), round(float(np.max(np.abs(err))), 3)))
                except Exception as ex:
                    print('  sin tramos de boca en', e['t'], ex); y = x; vstart = 0.3; mapa = lambda tv: tv
            elif not fw:
                y = x; vstart = 0.3; mapa = lambda tv: tv
            else:
                ew = [[w[0] - corte, w[1] - corte, w[2]] for w in VW.get(e['v'], []) if w[0] >= corte - 0.02]
                try:
                    lim = (e['d'] if e['d'] else L - e['a']) + 2.5
                    y, err = pegar_suave(x, ew, fw, lim, lo=0.8, hi=1.25, tmp=os.path.join(TMP, 'pg'))
                    y = np.concatenate([np.zeros(int(0.08 * SR), np.float32), y])   # la voz nunca antes que la boca
                    nz = np.where(np.abs(y) > 1e-4)[0]
                    y = y[: nz[-1] + 1] if len(nz) else y
                    vstart = 0.0; mapa = (lambda m: (lambda tv: m(tv) + 0.08))(lambda tv, s_=PG.ULTIMO: float(np.interp(tv, s_[0], s_[1])))
                    if err: SYNC.append((e['t'], round(float(np.mean(np.abs(err))), 3), round(float(np.max(np.abs(err))), 3)))
                except Exception as ex:
                    print('  sin anclas en', e['t'], ex)
                    y = x; vstart = fw[0][0] + 0.08; mapa = lambda tv: tv
        d = e['d']
        if e.get('dfija'): d = e['dfija']
        if d is None:
            need = (vstart or 0) + (len(y) / SR if y is not None else 0) + e.get('cola', 0.22)
            d = min(max(need, e.get('dmin', 1.4)), L - e['a'])
        d = min(d, L - e['a'])
        plan.append(dict(e, f=f, d=round(d, 3), t0=total, y=y, vs=vstart, mapa=mapa, corte=corte))
        total += d
    print('largo parte 1: %.1f s' % total)
    for t_, m_, x_ in SYNC: print('  sincronía', t_, 'promedio', m_, 's · máximo', x_, 's')
    N = int(total * SR) + SR
    voces = np.zeros(N, np.float32); toma = np.zeros(N, np.float32); musica = np.zeros(N, np.float32)
    amb = np.zeros(N, np.float32); fx = np.zeros(N, np.float32)
    subs = []
    def put(buf, sig, t, g=1.0):
        i = int(t * SR); j = min(N, i + len(sig))
        if j > i: buf[i:j] += sig[: j - i] * g
    prev_end = -1
    for p in plan:
        # sonido propio de la toma, sin la voz de Flow
        s = load(p['f'])[int(p['a'] * SR): int((p['a'] + p['d']) * SR)].copy()
        g = np.ones(len(s), np.float32)
        tapar = [(w[0] - p['a'] - 0.06, w[1] - p['a'] + 0.10) for w in FLOW.get(p['t'], [])]
        if p.get('v'): tapar += [(q[0] - 0.12, q[1] + 0.15) for q in boca_flow(p.get('archivo', p['t']), p['a'], p['a'] + p['d'])]
        if p.get('mudo_desde') is not None: tapar.append((p['mudo_desde'], p['d']))
        for w0, w1 in tapar:
            i0 = max(0, int(w0 * SR)); i1 = min(len(g), int(w1 * SR))
            if i1 > i0: g[i0:i1] = 0
        k = int(0.06 * SR); g = np.convolve(g, np.ones(k) / k, mode='same').astype(np.float32)
        lev = .12 if p['sc'] == 'cancion' else .7
        put(toma, s * g * lev, p['t0'])
        if p['y'] is not None:
            aj = AJ.get(p['v'], {})
            p['t_base'] = p['t0'] + p['vs']
            t = p['t_base'] + float(aj.get('mueve', 0))
            if aj.get('mute'): continue
            if aj.get('gain') is not None: p['y'] = p['y'] * float(aj['gain'])
            if t < prev_end + 0.05: print('  ojo: voz encima en', p['t'], round(prev_end - t, 2))
            put(voces, p['y'], t); prev_end = t + len(p['y']) / SR
            ew = [w for w in VW.get(p['v'][:3] if p['v'] not in ('V30a', 'V30b') else p['v'], []) if w[0] >= p['corte'] - 0.02]
            pal = [t - p['vs'] + p['mapa'](w[0] - p['corte']) + p['vs'] for w in ew] if p['mapa'] and ew else None
            subs.append((t, t + len(p['y']) / SR, p['v'], pal))
        for n_, ts, gg in p.get('fx', []): put(fx, sonido(n_), p['t0'] + ts, gg)
    # escenas → música y ambiente
    escenas = []
    for p in plan:
        if escenas and escenas[-1][0] == p['sc']: escenas[-1][2] = p['t0'] + p['d']
        else: escenas.append([p['sc'], p['t0'], p['t0'] + p['d']])
    cortes = [(p['t0'] + p['cortar_musica']) for p in plan if p.get('cortar_musica')]
    vueltas = [(p['t0'] + p['volver_musica']) for p in plan if p.get('volver_musica')]
    for sc, a, b in escenas:
        for tabla, buf in ((MUSICA, musica), (AMB, amb)):
            if sc not in tabla: continue
            n_, gg = tabla[sc]; m = sonido(n_); Ls = int((b - a) * SR)
            if sc == 'cancion' and tabla is MUSICA:
                Ls = min(len(m), Ls + int(1.2 * SR)); seg = m[:Ls].copy()
            else:
                reps = int(np.ceil(Ls / len(m))) + 1; seg = np.tile(m, reps)[:Ls].copy()
            fi = int(0.4 * SR); fo = int(0.6 * SR)
            seg[:fi] *= np.linspace(0, 1, fi); seg[-fo:] *= np.linspace(1, 0, fo)
            if tabla is MUSICA and sc == 'camino':
                for c in cortes:
                    for v_ in vueltas:
                        i0, i1 = int((c - a) * SR), int((v_ - a) * SR)
                        if 0 < i0 < i1 <= len(seg): seg[i0:i1] = 0; seg[i1:i1 + fi] *= np.linspace(0, 1, min(fi, len(seg) - i1))
            put(buf, seg, a, gg)
    # la voz manda: música y ambiente bajan cuando alguien habla
    env = np.sqrt(np.convolve(voces ** 2, np.ones(int(.05 * SR)) / int(.05 * SR), mode='same'))
    duck = 1 - 0.78 * np.clip(env / 0.02, 0, 1)
    duck = np.convolve(duck, np.ones(int(.25 * SR)) / int(.25 * SR), mode='same').astype(np.float32)
    mix = voces * 1.0 + toma * (0.55 + 0.45 * duck) + musica * duck + amb * (0.4 + 0.6 * duck) + fx
    mix = mix[: int(total * SR)]
    pk = max(1e-6, np.max(np.abs(mix))) / 0.9
    mix /= pk
    if EXPORTAR: exportar(plan, (toma * (0.55 + 0.45 * duck) + musica * duck + amb * (0.4 + 0.6 * duck) + fx)[: int(total * SR)] / pk, pk, total)
    wav = os.path.join(TMP, 'mix.wav')
    sp.run(['ffmpeg', '-v', 'error', '-y', '-f', 'f32le', '-ar', str(SR), '-ac', '1', '-i', '-', wav], input=mix.astype(np.float32).tobytes(), check=True)
    # subtítulos (ASS)
    escribir_ass(subs, plan, os.path.join(TMP, 'subs.ass'))
    # video
    lst = []
    for i, p in enumerate(plan):
        vf = [f'scale={W}:{H}:flags=lanczos', 'setsar=1', f'fps={FPS}']
        if p.get('zoom'): z = p['zoom']; vf.insert(0, f'crop=iw/{z}:ih/{z}')
        if p.get('recorte3'): vf.insert(0, 'crop=iw*0.9:ih*0.9:iw*0.1:ih*0.05')   # G29b: fuera lo que se asoma en el borde izquierdo
        if p.get('recorte2'): vf.insert(0, 'crop=iw*0.86:ih*0.86:0:ih*0.05')   # G40: fuera la figura borrosa de la esquina derecha
        if p.get('recorte'): vf.insert(0, 'crop=iw*0.82:ih*0.82:iw*0.02:ih*0.09')   # quita el brazo humano del borde derecho (G36)
        if p.get('voltear'): vf.append('hflip,vflip')
        if p.get('tarde'): vf.append("colortemperature=temperature=2600:mix=1,curves=r='0/0 0.5/0.6 1/1':b='0/0 0.5/0.38 1/0.85',eq=brightness=-0.05:saturation=1.15")
        if p.get('tinte_verde'): vf.append('colorbalance=gs=.10:gm=.08,eq=saturation=0.9')
        if p.get('tinte'): vf.append('eq=saturation=0.85:gamma=0.97,colorbalance=rs=.07:gs=.03:bs=-.07')
        o = os.path.join(TMP, f'seg{i:03d}.mp4')
        sp.run(['ffmpeg', '-v', 'error', '-y', '-ss', f"{p['a']:.3f}", '-i', p['f'], '-t', f"{p['d']:.3f}", '-an', '-vf', ','.join(vf),
                '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p', o], check=True)
        lst.append(f"file '{o}'")
    open(os.path.join(TMP, 'lista.txt'), 'w').write('\n'.join(lst))
    vid = os.path.join(TMP, 'video.mp4')
    sp.run(['ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', os.path.join(TMP, 'lista.txt'), '-c', 'copy', vid], check=True)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    sp.run(['ffmpeg', '-v', 'error', '-y', '-i', vid, '-i', wav, '-vf', f"ass={os.path.join(TMP, 'subs.ass')}:fontsdir={FONTS}",
            '-af', 'loudnorm=I=-14:TP=-1.5:LRA=11', '-c:v', 'libx264', '-preset', 'medium', '-crf', '22', '-maxrate', '4M', '-bufsize', '8M', '-pix_fmt', 'yuv420p',
            '-c:a', 'aac', '-b:a', '160k', '-ar', '48000', '-shortest', '-movflags', '+faststart', OUT], check=True)
    json.dump([{k: v for k, v in p.items() if k not in ('y',)} for p in plan], open(os.path.join(TMP, 'plan.json'), 'w'), indent=1, default=str)
    if EXPORTAR:
        sp.run(['ffmpeg', '-v', 'error', '-y', '-i', vid, '-vf', 'scale=540:960', '-c:v', 'libx264', '-preset', 'medium', '-b:v', '560k', '-maxrate', '700k', '-bufsize', '1400k',
                '-pix_fmt', 'yuv420p', '-an', '-movflags', '+faststart', os.path.join(TMP, 'export', 'video.mp4')], check=True)
    print('listo:', OUT, round(ffdur(OUT), 1), 's')

def exportar(plan, bed, pk, total):
    """Archivos para Claude Studio: video liviano sin audio, cama de sonido (sin voces) y cada voz suelta."""
    ex = os.path.join(TMP, 'export'); os.makedirs(os.path.join(ex, 'voces'), exist_ok=True)
    def mp3(sig, f, br='96k'):
        sp.run(['ffmpeg', '-v', 'error', '-y', '-f', 'f32le', '-ar', str(SR), '-ac', '1', '-i', '-', '-c:a', 'libmp3lame', '-b:a', br, f], input=sig.astype(np.float32).tobytes(), check=True)
    mp3(bed, os.path.join(ex, 'cama.mp3'), '96k')
    voces = []
    for p in plan:
        if p['y'] is None or 't_base' not in p: continue
        y = p['y'] / pk
        nz = np.where(np.abs(y) > 1e-4)[0]; lead = nz[0] if len(nz) else 0
        mp3(y[lead:], os.path.join(ex, 'voces', p['v'] + '.mp3'), '64k')
        voces.append(dict(id=p['v'], toma=p['t'], inicio=round(p['t_base'] + lead / SR, 3), dur=round((len(y) - lead) / SR, 3),
                          texto=SUBT.get(p['v'][:3], TXT[p['v'][:3]]) if p['v'] not in ('V30a', 'V30b') else ('¿Contraseña?' if p['v'] == 'V30a' else 'Siga.')))
    tomas = [dict(toma=p['t'], inicio=round(p['t0'], 3), dur=p['d'], escena=p['sc']) for p in plan]
    json.dump(dict(duracion=round(total, 3), tomas=tomas, voces=voces), open(os.path.join(ex, 'proyecto.json'), 'w'), ensure_ascii=False, indent=1)

def ass_t(t):
    t = max(0, t); h = int(t // 3600); m = int(t % 3600 // 60); s = t % 60
    return f'{h}:{m:02d}:{s:05.2f}'
def palabras(c):
    txt = SUBT.get(c[:3], TXT[c[:3]])
    if c == 'V30a': txt = '¿Contraseña?'
    if c == 'V30b': txt = 'Siga.'
    return txt.split()
def color(w):
    b = re.sub(r'[^\wáéíóúñ]', '', w.lower())
    return '{\\c&H3D3DFF&}' + w + '{\\c&HFFFFFF&}' if b in ROJO else w
def trozos(ws, maxw=3):
    out, cur = [], []
    for w in ws:
        cur.append(w)
        if len(cur) >= maxw or re.search(r'[.,!?…]$', w): out.append(cur); cur = []
    if cur: out.append(cur)
    return out
def escribir_ass(subs, plan, path):
    head = ('[Script Info]\nScriptType: v4.00+\nPlayResX: 1080\nPlayResY: 1920\nWrapStyle: 2\n\n[V4+ Styles]\n'
            'Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, '
            'ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding\n'
            'Style: Sub,Montserrat,68,&H00FFFFFF,&H00FFFFFF,&H00000000,&H80000000,-1,0,0,0,100,100,0,0,1,4,3,5,60,60,0,1\n'
            'Style: Tit,Montserrat,58,&H00FFFFFF,&H00FFFFFF,&H00000000,&H80000000,-1,0,0,0,100,100,6,0,1,4,2,5,60,60,0,1\n\n'
            '[Events]\nFormat: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n')
    ev = []
    for t0, t1, c, pal in subs:
        ws = palabras(c); tr = trozos(ws); n = sum(len(x) for x in tr); dur = t1 - t0
        # cada trozo aparece cuando empieza su primera palabra (tiempos reales de la voz ya pegada a la boca)
        if pal and len(pal) >= 2:
            ini, k = [], 0
            for x in tr:
                j = min(len(pal) - 1, int(round(k * len(pal) / n))); ini.append(max(t0, min(t1, pal[j]))); k += len(x)
            ini.append(t1)
            for i, x in enumerate(tr):
                a_, b_ = ini[i], max(ini[i] + 0.25, ini[i + 1] if i + 1 < len(tr) else t1 + 0.15)
                ev.append(f"Dialogue: 0,{ass_t(a_)},{ass_t(b_)},Sub,,0,0,0,,{{\\pos(540,{SUB_Y})}}{' '.join(color(w) for w in x)}")
            continue
        cur = t0
        for x in tr:
            d = dur * len(x) / n
            ev.append(f"Dialogue: 0,{ass_t(cur)},{ass_t(min(t1 + 0.15, cur + d + 0.05))},Sub,,0,0,0,,{{\\pos(540,{SUB_Y})}}{' '.join(color(w) for w in x)}")
            cur += d
    # canción
    c0 = next((p['t0'] for p in plan if p['sc'] == 'cancion'), 0)
    for (ta, txt), (tb, _) in zip(CANCION[:-1], CANCION[1:]):
        tr = trozos(txt.split(), 4); n = sum(len(x) for x in tr); cur = ta
        for x in tr:
            d = (tb - ta) * len(x) / n
            ev.append(f"Dialogue: 0,{ass_t(c0 + cur)},{ass_t(c0 + cur + d)},Sub,,0,0,0,,{{\\pos(540,{SUB_Y})}}{' '.join(color(w) for w in x)}")
            cur += d
    # título
    tt = next((p['t0'] for p in plan if p.get('titulo')), None)
    if tt is not None: ev.append(f"Dialogue: 1,{ass_t(tt + 0.3)},{ass_t(tt + 3.8)},Tit,,0,0,0,,{{\\pos(540,560)\\fad(250,350)}}EXTRAVÍO · VLOG 01")
    open(path, 'w').write(head + '\n'.join(ev) + '\n')

if __name__ == '__main__':
    main()
