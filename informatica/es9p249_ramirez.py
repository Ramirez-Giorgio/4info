with open("numeri_es9.txt", "w") as f:
    n = int(input("n valori: "))
    for i in range(n):
        numero = input("valore: ")
        f.write(numero + "\n")
cerca = input("numero da cercare: ")
contatore = 0
with open("numeri_es9.txt", "r") as f:
    for riga in f:
        if riga.strip() == cerca:
            contatore += 1
print(f"il numero {cerca} comprare {contatore}")