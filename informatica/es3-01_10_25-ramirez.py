import math
print("inserisci stop per uscire")
while True:
    try:
        n_in = input("Inserisci il primo numero: ")
        if n_in.lower() == "stop": #lower() -> minusc upper() -> maiuscolo
            break
        n = int(n_in)
        print(f"la radice di {n} è {math.sqrt(n):0.2f}")
        print(f"il logaritmo naturale di {n} è {math.log(n):0.2f}")
        print(f"il fattoriale di {n} è {math.factorial(n)}")
    except ValueError:
        print("valore non valido")
