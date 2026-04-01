s = 0
c = 0
while True:
    try:
        n_in = input("Inserisci un numero intero: ")
        if n_in.lower() == "stop":
            break
        n = int(n_in)
        s += n
        c += 1
    except ValueError:
        print("Errore: devi inserire solo numeri validi.")
    except ZeroDivisionError:
        print("Errore diviisone invalida")
m = s / c
print(f"la media dei valori inseriti è {m:2f}")