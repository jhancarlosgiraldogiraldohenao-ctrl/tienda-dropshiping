# Biblioteca de sonidos de Extravío (Dizzy)

Pedido de Jay (4-nov-2026): **no hacer sonidos nuevos en cada capítulo.** Primero se usa lo que ya está aquí. Si un
capítulo necesita algo que no existe, Claude se lo pide a Jay (solo lo que falte) y se guarda aquí con su código.
Flow ya pone el sonido propio de cada toma (pasos, puertas, cascos, fuego, gente); aquí van solo los efectos de chiste,
los de amenaza, los ambientes de fondo por lugar y la música.

## Música (`musica/`)
| Código | Archivo | Qué es | Dura | Usos |
|---|---|---|---|---|
| M1 | M1-finca-bambuco | Bambuco suave de tiple, amanecer en la finca | 1:04 | Finca, mañanas, escenas tranquilas |
| M2 | M2-camino-carranga | Carranga alegre de trote | 1:04 | Viajes en Bartolo, caminos, chistes de campo |
| M3 | M3-plaza-vallenato | Vallenato de fondo | 1:04 | Pueblo, plaza, fiestas tranquilas |
| M4 | M4-cancion-el-hueco | Canción «Bienvenido a El Hueco» (champeta; canta los nombres de los vendedores) | 0:34 | Cada vez que se entra a El Hueco |
| M5 | M5-tuerto-reggaeton | Reguetón oscuro lento | 1:04 | El Tuerto, peligro, negocios turbios |
| M6 | M6-cuca-saxofon | Saxofón coqueto de chiste | 0:15 | Coqueteos (Cuca, Tocino) |
| M7 | M7-domino-tension | Tambores de tensión | 0:15 | Apuestas y suspenso (se repite en bucle) |
| M8 | M8-abuela-western | Silbido de western, duelo | 0:30 | La abuela llega a salvar; enfrentamientos |
| M9 | M9-regreso-bambuco-tierno | Bambuco lento y tierno | 1:00 | Momentos sinceros, atardeceres, regresos |
| M10 | M10-misterio-camara | Misterio con zumbido eléctrico | 0:30 | La cámara mágica, cosas raras de noche |
| M11 | M11-tema-extravio | Tema de la serie (cumbia + guitarra punk) | 0:30 | Cierre de cada capítulo y pantallas finales |
| M12 | M12-mariachi-muertos | Mariachi de Día de Muertos, más tranquilo (112 bpm; entra suave y termina en silencio) | 1:04 | Llegada a México, la calle del altar, escenas tranquilas |
| M12b | M12b-mariachi-muertos-metales | Mariachi con más trompetas, más rápido (123 bpm; arranca fuerte) | 1:04 | El mercado, la fiesta, momentos de energía en México |
| M13 | M13-persecucion-cumbia | Cumbia rápida de persecución («Trompo Trouble») | 0:30 | Huida por el mercado, carrera al amanecer (se repite en bucle) |
| M14 | M14-bolero-tocino | Bolero cursi exagerado («Serenade of Silliness») | 0:30 | Serenatas y coqueteos de Tocino |
| M15 | M15-tema-chuy | Cumbia lenta y mareada («Lazy Wobble Cumbia») | 0:30 | Cada vez que habla Chuy |
| M15b | M15b-tema-chuy-suave | Cumbia lenta más suave («Sleepy Cumbia Drift») | 0:30 | Chuy en la trajinera, momentos tranquilos |
| M16 | M16-vals-catrina | Vals elegante y de miedito («Skeleton Lady Waltz»; viene muy bajito, se sube en la mezcla) | 0:30 | Cada vez que aparece la Catrina |

## Ambientes (`ambientes/`), por debajo de las voces
| Código | Archivo | Lugar |
|---|---|---|
| E01 | E01-zarzo-amanecer | El zarzo y la casa en la mañana |
| E02 | E02-ambiente-finca | La finca de día |
| E14 | E14-ambiente-olla | El Hueco (siempre de noche) |
| E25 | E25-ambiente-muertos-noche | México, Día de Muertos: calle, mercado, panteón |
| E26 | E26-ambiente-alcantarilla | Dentro de la alcantarilla / el túnel |
| E27 | E27-ambiente-canal | Los canales y las trajineras de noche |

## Efectos (`efectos/`)
| Archivo | Para qué |
|---|---|
| E09-grillo-silencio | Silencio incómodo de chiste |
| E16-cachetada-triple | Cachetadas |
| E17-bajo-amenaza | Aparece algo peligroso; finales en suspenso |
| E19-solo-guitarra-espantoso | Tocino tocando (se corta el pedazo que sirva) |
| E20-chanclazo | La chancla de la abuela |
| E24-camara-se-prende | La cámara mágica se prende sola |
| E28-calada-tos-chuy | Chuy le da una calada larga, tose y se ríe |
| E29-huesos-catrina | Los huesitos de la Catrina cuando se mueve |
| E30-violin-roto | Lupe le rompe el violín en la cabeza a Tocino |
| E31-grito-ajua | Grito mexicano «¡ajúa!» para remates |
| E32-campanas-amanecer | Campanas lejanas + gallo: va a salir el sol |
| E33-viaje-magico | La raya verde que cruza el mapa (viaje mágico) |
| whoosh-transiciones-y-caidas | Título, tomas aéreas, caídas, lanzamientos |
| golpe-de-chiste | Remate de cada chiste |
| rayon-de-disco | Frenazos, «se cortó la música» |
| brillo-magico | Magia, perico, la ficha de la manga |
| subida-de-tension | Antes de una apuesta o un susto |
| latido | Miedo, tensión cercana |
| remate-final-de-episodio | Golpe final del cierre |
- **E34-vaca-muu** (efectos): una vaca muge una vez, larga y confundida (cap. 2, 14-nov-2026).
- **E35-proyector** (efectos): proyector viejo que se prende con un clic y queda zumbando (cap. 2, 14-nov-2026).
