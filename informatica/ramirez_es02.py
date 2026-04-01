n1 = int(input("inserisci il primo numero: "))
n2 = int(input("inserisci il secondo numero: "))
n3 = int(input("inserisci il terzo numero: "))
if n1 > n2 and n1>n3:
    print(f"{n1} è il numero maggiore")
elif n2 > n3 and n2 > n1:
    print(f"{n2} è il numero maggiore")
elif n3 > n2 and n3 > n1:
    print(f"{n3} è il numero maggiore")