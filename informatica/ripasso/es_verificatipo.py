class Persona:
    def __init__(self, codice, nome, cognome):
        self.codice = codice [cite: 9]
        self.nome = nome [cite: 10]
        self.cognome = cognome [cite: 11]

    def scheda(self):
        return f"ID: {self.codice} | {self.nome} {self.cognome}" [cite: 12]

class Visitatore(Persona):
    def __init__(self, codice, nome, cognome, eta, abbonamento):
        super().__init__(codice, nome, cognome)
        # Se l'età è sballata la mette a 0 [cite: 18]
        if eta < 0 or eta > 120:
            print(f"!!! Età non valida per {nome}, resettata a 0.") [cite: 19]
            self.eta = 0 [cite: 18]
        else:
            self.eta = eta
        self.abbonamento = abbonamento [cite: 17]

class Dipendente(Persona):
    def __init__(self, codice, nome, cognome, ruolo, stipendio):
        super().__init__(codice, nome, cognome)
        self.ruolo = ruolo [cite: 22]
        # Se lo stipendio è negativo lo mette a 0 [cite: 24]
        self.stipendio = stipendio if stipendio >= 0 else 0 [cite: 24]

class Attrazione:
    def __init__(self, codice, nome, tipo, capacita):
        self.codice = codice [cite: 27]
        self.nome = nome [cite: 28]
        self.tipo = tipo [cite: 29]
        self.capacita = capacita [cite: 30]

    def scheda_tecnica(self):
        return f"{self.nome} ({self.tipo}) - Posti: {self.capacita}" [cite: 31]

class Biglietto:
    def __init__(self, codice, visitatore, attrazione, prezzo, data):
        self.codice = codice [cite: 34]
        self.visitatore = visitatore [cite: 35]
        self.attrazione = attrazione [cite: 36]
        self.prezzo = prezzo if prezzo >= 0 else 0 [cite: 37, 39]
        self.data = data [cite: 38]

# --- ARCHIVI (DIZIONARI) ---
visitatori = {} [cite: 42]
attrazioni = {} [cite: 44]
biglietti = {} [cite: 44]

def genera_report(cognome):
    # Report Attrazioni [cite: 53, 54]
    with open(f"{cognome}_report_attrazioni.txt", "w") as f:
        for a in attrazioni.values():
            f.write(a.scheda_tecnica() + "\n")

    # Report Biglietti [cite: 55, 56]
    with open(f"{cognome}_report_biglietti.txt", "w") as f:
        for b in biglietti.values():
            f.write(f"ID:{b.codice}, Vis:{b.visitatore.cognome}, Attr:{b.attrazione.nome}, Prezzo:{b.prezzo}€\n")

    # Report Incassi [cite: 56, 57]
    with open(f"{cognome}_report_incassi.txt", "w") as f:
        for a in attrazioni.values():
            v_attr = [b for b in biglietti.values() if b.attrazione.codice == a.codice]
            incasso = sum(b.prezzo for b in v_attr)
            f.write(f"{a.nome}\nBiglietti: {len(v_attr)}\nIncasso: {incasso:.2f} €\n\n") [cite: 62, 63, 64]

# --- LOGICA DI ESECUZIONE ---
def main():
    try:
        # 1. Creiamo un'attrazione e un visitatore
        a1 = Attrazione("A1", "RollerCoaster", "giostra", 2) [cite: 29, 30]
        attrazioni[a1.codice] = a1 [cite: 44]
        
        v1 = Visitatore("V1", "Tony", "Effe", 25, "mensile") [cite: 17]
        visitatori[v1.codice] = v1 [cite: 42]

        # 2. Creazione Biglietto con controlli [cite: 46]
        cod_v, cod_a = "V1", "A1"
        
        if cod_v in visitatori and cod_a in attrazioni:[cite:47,48]
            # Controllo capacità [cite: 49]
            count = len([b for b in biglietti.values() if b.attrazione.codice == cod_a])
            if count < attrazioni[cod_a].capacita:
                b1 = Biglietto("B1", visitatori[cod_v], attrazioni[cod_a], 15, "20/02/2026")
                biglietti[b1.codice] = b1 [cite: 44]
                print("Biglietto creato con successo!")
            else:
                print("Errore: Attrazione piena!") [cite: 50]
        
        # 3. Generiamo i file [cite: 52]
        genera_report("MioG")
        print("Report generati correttamente!")

    except Exception as e:
        print(f"C'è stato un errore nel flow: {e}")

# QUESTA è la chiamata che fa partire tutto!
if __name__ == "__main__":
    main()