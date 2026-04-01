# Crea un programma che permetta di inserire 3 paia di sneakers.

# Per ogni scarpa, chiedi all'utente: Modello, Taglia e Prezzo.

# Salva ogni scarpa in un dizionario.

# Aggiungi ogni dizionario a una lista chiamata stock.

# Cicla la lista e scrivi i dati in un file chiamato inventario.txt. Ogni riga nel file deve essere nel formato: modello,taglia,prezzo.

# Piccola mano (Suggerimento):
# Per scrivere nel file, usa open("inventario.txt", "w"). Quando scrivi la riga, ricordati di aggiungere \n alla fine per andare a capo, altrimenti ti ritrovi un ammasso di testo illeggibile!

#es1
try: 
    stock = []

    for i in range(3):
        print(f'---scarpe n{i+1}---')
        modello = input('inserisci modello scarpe: ')
        taglia = int(input('inserisci taglia scarpe: '))
        prezzo = int(input('inserisci prezzo scarpe: '))
        scarpa = {
            'modello' :modello,
            'taglia':taglia,
            'prezzo':prezzo
        }
        stock.append(scarpa)

    with open('stockscarpe.txt','w') as f:
        for s in stock :
            linea = f"{s['modello']},{s['taglia']},{s['prezzo']}"
            f.write(linea).strip()
        print('stock salvato\n')
except ValueError:
    print('valore non valido')

#es2
# Esercizio 2: Il "Check" (Lettura e Manipolazione)
# Il tuo compito:
# Adesso dobbiamo recuperare quei dati per lavorarci su.

# Leggi il file inventario.txt.

# Per ogni riga, trasforma i dati di nuovo in un dizionario.

# Inserisci tutti i dizionari in una nuova lista chiamata archivio.

# Obiettivo extra: Calcola il valore totale (somma dei prezzi) di tutto il tuo inventario e stampalo.

# Piccola mano (Suggerimento):
# Quando leggi una riga dal file (es: "Jordan1,42,150\n"), usa .strip() per levare il "vai a capo" e poi .split(",") per ottenere una lista di tre elementi. Occhio che quando leggi dal file è tutto testo (string), quindi per sommare i prezzi dovrai convertirli in numeri usando float() o int().
try:
    archivio = []
    with open('stockscarpe.txt','r') as f:
        print('---stock attuale---')
        for riga in f:
            dati = riga.strip().split(',')
            modello = dati[0]
            taglia = int(dati[1])
            print(f'modello: {modello} | taglia: {taglia}')
            prezzo = int(dati[2])
            scarpa_recuperata = {
                'modello':modello,'taglia':taglia,'prezzo':prezzo
            }
            archivio.append(scarpa_recuperata)

    print(f'archivio attuale salvato in una lista\n {archivio}')
except FileNotFoundError :
    print('file non trovato')
except FileExistsError:
    print('file non esiste')