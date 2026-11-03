import os, re, glob, shutil, subprocess, hashlib, unicodedata
import numpy as np
from faster_whisper import WhisperModel
U='/root/.claude/uploads/c684127a-90fa-5e05-b748-57ecc9507198'; S='/tmp/claude-0/-home-user-tienda-dropshiping/c684127a-90fa-5e05-b748-57ecc9507198/scratchpad'
R='/home/user/tienda-dropshiping/toffee/refs'; OUT=f'{S}/pack/EXTRAVIO-RECURSOS'
shutil.rmtree(OUT, ignore_errors=True)
def slug(t, n=60):
    t=unicodedata.normalize('NFD',t); t=''.join(c for c in t if unicodedata.category(c)!='Mn')
    t=re.sub(r'[^A-Za-z0-9 ]','',t).strip(); return re.sub(r'\s+','-',t)[:n].strip('-') or 'sin-texto'
def mp3(src, dst):
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    if src.endswith('.mp3'): shutil.copy(src, dst)
    else: subprocess.run(['ffmpeg','-v','error','-y','-i',src,'-vn','-c:a','libmp3lame','-b:a','192k',dst],check=True)
seen=set(); idx=[]
def md5(f): return hashlib.md5(open(f,'rb').read()).hexdigest()
# 1. imágenes
for sub in ['personajes','objetos','mundos','marca']:
    for f in sorted(glob.glob(f'{R}/extravio/{sub}/*.jpg')):
        d=f'{OUT}/1-IMAGENES/{sub}/{os.path.basename(f)}'; os.makedirs(os.path.dirname(d),exist_ok=True); shutil.copy(f,d); idx.append(('1-IMAGENES/'+sub, os.path.basename(f), ''))
for f in ['TOFFEE-viajero.jpg','GALLETA-viajero.jpg','TOFFEE-ficha.jpg','GALLETA-oficial.jpg']:
    d=f'{OUT}/1-IMAGENES/personajes/{f}'; shutil.copy(f'{R}/{f}',d); idx.append(('1-IMAGENES/personajes', f, 'referencia principal' if 'viajero' in f else ''))
for f in sorted(glob.glob(f'{R}/personajes/*')):
    d=f'{OUT}/1-IMAGENES/personajes-viejos/{os.path.basename(f)}'; os.makedirs(os.path.dirname(d),exist_ok=True); shutil.copy(f,d); idx.append(('1-IMAGENES/personajes-viejos', os.path.basename(f), 'del viaje al Polo Norte'))
# 2. voces
m=WhisperModel("small",device="cpu",compute_type="int8")
voces=sorted(glob.glob(f'{U}/*ElevenLabs_*_gen_*.mp3'))+[f'{R}/extravio/voces/voz_lucho_1.mp3',f'{R}/extravio/voces/voz_toffee_1.mp3']
VN={'toffee':'TOFFEE','lucho_el_raton':'LUCHO','Do_a_lechuza':'DONA-LECHUZA'}
for f in voces:
    h=md5(f)
    if h in seen: continue
    seen.add(h); b=os.path.basename(f)
    who=next((v for k,v in VN.items() if f'_{k}_gen' in b), 'LUCHO' if 'lucho' in b else 'TOFFEE')
    ts=re.search(r'(\d{4}-\d\d-\d\d)T(\d\d_\d\d_\d\d)',b); stamp=f"{ts.group(1)}_{ts.group(2)}" if ts else 'molde'
    a=np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i',f,'-ac','1','-ar','16000','-f','f32le','-'],capture_output=True).stdout,np.float32)
    txt=' '.join(s.text.strip() for s in m.transcribe(a,language='es')[0])
    name=f'{stamp}__{slug(txt)}.mp3'; mp3(f, f'{OUT}/2-VOCES/{who}/{name}'); idx.append((f'2-VOCES/{who}', name, txt))
# 3. efectos
FX={'Fast_cinematic':'whoosh transiciones y caidas','Body_falling':'caida en pelotas de plastico','Short_comedic_orches':'golpe de chiste','Vinyl_record':'rayon de disco','Short_sad_comedic':'wah wah triste (fracaso)',
    'Small_rubber_squeaky':'pelota que rebota y chilla','Cute_curious':'pop de curiosidad','Cinematic_tension':'subida de tension','Giant_moth':'alas gigantes (Polilla)','Slow_tense_heartbeat':'latido',
    'Small_animal_paws':'pasitos de patas','Magical_shimmering':'brillo magico','Metal_rolling_shutte':'cortina de metal','Short_whimsical_myst':'remate final de episodio'}
for f in sorted(glob.glob(f'{U}/*-17935*.mp3')):
    h=md5(f)
    if h in seen: continue
    seen.add(h); b=os.path.basename(f); k=next(k for k in FX if k in b); name=slug(FX[k])+'.mp3'
    n=2
    while os.path.exists(f'{OUT}/3-EFECTOS/{name}'): name=slug(FX[k])+f'-{n}.mp3'; n+=1
    mp3(f, f'{OUT}/3-EFECTOS/{name}'); idx.append(('3-EFECTOS', name, FX[k]))
AMB={'MAR.wav':'Mar de Pelotas (olas de pelotas)','NOCHE.wav':'ciudad de noche','AZOTEA.wav':'azotea de noche','CALLE_LLUVIA.wav':'calle con lluvia (casa de Toffee)'}
for k,v in AMB.items():
    name=slug(v)+'.mp3'; mp3(f'{S}/piloto/sfx/{k}', f'{OUT}/3-EFECTOS/ambientes/{name}'); idx.append(('3-EFECTOS/ambientes', name, v))
f=glob.glob(f'{U}/*Dusk_at_the_Market_Lane*')[0]; mp3(f, f'{OUT}/3-EFECTOS/ambientes/Ciudad-de-Extravio-mercado-al-atardecer.mp3'); idx.append(('3-EFECTOS/ambientes','Ciudad-de-Extravio-mercado-al-atardecer.mp3','calle y mercado de la ciudad'))
# 4. música
MU={'Key_of_the_Veil':'LOGO de EXTRAVIO (firma, primeros 4 s)','Mapmakers_Charm':'Tema de Extravio (casa, llegada, ciudad)','Comic_Pursuit':'Persecucion comica','Clockwork_Citadel':'Suspenso de noche',
    'Curious_Light':'Misterio (alcantarilla, recuerdos)','Chase_Through_the_Ruins':'Persecucion de noche (accion)','Memory_of_the_Leash':'Momento tierno (Galleta, MAX, finales)',
    'Sneaky_Little_Scheme':'Comedia bajo los dialogos','Three_Nights_And_A_Shore':'(sin usar) pista larga','Moonfall_Charm':'(sin usar) primera prueba 29-oct','Lost_Things_Waltz':'(sin usar) vals de las cosas perdidas',
    'Run_For_It':'(sin usar) persecucion 29-oct','La_Noche_Del_Miau':'(sin usar) cancion de la noche del miau'}
for k,v in MU.items():
    f=glob.glob(f'{U}/*{k}*')[0]; name=f"{k.replace('_','-')}.mp3"; mp3(f, f'{OUT}/4-MUSICA/{name}'); idx.append(('4-MUSICA', name, v))
# índice
L=['EXTRAVIO · todos los recursos (imagenes y audio) · 1-nov-2026','','Mandale esta carpeta a Claude al empezar cada capitulo.','']
cur=None
for d,n,t in idx:
    if d!=cur: L+=['',f'== {d} =='] ; cur=d
    L.append(f'- {n}' + (f'  ->  {t}' if t else ''))
# (luego se ordena por carpeta)
open(f"{OUT}/LEEME.txt","w").write('\n'.join(L)+'\n')
print(len(idx),'archivos')
