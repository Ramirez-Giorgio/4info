# --- 1. CLASSE BASE: PERSONA ---
class Persona:
    """Definisce la struttura comune a visitatori e dipendenti[cite: 7, 8]."""
    def __init__(self, codice, nome, cognome):
        self.codice = str(codice)  # Codice identificativo [cite: 9]
        self.nome = str(nome)      # Nome [cite: 10]
        self.cognome = str(cognome) # Cognome [cite: 11]

    def scheda_descrittiva(self):
        """Restituisce una scheda testuale[cite: 12]."""
        return f"ID: {self.codice} | {self.nome} {self.cognome}"


# --- 2. CLASSI DERIVATE ---
class Visitatore(Persona):
    """Estende Persona aggiungendo età e abbonamento[cite: 14, 15]."""
    def __init__(self, codice, nome, cognome, eta, abbonamento):
        super().__init__(codice, nome, cognome)
        self.abbonamento = str(abbonamento) # Tipo di abbonamento [cite: 17]
        
        # Correzione automatica età (0-120) [cite: 18, 19]
        if int(eta) < 0 or int(eta) > 120:
            print(f"Messaggio: Età {eta} non valida per {nome}. Corretta a 0. [cite: 19]")
            self.eta = 0
        else:
            self.eta = int(eta)

class Dipendente(Persona):
    """Estende Persona aggiungendo ruolo e stipendio[cite: 20, 21]."""
    def __init__(self, codice, nome, cognome, ruolo, stipendio):
        super().__init__(codice, nome, cognome)
        self.ruolo = str(ruolo) # Ruolo [cite: 22]
        
        # Correzione automatica stipendio negativo 
        if float(stipendio) < 0:
            self.stipendio = 0.0
        else:
            self.stipendio = float(stipendio)


# --- 3. CLASSE ATTRAZIONE ---
class Attrazione:
    """Rappresenta un'attrazione del parco[cite: 25, 26]."""
    def __init__(self, codice, nome, tipo, capacita):
        self.codice = str(codice) # Codice [cite: 27]
        self.nome = str(nome)     # Nome [cite: 28]
        self.tipo = str(tipo)     # Tipo (giostra/spettacolo) [cite: 29]
        self.capacita = int(capacita) # Capacità massima [cite: 30]
        self.ingressi_oggi = 0   # Contatore per gestire il limite [cite: 49]

    def scheda_tecnica(self):
        """Restituisce la scheda tecnica[cite: 31]."""
        return f"Attrazione {self.codice}: {self.nome} ({self.tipo}) - Cap: {self.capacita}"


# --- 4. CLASSE BIGLIETTO ---
class Biglietto:
    """Rappresenta l'acquisto di un accesso[cite: 32, 33]."""
    def __init__(self, codice_b, visitatore, attrazione, prezzo, data):
        self.codice_b = str(codice_b) # Codice biglietto [cite: 34]
        self.visitatore = visitatore   # Oggetto Visitatore [cite: 35]
        self.attrazione = attrazione   # Oggetto Attrazione [cite: 36]
        self.data = str(data)         # Data utilizzo [cite: 38]
        
        # Forza prezzo a 0 se negativo [cite: 39]
        self.prezzo = max(0.0, float(prezzo))


# --- 5. GESTIONE ARCHIVI (DIZIONARI)  ---
diz_visitatori = {}  # Chiave: codice visitatore [cite: 42]
diz_dipendenti = {}  # Chiave: codice dipendente [cite: 43]
diz_attrazioni = {}  # Chiave: codice attrazione [cite: 44]
diz_biglietti = {}   # Chiave: codice biglietto [cite: 44]
    

# --- 6. LOGICA DI INSERIMENTO E CONTROLLI ---
def emetti_biglietto(cod_b, cod_v, cod_a, prezzo, data):
    # Controllo esistenza visitatore e attrazione [cite: 46, 47, 48]
    if cod_v in diz_visitatori:
        pass
    else:
        print("Errore: Il visitatore non esiste! [cite: 47]")
        return
    if cod_a not in diz_attrazioni:
        print("Errore: L'attrazione non esiste! [cite: 48]")
        return

    attr = diz_attrazioni[cod_a]
    
    # Controllo capacità massima [cite: 49, 50]
    if attr.ingressi_oggi >= attr.capacita:
        print(f"Errore: Capacità massima raggiunta per {attr.nome}! Inserimento bloccato. [cite: 50]")
        return

    # Creazione biglietto e aggiornamento contatore
    nuovo_b = Biglietto(cod_b, diz_visitatori[cod_v], attr, prezzo, data)
    diz_biglietti[cod_b] = nuovo_b
    attr.ingressi_oggi += 1
    print(f"Biglietto {cod_b} emesso correttamente.")


# --- 7. GENERAZIONE REPORT SU FILE [cite: 51, 52] ---
def genera_report(cognome_studente):
    # Report Attrazioni [cite: 53, 54]
    with open(f"{cognome_studente}_report_attrazioni.txt", "w") as f:
        for a in diz_attrazioni.values():
            f.write(a.scheda_tecnica() + "\n")

    # Report Biglietti [cite: 55, 56]
    with open(f"{cognome_studente}_report_biglietti.txt", "w") as f:
        for b in diz_biglietti.values():
            f.write(f"ID: {b.codice_b} | Vis: {b.visitatore.cognome} | Attr: {b.attrazione.nome} | Prezzo: {b.prezzo}€\n")

    # Report Incassi [cite: 56, 57]
    with open(f"{cognome_studente}_report_incassi.txt", "w") as f:
        for a in diz_attrazioni.values():
            # Calcolo incasso totale per l'attrazione [cite: 60]
            incasso = sum(b.prezzo for b in diz_biglietti.values() if b.attrazione.codice == a.codice)
            f.write(f"{a.nome}\nBiglietti: {a.ingressi_oggi}\nIncasso: {incasso:.2f} €\n\n")


# --- ESEMPIO DI ESECUZIONE ---
# Caricamento dati iniziali
diz_visitatori["V1"] = Visitatore("V1", "Luca", "Verdi", 25, "Mensile")
diz_attrazioni["A1"] = Attrazione("A1", "Bruco Mela", "Giostra", 2)

# Test emissione biglietti
emetti_biglietto("B1", "V1", "A1", 10.0, "19/02/2026")
emetti_biglietto("B2", "V1", "A1", 10.0, "19/02/2026")
emetti_biglietto("B3", "V1", "A1", 10.0, "19/02/2026") # Supera capacità!

genera_report("MioCognome")