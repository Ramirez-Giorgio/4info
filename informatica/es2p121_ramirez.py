import math

def ax(a, b, c):
    d = b**2 - 4*a*c
    if d < 0:
        print("La parabola non interseca l'asse x (nessuna radice reale).")
    elif d == 0:
        x = -b / (2*a)
        print(f"La parabola tocca l'asse x in un solo punto: x = {x:.2f}")
    else:
        x1 = (-b + math.sqrt(d)) / (2*a)
        x2 = (-b - math.sqrt(d)) / (2*a)
        print(f"La parabola interseca l'asse x in x = {x1:.2f} e x = {x2:.2f}")

def ay(c):
    print(f"La parabola interseca l'asse y nel punto (0, {c})")

def vertice(a, b, c):
    x = -b / (2*a)
    y = -(b**2 - 4*a*c) / (4*a)
    print(f"Il vertice si trova nel punto ({x:.2f}, {y:.2f})")

# Inprut
a = int(input("Inserisci il valore di a: "))
b = int(input("Inserisci il valore di b: "))
c = int(input("Inserisci il valore di c: "))

# Funzini
ax(a, b, c)
ay(c)
vertice(a, b, c)
