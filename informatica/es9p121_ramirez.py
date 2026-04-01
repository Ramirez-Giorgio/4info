def punto_appartiene(m, q, xp, yp):
    return yp == m * xp + q

print("Controllo se un punto appartiene alla retta y = m*x + q")
m = float(input("Inserisci il coefficiente angolare m: "))
q = float(input("Inserisci il termine noto q: "))
xp = float(input("Inserisci la coordinata x del punto: "))
yp = float(input("Inserisci la coordinata y del punto: "))

if punto_appartiene(m, q, xp, yp):
    print("Il punto appartiene alla retta.")
else:
    print("Il punto NON appartiene alla retta.")
