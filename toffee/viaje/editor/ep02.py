import sys; sys.path.insert(0, '/home/user/tienda-dropshiping/toffee/viaje/editor')
from editor import *
WD='/tmp/claude-0/-home-user-tienda-dropshiping/c684127a-90fa-5e05-b748-57ecc9507198/scratchpad/ep2'
S=[('t1.mp4',0,6.0,1,.5,.5,0.0),      # 1 gancho: la lechuza aterriza (audio de Flow mudo: trae la voz de Flow)
   ('t2.mp4',0.4,6.04,1,.5,.5,0.0),   # 2 Toffee: a ver mis desgraciados
   ('r3.mp4',0,4.0,1,.5,.5,0.6),('r3.mp4',4.0,8.0,1.15,.6,.55,0.6),  # 3 el trineo no arranca
   ('r4.mp4',1.2,7.6,1,.5,.5,0.0),    # 4 la lechuza: tres cascabeles
   ('t4b.mp4',0,4.03,1,.5,.5,0.0),    # 4b la lechuza susurra: lleno de monstruos
   ('s5.mp4',0.8,6.0,1,.5,.5,0.0),    # 5 evaluando la situación
   ('t6.mp4',0,5.3,1,.5,.5,0.7),      # 6 Galleta tumba el farol (antes del corte de Flow)
   ('t7.mp4',0,6.0,1,.5,.5,0.6)]      # 7 el camino de calabazas
L='a_fa88fa2a.mp3'; L2='a_c0bc1382.mp3'; T1='a_003a29d1.mp3'; T2='a_172ba2f5.mp3'; T3='a_a2d37578.mp3'
VO=[(L,0.00,4.25,0.10,'t1.mp4',1.52,None,'¡Por fin!|Llevo tres siglos|esperando visitas.'),
    (T1,0.00,2.20,0.00,'t2.mp4',0.69,None,'A ver,|mis desgraciados…'),
    (T1,2.20,3.77,2.40,'t2.mp4',2.80,None,'nos estrellamos.'),
    (T1,3.77,5.72,3.97,'t2.mp4',4.41,None,'Y nos encontró|una bruja.'),
    (T2,0.00,2.12,0.00,'r3.mp4',None,0.6,'Plan A:|despegar.'),
    (T2,2.12,4.65,2.37,'r3.mp4',None,3.9,'Plan B:|culpar a Galleta.'),
    (L2,0.00,3.72,0.00,'r4.mp4',1.68,None,'Sin sus tres|cascabeles,|ese trineo|no vuela.'),
    (L2,3.72,6.03,4.06,'r4.mp4',5.23,None,'Cayeron en el|Valle de Octubre.'),
    ('a_lech3.mp3',0.00,3.35,0.05,'t4b.mp4',None,0.8,'Un valle…|lleno de|monstruos.'),
    (T3,0.00,1.06,0.00,'s5.mp4',1.02,None,'¿Monstruos?'),
    (T3,1.06,2.53,1.23,'s5.mp4',2.13,None,'Yo no tengo miedo.'),
    (T3,2.53,4.68,2.75,'s5.mp4',3.73,None,'Estoy evaluando|la situación.')]
VO+=[('a_07905d6e.mp3',0.00,4.78,0.0,'t6.mp4',None,0.4,'Galleta encontró|el camino.|Fue suerte.|Yo lo tenía|calculado.'),('a_280eedd3.mp3',0.00,3.33,0.09,'t7.mp4',None,1.2,'¿Qué monstruo|creen que|nos espera?|Los leo.')]
KEY={'bruja','cascabeles','galleta','monstruos','valle','octubre','miedo'}
tit=bloque([linea([('Nos encontró una',W)],66,7),linea([('BRUJA EN EL BOSQUE ',CAR),('EMO','🦉')],76,8)])
fin=bloque([linea([('Sígueme ',W),('EMO','👀')],86,9),linea([('para no perderte el próximo episodio',W)],56,6)])
print('total',armar(S,VO,KEY,tit,fin,'EP02-final.mp4',WD))
