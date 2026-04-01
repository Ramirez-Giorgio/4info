with open("insegnanties12.txt", "w") as f:
    n = int(input("Numero insegnanti: "))
    for i in range(n):
        nome = input("Nome insegnante: ")
        materia = input("Materia: ")
        f.write(nome + "-" + materia + "\n")
cerca = input("Inserisci nome insegnante da cercare: ")
trovato = 0
with open("insegnanties12.txt", "r") as f:
    for riga in f:
        dati = riga.split("-")
        nome = dati[0]
        materia = dati[1]
        if nome == cerca:
            print("Materia:", materia)
            trovato = 1
if trovato == 0:
    print("Insegnante non presente")
