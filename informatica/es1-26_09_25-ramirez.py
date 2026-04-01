#chiedi all utente numero n maggiore = 0 e fare fattoriale altrimenti scrivere operazione impossibile 

import math
while True:
    try:
        n = int(input("inserisci un numero intero: "))
        if n<0 :
            break
        else:
            r = math.factorial(n)
        print(f"il fattoriale di {n} è {r}")
    except ValueError:
        print("valore non valido")
print("programma finito numero minore di 0 inserito")