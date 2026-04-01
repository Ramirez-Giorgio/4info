import math
c1 = int(input("inserisci il primo cateto: "))
c2 = int(input("inserisci il secondo cateto: "))
i = math.hypot(c1,c2)
print(f"l'ipotenusa dati i cateti {c1} e {c2} è di {i:2f}")