import math 
n = int(input("inserisci un numero positivo:"))
ln = math.log(n)
ld = math.log10(n)
print(f"il logaritmo naturale di {n} è {ln:2f} mentre in base 10 è {ld:2f}")