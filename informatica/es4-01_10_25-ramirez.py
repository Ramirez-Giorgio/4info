while True:
    try:
        n = int(input("inserisci un numero :"))
        if n <= 0:
            raise ValueError("numero non valido")
        for i in  range(1,51):
            if i % n != 0:
                continue
            print(i)
            if i % 10 == 0 and i != 0:
                print(f"{i} è multiplo di {n} e di 10")
                break
    except ValueError as e:
        print(f"Errore: {e}")