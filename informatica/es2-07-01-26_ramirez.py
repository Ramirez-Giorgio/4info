with open("valori.txt", "w") as f:
    for i in range(5):
        numero = int(input(f"Inserisci il numero {i+1}: "))
        f.write(str(numero) + "\n")

numeri_file = []
with open("valori.txt", "r") as f:
    for riga in f:
        numeri_file.append(int(riga.strip()))
somma = sum(numeri_file)
print(f"\n somma: {somma}")
aumento_numeri = {}
for n in numeri_file:
    aumento_numeri[n] = n + (n * 20 / 100)

with open("risultati_incrementati.txt", "w") as f:
    for prima, dopo in aumento_numeri.items():
        f.write(f"{prima} --> {dopo}\n")