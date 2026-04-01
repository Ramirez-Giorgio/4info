#es1
nfile = input("Inserisci il nome del file: ")
try:
    with open(nfile, "r") as f:
        print("file trovato")
        for riga in f:
            print(riga.strip())
except FileNotFoundError:
    print("Il file non esiste o il nome è errato.")
except PermissionError:
    print("no permessi")
