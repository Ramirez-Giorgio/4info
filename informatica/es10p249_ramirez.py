with open("studenti_es10.txt", "w") as f:
    n = int(input("n studenti: "))
    for i in range(n):
        nome = input("nome studente: ")
        classe = input("classe: ")
        f.write(nome + " - " + classe + "\n")
print("dati salvati\n")

print("\ndati nel file\n")
with open("studenti_es10.txt", "r") as f:
    for riga in f:
        print(riga.strip())