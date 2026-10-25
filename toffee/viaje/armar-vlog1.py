import subprocess, sys
exec(open('../d1b/armar.py').read().split('W=(255,255,255,255)')[0])
W=(255,255,255,255)
VOZ2 = 'voz2.mp3' if len(sys.argv)>1 else None   # línea de la toma 2 (pendiente)
# segmentos: (clip, ini, fin, zoom, cx, cy, vol_ambiente)
S=[('t1',0,2.0,1.0,.5,.4,0),('t1',2.0,5.0,1.18,.5,.32,0),
   ('t2',0,3.2,1.0,.5,.5,.35),('t2',3.2,6.4,1.2,.55,.55,.35),
   ('t3',0.9,4.0,1.0,.5,.4,0),('t3',4.0,7.4,1.2,.5,.33,0),
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
# voz: (ini_EL, fin_EL, clip, ini_flow, fin_flow o None)
V=[(0.00,1.00,'t1',0.15,None),(1.00,3.00,'t1',2.02,4.28),
   (3.39,7.33,'t3',1.30,6.50),
   (7.69,12.42,'t4',0.40,None),
   (12.83,15.91,'t5',2.60,None),
   (16.34,18.34,'t6',0.05,2.32),(18.74,20.40,'t6',3.12,4.42),(20.75,22.12,'t6',5.06,6.88),
   (22.50,26.18,'t7',0.40,None),
   (26.59,30.69,'t8',1.90,5.16),
   (31.24,33.22,'t9c',2.48,4.38)]
pl=[]
for a,b,c,fa,fb in V:
    d=b-a; tempo=1.0; st=seg_t(c,fa)
    if fb:
        tempo=max(0.85,min(1.25,d/(fb-fa))); st=seg_t(c,fa)+((fb-fa)-d/tempo)/2
    pl.append((a,b,tempo,st,st+d/tempo))
for p in pl: print('voz',p)
# subtítulos en inglés por línea: (lista de trozos, índices de pl que cubre)
SUB=[(["Humans!"],[0]),(["Tomorrow I'm going","to the North Pole."],[1]),
     (["And I found out","Santa never brings gifts","to street animals."],[2]),
     (["So I'm going","to ask him in person.","Every animal","deserves a gift."],[3]),
     (["Galleta's coming with me.","He just doesn't know it yet."],[4]),
     (["Our vehicle:","my sleigh."],[5]),(["Well... it's my bed."],[6]),(["But it's shaped","like a sleigh."],[7]),
     (["Tell me in the comments","which street animal","deserves a gift.","Liftoff!"],[8]),
     (["I think...","I don't know how to drive this."],[9]),
     (["And you...","who are you?"],[10])]
ov=[]
def add(name,img,a,b,y): img.save(name); ov.append((name,a,b,y))
k=0
for trozos,idx in SUB:
    a=pl[idx[0]][3]; b=pl[idx[-1]][4]; L=sum(len(x) for x in trozos); x0=a
    for tz in trozos:
        x1=x0+(b-a)*len(tz)/L
        add(f'o_s{k}.png',linea([(tz,W)],68,7),x0,x1+(0.25 if tz==trozos[-1] else 0),1430); x0=x1; k+=1
if VOZ2:
    t2a=T[2]+0.4
    for tz,a,b in [("This is Galleta.",0,1.3),("His first Christmas",1.3,2.6),("he spent shaking",2.6,3.9),("under a car.",3.9,5.0)]:
        add(f'o_s{k}.png',linea([(tz,W)],68,7),t2a+a,t2a+b,1430); k+=1
add('o_tit.png',bloque([linea([('El viaje de Toffee al ',W),('Polo Norte',CAR)],66,7),linea([('Vlog 1 ',W),('EMO','🛷')],80,8)]),0,3.2,230)
t7=seg_t('t7',0.4)
add('o_cta.png',bloque([linea([('Comenta ',W),('EMO','👇')],70,7),linea([('¿Qué animalito merece un regalo?',W)],52,6)]),t7,t7+4.3,260)
add('o_fin.png',bloque([linea([('Vlog 2 mañana ',W),('EMO','🛷')],92,9),linea([('Sígueme para ver quién es ',W),('EMO','👀')],56,6)]),END,99,330)
# --- render ---
inp=[]
clips=sorted(set(s[0] for s in S),key=lambda c:[s[0] for s in S].index(c))
for c in clips: inp+=['-i',c+'.mp4']
inp+=['-i','voz.mp3']; VI=len(clips)
if VOZ2: inp+=['-i',VOZ2]
OI=len(clips)+1+(1 if VOZ2 else 0)
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
fc.append(f'[{VI}:a]asplit={len(pl)}'+''.join(f'[vs{i}]' for i in range(len(pl))))
vs=[]
for i,(a,b,tempo,st,en) in enumerate(pl):
    ms=int(st*1000)
    fc.append(f'[vs{i}]atrim={a}:{b},asetpts=PTS-STARTPTS,atempo={tempo:.3f},afade=t=out:st={(b-a)/tempo-0.05:.2f}:d=0.05,adelay={ms}|{ms}[p{i}]'); vs.append(f'[p{i}]')
if VOZ2:
    ms=int((T[2]+0.4)*1000); fc.append(f'[{VI+1}:a]adelay={ms}|{ms}[p2x]'); vs.append('[p2x]')
fc.append(f'[amb]{"".join(vs)}amix=inputs={len(vs)+1}:duration=first:normalize=0,alimiter=limit=0.95,afade=t=out:st={TOT-0.6:.2f}:d=0.6[aout]')
subprocess.run(['ffmpeg','-v','error','-y']+inp+['-filter_complex',';'.join(fc),'-map','[vout]','-map','[aout]','-c:v','libx264','-preset','slow','-crf','17','-profile:v','high','-c:a','aac','-b:a','192k','-ar','48000','-movflags','+faststart','VLOG1.mp4'],check=True)
print('ok',TOT,'toma2 en',T[2])
