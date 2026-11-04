# -*- coding: utf-8 -*-
"""Editor del capítulo 1 de Dizzy (vertical 9:16), parte 1 del video.
Sigue ESTUDIO-EDICION-GNOMO.md: cortes secos, el sonido nunca se corta, voces en L sobre la toma siguiente,
subtítulos Montserrat blancos en el centro con palabras clave en rojo, música por escena que baja bajo las voces,
golpes de sonido en los chistes. Quita la voz de Flow y pone la de ElevenLabs pegada a la boca.
python3 toffee/extravio/editor/ed_dizzy01.py  ->  toffee/videos-editados/EXTRAVIO-DIZZY-CAP01-P1.mp4
"""
import os, re, sys, json, subprocess as sp
import numpy as np
AQ = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQ)
from pegar import load, fit, pegar_suave, SR  # noqa: E402
RAIZ = os.path.abspath(os.path.join(AQ, '..'))
TK = os.path.join(RAIZ, 'serie', 'tomas-cap01')
VZ = os.path.join(RAIZ, 'serie', 'voces-cap01')
SN = os.path.join(RAIZ, 'sonidos')
DAT = os.path.join(AQ, 'datos-dizzy01')
TMP = os.environ.get('TMPED', '/tmp/ed_dizzy01')
FONTS = os.environ.get('FONTS', os.path.join(DAT, 'fonts'))
OUT = os.path.abspath(os.path.join(RAIZ, '..', 'videos-editados', 'EXTRAVIO-DIZZY-CAP01-P1.mp4'))
W, H, FPS = 1080, 1920, 30
os.makedirs(TMP, exist_ok=True)

VOZ = json.load(open(os.path.join(VZ, 'MAPA-VOCES.json')))
FLOW = json.load(open(os.path.join(DAT, 'ritmo-flow.json')))          # palabras de Flow por toma: [ini, fin, palabra]
sys.path.insert(0, os.path.join(RAIZ, 'serie'))
from cap01_voces_p1 import V as VTXT  # noqa: E402
TXT = {c: re.sub(r'\[[^\]]*\]', '', t).replace('  ', ' ').strip() for c, _, _, _, t, _ in VTXT}
# subtítulos con traducción (las frases en inglés de Tocino)
SUBT = {
 'V22': '¡Quiubo, parce!',
 'V23': 'Dios mío… ¿Eso es un cámara?',
 'V24': 'Con ese cámara y ese café… si lo vendemos en El Hueco nos pagan el doble: pagamos la deuda de tu abuela y nos sobra pa\' ser famosos, man. ¡A rockear, nena!',
 'V25': 'Dios mío, esto es una locura…',
 'V27': '¿Qué putas, parce?',
 'V28': '¿Qué? Es una cucaracha, ¿no? Cuca… cucaracha… Estoy confundido, parce.',
}
ROJO = {'cucha', 'cámara', 'malparidos', 'hijueputa', 'bartolo', 'perro', 'estúpido', 'tocino', 'perico', 'hueco', 'lucas',
        'cuca', 'tuerto', 'gonorrea', 'abuelita', 'mijito', 'arepaaa', 'tapas', 'talento', 'trampa', 'gringo', 'vlog', 'vlogger', 'cochino'}

# ---------------- lista de tomas (parte 1) ----------------
# t: toma · a: entrada (s) · d: duración (None = lo que pida la voz) · v: voz · vo: voz en off (segundos desde el inicio)
# sc: escena · fx: [(efecto, segundo, ganancia)] · fin: efecto al terminar la voz · tinte · zoom · titulo
E = [
 dict(t='G01', a=0.0, v='V01', vo=0.15, sc='zarzo', d=None),   # G01 nueva: Flow habló en inglés, la boca se mueve todo el tiempo
 dict(t='G02', a=0.2, d=None, v='V03', vo=0.2, sc='recuerdo', tinte=1),
 dict(t='G03', a=0.4, d=1.8, sc='recuerdo', tinte=1,),
 dict(t='G04', a=0.3, d=None, v='V04', vo=0.3, sc='recuerdo', tinte=1),
 dict(t='G01', a=6.6, v='V02', vo=0.1, sc='zarzo', d=None),
 dict(t='G05', a=0.0, d=3.4, sc='finca', titulo=1),
 dict(t='G06', a=0.0, v='V05', sc='finca', d=None),
 dict(t='G07', a=0.0, d=2.3, v='V20', sc='finca'),
 dict(t='G08', a=0.85, v='V06', sc='finca', d=None),
 dict(t='G07', a=2.2, d=1.4, sc='finca'),                                     # Bartolo mira (cola de la frase en L)
 dict(t='G09', a=1.6, v='V17', sc='finca', d=None),
 dict(t='G10', a=1.6, v='V07', sc='finca', d=None),
 dict(t='G11', a=0.0, v='V18', sc='finca', d=None),
 dict(t='G10', a=0.0, d=None, v='V19', vo=0.45, sc='finca'),                    # «¡Dios me lo bendiga!» sobre Dizzy
 dict(t='G12', a=0.0, d=2.6, sc='camino'),
 dict(t='G13', a=0.4, v='V08', sc='camino', d=None),
 dict(t='G14', a=0.0, d=2.7, sc='camino', cortar_musica=1.25),
 dict(t='G15', a=0.0, v='V09', sc='camino', d=None),
 dict(t='G16', a=0.0, d=1.9, sc='camino', fx=[('E09-grillo-silencio', 0.2, .7)]),
 dict(t='G17', a=0.0, d=3.0, sc='camino', volver_musica=1.6),
 dict(t='G18', a=0.0, d=3.4, sc='plaza'),
 dict(t='G19', a=0.5, v='V21', sc='plaza', d=None),
 dict(t='G20', a=0.5, v='V10', sc='plaza', d=None),
 dict(t='G21', a=1.6, v='V22', sc='plaza', d=None),
 dict(t='G22', a=1.4, v='V23', sc='plaza', d=None),
 dict(t='G23', a=0.0, v='V11', sc='plaza', d=None),
 dict(t='G24', a=0.3, v='V24', sc='plaza', d=None),
 dict(t='G25', a=0.5, v='V12', sc='plaza', d=None),
 dict(t='G26', a=0.4, d=3.2, sc='olla'),
 dict(t='G26b', a=0.3, v='V31', sc='olla', d=None),
 dict(t='G27', a=1.6, v='V25', sc='olla', d=None),
 dict(t='G28', a=0.0, d=1.9, v='V30a', sc='olla'),
 dict(t='G29', a=0.0, v='V13', sc='olla', d=None),
 dict(t='G28', a=2.4, d=2.0, v='V30b', sc='olla'),
 # la canción (sin voces habladas)
 dict(t='G30', a=3.0, d=4.0, sc='cancion'),
 dict(t='G32', a=0.5, d=2.0, sc='cancion'),
 dict(t='G33', a=1.0, d=3.0, sc='cancion'),
 dict(t='G34', a=0.5, d=4.0, sc='cancion'),
 dict(t='G35', a=2.0, d=3.0, sc='cancion'),
 dict(t='G31', a=0.0, d=4.0, sc='cancion'),
 dict(t='G35', a=5.0, d=1.8, sc='cancion'),
 dict(t='G31', a=5.5, d=2.5, sc='cancion'),
 # «muestra esa cuca»
 dict(t='G36', a=2.9, v='V26', sc='cuca', recorte=1, d=None),
 dict(t='G37', a=0.0, d=2.4, sc='cuca', fx=[('E09-grillo-silencio', 0.3, .8)]),
 dict(t='G38', a=0.4, d=2.6, sc='cuca', fx=[('E16-cachetada-triple', 1.2, .9)]),
 dict(t='G39', a=0.0, v='V27', sc='cuca', d=None),
 dict(t='G40', a=1.0, v='V14', sc='cuca', d=None),
 dict(t='G41', a=0.0, v='V28', sc='cuca', d=None),
 dict(t='G42', a=0.7, v='V29', sc='cuca', d=None),
 dict(t='G43', a=0.6, v='V15', sc='cuca', d=None),
 dict(t='G44', a=0.5, d=3.2, sc='cuca', fx=[('E17-bajo-amenaza', 0.8, 1.0)]),
 dict(t='G45', a=0.9, v='V16', sc='final', d=None),
]
MUSICA = {'recuerdo': ('M5-tuerto-reggaeton', .32), 'finca': ('M1-finca-bambuco', .38), 'camino': ('M2-camino-carranga', .42),
          'plaza': ('M3-plaza-vallenato', .30), 'cancion': ('M4-cancion-el-hueco', .95)}
AMB = {'zarzo': ('E01-zarzo-amanecer', .35), 'finca': ('E02-ambiente-finca', .30), 'camino': ('E02-ambiente-finca', .22),
       'olla': ('E14-ambiente-olla', .45), 'cancion': ('E14-ambiente-olla', .15), 'cuca': ('E14-ambiente-olla', .40), 'final': ('E14-ambiente-olla', .40)}
CANCION = [(0.2, 'Bienvenido a El Hueco, mi amor,'), (2.0, 'aquí se entra, pero no se sale.'), (4.0, '¡Gallinazo! Carnecita fresca… ¡de ayer!'),
           (6.1, '¡Sapo! Perico del bueno, pa\' que vueles sin avión.'), (9.0, '¡Rata vieja! Cambio tapas, cambio todo… hasta el alma.'),
           (13.0, '¡Todos!'), (16.0, '¡En El Hueco, en El Hueco!'), (18.0, 'Aquí todo tiene precio…'), (20.0, '¡y el precio lo pone el Tuerto!'), (23.0, None)]

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

SYNC = []
def main():
    total = 0.0; plan = []
    for k, e in enumerate(E):
        f = os.path.join(TK, e['t'] + '.mp4'); L = ffdur(f)
        y = None; vstart = None
        if e.get('v'):
            x = voz(e['v'])
            fw = [[w[0] - e['a'], w[1] - e['a'], w[2]] for w in FLOW.get(e['t'], []) if w[0] >= e['a'] - 0.05]
            if 'vo' in e or not fw or e['v'] in ('V30a', 'V30b'):
                y = x; vstart = e.get('vo', (fw[0][0] + 0.08) if fw else 0.3)
            else:
                ew = VW.get(e['v'], [])
                try:
                    lim = (e['d'] if e['d'] else L - e['a']) + 2.5
                    y, err = pegar_suave(x, ew, fw, lim, lo=0.8, hi=1.25, tmp=os.path.join(TMP, 'pg'))
                    y = np.concatenate([np.zeros(int(0.08 * SR), np.float32), y])   # la voz nunca antes que la boca
                    nz = np.where(np.abs(y) > 1e-4)[0]
                    y = y[: nz[-1] + 1] if len(nz) else y
                    vstart = 0.0
                    if err: SYNC.append((e['t'], round(float(np.mean(np.abs(err))), 3), round(float(np.max(np.abs(err))), 3)))
                except Exception as ex:
                    print('  sin anclas en', e['t'], ex)
                    y = x; vstart = fw[0][0] + 0.08
        d = e['d']
        if d is None:
            need = (vstart or 0) + (len(y) / SR if y is not None else 0) + 0.32
            d = min(max(need, 1.4), L - e['a'])
        d = min(d, L - e['a'])
        plan.append(dict(e, f=f, d=round(d, 3), t0=total, y=y, vs=vstart))
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
        for w in FLOW.get(p['t'], []):
            i0 = int((w[0] - p['a'] - 0.06) * SR); i1 = int((w[1] - p['a'] + 0.10) * SR)
            i0 = max(0, i0); i1 = min(len(g), i1)
            if i1 > i0: g[i0:i1] = 0
        k = int(0.06 * SR); g = np.convolve(g, np.ones(k) / k, mode='same').astype(np.float32)
        lev = .12 if p['sc'] == 'cancion' else .7
        put(toma, s * g * lev, p['t0'])
        if p['y'] is not None:
            t = p['t0'] + p['vs']
            if t < prev_end + 0.05: print('  ojo: voz encima en', p['t'], round(prev_end - t, 2))
            put(voces, p['y'], t); prev_end = t + len(p['y']) / SR
            subs.append((t, t + len(p['y']) / SR, p['v']))
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
    mix /= max(1e-6, np.max(np.abs(mix))) / 0.9
    wav = os.path.join(TMP, 'mix.wav')
    sp.run(['ffmpeg', '-v', 'error', '-y', '-f', 'f32le', '-ar', str(SR), '-ac', '1', '-i', '-', wav], input=mix.astype(np.float32).tobytes(), check=True)
    # subtítulos (ASS)
    escribir_ass(subs, plan, os.path.join(TMP, 'subs.ass'))
    # video
    lst = []
    for i, p in enumerate(plan):
        vf = [f'scale={W}:{H}:flags=lanczos', 'setsar=1', f'fps={FPS}']
        if p.get('zoom'): z = p['zoom']; vf.insert(0, f'crop=iw/{z}:ih/{z}')
        if p.get('recorte'): vf.insert(0, 'crop=iw*0.82:ih*0.82:iw*0.02:ih*0.09')   # quita el brazo humano del borde derecho (G36)
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
    print('listo:', OUT, round(ffdur(OUT), 1), 's')

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
    for t0, t1, c in subs:
        ws = palabras(c); tr = trozos(ws); n = sum(len(x) for x in tr); dur = t1 - t0
        cur = t0
        for x in tr:
            d = dur * len(x) / n
            ev.append(f"Dialogue: 0,{ass_t(cur)},{ass_t(min(t1 + 0.15, cur + d + 0.05))},Sub,,0,0,0,,{{\\pos(540,1200)}}{' '.join(color(w) for w in x)}")
            cur += d
    # canción
    c0 = next(p['t0'] for p in plan if p['sc'] == 'cancion')
    for (ta, txt), (tb, _) in zip(CANCION[:-1], CANCION[1:]):
        tr = trozos(txt.split(), 4); n = sum(len(x) for x in tr); cur = ta
        for x in tr:
            d = (tb - ta) * len(x) / n
            ev.append(f"Dialogue: 0,{ass_t(c0 + cur)},{ass_t(c0 + cur + d)},Sub,,0,0,0,,{{\\pos(540,1200)}}{' '.join(color(w) for w in x)}")
            cur += d
    # título
    tt = next(p['t0'] for p in plan if p.get('titulo'))
    ev.append(f"Dialogue: 1,{ass_t(tt + 0.3)},{ass_t(tt + 3.8)},Tit,,0,0,0,,{{\\pos(540,560)\\fad(250,350)}}EXTRAVÍO · VLOG 01")
    open(path, 'w').write(head + '\n'.join(ev) + '\n')

if __name__ == '__main__':
    main()
