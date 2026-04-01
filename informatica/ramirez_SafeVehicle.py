import os
import csv

# Inizializza la lista in memoria
veicoli_rubati = []

def carica_dati():
    """Carica i dati dal file CSV all'avvio"""
    global veicoli_rubati
    try:
        if os.path.exists("veicoli.csv"):
            with open("veicoli.csv", "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                veicoli_rubati = list(reader)
                print(f"Caricati {len(veicoli_rubati)} veicoli dal database.")
        else:
            print("Database non trovato. Verrà creato al primo inserimento.")
    except Exception as e:
        print(f"Errore durante il caricamento: {e}")
        veicoli_rubati = []

def cerca_veicolo():
    """Cerca un veicolo per targa (case insensitive)"""
    print("\n=== CERCA VEICOLO ===")
    targa_ricerca = input("Inserisci targa da controllare: ").upper().strip()
    
    for veicolo in veicoli_rubati:
        if veicolo['targa'].upper() == targa_ricerca:
            print(f"RISCONTRO POSITIVO: {veicolo['marca'].title()} {veicolo['modello'].title()} "
                  f"di colore {veicolo['colore'].title()}")
            return veicolo
    
    print("Nessun veicolo trovato con questa targa.")
    return None

def segnala_furto():
    """Registra un nuovo furto nel sistema"""
    print("\n=== SEGNALA NUOVO FURTO ===")
    
    try:
        # Input dati con validazione
        targa = input("Targa: ").upper().strip()
        if not targa:
            print("Errore: La targa non può essere vuota.")
            return
        
        # Verifica se la targa esiste già
        for veicolo in veicoli_rubati:
            if veicolo['targa'].upper() == targa:
                print("Errore: Veicolo già presente nel database!")
                return
        
        marca = input("Marca: ").title().strip()
        if not marca:
            print("Errore: La marca non può essere vuota.")
            return
        
        modello = input("Modello: ").title().strip()
        if not modello:
            print("Errore: Il modello non può essere vuoto.")
            return
        
        colore = input("Colore: ").title().strip()
        if not colore:
            print("Errore: Il colore non può essere vuoto.")
            return
        
        # Crea il dizionario del veicolo
        nuovo_veicolo = {
            'targa': targa,
            'marca': marca,
            'modello': modello,
            'colore': colore
        }
        
        # Aggiungi alla lista in memoria
        veicoli_rubati.append(nuovo_veicolo)
        
        # Scrivi nel file CSV (append)
        try:
            file_esiste = os.path.exists("veicoli.csv")
            with open("veicoli.csv", "a", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=['targa', 'marca', 'modello', 'colore'])
                
                # Se il file non esiste, scrivi l'header
                if not file_esiste:
                    writer.writeheader()
                
                writer.writerow(nuovo_veicolo)
            
            print("Furto registrato con successo ")
            
        except Exception as e:
            # Rimuovi dalla lista se il salvataggio fallisce
            veicoli_rubati.remove(nuovo_veicolo)
            print(f"Errore durante il salvataggio: {e}")
            print("Il veicolo non è stato salvato nel database.")
            
    except Exception as e:
        print(f"Errore durante la registrazione: {e}")

def segnala_ritrovamento():
    """Segnala il ritrovamento di un veicolo e lo rimuove dal database"""
    print("\n=== SEGNALA RITROVAMENTO ===")
    
    try:
        targa = input("Targa del veicolo ritrovato: ").upper().strip()
        
        # Cerca il veicolo
        veicolo_trovato = None
        for veicolo in veicoli_rubati:
            if veicolo['targa'].upper() == targa:
                veicolo_trovato = veicolo
                break
        
        if veicolo_trovato:
            # Mostra i dettagli del veicolo
            print(f"\nVeicolo trovato: {veicolo_trovato['marca']} {veicolo_trovato['modello']} "
                  f"({veicolo_trovato['colore']})")
            
            # Conferma
            conferma = input("Confermare la rimozione? (s/n): ").lower().strip()
            
            if conferma == 's':
                # Rimuovi dalla lista
                veicoli_rubati.remove(veicolo_trovato)
                
                # Sovrascrivi il file completo
                try:
                    with open("veicoli.csv", "w", newline="", encoding="utf-8") as file:
                        writer = csv.DictWriter(file, fieldnames=['targa', 'marca', 'modello', 'colore'])
                        writer.writeheader()
                        writer.writerows(veicoli_rubati)
                    
                    print(f"Veicolo {targa} rimosso dal database ✅")
                    
                except Exception as e:
                    # Ripristina la lista se il salvataggio fallisce
                    veicoli_rubati.append(veicolo_trovato)
                    print(f"Errore durante l'aggiornamento del database: {e}")
            else:
                print("Operazione annullata.")
        else:
            print("Veicolo non trovato nel database.")
            
    except Exception as e:
        print(f"Errore durante l'operazione: {e}")

def main():
    """Funzione principale del programma"""
    # Carica i dati all'avvio
    carica_dati()
    
    while True:
        try:
            print("\n" + "=" * 40)
            print("=== SISTEMA GESTIONE VEICOLI RUBATI ===")
            print("1. Cerca Veicolo")
            print("2. Segnala Nuovo Furto")
            print("3. Segnala Ritrovamento")
            print("4. Esci")
            print("=" * 40)
            
            scelta = input("Seleziona operazione (1-4): ").strip()
            
            if not scelta.isdigit():
                print("Errore: Inserisci un numero valido (1-4)")
                continue
                
            scelta = int(scelta)
            
            if scelta == 1:
                cerca_veicolo()
            elif scelta == 2:
                segnala_furto()
            elif scelta == 3:
                segnala_ritrovamento()
            elif scelta == 4:
                print("\nGrazie per aver utilizzato il sistema. Arrivederci! 👋")
                break
            else:
                print("Errore: Inserisci un numero tra 1 e 4")
                
        except KeyboardInterrupt:
            print("\n\nProgramma interrotto. Arrivederci!")
            break
        except ValueError:
            print("Errore: Inserisci un valore numerico valido")
        except Exception as e:
            print(f"Errore imprevisto: {e}")

# Punto di ingresso del programma
if __name__ == "__main__":
    main()

# import csv
# try:
#     while True:
#         print("""
# === SISTEMA GESTIONE VEICOLI RUBATI ===
# 1. Cerca Veicolo
# 2. Segnala Nuovo Furto
# 3. Segnala Ritrovamento
# 4. Esci
# """)

#         s = int(input("Selezione Operazione (1-4): "))

#         if s == 4:
#             break

#         if s == 2:
#             targa = input("Targa: ").upper()
#             marca = input("Marca: ").lower()
#             modello = input("Modello: ").lower()
#             colore = input("Colore: ").lower()
#             with open("veicoli.csv", "a", newline="", encoding="utf-8") as file:
#                     file.write(f"{chiave}")
#             print("Dati inseriti correttamente ✅")

# except ValueError:
#     print("Valore non valido")
# except FileNotFoundError:
#     print("File non trovato")
# except PermissionError:
#     print("Errore con i permessi")

