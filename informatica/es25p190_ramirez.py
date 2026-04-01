#es 25
voti = {}
n = int(input("numero studenti da inserire: "))
for i in range(n):
    matricola = input(f"Inserisci la matricola dello studente {i+1}: ")
    voto = int(input(f"Inserisci il voto di {matricola}: "))
    voti[matricola] = voto



