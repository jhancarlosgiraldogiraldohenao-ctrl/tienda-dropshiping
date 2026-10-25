import subprocess, sys
exec(open('../d1b/armar.py').read().split('W=(255,255,255,255)')[0])
W=(255,255,255,255)
VOZ2=None   # línea de la toma 2 (pendiente)
# segmentos: (clip, ini, fin, zoom, cx, cy, vol_ambiente)
S=[('t1',0,2.0,1.0,.5,.4,0),('t1',2.0,5.0,1.18,.5,.32,0),
   ('t2',0,3.2,1.0,.5,.5,.35),('t2',3.2,6.4,1.2,.55,.55,.35),
   ('t3',0.6,4.0,1.0,.5,.4,0),('t3',4.0,7.4,1.2,.5,.33,0),
   ('t4',0,6.0,1.0,.5,.5,.35),
   ('t5',0,4.0,1.0,.5,.5,.6),('t5',4.0,8.0,1.0,.5,.5,1.8),
   ('t6',0,3.0,1.0,.5,.5,0),('t6',3.0,7.3,1.15,.4,.5,0),
   ('t7',0,4.5,1.0,.5,.5,.35),('t7',4.5,9.2,1.0,.5,.5,.35),
   ('t8',1.4,5.8,1.0,.5,.5,0),
   ('t9a',0,6.0,1.0,.5,.5,.4),
   ('t9b',0,4.0,2.6,.535,.67,.5),
   ('t9c',1.6,6.0,1.0,.5,.5,0)]
T=[];t=0
for s in S: T.append(t); t+=s[2]-s[1]
END=t; TOT=END+3.2
def seg_t(clip,x):  # tiempo del clip -> tiempo en la línea de tiempo
    for i,s in enumerate(S):
        if s[0]==clip and s[1]<=x<s[2]+1e-6: return T[i]+x-s[1]
    raise ValueError((clip,x))
import subprocess as sp
# Cortes SOLO en silencios del audio de ElevenLabs (nunca dentro de una palabra).
# (archivo, ini_corte, fin_corte, inicio_voz, fin_voz, clip, boca_ini, boca_fin, subtítulo)  boca=None -> voz en off (boca_ini = desfase)
VO=[('voz.mp3',0.00,0.98,0.00,0.85,'t1',0.97,1.54,'¡Humanos!'),
    ('voz.mp3',0.98,3.22,1.14,3.04,'t1',2.12,4.08,'Mañana me voy|al Polo Norte.'),
    ('voz.mp3',3.22,7.52,3.40,7.34,'t3',1.28,6.37,'Y me enteré|de que Santa|nunca les trae|regalos|a los animales|de la calle.'),
    ('voz2.mp3',0.00,5.72,0.00,5.63,'t2',0.40,None,'Este es|Galleta.|Su primera|Navidad|la pasó|temblando|debajo de|un carro.'),
    ('voz.mp3',7.52,12.63,7.69,12.44,'t4',0.40,None,'Así que voy|a pedírselo|en persona.|Todos los|animales|merecen|un regalo.'),
    ('voz.mp3',12.63,16.13,12.82,15.92,'t5',2.60,None,'Galleta|viene conmigo.|Él todavía|no lo sabe.'),
    ('voz.mp3',16.13,17.45,16.34,17.29,'t6',0.13,1.11,'Nuestro vehículo:'),
    ('voz.mp3',17.45,18.55,17.61,18.36,'t6',1.53,2.15,'mi trineo.'),
    ('voz.mp3',18.55,19.51,18.74,19.37,'t6',3.13,3.37,'Bueno…'),
    ('voz.mp3',19.51,20.57,19.66,20.41,'t6',3.87,4.44,'es mi cama.'),
    ('voz.mp3',20.57,22.31,20.74,22.13,'t6',5.19,6.79,'Pero tiene|forma de trineo.'),
    ('voz.mp3',22.31,27.78,22.49,27.61,'t7',0.40,None,'Díganme en|los comentarios|qué animalito|de la calle|merece|un regalo.|¡Despegamos!'),
    ('voz.mp3',27.78,28.99,27.94,28.82,'t8',2.25,3.27,'Creo que…'),
    ('voz.mp3',28.99,30.97,29.16,30.71,'t8',3.87,5.10,'no sé|manejar esto.'),
    ('voz.mp3',30.97,32.08,31.23,31.89,'t9c',3.00,3.58,'¿Y tú…'),
    ('voz.mp3',32.08,33.15,32.27,33.03,'t9c',3.90,4.37,'quién eres?')]
VO.sort(key=lambda v: seg_t(v[5],v[6]))
import numpy as np
_cache={}
def _db(src,t):
    if src not in _cache:
        _cache[src]=np.frombuffer(sp.run(['ffmpeg','-v','error','-i',src,'-ac','1','-ar','16000','-f','s16le','-'],capture_output=True).stdout,np.int16).astype(np.float32)
    a=_cache[src]; i=int(t*16000); w=a[max(i-240,0):i+240]
    return 20*np.log10(np.sqrt((w**2).mean())+1e-9) if len(w) else -99
for v in VO:
    for t in (v[1],v[2]):
        d=_db(v[0],t); assert d<20, f'CORTE EN SONIDO: {v[0]} {t} nivel {d:.0f} dB ({v[8][:20]})'
placed=[]; subtxt=[]; last_end=-1
for n,(src,cs,ce,von,voff,c,b0,b1,txt) in enumerate(VO):
    if b1 is None: tempo=1.0; onset_tl=seg_t(c,b0)+(von-cs)
    else:
        tempo=1.0; onset_tl=seg_t(c,b0)
    start_tl=onset_tl-(von-cs)/tempo
    if start_tl<last_end: shift=last_end-start_tl; start_tl+=shift; onset_tl+=shift
    d=(ce-cs)/tempo; last_end=start_tl+d
    out=f'k{n}.wav'
    sp.run(['ffmpeg','-v','error','-y','-i',src,'-af',f'atrim={cs}:{ce},asetpts=PTS-STARTPTS'+(f',atempo={tempo:.4f}' if tempo!=1 else '')+f',afade=t=in:d=0.005,afade=t=out:st={d-0.006:.3f}:d=0.005','-ar','48000',out],check=True)
    placed.append((out,start_tl))
    subtxt.append((txt,onset_tl,onset_tl+(voff-von)/tempo))
    print(f'{c} {txt[:22]:22s} tempo={tempo:.3f} en {start_tl:.2f}')
KEY={'polo','norte','santa','regalo','regalos','galleta','trineo','animales','animalito','despegamos','navidad'}
ov=[]
def add(name,img,a,b,y): img.save(name); ov.append((name,a,b,y))
k=0; subs=[]
for txt,a0,b0 in subtxt:
    ps=txt.split('|'); L=sum(len(p) for p in ps); x0=a0
    for p in ps:
        x1=x0+(b0-a0)*len(p)/L; subs.append((p,x0,x1)); x0=x1
for i,(p,a0,b0) in enumerate(subs):
    nxt=subs[i+1][1] if i+1<len(subs) else 1e9
    b0=min(nxt,b0+0.35) if nxt-b0<0.6 else b0+0.2
    ws=p.split(' '); parts=[]
    for j,w in enumerate(ws):
        parts.append((w+(' ' if j<len(ws)-1 else ''),CAR if w.strip('¡!¿?.,:…').lower() in KEY else W))
    add(f'o_s{k}.png',linea(parts,76,8),a0,b0,1400); k+=1
add('o_tit.png',bloque([linea([('El viaje de Toffee al ',W),('Polo Norte',CAR)],66,7),linea([('Vlog 1 ',W),('EMO','🛷')],80,8)]),0,3.2,230)
t7=seg_t('t7',0.4)
add('o_cta.png',bloque([linea([('Comenta ',W),('EMO','👇')],70,7),linea([('¿Qué animalito merece un regalo?',W)],52,6)]),t7,t7+4.3,260)
add('o_fin.png',bloque([linea([('Vlog 2 mañana ',W),('EMO','🛷')],92,9),linea([('Sígueme para ver quién es ',W),('EMO','👀')],56,6)]),END,99,330)
# --- render ---
inp=[]
clips=sorted(set(s[0] for s in S),key=lambda c:[s[0] for s in S].index(c))
for c in clips: inp+=['-i',c+'.mp4']
VI=len(clips)
for w,_ in placed: inp+=['-i',w]
inp+=(['-i',VOZ2] if VOZ2 else [])
OI=len(clips)+len(placed)+(1 if VOZ2 else 0)
for o in ov: inp+=['-i',o[0]]
base='scale=1080:1920:flags=lanczos,hqdn3d=1.5:1.5:3:3,unsharp=5:5:0.7:5:5:0,setsar=1,fps=24'
fc=[];vl=[];al=[]
for i,(c,a,b,z,cx,cy,vol) in enumerate(S):
    ci=clips.index(c)
    crop='' if z==1 else f"crop=iw/{z}:ih/{z}:min(max(iw*{cx}-iw/{z}/2\\,0)\\,iw-iw/{z}):min(max(ih*{cy}-ih/{z}/2\\,0)\\,ih-ih/{z}),"
    last = i==len(S)-1
    fc.append(f'[{ci}:v]trim={a}:{b},setpts=PTS-STARTPTS,{crop}{base}'+(f',tpad=stop_mode=clone:stop_duration={TOT-END+0.1:.2f}' if last else '')+f'[g{i}]')
    fc.append(f'[{ci}:a]atrim={a}:{b},asetpts=PTS-STARTPTS,volume={vol},afade=t=in:d=0.05,afade=t=out:st={b-a-0.06:.2f}:d=0.06[h{i}]')
    vl.append(f'[g{i}]'); al.append(f'[h{i}]')
fc.append(''.join(vl)+f'concat=n={len(S)}:v=1:a=0[v0]'); prev='v0'
for j,(n,a,b,y) in enumerate(ov):
    fc.append(f"[{prev}][{OI+j}:v]overlay=x=(W-w)/2:y={y}:enable='between(t,{a:.2f},{b:.2f})'[v{j+1}]"); prev=f'v{j+1}'
fc.append(f'[{prev}]trim=0:{TOT:.2f},format=yuv420p[vout]')
fc.append(''.join(al)+f'concat=n={len(S)}:v=0:a=1,apad=whole_dur={TOT:.2f}[amb]')
vs=[]
for i,(w,st) in enumerate(placed):
    ms=int(st*1000); fc.append(f'[{VI+i}:a]adelay={ms}|{ms}[p{i}]'); vs.append(f'[p{i}]')
if VOZ2:
    ms=int((T[2]+0.4)*1000); fc.append(f'[{VI+len(placed)}:a]adelay={ms}|{ms}[p2x]'); vs.append('[p2x]')
fc.append(f'[amb]{"".join(vs)}amix=inputs={len(vs)+1}:duration=first:normalize=0,alimiter=limit=0.95,afade=t=out:st={TOT-0.6:.2f}:d=0.6[aout]')
subprocess.run(['ffmpeg','-v','error','-y']+inp+['-filter_complex',';'.join(fc),'-map','[vout]','-map','[aout]','-c:v','libx264','-preset','slow','-crf','17','-profile:v','high','-c:a','aac','-b:a','192k','-ar','48000','-movflags','+faststart','VLOG1-v7.mp4'],check=True)
print('ok',TOT,'toma2 en',T[2])
