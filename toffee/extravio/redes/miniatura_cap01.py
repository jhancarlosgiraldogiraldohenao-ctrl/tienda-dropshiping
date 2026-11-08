from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
import numpy as np
S='/tmp/claude-0/-home-user-tienda-dropshiping/776902c0-3e05-5e98-b1fb-d8ea92e4cfc1/scratchpad/mini/'
W,H=1280,720
bg=Image.open('lugares/horizontal/HUECO-RINCON-TUERTO.jpg').convert('RGB').resize((W,int(768*W/1376)))
bg=bg.crop((0,0,W,H)).filter(ImageFilter.GaussianBlur(3))
bg=ImageEnhance.Brightness(bg).enhance(0.75)
# red vignette glow on right
g=Image.new('RGB',(W,H),(200,20,20)); m=Image.new('L',(W,H),0); d=ImageDraw.Draw(m)
d.ellipse((620,-100,1500,820),fill=110); m=m.filter(ImageFilter.GaussianBlur(120))
bg=Image.composite(g,bg,m)
def limpia(p):
    a=np.array(p).astype(int); r,gg,b,al=a[...,0],a[...,1],a[...,2],a[...,3]
    mx=np.maximum(np.maximum(r,gg),b); mn=np.minimum(np.minimum(r,gg),b)
    gris=(mx>175)&(mx-mn<18); h=a.shape[0]; gris[int(h*.45):]=False
    al[gris]=0; a[...,3]=al
    return Image.fromarray(a.astype(np.uint8)).filter(ImageFilter.SMOOTH)
def pon(img,f,box,esc,x,y,flip=False,sombra=True):
    p=Image.open(S+f).crop(box)
    pass
    if flip: p=p.transpose(Image.FLIP_LEFT_RIGHT)
    p=p.resize((int(p.width*esc),int(p.height*esc)),Image.LANCZOS)
    if sombra:
        a=p.split()[3]; gl=Image.new('RGBA',p.size,(0,0,0,0)); gl.putalpha(a.filter(ImageFilter.GaussianBlur(18)).point(lambda v:int(v*.9)))
        img.paste(Image.new('RGB',p.size,(0,0,0)),(x+8,y+8),gl.split()[3])
    img.paste(p,(x,y),p)
img=bg.copy()
pon(img,'tuerto.png',(250,80,880,700),1.25,560,-20,flip=True)   # Tuerto right, big, looking left
pon(img,'dizzy.png',(250,40,780,620),1.12,30,130)                 # Dizzy left, front
d=ImageDraw.Draw(img)
F='/home/user/tienda-dropshiping/toffee/extravio/editor/datos-dizzy01/fonts/Montserrat.ttf'
f=ImageFont.truetype(F,128)
try: f.set_variation_by_name('Black')
except Exception: pass
t='¿TRAMPA?'
tw=d.textlength(t,font=f); x=(W-tw)/2+40
d.text((x,18),t,font=f,fill=(255,214,0),stroke_width=10,stroke_fill=(0,0,0))
img.save(S+'MINIATURA-CAP01.jpg',quality=95)
