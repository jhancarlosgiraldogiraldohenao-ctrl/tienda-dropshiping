# Voces que calzan con la boca (el error más caro del capítulo 1)

## Qué pasó
- La boca de Flow y la voz de ElevenLabs tienen ritmos distintos. Si la voz dura 8 s con pausas largas y la boca habla
  6 s casi sin parar, no hay edición que la salve (G01, V01/V02: se repitieron).
- Los tiempos de Whisper sobre el audio de Flow fallan hasta 1,5 s («What the…», «Siga», «¡Muévete!»). No sirven para pegar.

## Cómo se hace ahora
1. Con la toma de Flow ya generada, Claude mide **los tramos de boca** = tramos donde suena la voz de Flow
   (`boca_flow()` en `editor/ed_dizzy01.py`: volumen real, umbral = piso + 10 dB entre −28 y −20 dB).
2. Claude escribe el texto de ElevenLabs **con la duración de cada tramo**: tantas sílabas como dice Flow, las pausas donde
   la boca se cierra, y le dice a Jay cuánto debe durar («≈ 6 s, rápido y sin pausas»).
3. Acotaciones en inglés entre corchetes: [excited] [fast] [whispers] [shouting] [sighs] [nervous laugh] [short pause].
   **[fast]** cuando la boca no para; **[short pause]** solo donde la boca se cierra de verdad.
4. Jay manda 2–3 versiones de las difíciles; Claude mide cada una (frases y duración) y escoge.
5. Revisar cada frase transcrita: ElevenLabs cambia palabras.
6. Voz de cada personaje fija (ElevenLabs v4, estabilidad 50 %, similitud 75 %). Diseño de voz con menos de 500 caracteres.

## Cómo se pega en el editor
- `alinear()`: parte la voz en frases (silencios ≥ 0,15 s a −40 dB), empareja cada grupo de frases con un grupo de tramos
  de boca por duración (`emparejar()`, saltar tramos del principio cuesta caro) y estira o encoge suave (0,8–1,25) con
  rubberband. La voz entra 0,03 s después de la boca, nunca antes.
- Si la boca tiene un patrón raro, se ponen los arranques a mano: `fijos=[1.03, None, 3.63, 4.8]` (uno por frase).
- `quitar=1` quita la primera frase de una voz (p. ej. «¡Mía!») y `solo=1` deja solo la primera; `desde_boca` ignora la boca
  de antes de cierto segundo.
- Voz en off (`vo=s`): cuando la boca no se ve o está cerrada (recuerdos, Bartolo pensando).
- La voz de Flow se tapa por Whisper **y** por volumen (0,12 s antes, 0,15 s después): así no se cuela un «mue».

## Una sola versión por voz (Jay, 5-nov-2026 — regla fija desde el capítulo 2)
- Jay NO puede generar varias versiones de la misma frase (créditos). Claude manda **un solo texto final** por voz y
  controla la duración con el texto, no con repeticiones:
  - **Más rápido:** `[fast]`, comas en vez de «…», sin pausas escritas. `[whispers]`, `[menacing]`, `[calm]` y «…» la
    alargan (en la parte 2, V35, V36, V40, V50, V52 y V64 salieron entre 1,3 y 1,7 veces más largas que la boca).
  - **Más lento o con pausa:** «…» (≈ 0,5–0,8 s) o `[short pause]` / `[long pause]` justo donde la boca se cierra.
  - Palabras sueltas muy cortas en la boca («No.», «Juguemos.»): `[fast]` y sin acotaciones de emoción lentas.
- Meta: el habla de la voz (sin silencios) ≤ 1,2 × el tiempo de boca de Flow. El editor estira o encoge como mucho 0,8–1,25.
- En la parte 2 (cap. 1) Jay permitió repetir las que salieron largas; en los próximos capítulos, no.

## Cap. 2 (Omni 1.2, 8-nov-2026)
- Personajes con voz «lenta» (Chuy): en el texto NO poner [sleepy]/[slow] cuando la boca de Flow es rápida (T29); la lentitud ya está en la voz diseñada.
- Bocas muy cortas para una frase (T19 «tan feíto», T35 «literal»): se recorta el texto a lo que cabe; nunca alargar la toma.
- [whispers] alarga mucho: solo si la boca tiene tiempo de sobra.

## Tocino habla Spanglish (decisión de Jay, 8-nov-2026, desde la parte 2 del cap. 2)
- Habla sobre todo **español con acento gringo** (mal conjugado, chistoso) y se le salen **frases cortas en inglés** («bro», «dude», «oh my God», «what the heck»).
- En los prompts de Flow: «speaks in Spanish with a very heavy American gringo accent, mixing in a few short English words».
- El mercado de EE. UU. se busca con subtítulos en inglés (.srt) y el doblaje automático de YouTube, no con Tocino en inglés.

## Voice Changer: PROHIBIDO (decisión de Jay, 8-nov-2026, para siempre)
- Jay lo probó: la voz sale distorsionada y suena distinta cada vez. **Nunca más pedir Voice Changer.**
- Método fijo: Claude mide la boca de la toma (palabras de Whisper + tramos), escribe el texto de ElevenLabs (TTS, voz del personaje) con comas, puntos y «...» para que dure lo mismo, le dice a Jay cuántos segundos debe durar, y pega la voz con `sincronizar()` / `pegar_suave()` moviendo frases enteras.
- Los 19 audios `*-flow.mp3` de `p1-flow-para-voice-changer/` ya no se usan para eso: la parte 1 del cap. 2 se termina con las voces TTS que ya están en `voces-cap02/p1/`.
