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
