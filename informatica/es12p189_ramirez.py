parole = []

print("inserisci * per terminare")
try: 
    while True:
        parola = input("parola: ")
        if parola == "*":
            break
        parole.append(parola)
    print("Numero di parole inserite:", len(parole))
    print(parole)
    parole = []
except ValueError:
    print("valore non valido inseriscp stringhe")