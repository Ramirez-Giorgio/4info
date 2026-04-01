class Veicolo(object):
    def __init__(self, marca, colore, anno):
        self.marca = str(marca)
        self.colore = str(colore)
        self.anno = int(anno)
        
    def descrizione(self):
        # Corretto il bug: ora stampa self.anno e non self.colore
        print(f'Il veicolo è di marca {self.marca}, colore {self.colore} ed anno {self.anno}')

class Bus(Veicolo):
    def __init__(self, marca, colore, anno, posti):
        super().__init__(marca, colore, anno)
        self.posti = int(posti)
        
    def descrizione(self):
        super().descrizione()
        print(f'Questo Bus ha {self.posti} posti.\n')

class Auto(Veicolo):
    def __init__(self, marca, colore, anno, modello):
        super().__init__(marca, colore, anno)
        self.modello = str(modello)
        
    def descrizione(self):
        super().descrizione()
        print(f'Il modello dell\'auto è {self.modello}.\n')

# --- GESTIONE DELLA LISTA ---
lista_veicoli = []

# 1. RICHIAMO DINAMICO (Input utente)
print("--- INSERIMENTO DINAMICO ---")
m = input("Marca: ")
c = input("Colore: ")
a = input("Anno: ")
mod = input("Modello: ")

auto_utente = Auto(m, c, a, mod)
lista_veicoli.append(auto_utente)

# 2. RICHIAMO STATICO (Creato direttamente nel codice)
# Qui passiamo i valori direttamente tra le parentesi
bus_statico = Bus('Iveco', 'Blu', 2015, 50)
lista_veicoli.append(bus_statico)

print("\n--- RESOCONTO FINALE DELLA LISTA ---")
for veicolo in lista_veicoli:
    veicolo.descrizione()