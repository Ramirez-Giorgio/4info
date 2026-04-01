def maggiore(n1,n2):
    if n1 > n2:
        print(f"{n1} è più grande di {n2}")
    elif n2 > n1:
        print(f"{n2} è più grande di {n1}")
    else:
        print("i numeri inseriti sono uguali")
n1 = int(input("inserisci il primo numero: "))
n2 = int(input("inserisci il secondo numero: "))
maggiore(n1,n2)
