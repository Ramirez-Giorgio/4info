#es2
try: 
    with open("studenti2.txt", "w") as f:
        print("Inserisci 5 nomi:")
        for i in range(5):
            nome = input("Nome: ")
            f.write(nome + "\n")
    with open("studenti.txt", "a") as f:
        print("\nAggiungi altri 2 nomi:")
        for i in range(2):
            nome = input("Nome aggiuntivo: ")
            f.write(nome + "\n")
except FileExistsError:
    print("file esiste gia!")