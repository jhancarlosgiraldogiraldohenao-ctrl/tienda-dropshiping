# Estudio de planos para Extravío (versión 2, 30-oct-2026)

Pedido de Jay: «que no todas las tomas sean una cámara al frente y Toffee hablando»; que el mundo se sienta vivo y que
los personajes lo vivan. Base: el video de las 5 tomas creativas que mandó Jay + lenguaje de cine clásico + lo estudiado de
Gnomo Palomo, Desencanto y Rick and Morty. Cada plano trae la frase en inglés para pedirlo en Flow (Omni 1.1 Flash).

Reglas fijas de `CLAUDE.md` que mandan sobre todo esto: lente normal (nada de ojo de pez ni viñeta), nunca vista en primera
persona con patas (crea un segundo gato), Toffee siempre visto desde afuera, cabeza + gorro + cámara siempre en cuadro,
un solo gato y un solo perro, una acción clara por toma, decir quién está a la izquierda y quién a la derecha.

---

## 1. Tamaños de plano (qué tan cerca)

| Plano | Para qué | Frase para Flow |
|---|---|---|
| **Gran plano general / de ubicación** | Presentar un lugar; que el mundo se vea enorme y vivo. Abre cada escena | `Extreme wide establishing shot of …, tiny characters` |
| **Plano general** | Ver a los personajes completos y lo que pasa alrededor | `Wide shot, full bodies visible, the street busy around them` |
| **Plano americano / entero** | Acción física: caminar, correr, cargar | `Full shot from head to paws` |
| **Plano medio** | Conversación con gestos | `Medium shot from the chest up` |
| **Primer plano** | Emoción, chiste en la cara | `Close-up of the face` |
| **Primerísimo primer plano** | El momento más fuerte (grito, susto, revelación) | `Extreme close-up of the eyes / mouth` |
| **Plano detalle (inserto)** | Un objeto que importa: la llave, la placa MAX, el gancho vacío | `Extreme close-up insert of the …, shallow depth of field` |

**Gramática:** ubicación → general → medio → primer plano. Cada escena nueva empieza abierta y se va cerrando; cuando cambia la emoción, se vuelve a abrir.

## 2. Ángulos (desde dónde mira la cámara)

| Ángulo | Qué transmite | Ejemplo en Extravío | Frase para Flow |
|---|---|---|---|
| **Picado (desde arriba)** | El personaje se ve chiquito, perdido, débil | Toffee solo en la calle con lluvia; los tres frente a millones de llaves | `High angle looking down at …` |
| **Contrapicado (desde abajo)** | Poder, orgullo, amenaza | Toffee «famoso» en su trono; Lucho abriendo su local; la sombra de la Polilla | `Low angle looking up at …` |
| **Cenital (vista de pájaro)** | Mapa, orden, comedia | La calle desde arriba con todos corriendo a esconderse | `Top-down bird's-eye view` |
| **Ras de suelo** | Mundo de mascota, juego | Galleta y la pelota; patas corriendo en el empedrado | `Camera on the ground, at floor level` |
| **Holandés (inclinado)** | Algo anda mal, mareo | Recién caídos en Extravío; la noche de la Polilla | `Dutch angle, the camera tilted about 15 degrees` |
| **Por encima del hombro (OTS)** | Conversación de verdad: uno habla y vemos la nuca del otro | Lucho le explica las reglas a Toffee | `Over-the-shoulder shot from behind the cat's head (his nightcap and camera blurred in the foreground left), the mouse in focus on the right` |
| **Dos personajes (two-shot)** | Relación, contraste | Toffee orgulloso y Galleta mordiendo la pelota | `Two-shot: on the left …, on the right …` |
| **Perfil** | Caminar y hablar, enfrentamientos | Toffee y Lucho cara a cara | `Profile shot, both seen from the side facing each other` |

**Plano y contraplano:** en una conversación se alterna un OTS de uno y el del otro. **Regla de los 180°:** si Toffee está a la izquierda y Lucho a la derecha, se mantienen así en toda la escena (los prompts lo dicen siempre).

## 3. Movimientos de cámara

| Movimiento | Qué transmite | Ejemplo | Frase para Flow |
|---|---|---|---|
| **Acercamiento lento (push-in)** | Darse cuenta de algo, tensión | La placa MAX; Toffee entendiendo que nadie lo busca | `The camera slowly pushes in toward …` |
| **Alejamiento (pull-out)** | Revelar dónde está, soledad, chiste | De la cámara roja grabando a Toffee en el trineo | `Starts on an extreme close-up of … and pulls back to reveal …` |
| **Travelling de seguimiento** | Acompañar al personaje; el mundo pasa | Caminar por la calle principal | `Tracking shot following them from behind` |
| **Travelling lateral (walk and talk)** | Hablar mientras viven el mundo (lo de Desencanto) | Lucho explica las reglas mientras caminan | `Side tracking shot moving along with them as they walk` |
| **Grúa que sube (crane up)** | El «wow» del mundo | Revelar la ciudad de Extravío | `Crane shot rising from behind them over their heads to reveal …` |
| **Grúa que baja** | Llegar a un lugar | Del techo del edificio a la ventana de Toffee | `Crane shot descending from … to …` |
| **Órbita / arco** | Momento heroico o de decisión | Toffee decide correr por Galleta | `The camera orbits slowly around …` |
| **Paneo / tilt de revelación** | Mostrar algo enorme | Subir por la cortina de llaves hasta el techo | `The camera tilts up slowly to reveal …` |
| **Barrido rápido (whip pan)** | Energía, cambio brusco, chiste | De Toffee a Galleta haciendo un desastre | `Fast whip pan from … to …` |
| **Cámara en mano** | Acción, pánico, «alguien lo graba» | La persecución de noche | `Handheld camera with natural slight shake` |
| **Snorricam** | Pánico total: el personaje quieto, el mundo loco | Toffee cayendo en el remolino; Toffee corriendo hacia la luz | `The camera is rigidly fixed in front of the cat's face and moves with him; he stays locked in the center while the background shakes and spins wildly` |
| **Dolly zoom (vértigo)** | «¡No puede ser!» (máximo 1 por capítulo) | Toffee ve millones de llaves | `Dolly zoom (vertigo effect): the camera moves backward while zooming in; the cat stays the same size while the background stretches away behind him` |
| **Cambio de foco (rack focus)** | Guiar la mirada, aparición sorpresa | Del carrito roto en primer plano a Lucho asomándose | `Rack focus from … in the foreground to … in the background` |
| **POV de un objeto** | Ver desde una cosa | Desde la pelota rodando; desde adentro de la alcantarilla; desde una llave colgada | `Camera fixed on the …, looking at …` (nunca los ojos de Toffee o Galleta) |

## 4. Composición (cómo se acomoda el cuadro)

- **Capas: primer plano, medio y fondo.** Algo pasa adelante (llaves colgando, un paraguas que cruza), los personajes en el medio y la ciudad viva atrás. Es lo que más hace que el mundo **no parezca un fondo**. Frase: `foreground: …; midground: …; background: …`.
- **Encuadre dentro del encuadre:** ver por una ventana, una puerta, el hueco de una maleta, la rendija de la cortina metálica.
- **Regla de tercios:** el personaje a un lado y el mundo al otro; el centro solo para los momentos de poder o de pánico.
- **Espacio negativo:** mucho cielo vacío o calle vacía = soledad o calma (la pantalla final).
- **Siluetas:** contra el atardecer o la luz turquesa (la sombra de la Polilla).
- **Profundidad de campo baja:** fondo desenfocado en los insertos y en los momentos íntimos.

## 5. Transiciones (cómo pasar de una toma a otra)

| Transición | Cuándo | Cómo |
|---|---|---|
| **Match cut** | Cambio de lugar elegante | Misma forma o movimiento, centrado y del mismo tamaño: la pelota → el recuerdo turquesa; la rejilla brillante → el centro del remolino; el centro del remolino → la O-cerradura del logo; el ojo de Toffee → el sol del Mar de Pelotas. Yo alineo y corto |
| **Corte en la acción** | Que no se note el corte | Cortar mientras salta, cae o abre algo; la toma siguiente sigue la misma acción desde otro ángulo |
| **Corte seco cómico (smash cut)** | Remate de chiste (Gnomo, Rick and Morty) | «Yo nunca corro.» → corte a Toffee corriendo como loco |
| **Barrido (whip pan)** | Energía | Dos tomas con barrido en la misma dirección, unidas en el movimiento |
| **Cortina con un objeto** | Cambio de escena | Algo pasa muy cerca de la cámara (un paraguas, la cortina metálica que baja) y tapa el cuadro |
| **Sonido que se adelanta (J-cut) o se queda (L-cut)** | Que las escenas fluyan | La campana de la noche suena antes de ver la calle; la voz de Lucho sigue sobre la toma siguiente |
| **Fundido** | Paso del tiempo (atardecer → noche) | Solo entre escenas, nunca dentro de una conversación |

Lo que ya probamos que funciona en Flow para unir tomas: «usar el último cuadro de la toma X como primer cuadro».

## 6. Lo que tomamos de las series estudiadas

- **Gnomo Palomo / El Loco Blanco:** gancho de 3 segundos con lo más loco del capítulo; un corte cada 3,7–5 s; nada dura más de 8 s; el personaje le habla a la cámara como vlogger (Toffee lo es); remate y corte seco.
- **Rick and Morty:** el mundo raro se muestra con naturalidad; gags de fondo (cosas absurdas pasando mientras ellos hablan); el chiste remata con un corte seco o con un silencio incómodo (*deadpan*: la cámara se queda quieta 1 segundo de más en la cara).
- **Desencanto:** caminar y hablar por el pueblo; los habitantes hacen su vida (venden, discuten, cierran sus negocios) y reaccionan a lo que pasa; el lugar tiene reglas y horarios (en Extravío: la noche de la Polilla).
- **Comedia:** regla de tres (dos cosas normales y una absurda: «Medias, controles, llaves… y mascotas»), plano de reacción después de cada chiste, chiste repetido que vuelve (*callback*: «Yo no salgo / Yo no corro»).

## 7. El mundo vivo (lista para cada escena)

Cada toma en Extravío debe tener al menos **una cosa del mundo haciendo su vida**:
- **Habitantes:** el Osito Tuerto con su tienda de medias, la Señora Sombrilla, las Medias Oruga, la Tele con Patas, el Cartero Caracol repartiendo cartas, mascotas perdidas que no son gatos ni perros (loros, hámsteres, tortugas, conejos).
- **Lugares con puertas, ventanas, locales, balcones, faroles, ropa colgada, escaleras.**
- **Clima del mundo:** lluvia lenta de objetos perdidos, cometas, paraguas volando como pájaros, cartas que vuelan.
- **Reacción:** cuando pasa algo (la noche, un grito), el mundo reacciona: cierran puertas, apagan faroles, se esconden.

## 8. Lo que hago yo en la edición (gratis)

Acercamientos lentos digitales, match cuts alineados, temblor de cámara en mano, sonido que se adelanta o se queda, fundidos, burbujas de pensamiento, el logo saliendo del remolino.

## 9. Lo que Flow hace mal (evitarlo en los prompts)

- Dos personajes hablando en la misma toma → **un solo personaje habla por toma**.
- Movimientos de cámara combinados → **un movimiento por toma**.
- Texto en carteles → **los locales llevan símbolos, nunca letras** (una llave gigante, una media, un sobre).
- Vista desde los ojos del personaje → aparece otro gato; el POV es siempre de un **objeto**.
