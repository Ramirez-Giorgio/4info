import csv
try:
    with open('studenti.csv', 'r', encoding='utf-8') as file:
        lettore = csv.reader(file)
        for riga in lettore:
            print(riga) # Stampa ogni riga come lista
except FileNotFoundError:
    print("Errore: Il file studenti.csv non esiste.")