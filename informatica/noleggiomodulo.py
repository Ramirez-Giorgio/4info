def calcola_costo(categoria, giorni, categorie, prezzi, numero_noleggi, incassi):
    indice = -1
    for i in range(len(categorie)):
        if categorie[i].upper() == categoria.upper():
            indice = i
            break
    if indice == -1:
        raise ValueError("Categoria non valida")
    prezzo_giornaliero = prezzi[indice]
    costo = prezzo_giornaliero * giorni
    if giorni >= 7:
        sconto = costo * 20 / 100
        costo = costo - sconto
    elif giorni >= 3:
        sconto = costo * 10 / 100
        costo = costo - sconto
    numero_noleggi[indice] += 1
    incassi[indice] += costo
    return costo

def mostra_statistiche(categorie, numero_noleggi, incassi):
    for i in range(len(categorie)):
        print(f"""Categoria {categorie[i]}:
        Numero noleggi: {numero_noleggi[i]}
        Incasso: {incassi[i]:.2f}€\n""")
