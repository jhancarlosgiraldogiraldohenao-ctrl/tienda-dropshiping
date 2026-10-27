# Editor de episodios de Toffee (ffmpeg + Pillow). Reglas: la voz se corta SOLO en silencios (se comprueba),
# nunca se estira; cada frase arranca cuando la boca de la toma de Flow empieza a moverse.
import subprocess as sp, numpy as np, os
from PIL import Image, ImageDraw, ImageFont
FB='/usr/share/fonts/opentype/inter/InterDisplay-Bold.otf'; EMO='/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf'
NAVY=(22,33,62,255); CAR=(224,149,79,255); W=(255,255,255,255)
def emoji_img(ch,h):
    ef=ImageFont.truetype(EMO,109); im=Image.new('RGBA',(200,200),(0,0,0,0))
    ImageDraw.Draw(im).text((0,0),ch,font=ef,embedded_color=True); im=im.crop(im.getbbox())
    return im.resize((int(im.width*h/im.height),h),Image.LANCZOS)
def linea(partes,size,stroke):
    f=ImageFont.truetype(FB,size); d0=ImageDraw.Draw(Image.new('RGBA',(5,5))); asc,desc=f.getmetrics(); H=asc+desc+stroke*2+8
    pz=[];Wd=0
    for p in partes:
        if p[0]=='EMO': e=emoji_img(p[1],int(size*0.95)); pz.append(('i',e)); Wd+=e.width+10
        else: w=int(d0.textlength(p[0],font=f))+stroke*2; pz.append(('t',p,w)); Wd+=w
    im=Image.new('RGBA',(Wd+10,H),(0,0,0,0)); d=ImageDraw.Draw(im); x=5
    for q in pz:
        if q[0]=='i': im.alpha_composite(q[1],(x+5,(H-q[1].height)//2)); x+=q[1].width+10
        else: t,c=q[1]; d.text((x+stroke,stroke+4),t,font=f,fill=c,stroke_width=stroke,stroke_fill=NAVY); x+=q[2]
    return im
def bloque(ls,gap=6):
    Wd=max(l.width for l in ls); H=sum(l.height for l in ls)+gap*(len(ls)-1); im=Image.new('RGBA',(Wd,H),(0,0,0,0)); y=0
    for l in ls: im.alpha_composite(l,((Wd-l.width)//2,y)); y+=l.height+gap
    return im
_pcm={}
def nivel(src,t):
    if src not in _pcm: _pcm[src]=np.frombuffer(sp.run(['ffmpeg','-v','error','-i',src,'-ac','1','-ar','16000','-f','s16le','-'],capture_output=True).stdout,np.int16).astype(np.float32)
    a=_pcm[src]; i=int(t*16000); w=a[max(i-240,0):i+240]
    return 20*np.log10(np.sqrt((w**2).mean())+1e-9) if len(w) else -99

def armar(S, VO, SUB_KEY, titulo, cierre, out, workdir, fin_extra=3.0):
    """S: [(clip, ini, fin, zoom, cx, cy, vol)]; VO: [(src, corte_ini, corte_fin, voz_ini, clip, boca_ini o None, desfase_vo, subtitulo)]"""
    os.chdir(workdir)
    T=[];t=0
    for s in S: T.append(t); t+=s[2]-s[1]
    END=t; TOT=END+fin_extra
    def seg_t(c,x):
        for i,s in enumerate(S):
            if s[0]==c and s[1]-1e-6<=x<s[2]+1e-6: return T[i]+x-s[1]
        raise ValueError((c,x))
    for v in VO:
        for tt in (v[1],v[2]):
            assert nivel(v[0],tt)<20, f'CORTE CON SONIDO {v[0]} {tt}: {nivel(v[0],tt):.0f} dB'
    VO=sorted(VO,key=lambda v: seg_t(v[4], v[5] if v[5] is not None else v[6]))
    placed=[];subs=[];last=-1
    for n,(src,cs,ce,von,c,boca,off,txt) in enumerate(VO):
        onset=seg_t(c,boca) if boca is not None else seg_t(c,off)+(von-cs)
        st=onset-(von-cs)
        if st<last: onset+=last-st; st=last
        d=ce-cs; last=st+d
        f=f'_v{n}.wav'
        sp.run(['ffmpeg','-v','error','-y','-i',src,'-af',f'atrim={cs}:{ce},asetpts=PTS-STARTPTS,afade=t=in:d=0.005,afade=t=out:st={d-0.006:.3f}:d=0.005','-ar','48000',f],check=True)
        placed.append((f,st)); vd=d-(von-cs)
        ps=txt.split('|'); L=sum(len(p) for p in ps); x0=onset
        for p in ps:
            x1=x0+vd*len(p)/L; subs.append((p.strip(),x0,x1)); x0=x1
    ov=[]
    def add(name,img,a,b,y): img.save(name); ov.append((name,a,b,y))
    for k,(p,a0,b0) in enumerate(subs):
        nxt=subs[k+1][1] if k+1<len(subs) else 1e9
        b0=min(nxt,b0+0.35) if nxt-b0<0.6 else b0+0.2
        ws=p.split(' '); parts=[(w+(' ' if j<len(ws)-1 else ''),CAR if w.strip('¡!¿?.,:…').lower() in SUB_KEY else W) for j,w in enumerate(ws)]
        add(f'_s{k}.png',linea(parts,76,8),a0,b0,1400)
    add('_tit.png',titulo,0,3.2,230)
    add('_fin.png',cierre,END,99,330)
    clips=list(dict.fromkeys(s[0] for s in S))
    inp=[]
    for c in clips: inp+=['-i',c]
    VI=len(clips)
    for f,_ in placed: inp+=['-i',f]
    OI=VI+len(placed)
    for o in ov: inp+=['-i',o[0]]
    base='scale=1080:1920:flags=lanczos,hqdn3d=1.5:1.5:3:3,unsharp=5:5:0.7:5:5:0,setsar=1,fps=24'
    fc=[];vl=[];al=[]
    for i,(c,a,b,z,cx,cy,vol) in enumerate(S):
        ci=clips.index(c)
        crop='' if z==1 else f"crop=iw/{z}:ih/{z}:min(max(iw*{cx}-iw/{z}/2\\,0)\\,iw-iw/{z}):min(max(ih*{cy}-ih/{z}/2\\,0)\\,ih-ih/{z}),"
        last_=i==len(S)-1
        fc.append(f'[{ci}:v]trim={a}:{b},setpts=PTS-STARTPTS,{crop}{base}'+(f',tpad=stop_mode=clone:stop_duration={TOT-END+0.1:.2f}' if last_ else '')+f'[g{i}]')
        fc.append(f'[{ci}:a]atrim={a}:{b},asetpts=PTS-STARTPTS,volume={vol},afade=t=in:d=0.05,afade=t=out:st={b-a-0.06:.2f}:d=0.06[h{i}]')
        vl.append(f'[g{i}]'); al.append(f'[h{i}]')
    fc.append(''.join(vl)+f'concat=n={len(S)}:v=1:a=0[v0]'); prev='v0'
    for j,(n,a,b,y) in enumerate(ov):
        fc.append(f"[{prev}][{OI+j}:v]overlay=x=(W-w)/2:y={y}:enable='between(t,{a:.2f},{b:.2f})'[v{j+1}]"); prev=f'v{j+1}'
    fc.append(f'[{prev}]trim=0:{TOT:.2f},format=yuv420p[vout]')
    fc.append(''.join(al)+f'concat=n={len(S)}:v=0:a=1,apad=whole_dur={TOT:.2f}[amb]')
    vs=[]
    for i,(f,st) in enumerate(placed):
        ms=int(st*1000); fc.append(f'[{VI+i}:a]adelay={ms}|{ms}[p{i}]'); vs.append(f'[p{i}]')
    fc.append(f'[amb]{"".join(vs)}amix=inputs={len(vs)+1}:duration=first:normalize=0,alimiter=limit=0.95,afade=t=out:st={TOT-0.6:.2f}:d=0.6[aout]')
    sp.run(['ffmpeg','-v','error','-y']+inp+['-filter_complex',';'.join(fc),'-map','[vout]','-map','[aout]','-c:v','libx264','-preset','slow','-crf','17','-profile:v','high','-c:a','aac','-b:a','192k','-ar','48000','-movflags','+faststart',out],check=True)
    return TOT
