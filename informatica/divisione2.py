# divisione2.py : divisione tra interi con sottrazioni successive
# e controllo sul divisore
# inizializzazione delle variabili
a = 0  # dividendo
b = 0  # divisore
quoziente = 0  # quoziente
# input dei dati
a = int(input("Dividendo: "))
while b == 0:
    b = int(input("Divisore: "))
# ripetizione delle sottrazioni e conteggio
while a >= b:
    a = a - b
    quoziente = quoziente + 1
# output dei risultati
print("Quoziente =", quoziente)
print("Resto =", a)
