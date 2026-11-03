# -*- coding: utf-8 -*-
"""Capítulo 1 de Extravío (Dizzy) · parte 4: guion y estructura toma por toma.
python3 toffee/extravio/serie/cap01_guion.py  ->  CAP01-GUION.md (y el HTML lo arma el scratchpad)
Cada toma: (segundos en la edición, plano, qué se ve, quién habla y la frase, sonido)
"""
import os
AQUI = os.path.dirname(os.path.abspath(__file__))

# Escenas: (titulo, lugar/referencias, musica/ambiente, tomas)
P1 = [
("1. Gancho", "Zarzo (ZARZO), amanecer", "Ambiente: gallos a lo lejos, madera que cruje. Sin música hasta el título.", [
 (3, "Primerísimo plano, cámara pegada a la cara", "Dizzy pegado al lente, ojos enormes, luz de la ventana redonda detrás", "DIZZY: «¿Quiubo pues, mis ratas? Este es mi primer vlog…»", "—"),
 (3, "Primer plano, se aleja un poco", "Dizzy mira a los lados, desconfiado, y baja la voz", "DIZZY (susurra): «…y si mi cucha se entera de dónde saqué esta cámara, me mata.»", "Golpe de chiste al final"),
]),
("2. De dónde salió la cámara (recuerdo)", "Rincón del Tuerto y mesa de dominó (HUECO-RINCON-TUERTO, HUECO-DENTRO), noche, con un tono más cálido de recuerdo", "Música: bajo de reguetón lento, misterioso. La voz de Dizzy va en off (no se le ve la boca).", [
 (3, "Plano medio desde un lado de la mesa", "Dizzy empuja una montaña de tapas al centro de la mesa; enfrente, El Tuerto pone la cámara", "DIZZY (en off): «Me jugué todas mis tapas, mis ratas.»", "Tapas que caen"),
 (2, "Inserto, plano detalle debajo de la mesa", "La pata de Dizzy saca una ficha de dominó de la manga del buzo", "—", "«Tin» brillante"),
 (3, "Plano medio", "Dizzy pone la ficha, gana y arrastra la cámara hacia él; El Tuerto lo mira con su único ojo", "DIZZY (en off): «¿Trampa? No, mi llave. Talento.»", "Golpe en la mesa"),
 (2, "Primer plano en el zarzo (vuelve al presente)", "Dizzy, de nuevo en el zarzo, mira a cámara serio", "DIZZY: «Que es distinto, malparidos.»", "Golpe de chiste"),
]),
("3. Su mundo", "Finca desde el aire (AEREA-FINCA), finca (FINCA-ESPERANZA)", "Música: tiple y guitarra suave (bambuco). Ambiente: pájaros, viento en los cafetales.", [
 (3, "Toma aérea, el dron baja lento hacia la casa", "La finca entre los cafetales con niebla. TÍTULO: «EXTRAVÍO · VLOG 01»", "—", "Whoosh suave con el título"),
 (3, "Plano medio, Dizzy con el palo selfie caminando por el corredor", "Dizzy camina por el corredor de la casa, hamaca y flores al fondo", "DIZZY: «Esta es la finca de mi abuela. Aquí vivo… gratis.»", "Pasos en madera"),
 (2, "Primer plano de Bartolo, en el patio del café", "Bartolo mira a la cámara, aburrido, con los ojos medio cerrados", "BARTOLO: «…No.»", "Resoplido"),
 (3, "Plano medio de Dizzy (contraplano)", "Dizzy señala a Bartolo con el pulgar", "DIZZY: «Este es Bartolo, el hijueputa más amargado de Colombia.»", "Golpe de chiste"),
]),
("4. La abuela y el mandado", "Finca (FINCA-ESPERANZA), corredor y puerta azul", "Música: el bambuco sigue bajito. Ambiente: gallinas, una radio vieja lejos.", [
 (4, "Plano general del corredor, la cámara a la altura de Dizzy", "La puerta azul se abre de golpe; sale Doña Gertrudis con la chancla en el ala", "GERTRUDIS: «¡Mijito! Ay, Dios mío, ¿y esa vaina qué es?»", "Puerta que se abre"),
 (2, "Plano medio de Dizzy", "Dizzy esconde el palo selfie detrás de la espalda y sonríe", "DIZZY: «Nada, abuelita, nada.»", "—"),
 (5, "Plano medio de la abuela, desde abajo", "La abuela señala con el ala los dos bultos de café junto a Bartolo", "GERTRUDIS: «Lleve esos dos bultos de café al pueblo, que debemos en la tienda. Y me trae la panela, mi amor.»", "—"),
 (3, "Primer plano de la abuela", "La abuela levanta una pluma como un dedo, seria y cariñosa a la vez", "GERTRUDIS: «Y no se me demore, que a las seis hay comida. ¡Dios me lo bendiga!»", "Golpe suave"),
]),
("5. El camino con Bartolo", "Camino de las palmas (CAMINO-PALMAS)", "Música: carranga alegre. Ambiente: cascos en tierra, pájaros.", [
 (3, "Toma aérea siguiendo desde atrás y arriba", "Bartolo baja por el camino entre las palmas gigantes, con Dizzy encima y los dos bultos", "—", "—"),
 (3, "Plano medio de frente, cámara que retrocede con ellos", "Dizzy montado en Bartolo habla con el palo selfie", "DIZZY: «Vamos pa'l pueblo, mis ratas. Facilito.»", "Cascos"),
 (2, "Plano general de perfil", "Bartolo se frena en seco; Dizzy casi se cae hacia adelante", "—", "Frenazo de disco (la música se corta)"),
 (3, "Primer plano de Dizzy, encima de Bartolo", "Dizzy, furioso, le grita a la nuca de Bartolo", "DIZZY: «¡Muévete, perro! ¿Qué te pasa, estúpido?»", "—"),
 (2, "Primer plano de Bartolo de frente", "Bartolo, inmóvil, ni parpadea", "—", "Grillo (silencio de chiste)"),
 (3, "Plano medio", "Dizzy saca un pedazo de panela del morral y se lo muestra; Bartolo arranca de una", "—", "La música vuelve de golpe + cascos rápidos"),
]),
("6. El pueblo y Tocino", "Pueblo desde el aire (AEREA-PUEBLO), plaza (PLAZA), esquina de Tocino (PLAZA-ESQUINA-TOCINO)", "Música: vallenato de fondo. Ambiente: campanas, gente del pueblo, un jeep.", [
 (3, "Toma aérea, el dron avanza hacia la plaza", "El pueblo de colores en la montaña, la iglesia al centro", "—", "Campanas"),
 (3, "Plano general de la plaza", "Dizzy y Bartolo entran a la plaza; atrás pasa la Llorona flotando con su arepa quemada", "LLORONA (a gritos, de lejos): «¡Se me quemó la arepaaa!»", "Eco de lamento"),
 (2, "Primer plano de Dizzy", "Dizzy mira a cámara, cansado", "DIZZY: «Todos los días, parce.»", "—"),
 (3, "Plano medio en la esquina", "Tocino toca su guitarra rota en la banca; nadie le echa monedas", "—", "Guitarra desafinada"),
 (2, "Plano medio de Tocino", "Tocino ve a Dizzy y levanta la pata", "TOCINO: «¡Hey, dude!»", "—"),
 (3, "Primer plano de Tocino", "Tocino se baja las gafas y mira la cámara de la gorra de Dizzy", "TOCINO: «Oh my God… ¿Eso es un cámara?»", "—"),
 (3, "Plano medio de Dizzy (contraplano)", "Dizzy saca pecho, orgulloso", "DIZZY: «Mía, mi llave. Ahora soy vlogger.»", "—"),
 (5, "Primer plano de Tocino, se acerca la cámara despacio", "Tocino mira los bultos de café y se le ocurre la idea", "TOCINO: «Con ese cámara y ese café… vendemos el café en El Hueco por el doble de lucas…»", "—"),
 (5, "Primer plano de Tocino", "Tocino abre los ojos, emocionado, y hace los cuernos del rock", "TOCINO: «…compramos perico, hacemos un video mágico y ¡boom! Famosos, man. Let's rock, baby!»", "Acorde de guitarra"),
 (2, "Primer plano de Dizzy", "Dizzy sonríe con malicia", "DIZZY: «Usted es un genio, gringo hijueputa.»", "Golpe de chiste"),
]),
("7. El Hueco: la entrada y la contraseña", "Olla desde el aire (AEREA-OLLA), escaleras (HUECO-ENTRADA). En El Hueco siempre es de noche (regla nueva del mundo).", "Música: se apaga el vallenato. Ambiente: perros lejos, humo, gotas.", [
 (3, "Toma aérea, el dron baja hacia la cañada", "La olla de noche, con los barriles encendidos", "—", "Whoosh oscuro"),
 (3, "Plano general desde abajo de las escaleras", "Dizzy, Tocino y Bartolo bajan las escaleras rotas", "TOCINO: «Oh my God, this is insane…»", "Pasos"),
 (2, "Primer plano del gallinazo, desde abajo", "El gallinazo carnicero les cierra el paso con el cuchillo", "GALLINAZO: «¿Contraseña?»", "—"),
 (2, "Primer plano de Dizzy", "Dizzy, sin pensarlo", "DIZZY: «Hijueputa.»", "—"),
 (2, "Primer plano del gallinazo", "El gallinazo se hace a un lado", "GALLINAZO: «Siga.»", "Golpe de chiste"),
]),
("8. La canción: «Bienvenido a El Hueco»", "El Hueco por dentro (HUECO-DENTRO, HUECO-PUESTO-CARNE)", "CANCIÓN completa (≈ 28 s, champeta). Regla del manual: la canción se graba con cámara lejos y cortes a reacciones; solo frases cortas en primer plano.", [
 (4, "Grúa que sube por la calle del mercado", "Se revela todo El Hueco: puestos, humo, bombillos; Cuca sube a una mesa en bikini rojo", "CANCIÓN (Cuca): «Bienvenido a El Hueco, mi amor…»", "—"),
 (3, "Plano general de Cuca bailando en la mesa", "Cuca baila como diva; los vendedores aplauden", "CANCIÓN (Cuca): «…aquí se entra, pero no se sale.»", "—"),
 (3, "Plano medio en el puesto de carne", "El gallinazo corta carne al ritmo", "CANCIÓN (gallinazo): «Carnecita fresca… ¡de ayer!»", "Cuchillazo en el ritmo"),
 (3, "Plano medio", "El sapo con cadenas levanta un frasco de perico que brilla", "CANCIÓN (sapo): «Perico del bueno, pa' que vueles sin avión.»", "Brillo mágico"),
 (3, "Plano medio", "La rata vieja cuenta tapas; la chucha pasa con su bolsa de cosas robadas", "CANCIÓN (rata vieja): «Cambio tapas, cambio todo… hasta el alma.»", "Tapas"),
 (4, "Plano general, la cámara se mueve entre los puestos", "Todos los vendedores bailan; Tocino baila mal; Dizzy graba con el palo selfie", "CORO (todos): «¡En El Hueco, en El Hueco! Aquí todo tiene precio…»", "—"),
 (3, "Plano medio de Cuca, pose final", "Cuca termina con una pose de diva encima de la mesa", "CORO: «…¡y el precio lo pone el Tuerto!»", "Golpe final de la canción"),
]),
("9. «Muestra esa cuca»", "El Hueco por dentro (HUECO-DENTRO)", "Sin música: el silencio es el chiste. Ambiente del mercado bajito.", [
 (2, "Primer plano de Tocino", "Tocino se baja las gafas despacio mirando a Cuca", "—", "—"),
 (3, "Primer plano de Tocino", "Tocino sonríe de lado", "TOCINO: «Uy, mami… muestra esa cuca.»", "—"),
 (2, "Plano general", "Todo El Hueco se queda callado y lo mira (en YouTube se estira a 4 s)", "—", "Grillo"),
 (2, "Plano medio de perfil: Cuca a la izquierda, Tocino a la derecha", "Cuca le pega una cachetada con tres patas a la vez", "—", "Cachetada triple"),
 (2, "Primer plano de Tocino", "Tocino sobándose la cara", "TOCINO: «What the fuck, dude?»", "—"),
 (3, "Primer plano de Dizzy", "Dizzy le grita a Tocino", "DIZZY: «¡Es mi prima, cochino gran hijueputa!»", "—"),
 (4, "Primer plano de Tocino", "Tocino, confundido, con las patas abiertas", "TOCINO: «¿Qué? Es una cucaracha, ¿no? Cuca… cucaracha… I'm confused, dude.»", "Golpe de chiste"),
 (4, "Plano medio de Cuca", "Cuca, todavía brava, se cruza de patas y baja la voz", "CUCA: «Eche, primo, aquí no se puede vender nada sin pagarle al Tuerto.»", "—"),
 (2, "Primer plano de Dizzy", "Dizzy sonríe nervioso", "DIZZY: «Todo bien, todo bien…»", "—"),
 (2, "Plano medio de Dizzy", "Una sombra grande lo cubre por detrás", "—", "Bajo grave que entra"),
 (2, "Primerísimo plano de Dizzy", "Dizzy, aterrado, pegado al lente", "DIZZY: «Uy, no… triple hijueputa.»", "Corte en seco · FIN DE LA PARTE 1"),
]),
]

P2 = [
("10. El Tuerto", "Rincón del Tuerto (HUECO-RINCON-TUERTO)", "Música: bajo de reguetón oscuro y lento. Ambiente: barril que crepita.", [
 (3, "Primerísimo plano del Tuerto (arranca la parte 2 con la respuesta)", "El Tuerto, con el palillo en la boca, mira con su único ojo", "TUERTO: «Tú me debes, ratica… ¿sí o qué?»", "—"),
 (4, "Plano medio del Tuerto en su trono de sillas de carro", "El Tuerto señala los bultos de café", "TUERTO: «Esa cámara me la ganaste con trampa. Y ese café ahora es mío.»", "—"),
 (3, "Plano general", "La chucha y la iguana le quitan los bultos a Bartolo y los llevan al trono; Bartolo ni se mueve", "—", "Bultos arrastrados"),
 (2, "Primer plano de Dizzy", "Dizzy aprieta los dientes", "DIZZY (bajito): «Gonorrea…»", "—"),
]),
("11. Intento 1: el solo de guitarra", "Rincón del Tuerto", "Música: se corta cuando empieza el solo.", [
 (3, "Plano medio de Tocino", "Tocino agarra la guitarra rota", "TOCINO: «Tranquilo, dude. Yo lo distraigo.»", "—"),
 (3, "Plano general", "Tocino hace un solo horrible con la guitarra", "—", "Solo de guitarra espantoso"),
 (2, "Inserto", "La rata vieja y el sapo se tapan los oídos", "—", "—"),
 (2, "Primer plano del Tuerto", "El Tuerto ni parpadea", "—", "La guitarra sigue"),
 (2, "Primer plano de Dizzy", "Dizzy con las patas en las orejas", "DIZZY: «¡Qué te pasa, estúpido, eso es un crimen!»", "—"),
 (2, "Primer plano de Tocino", "Tocino, ofendido", "TOCINO: «Shut up, man, it's art!»", "Golpe de chiste"),
]),
("12. Intento 2: Cuca", "Rincón del Tuerto", "Música: saxofón coqueto, de chiste.", [
 (3, "Plano general", "Cuca camina hacia el Tuerto moviendo las caderas", "—", "Saxofón"),
 (4, "Plano medio de Cuca", "Cuca se apoya en el trono, coqueta", "CUCA: «Ay, Tuertico, mi vida… ¿y si me regalas ese cafecito?»", "—"),
 (2, "Primer plano del Tuerto", "El Tuerto la mira de arriba abajo", "TUERTO: «No.»", "El saxofón se corta"),
 (2, "Plano medio de Tocino, al fondo", "Tocino levanta la pata", "TOCINO: «¡Yo sí, mami!»", "—"),
 (4, "Plano medio de Cuca", "Cuca, ofendida por los dos, señala a Dizzy", "CUCA: «¡Ajá! Pues que sepas que este anda grabando todo, Tuerto.»", "—"),
 (2, "Primer plano de Dizzy", "Dizzy, traicionado", "DIZZY: «¡Sapa malparida!»", "—"),
]),
("13. Intento 3: la apuesta", "Mesa de dominó (HUECO-DENTRO)", "Música: tensión, tambores lentos. Todo El Hueco mira.", [
 (4, "Plano medio de Dizzy frente al Tuerto, de perfil: Dizzy a la izquierda, el Tuerto a la derecha", "Dizzy da un paso adelante", "DIZZY: «Le juego el café al dominó, gato hijueputa.»", "—"),
 (3, "Primer plano de Dizzy", "Dizzy se toca la cámara de la gorra", "DIZZY: «Y si pierdo… le doy la cámara.»", "—"),
 (2, "Primer plano del Tuerto", "El Tuerto sonríe por primera vez", "TUERTO: «Juguemos.»", "—"),
 (3, "Cenital sobre la mesa", "La mesa de dominó desde arriba, todos los vendedores alrededor", "—", "Fichas que se mueven"),
 (2, "Inserto debajo de la mesa", "Bartolo se va caminando en silencio hacia las escaleras (nadie lo ve)", "—", "—"),
 (2, "Inserto, plano detalle", "La pata del Tuerto saca una ficha de la manga (igual que Dizzy en el recuerdo)", "—", "El mismo «tin» del recuerdo"),
 (2, "Primer plano de Dizzy", "Dizzy, con los ojos enormes", "DIZZY: «¿Qué…? ¡Eso es trampa!»", "—"),
 (2, "Primer plano del Tuerto", "El Tuerto, tranquilo", "TUERTO: «No, ratica. Talento.»", "Golpe de chiste"),
 (3, "Plano medio", "El Tuerto levanta a Dizzy de la cola y lo deja colgando", "—", "—"),
 (3, "Primer plano de Dizzy de cabeza", "Dizzy colgando, pataleando", "DIZZY: «¡Suélteme, pirobo! ¡Perro hijueputa!»", "—"),
 (3, "Primer plano del Tuerto", "El Tuerto acerca la pata a la cámara de la gorra", "TUERTO: «Así se siente, ratica.»", "Bajo grave"),
]),
("14. La abuela", "Escaleras (HUECO-ENTRADA) y El Hueco por dentro", "Música: silbido de western, como un duelo. Chancla en cámara lenta.", [
 (3, "Plano general de El Hueco", "Se oye un grito y todos se congelan", "GERTRUDIS (de lejos): «¡MIJITO!»", "La música se corta de golpe"),
 (3, "Plano general desde abajo de las escaleras", "Doña Gertrudis baja las escaleras montada en Bartolo (Bartolo fue a buscarla)", "—", "Silbido de western"),
 (4, "Primer plano de la abuela, desde abajo", "La abuela, furiosa, levanta la chancla", "GERTRUDIS: «¡Virgen santísima, suelte a mi muchacho!»", "—"),
 (3, "Plano medio, cámara lenta", "La abuela lanza la chancla", "—", "Whoosh largo"),
 (2, "Inserto en cámara lenta", "La chancla vuela entre los puestos del mercado", "—", "Whoosh"),
 (2, "Primer plano del Tuerto", "La chancla le pega en la cara al Tuerto", "—", "Golpe fuerte"),
 (3, "Plano medio", "El Tuerto suelta a Dizzy, que cae al barro", "TUERTO: «Señora… perdón, señora.»", "Caída en el barro"),
 (2, "Primer plano de Tocino", "Tocino, enamorado", "TOCINO: «Holy shit… I love this woman.»", "Golpe de chiste"),
 (3, "Plano medio", "La abuela recoge los bultos y la cámara, y agarra a Dizzy de la oreja", "—", "—"),
]),
("15. El camino de vuelta", "Camino de las palmas (CAMINO-PALMAS) al atardecer", "Música: bambuco lento y tierno. Ambiente: grillos que empiezan, viento.", [
 (3, "Toma aérea al atardecer", "Bartolo sube por el camino con la abuela, Dizzy y Tocino encima", "—", "—"),
 (4, "Plano medio de los cuatro, cámara que retrocede con ellos", "Tocino, detrás de la abuela, le habla al oído", "TOCINO: «Señora, usted tiene unas piernas muy…»", "—"),
 (2, "Mismo plano", "La abuela le pega con la chancla sin voltear", "—", "Chanclazo"),
 (5, "Primer plano de Dizzy, bajito a cámara", "Dizzy, serio por primera vez", "DIZZY (bajito): «Esa cucha me salvó la vida, mi llave… pero no le digan que dije eso.»", "—"),
 (3, "Primer plano de la abuela, de espaldas a Dizzy", "La abuela, sin voltear, sonríe", "GERTRUDIS: «Lo oí, mijito.»", "La música sube un poquito"),
]),
("16. La comida", "Cocina con el fogón (COCINA-FOGON), de noche", "Música: el bambuco sigue suave. Ambiente: fogón que crepita, olla hirviendo.", [
 (4, "Plano medio", "La abuela sirve un plato enorme de sancocho a Dizzy", "GERTRUDIS: «Venga y coma primero, mi amor, que se me va a enfermar.»", "—"),
 (4, "Plano medio de la abuela, mirando a Tocino", "La abuela le sirve a Tocino y le pellizca la barriga", "GERTRUDIS: «Y usted coma también, mijo, que pa' diciembre lo quiero gordito.»", "—"),
 (2, "Primer plano de Tocino", "Tocino se pone pálido y traga saliva", "TOCINO: «…Oh, no.»", "Golpe de chiste"),
]),
("17. El misterio", "Zarzo (ZARZO) de noche; video del futuro en el callejón (CALLEJON-ALCANTARILLA)", "Música: suspenso, zumbido eléctrico.", [
 (4, "Plano general del zarzo de noche", "Dizzy duerme en el colchón; la gorra con la cámara está en la repisa y la cámara se prende sola", "—", "Pitido y zumbido"),
 (4, "Inserto: la pantalla de la cámara", "En la pantalla: Dizzy, gritando, cae de noche por la alcantarilla verde del callejón", "DIZZY (en el video, gritando): «¡Aaaah!»", "Grito con eco"),
 (2, "Primerísimo plano de Dizzy despierto", "Dizzy con los ojos enormes", "DIZZY: «Hijueputa…»", "—"),
]),
("18. Cierre", "Zarzo de noche", "Música: el tema de la serie entra suave.", [
 (5, "Primer plano de Dizzy con el palo selfie", "Dizzy le habla a la cámara, todavía asustado", "DIZZY: «¿Me meto por esa alcantarilla o qué, mis ratas? Escríbanlo en los comentarios.»", "—"),
 (3, "Primer plano", "Dizzy guiña el ojo", "DIZZY: «Sígueme pa' no perderte el próximo vlog, mi llave.»", "Golpe final"),
 (16, "Solo en YouTube: escena tranquila (pantallas finales)", "La finca desde el aire de noche con estrellas (8 s) y Dizzy dormido en el zarzo (8 s)", "—", "Grillos y el tema de la serie"),
]),
]

LETRA = """**«Bienvenido a El Hueco»** (champeta, ≈ 28 s; la canta Cuca, con los vendedores de coro)

> **Cuca:** Bienvenido a El Hueco, mi amor,
> aquí se entra, pero no se sale.
> **Gallinazo:** Carnecita fresca… ¡de ayer!
> **Sapo:** Perico del bueno, pa' que vueles sin avión.
> **Rata vieja:** Cambio tapas, cambio todo… hasta el alma.
> **Coro (todos):** ¡En El Hueco, en El Hueco!
> Aquí todo tiene precio…
> ¡y el precio lo pone el Tuerto!
"""

def fmt(t):
    return f"{int(t//60)}:{int(t%60):02d}"

def tabla(escenas, t0, n0):
    out = []; t = t0; n = n0
    for titulo, lugar, sonido, tomas in escenas:
        dur = sum(x[0] for x in tomas)
        out.append(f"\n### {titulo} · {fmt(t)} ({dur} s)\n\n**Lugar:** {lugar}  \n**Música y ambiente:** {sonido}\n")
        out.append("| # | Tiempo | Seg. | Plano | Qué se ve | Quién habla | Efecto |\n|---|---|---|---|---|---|---|")
        for d, plano, ve, habla, sfx in tomas:
            n += 1
            out.append(f"| {n} | {fmt(t)} | {d} | {plano} | {ve} | {habla} | {sfx} |")
            t += d
    return "\n".join(out), t, n

def main():
    t1, fin1, n1 = tabla(P1, 0, 0)
    t2, fin2, n2 = tabla(P2, 0, n1)
    largo_yt = fin1 + fin2
    todas = [x for e in P1+P2 for x in e[3]]
    def buscar(txt):
        acc = 0
        for i, x in enumerate(todas):
            if txt in x[2]:
                return i + 1, fmt(sum(y[0] for y in todas[:i]) if i < sum(len(e[3]) for e in P1) else sum(y[0] for y in todas[sum(len(e[3]) for e in P1):i]))
    n_mandado, t_mandado = buscar("señala con el ala los dos bultos")
    n_bartolo, _ = buscar("Bartolo se va caminando")
    n_camara, _ = buscar("acerca la pata a la cámara")
    sin_final = fin2 - 16
    md = f"""# Capítulo 1 · «Mi primer vlog (y casi me mata mi abuela)» · parte 4: el guion

Guion y estructura toma por toma, todo en **vertical 9:16**. Todavía no son los prompts de Flow: eso es la parte 6.
Basado en la historia aprobada (`CAP01-HISTORIA.md`), el estudio de Gnomo Palomo y el manual de producción.

## Resumen

| | Duración | Tomas |
|---|---|---|
| **Parte 1** (reel del día 1) | **{fmt(fin1)}** | {n1} |
| **Parte 2** (reel del día 2) | **{fmt(sin_final)}** | {n2-n1-1} |
| **Video de YouTube** (parte 1 + parte 2 + 16 s de pantallas finales + chistes estirados) | **≈ {fmt(largo_yt+6)}** | {n2} |

- **Cada parte cabe en un Short** (máximo 3 minutos). La parte 1 de Gnomo con Santa duraba 2:50.
- **Muchas tomas salen de una sola generación** de Flow: en las conversaciones se genera una toma larga de cada
  personaje y se corta en pedazos (como hace Gnomo). Por eso las generaciones son bastantes menos que las tomas.
- **Subtítulos estilo Gnomo en todo** (blancos, negrita, borde negro). Las frases de Tocino en inglés salen traducidas.
- **Título** «EXTRAVÍO · VLOG 01» sobre la primera toma aérea (toma 7). Sin logo.
- **Regla nueva del mundo:** en El Hueco siempre es de noche (por eso pasan de la plaza de día a la olla de noche).
- **Groserías:** ninguna en los primeros 10 segundos.

## La canción

{LETRA}
## Parte 1 · el reel del día 1 ({fmt(fin1)})
{t1}

## Parte 2 · el reel del día 2 y el resto del video de YouTube ({fmt(sin_final)} + pantallas finales)
{t2}

## Revisión de continuidad (antes de pasar a voces y prompts)

- **Por qué están ahí, antes del minuto 1:** la abuela los manda a pagar la deuda con el café (toma {n_mandado}, ≈ {t_mandado}).
- **Cada frase responde a algo que ya se dijo o se vio:** la «cámara» la nombra Dizzy en el gancho; el «Tuerto» lo
  presenta el recuerdo y la canción antes de que aparezca; «perico» y «lucas» los dice Tocino antes de la canción;
  «Talento» del Tuerto repite el de Dizzy en el recuerdo; «diciembre» es el miedo de Tocino que ya está en su ficha.
- **Cómo llegan de un lugar a otro:** zarzo → corredor → camino (toma aérea) → pueblo (toma aérea) → plaza → esquina →
  olla (toma aérea) → escaleras → mercado → rincón → escaleras (la abuela) → camino al atardecer → cocina → zarzo.
- **Bartolo:** baja con ellos a El Hueco, le quitan los bultos, se va en silencio durante el dominó (toma
  {n_bartolo}) y vuelve con la abuela. Es el héroe callado del capítulo.
- **La cámara:** va en la gorra de Dizzy todo el capítulo; el Tuerto la toca en la toma {n_camara}; la abuela la
  recupera; de noche está en la repisa cuando se prende sola.
- **Un solo personaje habla por toma** en todas las tomas.
- **Mínimo tres encuadres distintos por escena** (general, medio y primer plano o inserto) en todas.
"""
    open(os.path.join(AQUI, "CAP01-GUION.md"), "w").write(md)
    print(fmt(fin1), fmt(sin_final), fmt(largo_yt), n1, n2)

if __name__ == "__main__":
    main()
