#es1-3
auto = {'marca':'', 'modello':'', 'anno':'' }
marca_v = input('inserisci la marca della macchina:')
modello_v = input('inserisci il modello della macchina:')
anno_v = int(input('inserisci l anno della macchina:'))
auto['marca'] = marca_v
auto['modello'] = modello_v
auto['anno'] = anno_v

print(auto.get('modello','unknown'))
print(auto.get('anno','unknown'))

#es2
colore_v = input('inserisci il colore della macchina: ')
auto['colore'] = colore_v
print(f'dizionario\n chiavi:{auto.keys()} \n valori:{auto.values()}')

#es5-6
prezzi = {'mela': 0.5, 'banana': 0.8, 'arancia': 0.7}
for frutto in prezzi:
    prezzi[frutto] = prezzi[frutto] * 1.1

#es7-8
studente = {'nome': 'Marco', 'materie': ['info', 'telecom', 'sistemi']}
studente['materie'].append('TPSI')#le materie non sono un dizionario ma una lista quindi per aggiungere uso append

#es9
s = input('inserisci una stringa: ')
stringa = {}
for lettere in s:
    stringa[lettere] = stringa.get(lettere, 0) + 1
print(stringa)

#es10
studenti = {
    "Anna": {"eta": 16, "media": 8.5},
    "Marco": {"eta": 17, "media": 7.2},
    "Luca": {"eta": 16, "media": 9.1}
}
studmax = ""
mediamax = 0
for nome, dati in studenti.items():
    if dati["media"] > mediamax:
        mediamax = dati["media"]
        studmax = nome
print(f"Lo studente con la media più alta è: {studmax} (Media: {mediamax})")
somma_medie = 0
numero_studenti = len(studenti)
for dati in studenti.values():
    somma_medie += dati["media"]
if numero_studenti > 0:
    media_classe = somma_medie / numero_studenti
    print(f"La media della classe è: {media_classe:.2f}")
else:
    print("Nessuno studente presente per calcolare la media della classe.")

#es11
inventario_prodotti = {}
def menu_principale():
    while True:
        print("\n--- Menu ---")
        print("1. Aggiungere un prodotto")
        print("2. Cercare un prodotto")
        print("3. Eliminare un prodotto")
        print("4. Visualizzare l'intero inventario")
        print("5. Uscire")
        print("-"*40)

        scelta = input("Inserisci il numero dell'opzione desiderata (1-5): ")

        if scelta == '1':
            aggiungi_prodotto()
        elif scelta == '2':
            cerca_prodotto()
        elif scelta == '3':
            elimina_prodotto()
        elif scelta == '4':
            visualizza_inventario()
        elif scelta == '5':
            break
        else:
            print("valore non valido")

def aggiungi_prodotto():
    nome = input("Inserisci il nome del prodotto da aggiungere: ").strip()
    if nome == '':
        print("valore non valido")
        return

    if nome in inventario_prodotti:
        print(f"'{nome}' gia presente")
        return

    try:
        prezzo = float(input(f"Inserisci il prezzo per '{nome}': "))
        if prezzo <= 0:
             print("Il prezzo deve essere un numero positivo.")
             return
        inventario_prodotti[nome] = prezzo
        print(f"Prodotto '{nome}' (Prezzo: {prezzo:.2f}€) aggiunto con successo.")
    except ValueError:
        print("Input prezzo non valido. Inserisci un numero.")

def cerca_prodotto():
    nome = input("Inserisci il nome del prodotto da cercare: ").strip()
    if nome in inventario_prodotti:
        prezzo = inventario_prodotti[nome]
        print(f"Trovato: '{nome}' ha un prezzo di {prezzo:.2f}€.")
    else:
        print(f"Il prodotto '{nome}' non è presente nell'inventario.")

def elimina_prodotto():
    nome = input("Inserisci il nome del prodotto da eliminare: ").strip()
    if nome in inventario_prodotti:
        prezzo_eliminato = inventario_prodotti.pop(nome)
        print(f"Prodotto '{nome}' (Prezzo: {prezzo_eliminato:.2f}€)")
    else:
        print(f"Il prodotto '{nome}' non è presente nell'inventario.")

def visualizza_inventario():
    if not inventario_prodotti:
        print("L'inventario è attualmente vuoto.")
    else:
        print("\n--- Inventario Completo ---")
        for nome, prezzo in inventario_prodotti.items():
            print(f"- {nome}: {prezzo:.2f}€")
        print("-"*30)

if __name__ == "__main__":
    menu_principale()

