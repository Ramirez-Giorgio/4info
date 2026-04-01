MappaRegioni = {
    "Lombardia": ["Milano", "Bergamo", "Brescia", "Como"],
    "Campania": ["Napoli", "Salerno", "Caserta", "Avellino"],
    "Lazio": ["Roma", "Frosinone", "Latina", "Viterbo"],
    "Sicilia": ["Palermo", "Catania", "Messina", "Trapani"]
}
    
def cerca_regione():
    provincia = input("Inserisci il nome della provincia: ").capitalize()
    trovata = 0
    for regione, province in MappaRegioni.items():
        if provincia in province:
            print(f"La provincia di {provincia} appartiene alla regione {regione}")
            trovata = 1
            break
    if trovata == 0:
        print("Provincia non presente nell'archivio")
cerca_regione()
