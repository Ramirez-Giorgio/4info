import csv
dati = [
    ['Nome', 'Età', 'Classe'],
    ['Marco', '14', '3A'],
    ['Giulia', '15', '3B'],['Sara', '14', '3A']
    ]

try:
    with open('studenti.csv', 'w', newline='') as file:
        scrittore = csv.writer(file)
        scrittore.writerows(dati)
    print("File studenti.csv creato con successo.")
except Exception as e:
    print(f"Errore durante la creazione: {e}")