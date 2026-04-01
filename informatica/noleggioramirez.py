import noleggiomodulo

categorie = ["A", "B", "C", "D"]
prezzi = [40, 60, 80, 100]
numero_noleggi = [0, 0, 0, 0]#li inizializzo a 0
incassi = [0, 0, 0, 0]

def main():
    while True:
        try:
            print("""
            1 per calcolare il costo del noleggio
            2 per mostrare le statistiche
            3 pre uscire""")
            s = input("inserisci: ")
            if s == "1":
                categoria = input("Inserisci categoria A B C D: ")
                giorni = int(input("Numero di giorni: "))
                if giorni <= 0:
                    raise ValueError("valore non valido")
                costo = noleggiomodulo.calcola_costo(categoria, giorni,categorie, prezzi, numero_noleggi, incassi)
                print(f"prezzo totale: {costo:.2f}€")
            elif s == "2":
                noleggiomodulo.mostra_statistiche(categorie, numero_noleggi, incassi)
            elif s == "3":
                break
            else:
                print("valore non valido")
        except ValueError:
                    print("valore non valido")
if __name__ == "__main__":
    main()
