# ScontoProgressivo.py: sconto progressivo sui prodotti
# input dei dati
pezzi = int(input("Pezzi acquistati: "))
prezzo = float(input("Prezzo del prodotto: "))
# determina lo sconto con una selezione multipla
if pezzi == 1 or pezzi == 2 or pezzi == 3:
    sconto = 5
elif pezzi == 4 or pezzi == 5:
    sconto = 10
elif pezzi >= 6 and pezzi <= 10:
    sconto = 20
else:
    sconto = 30
# calcolo e output del risultato
importo = pezzi * prezzo * (100.0 - sconto) / 100.0
print("Importo da pagare = {:12.2f} euro".format(importo))
