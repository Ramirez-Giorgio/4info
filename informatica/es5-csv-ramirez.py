import csv
dati = [
    ['Prodotto', 'Prezzo', 'Quantita'],
    ['Penna', '1.20', '100'],
    ['Quaderno', '2.50', '2.50'],
    ['Gomma', '0.80', '200']
    ]

try:
    with open('prodotti.csv', 'w', newline='') as file:
        scrittore = csv.writer(file)
        scrittore.writerows(dati)
    print("File studenti.csv creato con successo.")

    with open('prodotti.csv', 'r', newline='') as file:
        lettore_diz=csv.DictReader(file)
        for riga in lettore_diz:
            print(dict(riga))
except Exception as e:
    print(f"Errore durante la creazione: {e}")