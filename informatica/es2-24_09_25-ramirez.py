#inserire un numero intero da testiera calcola somma dei quadrati
c = 0
try: 
    n1 = int(input("inserisci un numero intero da testiera: "))
    for i in range (n1 + 1):
        n = i*i 
        c += n    
    print(f"somma dei quadrati di {n1} è uguale a {c} ")
except ValueError:
    print("valore non valido!!")