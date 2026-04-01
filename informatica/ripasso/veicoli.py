class Veicoli:
    def __init__(self, targa, modello, carico):
        self.targa = targa
        self.modello = str(modello)
        self.carico = float(carico)

    def __str__(self):
        return f"targa:{self.targa.upper()}, modello:{self.modello.capitalize()}, capacità:{self.carico}kg"

    def calcola_costo(self, distanza, peso_pacco=0):
        raise NotImplementedError("Implementare nelle sottoclassi")

class Furgoni(Veicoli):
    def calcola_costo(self, distanza, peso_pacco=0):
        return distanza * 0.50
    def __str__(self):
        return "[FURGONE] " + super().__str__()

class Camion(Veicoli):
    def __init__(self, targa, modello, carico, costo_fisso_mantenimento=12.50):
        super().__init__(targa, modello, carico)
        self.mantenimento = costo_fisso_mantenimento
    def calcola_costo(self, distanza, peso_pacco=0):
        return (distanza * 0.80) + self.mantenimento

    def __str__(self):
        return "[FRIGO] " + super().__str__()

class Droni(Veicoli):
    def calcola_costo(self, distanza, peso_pacco=0):
        soglia = self.carico * 0.10
        if peso_pacco <= soglia:
            return 15.00
        return 30.00

    def __str__(self):
        return "[DRONE] " + super().__str__()

def salva_flotta(lista_veicoli, filename="flotta.txt"):
    with open(filename, 'w', encoding='utf-8') as f:
        for v in lista_veicoli:
            tipo = v.__class__.__name__
            f.write(f"{tipo},{v.targa},{v.modello},{v.carico}\n")

def carica_flotta(filename="flotta.txt"):
    flotta = []
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for riga in f:
                parti = riga.strip().split(',')
                if len(parti) == 4:
                    tipo, targa, mod, cap = parti
                    cap = float(cap)
                    if tipo == "Furgoni":
                        flotta.append(Furgoni(targa, mod, cap))
                    elif tipo == "Camion":
                        flotta.append(Camion(targa, mod, cap))
                    elif tipo == "Droni":
                        flotta.append(Droni(targa, mod, cap))
    except FileNotFoundError:
        print("File non trovato.")
    return flotta

def modulo_analisi(flotta, distanza_test=100, peso_specifico=500):
    print(f"\n--- SIMULAZIONE VIAGGIO ({distanza_test} KM) ---")
    
    classifica = sorted(flotta, key=lambda v: v.calcola_costo(distanza_test))
    for i, v in enumerate(classifica, 1):
        print(f"{i}. {v.modello} - Costo: {v.calcola_costo(distanza_test):.2f}€")

    idonei = [v for v in flotta if v.carico >= peso_specifico]
    if idonei:
        media = sum(v.calcola_costo(distanza_test) for v in idonei) / len(idonei)
        print(f"\nMedia costi operativi flotta (carico {peso_specifico}kg): {media:.2f}€")

    costo_totale_50km = sum(v.calcola_costo(50) for v in flotta)
    with open("report_efficienza.txt", "w") as f:
        f.write(f"Costo totale stimato flotta (50km): {costo_totale_50km:.2f}€")
    print("\nFILE GENERATI\n> flotta.txt aggiornato.\n> report_efficienza.txt creato con successo.")

if __name__ == "__main__":
    test_flotta = [
        Droni("DR01", "Modello X1", 50),
        Furgoni("AA123BB", "Fiat Ducato", 1500),
        Camion("CC999ZZ", "Scania V8", 12000)
    ]

    salva_flotta(test_flotta)
    flotta_caricata = carica_flotta()
    
    if flotta_caricata:
        print(f"CARICAMENTO FLOTTA ---\nCaricati {len(flotta_caricata)} veicoli.")
        modulo_analisi(flotta_caricata)