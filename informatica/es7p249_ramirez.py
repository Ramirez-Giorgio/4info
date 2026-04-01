nome_file = input("nome file: ")
try:
    with open(nome_file, "r") as f:
        contatore = 0
        for riga in f:
            contatore += 1
    print(f"n righe: {contatore}")
except FileNotFoundError:
    print("f non presente")
