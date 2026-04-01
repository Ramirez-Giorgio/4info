#es19 
lista_comuni = []

s = int(input("inserisci il numero lista: "))
for i in range(s):
    comune = input("Inserisci comune: ")
    lista_comuni.append(comune.lower())
print(lista_comuni)
cerca = input("inserisci comune da cercare: ").lower()
c = 0
for comune in lista_comuni:
    if comune == cerca:
        c += 1
if c > 0:
    print(f"{cerca} compare {c} volte")
else:
    print("comune inesistente")

#es20
lista_comuni = []

s = int(input("inserisci il numero lista: "))
for i in range(s):
    comune = input("Inserisci comune: ")
    lista_comuni.append(comune.lower())
print(lista_comuni)
c = 0
cerca = lista_comuni[1]
for i in lista_comuni:
    if cerca != lista_comuni[i]:
        c += 1
if c > 0:
    print(f"gli studenti vengono da {c} comuni")

#es21
numeri = []

n = int(input("Quanti numeri vuoi inserire? "))
for i in range(n):
    numeri.append(int(input("Inserisci un numero: ")))

risultato = []

for num in numeri:
    if num < 100:
        risultato.append(num * 2)
    else:
        risultato.append(num * 3)

print("Array risultante:", risultato)

#es22
classe_1A = []
classe_1B = []

n1 = int(input("Quanti cognomi in 1A? "))
for i in range(n1):
    classe_1A.append(input("Cognome 1A: "))

n2 = int(input("Quanti cognomi in 1B? "))
for i in range(n2):
    classe_1B.append(input("Cognome 1B: "))

uniti = classe_1A + classe_1B
uniti.sort()
#sorted crea una seconda lista con gli elementi ordinati

print("Elenco alfabetico:", uniti)

#es23
tempi = []

n = int(input("Quanti tempi vuoi inserire? "))
for i in range(n):
    tempi.append(float(input("Inserisci un tempo: ")))

tempi_ordinati = sorted(tempi)
migliori_3 = tempi_ordinati[:3]

print("I tre migliori tempi sono:", migliori_3)

#es24
prodotti = {}
n = int(input("Quanti prodotti vuoi inserire? "))
    
for i in range(n):
    nome = input("Nome prodotto: ")
    prezzo = float(input("Prezzo prodotto: "))
    prodotti[nome] = prezzo

percentuale = float(input("Percentuale aumento prezzo: "))

def incrementa(prezzo, perc):
    return prezzo * (1 + perc / 100)

print("\nPrezzi aggiornati:")
for nome, prezzo in prodotti.items():
    nuovo = incrementa(prezzo, percentuale)
    print(nome, "→", round(nuovo, 2))

#es25
voti = {}
for i in range (30):
    matricola = input("inserisci la matricola: ")
    voto = int(input(f"inserisci il voto di {matricola}: "))
    voti[matricola] = voto
voti_srtd = sorted(voti)
print(voti_srtd)

#es26
voti = {}
n = int(input("Quanti studenti? "))

for i in range(n):
    matr = int(input("Matricola: "))
    voto = int(input("Voto: "))
    voti[matr] = voto

media = sum(voti.values()) / len(voti)
print("Media voti:", round(media, 2))

superiori = [m for m, v in voti.items() if v > media]
print("Matricole con voto superiore alla media:", superiori)

#27
rubrica = {}

n = int(input("Quante persone vuoi inserire in rubrica? "))
for _ in range(n):
    nome = input("Nome: ")
    numero = input("Numero: ")
    rubrica[nome] = numero

cerca = input("Chi vuoi cercare? ")

if cerca in rubrica:
    print("Numero di", cerca + ":", rubrica[cerca])
else:
    print("La persona non è presente in rubrica.")
