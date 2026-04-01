carrello = []

def aggiungi_prodotto(nome, prezzo):
    carrello.append({'nome': nome, 'prezzo': prezzo})
    return carrello

def elimina_prodotto(indice):
    if 0 <= indice < len(carrello):
        prodotto_rimosso = carrello.pop(indice)
        return prodotto_rimosso['nome']
    else:
        return None

def calcola_totale():
    totale = 0
    for prodotto in carrello:
        totale += prodotto['prezzo']
    return totale

def visualizza_prodotti():
    if not carrello:
        return "Il carrello è vuoto."

    output = ["\n--- Contenuto Carrello ---"]
    for i, prodotto in enumerate(carrello):
        output.append(f"[{i + 1}] {prodotto['nome']} - €{prodotto['prezzo']:.2f}")
    
    return "\n".join(output)

def get_carrello_lunghezza():
    return len(carrello)
