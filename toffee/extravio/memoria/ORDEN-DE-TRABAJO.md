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
6. Edición → video a Jay → correcciones → versión final.

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
