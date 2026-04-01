import math

d = int(input("inserisci la diagonale: "))
n = d / math.sqrt(2)
p = n * 4
a = n**2
print(f"data la diagonale {d}, il perimetro è {p} e l'area è {a}")
