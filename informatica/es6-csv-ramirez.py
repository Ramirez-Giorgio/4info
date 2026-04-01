import csv
dati = [['Matita', '0.50', '300']]

try:
    with open('prodotti.csv', 'a', newline='') as file:
        scrittore = csv.writer(file)
        scrittore.writerows(dati)
    print("File studenti.csv aggiornato")

    with open('prodotti.csv', 'r', newline='') as file:
        lettore_diz=csv.DictReader(file)
        for riga in lettore_diz:
            print(dict(riga))
except Exception as e:
    print(f"Errore durante la creazione: {e}")