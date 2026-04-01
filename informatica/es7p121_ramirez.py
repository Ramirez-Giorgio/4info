def sconto(n,s):
    ps = (n*s)/100
    pds = n - ps
    print(f"il prezzo dopo lo sconto è {pds}")

n = int(input("inserisci il prezzo: "))
s = int(input("inserisci la percentuale di sconto: "))
sconto(n,s)