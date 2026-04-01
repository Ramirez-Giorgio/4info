archivio = []

# Inserimento dati
for i in range(1, 4):
    print(f"\nDati persona {i}")
    nome = input("Nome: ")
    cognome = input("Cognome: ")
    citta = input("Città: ")
    nazione = input("Nazione: ")

    persona = {
        "ID": i,
        "Nome": nome,
        "Cognome": cognome,
        "Città": citta,
        "Nazione": nazione
    }

    archivio.append(persona)

# Scrittura su file
with open("anagrafica.txt", "w", encoding="utf-8") as f:
    for persona in archivio:
        riga = (
            f"{persona['ID']};"
            f"{persona['Nome']};"
            f"{persona['Cognome']};"
            f"{persona['Città']};"
            f"{persona['Nazione']}\n"
        )
        f.write(riga)

print("\nDati salvati su file.")

# Lettura dal file
archivio_file = []

with open("anagrafica.txt", "r", encoding="utf-8") as f:
    for riga in f:
        dati = riga.strip().split(";")

        persona = {
            "ID": int(dati[0]),
            "Nome": dati[1],
            "Cognome": dati[2],
            "Città": dati[3],
            "Nazione": dati[4]
        }

        archivio_file.append(persona)

# Ricerca per ID
cerca = int(input("\nInserisci l'ID da cercare: "))
trovato = False

for persona in archivio_file:
    if persona["ID"] == cerca:
        print("\nPersona trovata:")
        print(f"ID: {persona['ID']}")
        print(f"Nome: {persona['Nome']}")
        print(f"Cognome: {persona['Cognome']}")
        print(f"Città: {persona['Città']}")
        print(f"Nazione: {persona['Nazione']}")
        trovato = True
        break

if not trovato:
    print("ID non presente nell'archivio.")
