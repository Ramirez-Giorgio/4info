while True:
    try:
        n = int(input("inserisci un numero intero: "))
        if n<0 :
            break
        else:
            f= 1
            for i in range(1, n + 1):
                f *= i
            print(f"il fattoriale di {n} è {f}")
    except ValueError:
        print("valore non valido")
print("programma finito numero minore di 0 inserito")