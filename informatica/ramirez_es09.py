import math
n = float(input("inserisci un numero decimale:"))
ad = math.floor(n)
ae = math.ceil(n)
va = math.fabs(n)
print(f"il numero {n} arrotondato per difetto è {ad} per eccesso è {ae} ed il valore assoluto è {va}")