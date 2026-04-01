# Calcolatrice semplice con + - * / con 25/09/25
print("Calcolatrice (+  -  *  /)")
print("Digita 'e' per uscire.\n")

while True:
    try:
        # Primo numero
        a_in = input("Inserisci il primo numero: ")
        if a_in.lower() == "e": #lower() -> minusc upper() -> maiuscolo
            break
        a = float(a_in)

        # Operatore
        op = input("Scegli l'operatore (+ - * /): ")
        if op.lower() == "e":
            break

        # Secondo numero
        b_in = input("Inserisci il secondo numero: ")
        if b_in.lower() == "e":
            break
        b = float(b_in)

        # Calcolo
        if op == "+":
            risultato = a + b
        elif op == "-":
            risultato = a - b
        elif op == "*":
            risultato = a * b
        elif op == "/":
            if b == 0:
                if a == 0:
                    risultato = "indeterminata (0/0)"
                else:
                    risultato = "impossibile (divisione per zero)"
            else:
                risultato = a / b
        else:
            print("Operatore non valido!")
            continue

        # Stampa risultato
        print("Risultato:", risultato)

    except ValueError:
        print("Errore: devi inserire solo numeri validi.")
    except Exception as e:
        print("Errore imprevisto:", e)

print("Fine!")