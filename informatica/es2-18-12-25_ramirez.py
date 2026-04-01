with open("valori.txt", "w") as f:
    f.write("10\n5\n15\n20\n")
numeri = []
with open("valori.txt", "r") as f:
    for riga in f:
        numeri.append(int(riga.strip()))
somma = sum(numeri)
print("Somma dei numeri:", somma)
incrementi = {}
for numero in numeri:
    incremento = numero + 1
    incrementi[numero] = incremento
with open("valori.txt", "a") as f:
    for originale, incrementato in incrementi.items():
        f.write(f"{originale}==>{incrementato}\n")
