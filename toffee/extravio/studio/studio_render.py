"""Video final desde Claude Studio: lo que Jay ve en el editor es lo que sale.

Uso:
  python3 toffee/extravio/studio/studio_render.py --datos <carpeta con proyectos/cap01p1/voces/*.json y proyecto.json>
      --cama <cama.wav|mp3> --voces <carpeta con V##.wav> --video <video sin audio ni letras> --ass <subs.ass del editor (para el estilo)>
      --out <video.mp4>
Las voces se ponen igual que en el editor: posición = inicio + mueve + desde, suena del segundo «desde» al «hasta»
del archivo, con su volumen; los subtítulos de cada pedazo se mueven con él.
"""
import argparse, glob, json, os, re, subprocess as sp
import numpy as np

SR = 48000
ap = argparse.ArgumentParser()
for k in ('datos', 'cama', 'voces', 'video', 'ass', 'out'): ap.add_argument('--' + k, required=True)
a = ap.parse_args()

def load(f):
    r = sp.run(['ffmpeg', '-v', 'error', '-i', f, '-f', 'f32le', '-ac', '1', '-ar', str(SR), '-'], capture_output=True, check=True)
    return np.frombuffer(r.stdout, np.float32).copy()

P = json.load(open(os.path.join(a.datos, 'proyecto.json')))
V = [json.load(open(f)) for f in sorted(glob.glob(os.path.join(a.datos, 'proyectos', 'cap01p1', 'voces', '*.json')))]
dur = float(P['duracion'])
mix = np.zeros(int((dur + 1) * SR), np.float32)
cama = load(a.cama)[:len(mix)]; mix[:len(cama)] += cama
cache = {}
ev = []
def ts(t):
    t = max(0, t); h = int(t // 3600); m = int(t % 3600 // 60); s = t % 60
    return f'{h}:{m:02d}:{s:05.2f}'
def ass_txt(t): return t.replace('<r>', '{\\c&H3D3DFF&}').replace('</r>', '{\\c&HFFFFFF&}')
for v in V:
    if v.get('mute'): continue
    base = v.get('base') or v['id']
    if base not in cache: cache[base] = load(os.path.join(a.voces, base + '.wav'))
    y = cache[base]; d = float(v.get('desde') or 0); h = float(v['hasta'] if v.get('hasta') is not None else v['dur'])
    seg = y[int(d * SR):int(h * SR)] * float(v.get('gain', 1) if v.get('gain') is not None else 1)
    t0 = float(v['inicio']) + float(v.get('mueve') or 0)  # momento del segundo 0 del archivo
    i = int((t0 + d) * SR)
    if i < 0: seg = seg[-i:]; i = 0
    seg = seg[:max(0, len(mix) - i)]; mix[i:i + len(seg)] += seg
    for k in v.get('subs', []):
        if k['b'] <= d or k['a'] >= h: continue
        ev.append((t0 + max(k['a'], d), t0 + min(k['b'], h), f"{{\\pos(540,1200)}}{ass_txt(k['t'])}", 'Sub'))
for k in P.get('subs_fijos', []):
    ev.append((k['a'], k['b'], f"{{\\pos(540,{k.get('y', 1200)})}}{ass_txt(k['t'])}", k.get('estilo', 'Sub')))
mix = mix[:int(dur * SR)]
pk = float(np.max(np.abs(mix))) or 1.0
if pk > 0.98: mix *= 0.98 / pk
tmp = os.path.splitext(a.out)[0]
wav, ass = tmp + '.mix.wav', tmp + '.ass'
sp.run(['ffmpeg', '-v', 'error', '-y', '-f', 'f32le', '-ar', str(SR), '-ac', '1', '-i', '-', '-c:a', 'pcm_s16le', wav], input=mix.tobytes(), check=True)
head = open(a.ass, encoding='utf8').read().split('[Events]')[0]
with open(ass, 'w', encoding='utf8') as f:
    f.write(head + '[Events]\nFormat: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n')
    for t0, t1, txt, st in sorted(ev):
        f.write(f'Dialogue: 0,{ts(t0)},{ts(t1)},{st},,0,0,0,,{txt}\n')
fonts = os.path.join(os.path.dirname(__file__), '..', 'editor', 'datos-dizzy01', 'fonts')
sp.run(['ffmpeg', '-v', 'error', '-y', '-i', a.video, '-i', wav, '-vf', f'ass={ass}:fontsdir={fonts}',
        '-af', 'loudnorm=I=-14:TP=-1.5:LRA=11', '-c:v', 'libx264', '-preset', 'medium', '-crf', '22', '-maxrate', '4M', '-bufsize', '8M',
        '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '160k', '-ar', '48000', '-shortest', '-movflags', '+faststart', a.out], check=True)
os.remove(wav)
print('listo:', a.out, f'{len(V)} pedazos de voz, {len(ev)} subtítulos')
