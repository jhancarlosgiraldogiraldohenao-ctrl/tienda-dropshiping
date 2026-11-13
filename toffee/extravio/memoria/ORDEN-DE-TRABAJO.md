# Orden de trabajo (aprendido en el capítulo 1)

## Secciones de dos partes (decisión de Jay, 5-nov-2026)
- Se trabaja por **secciones de dos partes** (= un capítulo). Jay hace las dos partes y **al día siguiente** empieza a subir.
- De cada sección salen los videos de YouTube y **cuatro** shorts / reels / TikToks.
- Cada parte dura **máximo 3:00** (para que entre como Short). Al terminar las dos, Claude ayuda con YouTube, Instagram y TikTok.

## El orden que ahorra créditos
1. Personajes → historia → lugares → guion (Jay da el aval de cada uno: «parte N lista»).
2. **Prompts de Flow primero.** Jay genera las tomas.
3. Claude revisa cada toma en silencio («✓») y, cuando Jay dice «listo», da la revisión completa: qué se repite y por qué.
4. **Claude mide la boca de cada toma** (tramos de volumen del audio de Flow) y recién ahí escribe los textos de ElevenLabs
   con la duración y las pausas de esa boca (ver `VOCES-Y-BOCAS.md`). Así la voz entra a la primera.
5. Jay genera las voces (2–3 versiones de las difíciles). Claude escoge la que mejor calza.
6. **Armado sin voces (regla fija de Jay, 13-nov-2026):** con todas las tomas, Claude arma el video completo (orden, cortes,
   fundidos, transiciones, visor REC, recuadros) con el audio guía de Flow y SIN voces, música ni sonidos. Lo manda a Jay.
   **Solo con «aprobado»** se pasa a medir bocas (paso 4), voces, sonidos y música.
7. Edición final → video a Jay → correcciones → versión final.

> En la parte 1 se hizo al revés (voces antes que las tomas) y hubo que repetir V01 y V02: la boca de Flow tenía otro
> ritmo. **Nunca más voces antes de tener la toma.**

## Reusar antes de pedir
- Sonidos: biblioteca fija `toffee/extravio/sonidos/` (M1–M11, E01–E24). Pedir solo lo que falte.
- Tomas: las sobrantes de una parte sirven en otra (ej. G37 «todos se quedan quietos» sirve para «¡MIJITO!»; las
  tomas aéreas de día se pasan a atardecer o noche con color). Decírselo a Jay en la lista de prompts.
- Voces ya diseñadas en ElevenLabs: una por personaje, fija (`serie/CAP01-VOCES.md`).

## Lo que Jay no quiere
- Que Claude borre escenas por su cuenta. Si hay que ganar tiempo, **preguntar** o recortar solo de transiciones
  (nunca las tomas aéreas, nunca una escena que explica algo, como la gallina saliendo de la casa).
- Efectos de impacto viejos, grillos de chiste, «boing». Menos es más.

## Un mundo vivo (Jay, 5-nov-2026)
- Cada capítulo trae lugares nuevos; Jay los crea con gusto. Claude le pide la foto propia de cada lugar donde pasa una
  escena (y de cada hora distinta: noche, atardecer), en vez de forzar una foto de otro lugar o de otra hora.
- Prompts de lugares: Nano Banana Pro, vertical 9:16, sin personajes, «empty space in the center for small characters».

## Cada parte es un video completo (Jay, 5-nov-2026)
- La parte 2 también sale sola en TikTok, Instagram y Shorts: **toda parte lleva su propio gancho** (el momento más fuerte
  en el primer segundo), su título («EXTRAVÍO · VLOG 01 · PARTE 2») y un **recuento en off** de 4 s sobre una toma aérea
  para quien no vio la parte 1.
- **Continuidad ante todo:** tomas aéreas para ubicar cada lugar (llegar, salir, cambiar de lugar). Una toma aérea al revés
  (`reversa=1`) sirve de salida gratis.

## Dinamismo de lugares (Jay, 5-nov-2026)
- En el paso 3 (lugares), por cada lugar importante pedir **3–4 fotos de zonas o ángulos distintos** del mismo sitio, no una sola.
- En los prompts, rotar esas fotos y los ángulos de cámara; revisar que no haya más de 3 tomas seguidas iguales.
- Antes de pedir algo nuevo, mirar `reusables/LEEME.md`.

## Flow: Omni 1.2 Flash (7-nov-2026, grabación de Jay)
- Nuevo modelo **Omni 1.2 Flash**: mejor consistencia de personajes y escenarios, imagen más nítida y menos cortes raros.
  Omni 1.1 Flash y Veo 3.1 dicen «dejará de estar disponible»: **desde el cap. 2 se usa Omni 1.2 Flash**.
- Precio leído en la pantalla (720p, 9:16, x1): **3 créditos por segundo**, duración libre de 3 a 10 s
  (3 s = 9 · 4 s = 12 · 5 s = 15 · 6 s = 18 · 7 s = 21 · 8 s = 24 · 9 s = 27 · 10 s = 30).
- Regla: siempre x1 (una sola salida), duración exacta que pide la toma (no redondear a 4/6/8/10), y repartir las tomas
  entre las cuentas para que el saldo de cada una quede en 0 (el sobrante se llena con insertos de 3–4 s).

## Créditos (Jay, 7-nov-2026): 10 cuentas × 50 créditos gratis cada 24 h = 500 por día
- Omni 1.2 Flash: 3 créditos por segundo (3–10 s). Omni 1.1 Flash: 4 s = 7 · 6 s = 10 · 8 s = 12 · 10 s = 15.
- 1.1 sale a mitad de precio en tomas largas: se usa para tomas SIN diálogo ni personajes importantes (aéreas, lugares,
  caminos, puentes). 1.2 para todo lo que tenga personajes hablando o continuidad delicada.
- Paquete exacto por cuenta (50 justos): **36 s de 1.2 + dos tomas de 4 s en 1.1** (36+7+7), o 33 s de 1.2 + 4 s + 6 s
  en 1.1 (33+7+10), o 30 s de 1.2 + dos de 6 s en 1.1 (30+10+10). Solo 1.1: 10+10+6+6 s = 50 (32 s de video).
- Con 1.2 solo, lo máximo es 48 (16 s) y sobran 2: por eso cada cuenta lleva sus tomas de 1.1.
- Las listas de prompts se entregan **por cuenta** (Cuenta 1 … Cuenta 10), cada una sumando 50 exactos, siempre x1.

## DECISIÓN DE JAY (7-nov-2026): SOLO Omni 1.2 Flash, nada de 1.1 (se va el 5-dic)
- Calidad de película primero. Por cuenta: 16 s de 1.2 = 48 créditos (sobran 2, se acepta). 10 cuentas = 160 s por día.
- Ritmo: una parte cada 2 días (≈ 200–220 s de tomas por parte, con repeticiones), un capítulo cada 4 días.
  Los días sin parte nueva salen shorts del capítulo anterior, fotos e historias.
- Para estirar créditos sin bajar calidad: aéreas y planos de lugar SIN personajes se hacen con las fotos de Nano Banana
  animadas en la edición (movimiento lento de cámara, luces, humo, partículas), sin gastar Flow. Las tomas de Flow quedan
  para personajes y acción; ninguna toma dura más de lo que se usa.
- Tomas por cuenta: combinaciones de 16 s (8+8, 6+6+4, 5+5+6, 4+4+4+4, 10+6, 7+9, 3+3+…).

## Entrega de prompts de Flow (Jay, 7-nov-2026)
- UNA toma por respuesta: arriba las fotos (SendUserFile con display "render") y abajo el prompt en un bloque para copiar.
  El texto escrito entre llamadas a herramientas NO le llega a Jay: solo el texto final de cada respuesta.
- Cuando Jay manda el video terminado de esa toma → «✓» y, en la misma respuesta, las fotos y el prompt de la toma siguiente
  (orden de las cuentas: `serie/cap02/cap02_flow.py`, CUENTAS). Sin pedirle «ok».
