inventory = []

def vedi_inventario():
    if len(inventory) == 0:
        print("Inventario vuoto")
        return    
    print(f"\n{inventory}\n")

def aggiungi(oggetto):
    if oggetto != "":
        oggetto = oggetto.strip().capitalize()
        inventory.append(oggetto)
        print(f"{oggetto} aggiunto all'inventario.\n")
    else:
        print("valore non valido")

def ricerca(keyword):
    pkeyword = keyword.strip().lower()
    if len(pkeyword) == 0:
        print("parola non valida")
        return
    results = []    
    for item in inventory:
        if pkeyword in item.lower():
            results.append(item)
    if len(results) > 0:
        print(f"Risultati per '{pkeyword}'")
        for item in results:
            print(f"{item}")
    else:
        print("oggetto non trovato")