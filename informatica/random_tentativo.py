import random
segreto = random.randint(1,50) #range del random
tentativo = 0 #tentativi che fa l'utente
c = 5 #numero di tentativi rimanenti
while tentativo != segreto:
    tentativo = int(input("indovina il numero (1-50): "))
    if tentativo < segreto and c > 0:
        print("troppo basso!")
        c -= 1
    elif tentativo > segreto and c>0:
        print("troppo alto!")
        c -= 1
    elif tentativo == segreto :
        print("bravo hai indovinato!")
        break
    elif c == 0:
        print(f"HAI PERSO il numero era {segreto}!!")