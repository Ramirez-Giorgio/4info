#convertitore di votido nypà7vncygr 
while True:
    n = int(input("inserisci il voto:"))
    if n > 10 or n <= 0:
        break
    elif n <= 4:
        print("voto gravemente insufficente")
    elif n == 5:
        print("voto insufficente")
    elif n == 6:
        print("voto sufficente")
    elif n == 7:
        print("voto discreto")
    elif n == 8:
        print("voto buono")
    elif n == 9:
        print("voto distinto")
    elif n == 10:
        print("voto ottimo")
print("programma concluso")