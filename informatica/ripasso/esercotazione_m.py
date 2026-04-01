class Persona:
    def __init__(self,cod_i,nome,cognome):
        self.cod_i = int(cod_i)
        self.nome = str(nome)
        self.cognome = str(cognome)
    def scheda_descrittiva(self):
        return f'nome{self.nome},cognome{self.cognome}|codice{self.cod_i}'

class Visitatore(Persona):
    def __init__(self,cod_i,nome,cognome,eta,tipo):
        super().__init__(cod_i,nome,cognome)
        self.eta = int(eta)
        if self.eta < 0 or self.eta > 120:
            self.eta = 0
        self.tipo = str(tipo)
    def scheda_descrittiva(self):
        return f'nome{self.nome},cognome{self.cognome},eta{self.eta}|codice{self.cod_i},tipo abbonamento{self.tipo}'

class Dipendente(Persona):
    def __init__(self,cod_i,nome,cognome,ruolo,stipendio):
        super().__init__(cod_i,nome,cognome)
        self.ruolo = str(ruolo)
        self.stipendio = int(stipendio)
        if self.stipendio < 0: 
            self.stipendio = 0

class Attrazione:
    def __init__(self,cod_a,nome,Tipo,capacita):
        self.cod_a = int(cod_a)
        self.nome = str(nome)
        self.Tipo = str(Tipo)
        self.capacita = int(capacita)
    def scheda_tecnica(self):
        return f'nome attrazione:{self.nome},tipo attrazione:{self.Tipo},capacita massima:{self.capacita}|codice:{self.cod_a}'

class Biglietto:
    def __init__(self,cod_b,ogg_v,ogg_a,prezzo,data):
        self.cod_b = int(cod_b)
        self.ogg_v = ogg_v
        self.ogg_a = ogg_a
        self.prezzo = int(prezzo)
        if self.prezzo < 0:
            self.prezzo = 0
        self.data = str(data)
    
diz_visitatori = {}
diz_dipendenti = {}
diz_attrazioni = {}
diz_biglietti = {}

def emetti_biglietto(cod_v,cod_b,cod_a,prezzo,data):
    if cod_v in diz_visitatori:
        pass
    else:
        print('visitatore non presente')
        return
    if cod_a in diz_attrazioni:
        pass
    else:
        print('attrazione inesistente')
    attr = diz_attrazioni[cod_a]# 2. Recupero l'oggetto attrazione per controllare la capacità
    occupati = 0
    # Cicliamo tutti i biglietti salvati nell'archivio 
    for b in diz_biglietti.values():
        if b.ogg_a == cod_a and b.data == data: #controlla se gli oggetti delle attrazioni e le date sono uguali
            occupati += 1 # se sono uguali i posti occupati aumentano
    if occupati >= attr.capacita:
        print(f"Capacità massima raggiunta per {attr.nome}") #se superano le capacita massime 
        return
    nuovo_b = Biglietto(cod_b, diz_visitatori[cod_v], attr, prezzo, data)
    diz_biglietti[cod_b] = nuovo_b
    print(f'Biglietto {cod_b} emesso per {attr.nome}')

def genera_report(cognome):
    # 1. Report Attrazioni [cite: 53]
    with open(f"{cognome}_report_attrazioni.txt", "w") as f:
        for a in diz_attrazioni.values():
            # Usiamo il metodo della classe che hai scritto tu! [cite: 31, 54]
            f.write(a.scheda_tecnica() + "\n")
    
    # 2. Report Biglietti (uno per riga) [cite: 55, 56]
    with open(f"{cognome}_report_biglietti.txt", "w") as f:
        for b in diz_biglietti.values():
            # Scriviamo i dati essenziali del biglietto [cite: 34, 37, 38]
            linea = f"{b.cod_b}, Visitatore:{b.ogg_v.cognome}, Attr:{b.ogg_a.nome}, Prezzo:{b.prezzo}€\n"
            f.write(linea)
            
    with open(f"{cognome}_report_incassi.txt", "w") as f:
        # Cicliamo ogni attrazione nel dizionario 
        for a in diz_attrazioni.values():
            biglietti_venduti = 0
            incasso_totale = 0
            
            # Per ogni attrazione, controlliamo tutti i biglietti emessi
            for b in diz_biglietti.values():
                # Se l'oggetto attrazione nel biglietto è lo stesso che stiamo analizzando
                if b.ogg_a.cod_a == a.cod_a:
                    biglietti_venduti += 1
                    incasso_totale += b.prezzo
            
            # Scriviamo i dati nel formato richiesto dal PDF [cite: 62, 63, 64]
            f.write(f"{a.nome}\n")
            f.write(f"Biglietti: {biglietti_venduti}\n")
            f.write(f"Incasso: {incasso_totale:.2f} €\n")
            f.write("-" * 20 + "\n") # Separatore per renderlo leggibile
 
# 1. Popoliamo i dizionari (Esempio)
diz_visitatori[1] = Visitatore(1, "Mario", "Rossi", 25, "mensile")
diz_attrazioni[101] = Attrazione(101, "Ruota Panoramica", "giostra", 50)

# 2. Chiamiamo la funzione per emettere un biglietto
emetti_biglietto(1, 5001, 101, 15, "20/02/2026")

# 3. Chiamiamo la funzione per generare i file
genera_report("Rossi")