#sommare numeri inseriti da tastiera finche non superano 100 numeri
c = 0
s = 0
while s <= 100:
    try: 
        c += 1
        n = int(input(f"inserisci un il valore {c} :"))
        s += n
    except ValueError:
        print("valore non valido")
        c -= 1
print(f"somma maggiore di 100 valori totali inseriti {c}")