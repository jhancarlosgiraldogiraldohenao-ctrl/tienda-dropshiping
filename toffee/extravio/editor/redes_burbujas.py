# Burbujas redondeadas de redes sociales (YouTube, TikTok, Instagram) para el final de los videos.
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os
R='/home/user/tienda-dropshiping/toffee/extravio/editor'
F=R+'/datos-dizzy01/fonts/Montserrat.ttf'
OUT=R+'/redes/'
NOMBRE='El Dizzy'; USUARIO='@el_dizzy_vlogs'
K=4  # supermuestreo
def fuente(t,peso):
    f=ImageFont.truetype(F,t*K)
    try: f.set_variation_by_name(peso)
    except Exception: pass
    return f
def logo_youtube(s):
    im=Image.new('RGBA',(s,s),(0,0,0,0)); d=ImageDraw.Draw(im)
    w,h=int(s*.96),int(s*.68); x0=(s-w)//2; y0=(s-h)//2
    d.rounded_rectangle((x0,y0,x0+w,y0+h),radius=int(h*.28),fill=(255,0,0))
    cx,cy=s//2+int(s*.03),s//2; t=int(h*.26)
    d.polygon([(cx-t,cy-t),(cx-t,cy+t),(cx+int(t*1.1),cy)],fill='white'); return im
def nota(d,ox,oy,s,c):
    u=s/100
    d.rounded_rectangle((ox+48*u,oy+14*u,ox+62*u,oy+70*u),radius=3*u,fill=c)      # tallo
    d.ellipse((ox+22*u,oy+50*u,ox+56*u,oy+84*u),outline=c,width=int(13*u))      # bolita
    d.pieslice((ox+48*u,oy+-6*u,ox+92*u,oy+38*u),90,180,fill=c)                  # bandera
    d.pieslice((ox+62*u,oy+8*u,ox+80*u,oy+24*u),90,180,fill=(0,0,0))
def logo_tiktok(s):
    im=Image.new('RGBA',(s,s),(0,0,0,0)); d=ImageDraw.Draw(im)
    d.rounded_rectangle((0,0,s,s),radius=int(s*.24),fill=(0,0,0))
    m=int(s*.12); n=s-2*m
    nota(d,m-int(s*.035),m-int(s*.035),n,(37,244,238)); nota(d,m+int(s*.035),m+int(s*.035),n,(254,44,85)); nota(d,m,m,n,(255,255,255))
    return im
def logo_instagram(s):
    g=Image.new('RGBA',(s,s)); px=g.load()
    cs=[(254,218,117),(250,126,30),(214,41,118),(150,47,191),(79,91,213)]
    for y in range(s):
        for x in range(s):
            t=min(.999,max(0,(x*.4+(s-y)*.6)/s)); t=1-t
            i=int(t*(len(cs)-1)); f=t*(len(cs)-1)-i; a,b=cs[i],cs[i+1]
            px[x,y]=tuple(int(a[j]+(b[j]-a[j])*f) for j in range(3))+(255,)
    m=Image.new('L',(s,s),0); ImageDraw.Draw(m).rounded_rectangle((0,0,s,s),radius=int(s*.28),fill=255)
    im=Image.new('RGBA',(s,s),(0,0,0,0)); im.paste(g,(0,0),m); d=ImageDraw.Draw(im); w=int(s*.075)
    d.rounded_rectangle((s*.2,s*.2,s*.8,s*.8),radius=int(s*.18),outline='white',width=w)
    d.ellipse((s*.35,s*.35,s*.65,s*.65),outline='white',width=w)
    d.ellipse((s*.66,s*.27,s*.74,s*.35),fill='white'); return im
def burbuja(logo,red,archivo):
    W,H=640,116; P=24
    im=Image.new('RGBA',((W+2*P)*K,(H+2*P)*K),(0,0,0,0))
    sh=Image.new('L',im.size,0); ImageDraw.Draw(sh).rounded_rectangle((P*K,(P+6)*K,(P+W)*K,(P+H+6)*K),radius=H*K//2,fill=120)
    im.paste((0,0,0,255),(0,0),sh.filter(ImageFilter.GaussianBlur(10*K)))
    d=ImageDraw.Draw(im); d.rounded_rectangle((P*K,P*K,(P+W)*K,(P+H)*K),radius=H*K//2,fill=(255,255,255,245))
    L=84*K; lg=logo(L); im.alpha_composite(lg,((P+16)*K,(P*K+(H*K-L)//2)))
    x=(P+16+84+22)*K
    d.text((x,(P+20)*K),NOMBRE,font=fuente(38,'Bold'),fill=(20,20,20))
    d.text((x,(P+64)*K),USUARIO+'  ·  '+red,font=fuente(27,'Medium'),fill=(110,110,110))
    im.resize((W+2*P,H+2*P),Image.LANCZOS).save(OUT+archivo)
burbuja(logo_youtube,'YouTube','RED-YOUTUBE.png')
burbuja(logo_tiktok,'TikTok','RED-TIKTOK.png')
burbuja(logo_instagram,'Instagram','RED-INSTAGRAM.png')
print('ok')
