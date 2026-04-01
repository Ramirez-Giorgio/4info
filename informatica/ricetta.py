ricetta = {}
ingredienti = {}
try:
    with open("torta.txt", "r") as f:
        for riga in f:
            nome, quantita = riga.strip().split(",")
            ricetta[nome] = float(quantita)
    with open("ingredienti.txt", "r") as f:
        for riga in f:
            nome, quantita = riga.strip().split(",")
            ingredienti[nome] = float(quantita)
    sufficiente = 0
    for nome, quantita_necessaria in ricetta.items():
        if nome not in ingredienti:
            print(f"Manca l'ingrediente: {nome}")
            sufficiente = 0
        elif ingredienti[nome] < quantita_necessaria:
            print(f"{nome} insufficiente")
            sufficiente = 0
    if sufficiente == 1:
        print("ingredienti sufficenti")
except FileNotFoundError:
    print("File non trovato o inesistente")
