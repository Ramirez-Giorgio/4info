def media():
    n_valori = int(input("Quanti numeri vuoi inserire? "))
    if n_valori <= 0:
        print("numero di valori deve essere positivo.")
        return

    somma = 0
    for i in range(n_valori):
        valore = float(input(f"Inserisci il valore {i+1}: "))
        somma += valore

    media_ar = somma / n_valori
    print(f"La media aritmetica è: {media_ar:.2f}")

media()
