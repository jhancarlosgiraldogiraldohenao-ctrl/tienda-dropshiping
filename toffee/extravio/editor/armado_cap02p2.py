# Capítulo 2 · PARTE 2 · ARMADO SIN VOCES (regla de Jay, 13-nov-2026: primero el armado, después bocas/voces/música).
# Orden, cortes, fundidos, título, proyección en la vaca y visor REC. Audio = el de Flow, solo como guía.
# python3 toffee/extravio/editor/armado_cap02p2.py -> toffee/videos-editados/EXTRAVIO-DIZZY-CAP02-P2-ARMADO.mp4
import os, subprocess as sp, numpy as np, cv2
AQ = os.path.dirname(os.path.abspath(__file__)); RAIZ = os.path.abspath(os.path.join(AQ, '..'))
TK = os.path.join(RAIZ, 'serie', 'tomas-cap02', 'p2'); TK1 = os.path.join(RAIZ, 'serie', 'tomas-cap02', 'horizontal')
FONT = os.path.join(AQ, 'datos-dizzy01', 'fonts', 'Montserrat.ttf')
TMP = os.environ.get('TMPED', '/tmp/armado_cap02p2'); os.makedirs(TMP, exist_ok=True)
OUT = os.path.abspath(os.path.join(RAIZ, '..', 'videos-editados', 'EXTRAVIO-DIZZY-CAP02-P2-ARMADO.mp4'))
W, H, FPS, XF = 1920, 1080, 30, 0.3

# t = toma, a/b = corte. rec = visto por la cámara de Dizzy. proy = (toma proyectada en el recuadro verde, desde, velocidad)
E = [
 dict(t='U18', a=0.0, b=2.3),                                   # GANCHO: el violinazo (corta antes de que el violín quede en el cuello)
 dict(t='A-BARRIO', src=TK1, a=0.0, b=4.0, titulo='EXTRAVÍO · VLOG 02 · PARTE 2'),
 dict(t='U02', a=0.6, b=4.8), dict(t='U03', a=1.5, b=5.4), dict(t='U03b', a=0.5, b=3.6), dict(t='U04', a=0.0, b=4.0),
 dict(t='U05', a=0.6, b=3.2), dict(t='U05b', a=0.0, b=4.0),
 dict(t='A-CANALES', a=0.0, b=3.5),
 dict(t='U06', a=0.2, b=4.0), dict(t='U07', a=1.2, b=4.6), dict(t='U08', a=0.4, b=8.0), dict(t='U09', a=0.0, b=4.0),
 dict(t='U10a', a=0.0, b=4.0), dict(t='U10b', a=1.0, b=5.6),
 dict(t='U11', a=1.4, b=4.9), dict(t='U12b', a=0.0, b=6.0), dict(t='U12', a=0.0, b=3.0), dict(t='U13', a=0.0, b=3.0),
 dict(t='V0', a=1.5, b=9.0), dict(t='V5', a=0.4, b=2.9),
 dict(t='U15', a=0.6, b=3.8), dict(t='U16', a=0.5, b=6.6), dict(t='U17', a=0.4, b=4.0), dict(t='U18', a=0.0, b=2.3),
 dict(t='U19', a=0.9, b=3.8), dict(t='U21', a=1.2, b=3.9), dict(t='U20', a=0.0, b=3.5),   # «ya va a salir el sol» → campanas y cielo rosado → corren
 dict(t='U22', a=1.0, b=5.5), dict(t='U23', a=1.0, b=5.4),
 # corte a Colombia: El Hueco
 dict(t='A-HUECO', a=0.0, b=4.2), dict(t='H0', a=2.6, b=6.0), dict(t='H0b', a=0.0, b=3.0),
 dict(t='H1', a=1.2, b=5.0), dict(t='H2', a=1.2, b=5.8), dict(t='H3', a=0.0, b=4.0),
 dict(t='H3b', a=0.0, b=6.0, proy=('U24', 0.0, 1.0)),
 dict(t='H3c', a=0.0, b=4.0, proy=('A-MX-AMANECER', 0.0, 0.75)),
 # México visto por la cámara de Dizzy
 dict(t='A-MX-AMANECER', a=3.0, b=6.0, rec=1), dict(t='U24', a=0.0, b=5.0, rec=1), dict(t='U25', a=1.2, b=5.0, rec=1),
 dict(t='I-TAPA', a=0.0, b=4.0, rec=1), dict(t='U26-v2', a=0.8, b=4.0, rec=1), dict(t='U26b', a=0.0, b=4.0, rec=1),
 # vuelta a El Hueco
 dict(t='H4', a=0.0, b=7.0), dict(t='H5', a=0.0, b=3.0), dict(t='H6', a=0.8, b=4.0),
 dict(t='H3b', a=3.0, b=6.0, proy=('W2-v3', 0.0, 1.0)),          # Dizzy aparece en la vaca…
 dict(t='W2-v3', a=3.0, b=8.0, rec=1, fin=1),                    # …y luego a pantalla completa
]

def run(a): sp.run(a, check=True)

REC = ("drawbox=x=60:y=50:w=140:h=8:c=white:t=fill,drawbox=x=60:y=50:w=8:h=110:c=white:t=fill,"
       "drawbox=x=1720:y=50:w=140:h=8:c=white:t=fill,drawbox=x=1852:y=50:w=8:h=110:c=white:t=fill,"
       "drawbox=x=60:y=1022:w=140:h=8:c=white:t=fill,drawbox=x=60:y=920:w=8:h=110:c=white:t=fill,"
       "drawbox=x=1720:y=1022:w=140:h=8:c=white:t=fill,drawbox=x=1852:y=920:w=8:h=110:c=white:t=fill,"
       "drawbox=x=1620:y=96:w=26:h=26:c=red:t=fill:enable='lt(mod(t,1),0.6)',"
       f"drawtext=fontfile={FONT}:text=REC:x=1660:y=90:fontsize=40:fontcolor=white,noise=alls=6:allf=t")

def leer(path, a, n, vel=1.0):
    """n cuadros 1920x1080 desde el segundo a, a la velocidad vel."""
    raw = sp.run(['ffmpeg', '-v', 'error', '-ss', str(a), '-i', path, '-vf', f'setpts=PTS/{vel},scale={W}:{H},fps={FPS}',
                  '-frames:v', str(n), '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-'], capture_output=True, check=True).stdout
    f = np.frombuffer(raw, np.uint8).reshape(-1, H, W, 3)
    if len(f) < n: f = np.concatenate([f, np.repeat(f[-1:], n - len(f), 0)])
    return f

def proyectar(e, out):
    """Pone la toma `proy` dentro del recuadro verde de la vaca (sigue al recuadro cuadro a cuadro)."""
    n = int(round((e['b'] - e['a']) * FPS))
    base = leer(os.path.join(TK, e['t'] + '.mp4'), e['a'], n)
    pt, pa, pv = e['proy']; cont = leer(os.path.join(TK, pt + '.mp4'), pa, n, pv)
    p = sp.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                  '-c:v', 'libx264', '-crf', '16', '-preset', 'fast', '-pix_fmt', 'yuv420p', out], stdin=sp.PIPE)
    for f, c in zip(base, cont):
        hsv = cv2.cvtColor(f, cv2.COLOR_BGR2HSV)
        m = cv2.inRange(hsv, (35, 50, 120), (90, 255, 255))
        m = cv2.morphologyEx(m, cv2.MORPH_CLOSE, np.ones((15, 15), np.uint8))
        cs, _ = cv2.findContours(m, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        o = f.astype(np.float32)
        if cs:
            k = max(cs, key=cv2.contourArea)
            if cv2.contourArea(k) > 4000:
                x, y, w, h = cv2.boundingRect(k)
                hull = cv2.convexHull(k); mm = np.zeros((H, W), np.float32); cv2.fillPoly(mm, [hull], 1.0)
                mm = cv2.GaussianBlur(mm, (0, 0), 2.5)[..., None]
                # recorta el contenido al tamaño del recuadro (16:9 llenando)
                ch, cw = c.shape[:2]; s = max(w / cw, h / ch)
                r = cv2.resize(c, (int(cw * s) + 2, int(ch * s) + 2), interpolation=cv2.INTER_AREA)
                ox, oy = (r.shape[1] - w) // 2, (r.shape[0] - h) // 2
                lay = np.zeros_like(o); lay[y:y + h, x:x + w] = r[oy:oy + h, ox:ox + w]
                # luz de proyector: el contenido brilla un poco y deja ver la textura del pelo
                tex = cv2.cvtColor(f, cv2.COLOR_BGR2GRAY).astype(np.float32)[..., None] / 255
                proj = np.clip(lay * (0.75 + 0.35 * tex) + 12, 0, 255)
                o = o * (1 - mm) + proj * mm
        p.stdin.write(o.astype(np.uint8).tobytes())
    p.stdin.close(); p.wait()

def segmento(i, e):
    out = os.path.join(TMP, f's{i:02d}.mp4'); d = e['b'] - e['a']
    src = os.path.join(e.get('src', TK), e['t'] + '.mp4')
    vid = os.path.join(TMP, f'v{i:02d}.mp4')
    if 'proy' in e:
        proyectar(e, vid); vin = ['-i', vid]; vss = []
    else:
        vin = ['-ss', str(e['a']), '-t', str(d), '-i', src]; vss = []
    vf = f'scale={W}:{H}:flags=lanczos,fps={FPS},setsar=1'
    if e.get('rec'): vf += ',' + REC
    if e.get('titulo'):  # letra de Gnomo: Montserrat negrita, blanca, borde fino oscuro, pequeña, igual que la parte 1
        ass = os.path.join(TMP, f't{i:02d}.ass')
        open(ass, 'w').write('[Script Info]\nScriptType: v4.00+\nPlayResX: 1920\nPlayResY: 1080\n\n[V4+ Styles]\n'
            'Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding\n'
            'Style: Tit,Montserrat,50,&H00FFFFFF,&H00FFFFFF,&H00000000,&H80000000,-1,0,0,0,100,100,6,0,1,4,2,5,60,60,0,1\n\n'
            '[Events]\nFormat: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n'
            f'Dialogue: 1,0:00:00.30,0:00:{d - 0.2:05.2f},Tit,,0,0,0,,{{\\pos(960,300)\\fad(250,350)}}' + e['titulo'] + '\n')
        vf += f",subtitles={ass}:fontsdir={os.path.dirname(FONT)}"
    if e.get('fin'): vf += f',fade=t=out:st={d - 1.0}:d=1.0'
    vf += ',format=yuv420p'
    # audio guía de Flow (de la toma original, mismo tramo)
    ain = ['-ss', str(e['a']), '-t', str(d), '-i', src]
    run(['ffmpeg', '-v', 'error', '-y', *vin, *ain, '-f', 'lavfi', '-t', str(d), '-i', 'anullsrc=r=48000:cl=stereo',
         '-filter_complex', f'[0:v]{vf}[v];[1:a]aresample=48000,aformat=channel_layouts=stereo,apad[a1];[a1][2:a]amix=2:duration=shortest:normalize=0[a]',
         '-map', '[v]', '-map', '[a]', '-t', str(d), '-c:v', 'libx264', '-crf', '16', '-preset', 'fast', '-c:a', 'aac', '-b:a', '192k', out])
    return out, d

def main():
    segs = [segmento(i, e) for i, e in enumerate(E)]
    ins = sum([['-i', s] for s, _ in segs], []); fc = []; t = segs[0][1]; lv, la = '[0:v]', '[0:a]'
    for i in range(1, len(segs)):
        off = t - XF
        fc.append(f'{lv}[{i}:v]xfade=transition=fade:duration={XF}:offset={off:.3f}[v{i}]')
        fc.append(f'{la}[{i}:a]acrossfade=d={XF}[a{i}]')
        lv, la = f'[v{i}]', f'[a{i}]'; t = off + segs[i][1]
    run(['ffmpeg', '-v', 'error', '-y', *ins, '-filter_complex', ';'.join(fc), '-map', lv, '-map', la,
         '-c:v', 'libx264', '-crf', '18', '-preset', 'medium', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '192k',
         '-movflags', '+faststart', OUT])
    print('ok', OUT, round(t, 1), 's')

if __name__ == '__main__':
    main()
