import subprocess, sys
exec(open('../d1b/armar.py').read().split('W=(255,255,255,255)')[0])
W=(255,255,255,255)
VOZ2 = 'voz2.mp3' if len(sys.argv)>1 else None   # línea de la toma 2 (pendiente)
# segmentos: (clip, ini, fin, zoom, cx, cy, vol_ambiente)
S=[('t1',0,2.0,1.0,.5,.4,0),('t1',2.0,5.0,1.18,.5,.32,0),
   ('t2',0,3.2,1.0,.5,.5,.35),('t2',3.2,6.4,1.2,.55,.55,.35),
   ('t3',0.6,4.0,1.0,.5,.4,0),('t3',4.0,7.4,1.2,.5,.33,0),
   ('t4',0,6.0,1.0,.5,.5,.35),
   ('t5',0,4.0,1.0,.5,.5,.35),('t5',4.0,8.0,1.15,.7,.6,.35),
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
import json
WJ=json.load(open('words.json')); EW=WJ['voz']
def ew(i0,i1): return EW[i0:i1]
# líneas: (índices de palabras EL [i0,i1), clip, desfase voz-en-off o None si habla en cámara)
LN=[((0,7),'t1',None),((7,23),'t3',None),((23,36),'t4',0.4),((36,43),'t5',2.6),((43,56),'t6',None),
    ((56,69),'t7',0.4),((69,75),'t8',None),((75,79),'t9c',None)]
import subprocess as sp
subtxt=[]
CH={
 't1':[(0.06,0.60,0.97,1.54,'¡Humanos!'),(1.16,2.92,2.12,4.08,'Mañana me voy al |Polo Norte.')],
 't3':[(3.41,3.96,1.28,2.04,'Y me enteré'),(3.96,4.58,2.46,3.26,'de que |Santa'),(4.58,5.12,3.46,4.04,'nunca'),(5.12,7.30,4.20,6.37,'les trae |regalos|a los |animales|de la calle.')],
 't6':[(16.35,17.25,0.13,1.11,'Nuestro vehículo:'),(17.62,18.19,1.53,2.15,'mi |trineo.'),(18.89,19.19,3.13,3.37,'Bueno…'),(19.75,20.31,3.87,4.44,'es mi cama.'),(20.75,22.12,5.19,6.79,'Pero tiene forma |de |trineo.')],
 't8':[(27.95,28.72,2.25,3.27,'Creo que…'),(29.32,30.66,3.80,5.30,'no sé |manejar esto.')],
 't9c':[(31.24,31.87,3.00,3.58,'¿Y tú…'),(32.38,32.82,3.90,4.37,'quién eres?')]}
placed=[]   # (wav, inicio en línea de tiempo)
subw_chunks=[]
subw=[]     # (palabra, ini, fin) en línea de tiempo
for n,((i0,i1),c,off) in enumerate(LN):
    E=EW[i0:i1]; out=f'l{n}.wav'
    if off is None:
        fl=[]; 
        for j,(ea,eb,fa,fb,txt) in enumerate(CH[c]):
            tp=max(0.75,min(1.3,(eb-ea)/(fb-fa))); d=(eb-ea)/tp
            ms=int((seg_t(c,fa)-seg_t(c,CH[c][0][2]))*1000)
            fl.append(f'[0:a]atrim={ea}:{eb},asetpts=PTS-STARTPTS,atempo={tp:.4f},afade=t=in:d=0.01,afade=t=out:st={d-0.03:.3f}:d=0.03,adelay={ms}|{ms}[q{j}]')
            subtxt.append((txt,seg_t(c,fa),seg_t(c,fa)+d))
        fl.append(''.join(f'[q{j}]' for j in range(len(CH[c])))+f'amix=inputs={len(CH[c])}:normalize=0[o]')
        sp.run(['ffmpeg','-v','error','-y','-i','voz.mp3','-filter_complex',';'.join(fl),'-map','[o]','-ar','48000',out],check=True)
        placed.append((out,seg_t(c,CH[c][0][2])))
    else:
        st=seg_t(c,off); a0=E[0][1]; b0=E[-1][2]+0.1
        sp.run(['ffmpeg','-v','error','-y','-i','voz.mp3','-af',f'atrim={a0}:{b0},asetpts=PTS-STARTPTS,afade=t=out:st={b0-a0-0.05:.2f}:d=0.05','-ar','48000',out],check=True)
        for k,w in enumerate(E):
            subw.append((w[0],st+w[1]-a0,st+(E[k+1][1] if k+1<len(E) else w[2])-a0))
        placed.append((out,st))
for txt,a0,b0 in subtxt:
    ps=[p for p in txt.split('|')]; L=sum(len(p) for p in ps); x0=a0
    for p in ps:
        x1=x0+(b0-a0)*len(p)/L; subw_chunks.append((p.strip(),x0,x1)); x0=x1
# subtítulos en español: grupos de 1-3 palabras, cortando en puntuación
KEY={'polo','norte','santa','regalo','regalos','galleta','trineo','animales','animalito','despegamos'}
FIX={'¡Humanos!':'¡Humanos!','Norte.':'Norte.','que':'que'}
ov=[]
def add(name,img,a,b,y): img.save(name); ov.append((name,a,b,y))
grp=[];k=0
def flush():
    global grp,k
    if not grp: return
    parts=[]
    for i,(w,a,b) in enumerate(grp):
        base=w.strip('¡!¿?.,:…').lower()
        parts.append((w+(' ' if i<len(grp)-1 else ''), CAR if base in KEY else W))
    add(f'o_s{k}.png',linea(parts,76,8),grp[0][1],grp[-1][2]+0.05,1400); k+=1; grp=[]
for i,(w,a,b) in enumerate(subw):
    grp.append((w,a,b))
    nxt=subw[i+1][1] if i+1<len(subw) else None
    if len(grp)==3 or w[-1] in '.,!?:' or nxt is None or nxt-b>0.35: flush()
flush()
for p,a0,b0 in subw_chunks:
    parts=[]
    for i,w in enumerate(p.split(' ')):
        base=w.strip('¡!¿?.,:…').lower(); parts.append((w+(' ' if i<len(p.split(' '))-1 else ''),CAR if base in KEY else W))
    add(f'o_s{k}.png',linea(parts,76,8),a0,b0+0.05,1400); k+=1
# cerrar huecos pequeños entre grupos para que no parpadee
ov.sort(key=lambda o:o[1])
for j in range(len(ov)-1):
    if 0<ov[j+1][1]-ov[j][2]<0.25: ov[j]=(ov[j][0],ov[j][1],ov[j+1][1],ov[j][3])
if VOZ2:
    pass
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
subprocess.run(['ffmpeg','-v','error','-y']+inp+['-filter_complex',';'.join(fc),'-map','[vout]','-map','[aout]','-c:v','libx264','-preset','slow','-crf','17','-profile:v','high','-c:a','aac','-b:a','192k','-ar','48000','-movflags','+faststart','VLOG1-v3.mp4'],check=True)
print('ok',TOT,'toma2 en',T[2])
