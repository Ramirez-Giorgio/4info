sq1 = int(input("inserisci i punti della squadra 1: "))
sq2 = int(input("inserisci i punti della squadra 2: "))
if sq1 == sq2:
    print("punti non validi")
elif sq1 > sq2:
    print("ha vinto la squadra 1")
else:
    print("ha vinto la squadra 2")
