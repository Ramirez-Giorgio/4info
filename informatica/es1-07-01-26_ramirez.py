dati_salvati = []
for i in range(1,4):
    print(f"\n inserisci dati persona {i}")
    nome=input("nome: ")
    cognome=input("cognome: ")
    citta=input("citta: ")
    nazione=input("nazione: ")
    persona = {
            "id": i,
            "nome": nome,
            "cognome": cognome,
            "citta": citta,
            "nazione": nazione
        }  
    dati_salvati.append(persona)

with open("anagrafica.txt", "w") as f:
    for persona in dati_salvati:
        riga = (
                    f"{persona['id']};"
                    f"{persona['nome']};"
                    f"{persona['cognome']};"
                    f"{persona['citta']};"
                    f"{persona['nazione']}\n"
                )        
        f.write(riga)
print("\nDati salvati su file.")

dati_file = []
with open("anagrafica.txt", "r") as f:
    for riga in f:
        dati = riga.strip().split(";")
        persona = {
            "id": int(dati[0]),
            "nome": dati[1],
            "cognome": dati[2],
            "citta": dati[3],
            "nazione": dati[4]
            }       
        dati_file.append(persona)

cerca = int(input("\nInserisci l'id da cercare: "))
trova=0
for persona in dati_file:
    if persona["id"] == cerca:
        print(f"id: {persona['id']}")
        print(f"nome: {persona['nome']}")
        print(f"cognome: {persona['cognome']}")
        print(f"citta: {persona['citta']}")
        print(f"nazione: {persona['nazione']}")
        trova=1

if trova==0:
    print("id non presente")
