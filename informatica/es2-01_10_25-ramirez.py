while True:
    try:
        frase = input("inserisci una frase: ")
        print("la frase in maiuscolo è", frase.lower())
        print("la frase in minoscolo è", frase.upper())
        print("la frase invertiti è", frase[::-1 ])
    except SyntaxError:
        print("input non valido!")