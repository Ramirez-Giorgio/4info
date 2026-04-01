from datetime import datetime, date, timedelta

# === 1. Quanti giorni mancano al tuo compleanno ===
def giorni_al_compleanno(giorno, mese):
    oggi = date.today()
    anno_corrente = oggi.year
    compleanno = date(anno_corrente, mese, giorno)
    if compleanno < oggi:
        compleanno = date(anno_corrente + 1, mese, giorno)
    giorni_mancanti = (compleanno - oggi).days
    return giorni_mancanti

# === 2. Da quanti giorni sei nato ===
def giorni_da_nascita(giorno, mese, anno):
    nascita = date(anno, mese, giorno)
    oggi = date.today()
    giorni_passati = (oggi - nascita).days
    return giorni_passati

# === 3. Data di 100 giorni fa e tra 100 giorni ===
def date_100_giorni():
    oggi = date.today()
    fa_100 = oggi - timedelta(days=100)
    tra_100 = oggi + timedelta(days=100)
    return fa_100, tra_100

# === 4. Data e ora attuale nel formato personalizzato ===
def data_ora_formattata():
    adesso = datetime.now()
    giorni_settimana = ["lunedì", "martedì", "mercoledì", "giovedì",
                        "venerdì", "sabato", "domenica"]
    nome_giorno = giorni_settimana[adesso.weekday()]
    return f"Oggi è {nome_giorno} {adesso.day} {adesso.strftime('%B')} {adesso.year}, ore {adesso.strftime('%H:%M')}"

# === 6-8. Funzione per sapere se un anno è bisestile ===
def bisestile(anno):
    return (anno % 4 == 0 and anno % 100 != 0) or (anno % 400 == 0)


# ======== PROGRAMMA PRINCIPALE ========
if __name__ == "__main__":
    # Inserisci la tua data di nascita
    giorno = int(input("Inserisci il giorno del tuo compleanno: "))
    mese = int(input("Inserisci il mese del tuo compleanno (numero): "))
    anno = int(input("Inserisci l'anno di nascita: "))

    print("\n=== RISULTATI ===")
    print(f"1. Mancano {giorni_al_compleanno(giorno, mese)} giorni al tuo compleanno.")
    print(f"2. Sei nato da {giorni_da_nascita(giorno, mese, anno)} giorni.")

    fa_100, tra_100 = date_100_giorni()
    print(f"3. 100 giorni fa era il {fa_100.strftime('%d/%m/%Y')}, tra 100 giorni sarà il {tra_100.strftime('%d/%m/%Y')}.")

    print(f"4-5. {data_ora_formattata()}")

    anno_da_testare = int(input("\nInserisci un anno per sapere se è bisestile: "))
    if bisestile(anno_da_testare):
        print(f"{anno_da_testare} è un anno bisestile.")
    else:
        print(f"{anno_da_testare} non è un anno bisestile.")
