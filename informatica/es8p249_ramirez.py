try:
    with open("tappe_es8.txt", "w") as f:
        n = int(input("n tappe: "))
        for i in range(n):
            distanza = float(input("inserisci distanza: "))
            f.write(distanza + "\n")
    somma = 0
    contatore = 0
    with open("tappe_es8.txt", "r") as f:
        for riga in f:
            somma += riga.strip()
            contatore += 1
    if contatore > 0:
        media = somma / contatore
        print(f"distanza media:{media}")
    else:
        print("file vuoto")
except FileNotFoundError:
    print("file non trivato")
except PermissionError:
    print("no permessp")