import csv

class Libro:
    def __init__(self, titolo, autore, pagine):
        self.titolo = str(titolo)
        self.autore = str(autore)
        self.pagine = int(pagine)
    
    def __str__(self):
        # Questo formato deve corrispondere esattamente alle colonne del CSV
        return f'{self.titolo.upper()};{self.autore.capitalize()};{self.pagine}'

def leggi_libreria():
    libri_caricati = []
    try:
        with open('libreria.csv', 'r') as f:
            # FIX 1: Bisogna specificare il delimitatore ';'
            reader = csv.DictReader(f, delimiter=';')
            for riga in reader:
                # I nomi tra parentesi devono essere identici all'intestazione del file
                nuovo = Libro(riga['TITOLO'], riga['AUTORE'], riga['Npagine'])
                libri_caricati.append(nuovo)
        
        if not libri_caricati:
            print("La libreria è vuota.")
        else:
            for i in libri_caricati:
                print(f"Libro trovato: {i}") # Chiama automaticamente __str__

    except FileNotFoundError:
        print("Errore: il file libreria.csv non esiste ancora!")

def inserisci():
    titolo = input('inserisci nome libro: ')
    autore = input('inserisci nome autore: ')
    pagine = input('inserisci numero di pagine: ')
    nuovo_libro = Libro(titolo, autore, pagine)
    
    print('Salvataggio nel file csv...')
    # Nota: 'w' sovrascrive il file ogni volta. 
    with open('libreria.csv', 'a') as f:
        # FIX 2: Aggiungere \n alla fine della riga
        f.write(str(nuovo_libro) + '\n')
    print('Dati salvati.')

def main():
    try:
        scelta = int(input('1 leggi - 2 scrivi: '))
        if scelta == 1:
            leggi_libreria()
        elif scelta == 2:
            inserisci()
        else:
            print('Scelta invalida.')
    except ValueError:
        print("Per favore, inserisci un numero (1 o 2).")

if __name__ == "__main__":
    main()