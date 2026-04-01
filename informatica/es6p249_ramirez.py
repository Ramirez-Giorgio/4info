with open("numeri_es6.txt", "w") as f:
    n = int(input("n valori: "))
    for i in range(n):
        num = input("Inserisci valore: ")
        f.write(num + "\n")
with open("numeri_es6.txt", "r") as f:
    numeri = []
    for riga in f:
        numeri.append(riga.strip())
for n in numeri:
    valore = float(n)
    print(f"valore:{valore} , valore+20%: {valore*1.2}")

