import classcalcolatrice as calc

try:
    while True:
        a = int(input("Inserisci a: "))
        b = int(input("Inserisci b: "))
        calcolatrice = calc.Calcolatrice(a, b)
        op = int(input(
            """\nScegli operazione:"
            1 somma"
            2 sottrazione
            3 moltiplicazione
            4 divisione
            5 potenza
            6 quadrato
            7 logaritmo
            8 fattoriale
            9 radice
            scelta: """
        ))
        if op == 1:
            print(calcolatrice.somma())
        elif op == 2:
            print(calcolatrice.sottrazione())
        elif op == 3:
            print(calcolatrice.moltiplicazione())
        elif op == 4:
            print(calcolatrice.divisione())
        elif op == 5:
            print(calcolatrice.potenza())
        elif op == 6:
            print(calcolatrice.quadrato())
        elif op == 7:
            print(calcolatrice.logaritmo())
        elif op == 8:
            print(calcolatrice.fattoriale())
        elif op == 9:
            print(calcolatrice.radice())
        else:
            print("Operazione non valida")

        c = input("\nVuoi continuare (s/n): ").lower()
        if c == "n":
            break

except ValueError as e:
    print("Errore:", e)
