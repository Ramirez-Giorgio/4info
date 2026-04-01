print("lista prezzi - per terminare programma inserire 0\n")
n = float
i = 0
c = 0
while n != 0:
    n = float(input(f"inserisci prezzo prodotto {i} : "))
    i += 1
    c += n
print(f"prezzo totale prodotti: {c}")