FILE = "veicoli.txt"
veicoli = []

# ================== CARICAMENTO DATI ==================
def carica_dati():
    try:
        with open(FILE, "r", encoding="utf-8") as file:
            for riga in file:
                targa, marca, modello, colore = riga.strip().split(",")
                veicoli.append({
                    "targa": targa,
                    "marca": marca,
                    "modello": modello,
                    "colore": colore
                })
    except FileNotFoundError:
        # Il file non esiste ancora: partiamo con lista vuota
        pass
    except Exception:
        print("Errore nella lettura del file")

# ================== INSERIMENTO FURTO (APPEND) ==================
def segnala_furto():
    try:
        targa = input("Targa: ").upper()
        marca = input("Marca: ").lower()
        modello = input("Modello: ").lower()
        colore = input("Colore: ").lower()

        auto = {
            "targa": targa,
            "marca": marca,
            "modello": modello,
            "colore": colore
        }

        veicoli.append(auto)

        with open(FILE, "a", encoding="utf-8") as file:
            file.write(f"{targa},{marca},{modello},{colore}\n")

        print("Furto registrato con successo.")
    except Exception:
        print("Errore nell'inserimento dei dati")

# ================== RICERCA VEICOLO ==================
def cerca_veicolo():
    try:
        targa = input("Inserisci targa da controllare: ").upper()

        for auto in veicoli:
            if auto["targa"] == targa:
                print(f"RISCONTRO POSITIVO: {auto['marca'].capitalize()} "
                      f"{auto['modello'].capitalize()} di colore {auto['colore'].capitalize()}")
                return

        print("Nessun veicolo trovato.")
    except Exception:
        print("Errore nella ricerca")

# ================== RITROVAMENTO (WRITE) ==================
def segnala_ritrovamento():
    try:
        targa = input("Targa del veicolo ritrovato: ").upper()
        trovato = False

        for auto in veicoli:
            if auto["targa"] == targa:
                veicoli.remove(auto)
                trovato = True
                break

        if trovato:
            with open(FILE, "w", encoding="utf-8") as file:
                for auto in veicoli:
                    file.write(f"{auto['targa']},{auto['marca']},"
                               f"{auto['modello']},{auto['colore']}\n")
            print(f"Veicolo {targa} rimosso dal database.")
        else:
            print("Veicolo non trovato.")
    except Exception:
        print("Errore nella rimozione del veicolo")

# ================== MENU PRINCIPALE ==================
def menu():
    while True:
        print("""
=== SISTEMA GESTIONE VEICOLI RUBATI ===
1. Cerca Veicolo
2. Segnala Nuovo Furto
3. Segnala Ritrovamento
4. Esci
""")
        try:
            scelta = int(input("Seleziona operazione (1-4): "))
        except ValueError:
            print("Inserisci un numero valido")
            continue

        if scelta == 1:
            cerca_veicolo()
        elif scelta == 2:
            segnala_furto()
        elif scelta == 3:
            segnala_ritrovamento()
        elif scelta == 4:
            break
        else:
            print("Scelta non valida")

# ================== AVVIO PROGRAMMA ==================
carica_dati()
menu()
