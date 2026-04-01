voto1 = float(input("inserisci il voto n1: "))
voto2 = float(input("inserisci il voto n2: "))
voto3 = float(input("inserisci il voto n3: "))
if (2 < voto1 > 10) and (2 < voto2 > 10) and (2 < voto3 > 10):
    somma = voto1 + voto2 + voto3
    media = somma / 3
    print(f"la media dei voti è {media}")
else:
    print("voto non valido")
