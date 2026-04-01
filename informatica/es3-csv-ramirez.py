import csv# Convertire una stringa in numero per fare dei calcoli
# Creazione file numeri.csv
with open('numeri.csv', 'w', newline='') as f:
    f.write("Numero\n10\n20\n30\n40")
totale = 0
try:
    with open('numeri.csv', 'r') as file:
        lettore = csv.DictReader(file)
# Uso DictReader per accedere alla colonna per nome, cerca il nome della colonna e non la sua
# posizione. Il metodo csv.DictReader è uno strumento del modulo csv che legge le righe di un
# file CSV non come semplici liste, ma come dizionari.
        for riga in lettore:
            totale += int(riga['Numero'])
    print(f"Il totale è: {totale}") # Output atteso: 100
except Exception as e:
    print(f"Errore: {e}")