import cv2, numpy as np, subprocess, sys
L='/home/user/tienda-dropshiping/toffee/refs/extravio/lugares/'
W,H,FPS=1080,1920,30
rng=np.random.default_rng(3)
def load(n):
    im=cv2.imread(L+n).astype(np.float32)/255
    return cv2.resize(im,(W*2,H*2),interpolation=cv2.INTER_CUBIC)  # trabajar a 2x para movimiento suave
def ease(t): return t*t*(3-2*t)
def cam(img,z,cx,cy):
    # z>=1 acercamiento, centro en coords 0..1 de la imagen 2x
    h,w=img.shape[:2]; s=(W/w)*z
    M=np.float32([[s,0,W/2-s*cx*w],[0,s,H/2-s*cy*h]])
    return cv2.warpAffine(img,M,(W,H),flags=cv2.INTER_LINEAR,borderMode=cv2.BORDER_REFLECT)
p=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','bgr24','-s',f'{W}x{H}','-r',str(FPS),'-i','-',
   '-c:v','libx264','-crf','17','-preset','medium','-pix_fmt','yuv420p','video.mp4'],stdin=subprocess.PIPE)
def out(f):
    g=rng.normal(0,0.012,(H//2,W//2,1)).astype(np.float32); g=cv2.resize(g,(W,H))[...,None]
    f=np.clip(f+g,0,1); p.stdin.write((f*255).astype(np.uint8).tobytes())

# ---------- Toma 1: el mapa, raya verde de Colombia a México (7 s) ----------
A=load('AEREA-AMERICA-NOCHE.jpg'); h,w=A.shape[:2]
sx,sy=w/1116,h/2000
P0=np.array([870*sx,1235*sy]); P1=np.array([560*sx,930*sy]); P2=np.array([95*sx,690*sy])  # Cartagena -> Caribe -> centro de México
bez=lambda t:((1-t)**2)[:,None]*P0+(2*(1-t)*t)[:,None]*P1+(t**2)[:,None]*P2
pts=bez(np.linspace(0,1,600))
spark=[]
N1=7*FPS
for i in range(N1):
    t=i/N1
    prog=np.clip((t-0.12)/0.62,0,1); pe=ease(prog)
    lay=np.zeros((h,w,3),np.float32)
    k=int(pe*599)
    if k>1:
        pl=pts[:k+1].astype(np.int32).reshape(-1,1,2)
        cv2.polylines(lay,[pl],False,(0.35,1.0,0.45),10,cv2.LINE_AA)
        glow=cv2.GaussianBlur(lay,(0,0),28)*2.2
        core=np.zeros_like(lay); cv2.polylines(core,[pl],False,(0.85,1,0.9),3,cv2.LINE_AA)
        hx,hy=pts[k]
        if prog<1:
            for _ in range(4): spark.append([hx+rng.normal(0,10),hy+rng.normal(0,10),rng.normal(0,2.2),rng.normal(-1,2.2),1.0])
            cv2.circle(core,(int(hx),int(hy)),14,(0.9,1,0.95),-1,cv2.LINE_AA)
        flash=np.zeros_like(lay)
        if prog>=1:  # llegada a México: destello
            a=max(0,1-(t-0.74)/0.18)
            cv2.circle(flash,tuple(P2.astype(int)),60,(0.5,1,0.6),-1); flash=cv2.GaussianBlur(flash,(0,0),45)*3*a
        sp=np.zeros_like(lay)
        for s in spark:
            s[0]+=s[2]; s[1]+=s[3]; s[4]*=0.95
            cv2.circle(sp,(int(s[0]),int(s[1])),3,(0.6*s[4],1*s[4],0.7*s[4]),-1,cv2.LINE_AA)
        spark[:]=[s for s in spark if s[4]>0.05]
        lay=glow+core+cv2.GaussianBlur(sp,(0,0),2)*1.5+flash
    img=A*(1-np.clip(lay.max(2,keepdims=True)*0.15,0,0.3))+lay
    z=1.05+0.22*ease(t); cx=0.5+(-0.12)*ease(t); cy=0.52+(-0.12)*ease(t)
    out(np.clip(cam(img,z,cx,cy),0,1))
# ---------- Toma 2: Ciudad de México en Día de Muertos (6 s) ----------
B=load('AEREA-CDMX-NOCHE.jpg'); hb,wb=B.shape[:2]
hsv=cv2.cvtColor((B*255).astype(np.uint8),cv2.COLOR_BGR2HSV)
warm=((hsv[...,2]>170)&(hsv[...,0]<30)).astype(np.float32); warm=cv2.GaussianBlur(warm,(0,0),3)[...,None]
fields=[cv2.resize(rng.random((24,14)).astype(np.float32),(wb,hb),interpolation=cv2.INTER_CUBIC) for _ in range(6)]
emb=[[rng.uniform(0,wb),rng.uniform(hb*0.3,hb*1.1),rng.uniform(-0.6,0.6),rng.uniform(-3.5,-1.2),rng.uniform(2,5),rng.uniform(0,6.28)] for _ in range(140)]
N2=6*FPS; last=None
for i in range(N2):
    t=i/N2
    a=(i/8.0)%6; j=int(a); f=a-j
    fl=fields[j]*(1-f)+fields[(j+1)%6]*f
    img=B*(1+warm*(fl[...,None]-0.5)*0.35)
    ep=np.zeros_like(B)
    for e in emb:
        e[0]+=e[2]+0.6*np.sin(i/15+e[5]); e[1]+=e[3]
        if e[1]<-10: e[1]=hb+10
        tw=0.6+0.4*np.sin(i/5+e[5])
        cv2.circle(ep,(int(e[0]),int(e[1])),int(e[4]),(0.25*tw,0.6*tw,1.0*tw),-1,cv2.LINE_AA)
    img=img+cv2.GaussianBlur(ep,(0,0),3)*0.9
    z=1.0+0.18*ease(t); cy=0.5+0.06*ease(t)
    fr=np.clip(cam(img,z,0.5,cy),0,1)
    if i<12 and last is not None: pass
    out(fr)
p.stdin.close(); p.wait()
