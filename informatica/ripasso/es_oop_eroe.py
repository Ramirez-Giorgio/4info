class Eroe:
    def __init__(self, nome, salute):
        self.nome = str(nome)
        self.salute = int(salute)
        pass

    def attacco(self):
        print(f"{self.nome} si prepara...")

class Guerriero(Eroe):
    def __init__(self, nome, salute, forza):
        super().__init__(nome,salute)
        self.forza = int(forza)
        pass

    def attacco(self):
        # Usa super().attacco() e aggiungi il messaggio della spada
        super().attacco()
        print(f'attacco con forza {self.forza}')
        pass

class Mago(Eroe):
    def __init__(self, nome, salute, incantesimo):
        # Usa super() e aggiungi l'incantesimo
        super().__init__(nome,salute)
        self.incantesimo = str(incantesimo)
        pass

    def attacco(self):
        # Usa super().attacco() e aggiungi il messaggio della magia
        super().attacco()
        print(f'lancio incantesimo {self.incantesimo}')
        pass

# --- MAIN ---
party = []

# 1. Aggiungi un Guerriero statico (CORRETTO: lo aggiungiamo alla lista)
party.append(Guerriero('Aragorn', 150, 25)) 

# 2. Chiedi input per un Mago
print("--- Crea il tuo Mago ---")
nome_m = input('Inserisci nome mago: ')
salute_m = int(input('Inserisci la quantita di salute: '))
inc_m = input('Inserisci il nome dell incantesimo: ')

# Creiamo l'oggetto Mago con i dati dell'utente e lo aggiungiamo
mago_utente = Mago(nome_m, salute_m, inc_m)
party.append(mago_utente)

# 3. Ciclo for per il polimorfismo
print("\n--- INIZIO BATTAGLIA ---")
for eroe in party:
    eroe.attacco() # Qui avviene il polimorfismo: chiama il metodo giusto per ogni classe