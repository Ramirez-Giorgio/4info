#es3
try:
    c = 0
    with open("testo.txt", "r") as f:
        for riga in f:
            linee = len(riga.split())
            c += linee
    print(f"numero parole: {c}") 
except FileNotFoundError:
    print("Il file non esiste o il nome è errato.")
except PermissionError:
    print("no permessi")

