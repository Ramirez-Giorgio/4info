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
