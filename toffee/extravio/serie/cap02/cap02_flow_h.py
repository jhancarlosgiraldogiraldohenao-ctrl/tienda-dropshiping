# Capítulo 2 · parte 1 en HORIZONTAL 16:9 (decisión de Jay, 8-nov-2026, tras la prueba de la calle de México).
# Reusa guion, candados y lugares de cap02_flow.py; cambia el encabezado a 16:9, refuerza el fondo vivo y la cámara de cine.
import cap02_flow as F
H_HEAD=("Horizontal 16:9, {d} seconds. High-quality 3D animated movie style like a big-budget animated feature film, exactly the same look as the character reference images, "
        "rich cinematic lighting, shallow depth of field, normal lens (no fisheye, no vignette, no dark corners). One continuous shot with no cuts, full frame from edge to edge, no black bars.")
VIVO={
 "ZARZO-NOCHE":"The background is alive: the candle flame flickers, dust floats in the moonlight, the curtain of the round window sways and fireflies blink far outside",
 "PUEBLO-CALLE":"The background is alive: moths circle the street lamp, a curtain moves in a lit window, dry leaves blow along the street and thin fog drifts slowly between the houses",
 "CALLEJON":F.FONDO["CALLEJON"]+"; water drips from a broken gutter and a torn poster flaps on the wall",
 "CALLEJON-ABIERTO":F.FONDO["CALLEJON-ABIERTO"]+"; water drips from a broken gutter and a torn poster flaps on the wall",
 "TUNEL":F.FONDO["TUNEL"],
 "MX-ALTAR":"The background is alive: hundreds of candle flames flicker, marigold petals float in the warm air, cut paper flags flutter above and small colorful fireworks burst very far away in the sky",
 "MX-CALLE":"The background is fully alive: small chihuahua mariachi musicians in black charro suits play on a corner; animal neighbors (a turtle, a parrot, a donkey and an iguana) walk by in both directions carrying flowers and candles; cut paper flags flutter; marigold petals blow across the street; candles flicker; small fireworks burst very far away. All background characters stay out of focus and never look at the camera",
 "MX-MERCADO":"The background is fully alive: animal vendors (an old turtle, a green parrot, an iguana) tend their stalls out of focus, paper lanterns sway, steam rises from clay pots, piñatas spin slowly and cut paper flags flutter; they never look at the camera",
 "MX-ESCONDITE":F.FONDO["MX-ESCONDITE"]+"; through the gap of the tablecloth we see blurred feet of market animals walking by outside",
}
# cámara de cine en 16:9 (si no está aquí, se usa la del guion vertical)
ACC={"T02":"He climbs up onto the window frame with his back to the camera, squeezes through the small round window and jumps out into the night; he never turns around and never comes back inside; his tail disappears last and for the final second the window is empty"}
CAM={"T01":"Medium close-up, the rat sits on the left third of the frame, the round moonlit window and the candle visible on the right side; the camera slowly pushes in, his whole head, cap and camera always inside the frame; both of his eyes look straight into the lens, never cross-eyed"}
# tomas que se rehacen en horizontal (orden de la edición). Fuera: T04 (sin voz) y T13 (Jay: no va el gancho de la alcantarilla).
ORDEN=["T01","T02","T03","T06","T07","T07b","T08","T09","T10","T11","T14","T15","T16","T17","T18","T19","T20","T21",
       "T22","T23","T24","T25","T26","T27","T28","T29","T30","T31","T33","T34","T35"]
R360={"T02","T07b","T08","T09","T10","T11","T14","T15","T18","T26","T28","T33"}  # planos abiertos o de acción: 360p + Claude los sube
DUR={"T01":8,"T02":6,"T03":8,"T06":6,"T07":6,"T07b":4,"T08":4,"T09":6,"T10":6,"T11":6,"T14":6,"T15":5,"T16":6,"T17":4,
     "T18":8,"T19":6,"T20":6,"T21":6,"T22":4,"T23":8,"T24":4,"T25":6,"T26":6,"T27":6,"T28":4,"T29":8,"T30":4,"T31":8,
     "T33":4,"T34":6,"T35":4}
def tomas():
    T={g[0]:g for g in F.P1}
    for g in F.P1B+F.P1C: T[g[0]]=g
    return T
def prompt(tid):
    g=list(tomas()[tid]); g[1]=DUR[tid]
    if tid in CAM: g[5]=CAM[tid]
    if tid in ACC: g[7]=ACC[tid]
    p=F.prompt(tuple(g))
    p=p.replace(F.HEAD.format(d=g[1]),H_HEAD.format(d=g[1]))
    p=p.replace(F.FONDO[g[2]]+".",VIVO.get(g[2],F.FONDO[g[2]])+".")
    return p
AEREAS_H=[("A-FINCA",6,"AEREA-FINCA-NOCHE.jpg","Horizontal 16:9, 6 seconds. Cinematic aerial drone shot of the lonely two-story coffee farmhouse on the green mountain from the reference image at midnight, exactly the same place: white walls, wooden balconies, warm light in the windows, smoke from the chimney, coffee plants and banana trees around it, misty mountains behind under a full moon and a starry sky. The drone slowly glides forward and down toward the house. Fireflies blink in the coffee plants and the mist moves slowly. It is night, not day. One continuous shot with no cuts, full frame from edge to edge, normal lens, no black bars. No characters, no animals, no people, no text, no music; only crickets and soft wind.")]
AEREAS_H+=[(a,d,f,p.replace("Vertical 9:16","Horizontal 16:9").replace("full vertical frame","full frame from edge to edge")) for a,d,f,p in F.AEREAS]
if __name__=="__main__":
    tot=sum(DUR[t]*(1 if t in R360 else 3) for t in ORDEN)+sum(a[1] for a in AEREAS_H)
    print("créditos aprox.:",tot)
    for t in ORDEN: print(t,DUR[t],"360p" if t in R360 else "720p")
