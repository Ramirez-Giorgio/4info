try:
    with open("studenti.txt", "r") as fini:
        with open("copia.txt", "w") as ffine:
            for riga in fini:
                ffine.write(riga)
    print("Copia completata.")
except FileNotFoundError:
    print("file non trovato")
except PermissionError:
    print("no permessi")
