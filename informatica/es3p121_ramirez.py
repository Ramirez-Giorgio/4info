def successivi(n):
    if n <= 0:
        print("Inserisci un numero intero positivo!")
    else:
        print(f"I 5 numeri successivi a {n} sono:")
        for i in range(1, 6):   # da 1 a 5
            print(n + i, end=" ")
        print()  

num = int(input("Inserisci un numero intero positivo: "))
successivi(num)
