from datetime import date

def calcola_eta(anno):
    anno_attuale = date.today().year
    eta = anno_attuale - anno
    print(f"Hai {eta} anni.")

anno = int(input("Inserisci il tuo anno di nascita: "))
calcola_eta(anno)
