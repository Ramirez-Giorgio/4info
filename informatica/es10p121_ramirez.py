def acquisisci_dati():
    tot = 0
    c = 0
    n = int(input("Quanti reparti vuoi inserire? : "))
    i = 0
    while i < n:
        nome = input(f"Inserisci il nome del reparto {i+1}: ")
        incasso = float(input(f"Inserisci l'incasso giornaliero del reparto '{nome}': "))
        tot += incasso
        c += 1
        i += 1
    return totale, contatore

def calcola_media(totale, contatore):
    if contatore == 0:
        return 0
    return totale / contatore

print("Calcolo dell'incasso medio dei reparti\n")
totale, contatore = acquisisci_dati()
media = calcola_media(totale, contatore)
print(f"L'incasso medio giornaliero è: {media:.2f} €")
