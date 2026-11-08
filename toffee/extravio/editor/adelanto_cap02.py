import subprocess as sp, os, json
R='/home/user/tienda-dropshiping/toffee/extravio'
TK=R+'/serie/tomas-cap02/'; VZ=R+'/serie/voces-cap02/p1/'; SN=R+'/sonidos/'
FONTS=R+'/editor/datos-dizzy01/fonts'
OUT='/home/user/tienda-dropshiping/toffee/videos-editados/EXTRAVIO-DIZZY-CAP02-ADELANTO.mp4'
def run(a): sp.run(a,check=True)
# 1) video: T13 (1.0-3.4) + T23 (0-7.04) + T24 (0.6-4.03) + T14 (0-5.0) con título
segs=[('T13',1.0,3.4),('T23',0.0,7.04),('T24',0.6,4.03),('T14',0.0,5.0),('CTA',0.0,8.0)]
parts=[]
for i,(t,a,b) in enumerate(segs):
    o=f'v{i}.mp4'
    run(['ffmpeg','-v','error','-y','-ss',str(a),'-to',str(b),'-i',TK+t+'.mp4','-an','-vf','scale=1080:1920:flags=lanczos,fps=30,format=yuv420p','-c:v','libx264','-crf','16','-preset','fast',o]); parts.append((o,b-a))
open('l.txt','w').write(''.join(f"file '{p}'\n" for p,_ in parts))
run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i','l.txt','-c','copy','video.mp4'])
st=[0]; 
for _,d in parts: st.append(st[-1]+d)
T13,T23,T24,T14,CTA=st[0],st[1],st[2],st[3],st[4]; TOT=st[5]
# 2) voces (piezas: archivo, desde, hasta, momento en el video)
V=[('T13',0.0,2.2, T13+0.15),
   ('T23',0.0,3.3, T23+1.72),('T23',3.4,4.9, T23+5.55),
   ('T24',0.0,0.85,T24+(1.28-0.6)-0.11),('T24',0.9,3.08,T24+(1.8-0.6)-0.98+0.9),
   # CTA: voz medida contra la boca (frases enteras, sin estirar)
   ('CTA',0.0,3.40,CTA+0.30),('CTA',3.42,5.98,CTA+3.50),('CTA',6.04,7.0,CTA+5.98)]
inp=[]; flt=[]; k=0
for f,a,b,at in V:
    inp+=['-i',VZ+f+'.mp3']; flt.append(f'[{k}:a]atrim={a}:{b},asetpts=N/SR/TB,adelay={int(at*1000)}|{int(at*1000)},volume=1.0[v{k}]'); k+=1
inp+=['-stream_loop','-1','-i',SN+'musica/M6-cuca-saxofon.mp3']; flt.append(f'[{k}:a]atrim=0:{T14},afade=t=in:st={T23}:d=0.4,afade=t=out:st={T14-0.6}:d=0.6,volume=0.22[m1]'); k+=1
inp+=['-i',SN+'musica/M12b-mariachi-muertos-metales.mp3']; flt.append(f'[{k}:a]atrim=0:{TOT-T14+0.5},adelay={int((T14-0.3)*1000)}|{int((T14-0.3)*1000)},afade=t=in:st={T14-0.3}:d=0.3,afade=t=out:st={TOT-1.2}:d=1.2,volume=\'if(gte(t,{CTA}),0.28,0.5)\':eval=frame[m2]'); k+=1
inp+=['-i',SN+'efectos/E33-viaje-magico.mp3']; flt.append(f'[{k}:a]volume=0.5[e1]'); k+=1
inp+=['-i',SN+'efectos/E29-huesos-catrina.mp3']; flt.append(f'[{k}:a]adelay={int((T24+0.2)*1000)}|{int((T24+0.2)*1000)},volume=0.7[e2]'); k+=1
inp+=['-i',SN+'ambientes/E25-ambiente-muertos-noche.mp3']; flt.append(f'[{k}:a]atrim=0:{TOT},volume=0.35[amb]'); k+=1
mix=''.join(f'[v{i}]' for i in range(len(V)))+'[m1][m2][e1][e2][amb]'
flt.append(f'{mix}amix=inputs={len(V)+5}:normalize=0,atrim=0:{TOT},loudnorm=I=-14:TP=-1.5[a]')
run(['ffmpeg','-v','error','-y']+inp+['-filter_complex',';'.join(flt),'-map','[a]','-ar','48000','-ac','2','audio.wav'])
# 3) subtítulos (palabras clave en rojo), y=1400
SUBY=900  # altura de los subtítulos, como Gnomo Palomo (46 % del alto)
def t(s): h=int(s//3600); m=int(s%3600//60); return f'{h}:{m:02d}:{s%60:05.2f}'
R_='{\\c&H3B3BFF&}'; W_='{\\c&HFFFFFF&}'
subs=[(T23+1.75,T23+2.6,'¡Mamacita!'),(T23+2.6,T23+3.6,'No me importa'),(T23+3.6,T23+4.9,'que seas '+R_+'puro hueso'+W_),
      (T23+5.55,T23+7.0,'Me gustan '+R_+'flaquitas'+W_),
      (T24+0.6,T24+1.2,'¡Ay!'),(T24+1.2,T24+2.3,'¡Qué '+R_+'marrano'+W_),(T24+2.3,T24+3.4,'tan atrevido!'),
      (CTA+0.3,CTA+1.4,'El '+R_+'vlog uno'+W_),(CTA+1.4,CTA+2.04,'ya está completo'),(CTA+2.04,CTA+2.86,'en '+R_+'YouTube'+W_),(CTA+2.86,CTA+3.6,'mis ratas'),
      (CTA+3.6,CTA+4.44,'Corran a verlo'),(CTA+4.44,CTA+5.4,'que esto apenas'),(CTA+5.4,CTA+6.0,'empieza'),(CTA+6.0,CTA+6.7,'mi llave')]
ass=('[Script Info]\nScriptType: v4.00+\nPlayResX: 1080\nPlayResY: 1920\n\n[V4+ Styles]\n'
 'Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding\n'
 'Style: Sub,Montserrat,62,&H00FFFFFF,&H00FFFFFF,&H00000000,&H80000000,-1,0,0,0,100,100,0,0,1,4,3,5,60,60,0,1\n'
 'Style: Tit,Montserrat,84,&H00FFFFFF,&H00FFFFFF,&H00000000,&H80000000,-1,0,0,0,100,100,6,0,1,5,3,5,60,60,0,1\n\n'
 '[Events]\nFormat: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n')
for a,b,x in subs: ass+=f'Dialogue: 0,{t(a)},{t(b)},Sub,,0,0,0,,{{\\pos(540,{SUBY})}}{x}\n'
ass+=f'Dialogue: 1,{t(T14+1.4)},{t(CTA)},Tit,,0,0,0,,{{\\pos(540,560)\\fad(300,0)}}EXTRAVÍO · VLOG 02\\N{{\\fs60\\c&H3B3BFF&}}MUY PRONTO\n'
ass+=f'Dialogue: 1,{t(CTA+3.4)},{t(TOT)},Sub,,0,0,0,,{{\\pos(540,1335)\\fad(250,0)}}Sígueme en '+R_+'YouTube'+W_+' y en mis redes\n'
open('subs.ass','w').write(ass)
# 4) burbujas de redes (aparecen una por una, suben y se funden)
RD=R+'/editor/redes/'
B=[('RED-YOUTUBE.png',CTA+3.7,1385),('RED-TIKTOK.png',CTA+3.95,1525),('RED-INSTAGRAM.png',CTA+4.2,1665)]
inp=['-i','video.mp4','-i','audio.wav']; fc=[f'[0:v]ass=subs.ass:fontsdir={FONTS}[b0]']
for i,(png,t0,y) in enumerate(B):
    inp+=['-loop','1','-t',str(TOT),'-i',RD+png]
    fc.append(f'[{i+2}:v]format=rgba,fade=t=in:st={t0}:d=0.3:alpha=1[p{i}]')
    fc.append(f"[b{i}][p{i}]overlay=x=196:y='{y}+40*max(0,1-(t-{t0})/0.3)':enable='gte(t,{t0})'[b{i+1}]")
run(['ffmpeg','-v','error','-y']+inp+['-filter_complex',';'.join(fc),'-map',f'[b{len(B)}]','-map','1:a','-c:v','libx264','-crf','18','-preset','medium','-c:a','aac','-b:a','192k','-shortest','-movflags','+faststart',OUT])
print('ok',round(TOT,2))
