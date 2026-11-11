# Reglas de oro de Extravío (resumen de TODOS los errores, 11-nov-2026)
Leer esto primero; el detalle está en ERRORES.md, PROMPTS-FLOW.md, VOCES-Y-BOCAS.md, EDICION.md y MODO-PELICULA.md.

## A. Prompts de Flow (Omni 1.2 Flash, horizontal 16:9)
1. **Plantilla limpia y corta** (`cap02_flow_limpio.py`): formato → estilo corto → lugar en 1 frase → cámara → personajes (descripción corta) → UNA acción → diálogo → 1 línea de fondo vivo → 1 línea de sonido. Si se bloquea, versión larga (`cap02_flow_h.py`); bloqueo = reembolso.
2. **Nunca:** comparar con películas/estudios, «exactly like the reference», voces «como» alguien, listas largas de extras con trajes, bloque largo de prohibiciones, piropos sobre el cuerpo («mamacita», «skinny», «all bones»), marcas o plataformas dentro de las comillas («YouTube»), carteles/pósters (llevan letras), nombres propios fuera de las comillas.
3. **Tocino:** siempre en 4 patas, sin manos; jamás verbos humanos de brazos u hombros (shrug, wave, point, hold); «his four hooves stay on the ground». Habla **español con acento gringo y palabras sueltas en inglés** (Spanglish).
4. **Dizzy:** buzo negro siempre; gorra y cámara completas en el cuadro; «both eyes look the same way, never cross-eyed» (salió bizco).
5. **Chuy:** cigarrillo en la boca toda la toma; nunca «marijuana/joint/weed».
6. **Salidas y entradas:** decir que no se devuelve («never comes back inside; the window is empty at the end»); cada personaje que llega necesita su toma de llegada; nadie aparece de la nada.
7. **Insertos de una mano:** desde dónde se ve, por qué lado entra, «one single hand, no face, no body», sin la descripción completa del personaje.
8. **Dos o más personajes:** quién a la izquierda y quién a la derecha, tamaños («the rat is much smaller, half the pig's height»), cuerpos enteros con los pies en el suelo, un solo personaje habla.
9. **Continuidad física:** lo que se usa tiene que verse posible (la tapa abierta antes de caer); la pose de una toma sigue en la siguiente (si quedaron de pie, la próxima los muestra de pie); una sola hora por escena y foto nueva si cambia la hora.
10. **Revisar cada toma:** primer y último segundo, 4 esquinas (humanos), personajes duplicados, ropa, idioma de la boca. Si se ve una persona en el borde, se recorta.

## B. Voces (ElevenLabs v4, est. 50, sim. 75, una sola versión)
1. Primero la toma, después la voz: Claude mide la boca y escribe el texto con esa duración.
2. **Nunca Voice Changer. Nunca estirar la voz.** Se corta solo en silencios reales y se mueve la frase entera a su boca.
3. **Sin gritos largos** en caídas (Jay: «horribles»): la caída va con un whoosh.
4. Ninguna frase dos veces (voz de Flow + ElevenLabs): en tomas con voz, el audio de Flow se apaga.

## C. Edición (`editor/ed_dizzy02p1h.py` es la base)
1. **Cero zonas muertas:** música SIEMPRE sonando de principio a fin; solo baja ~3 dB, suave, en las tomas con diálogo. Ambiente de cada lugar debajo de todo.
2. Volumen final lineal (loudnorm de 2 pasadas), −14 LUFS.
3. **Fundido de 0,3 s entre todas las tomas** (imagen y sonido); nada de tomas «pegadas».
4. Gancho con lo más fuerte en el segundo 0; aéreas ≤ 4,5 s; en cada escena puente hay diálogo entre personajes (si no, se siente vacío).
5. Subtítulos horizontales abajo al centro (y = 880 de 1080), Montserrat negrita, palabras clave en rojo; los de Tocino en inglés con traducción.
6. Cada parte ≤ 3:00, con su gancho, su título y recuento en off.
