import carrello_ramirez

def menu_principale():
    
    while True:
        print("\n1. Aggiungi prodotto")
        print("2. vedi carrello e tot")
        print("3. Elimina prodotto (numero)")
        print("4. Paga")
        print("5. termina")
        scelta = input("inserisci(1-5): ")
        if scelta == '1':
            nome = input("Inserisci il nome del prodotto: ")
            try:
                prezzo = float(input("Inserisci prezzo prodotto: "))
                carrello_ramirez.aggiungi_prodotto(nome, prezzo)
                print(f"{nome} aggiunto")
            except ValueError:
                print("Valore non valido")
        elif scelta == '2':
            print(carrello_ramirez.visualizza_prodotti())
            if carrello_ramirez.get_carrello_lunghezza() > 0:
                totale = carrello_ramirez.calcola_totale()
                print(f"\nPrezzo tot: {totale:.2f}€")

        elif scelta == '3':
            print(carrello_ramirez.visualizza_prodotti())
            if carrello_ramirez.get_carrello_lunghezza() == 0:
                continue
            try:
                indice_utente = int(input("inserisci il numero del prodotto da togliere: "))
                indice_da_eliminare = indice_utente - 1
                nome_rimosso = carrello_ramirez.elimina_prodotto(indice_da_eliminare)
                if nome_rimosso is not None:
                    print(f"'{nome_rimosso}' è satto tolto")
                else:
                    print("valore non valido")
            except ValueError:
                print("Valore non valido")
        elif scelta == '4':
            totale_finale = carrello_ramirez.calcola_totale()
            print("\n*** Acquisto ***")
            print(f"prezzo totale: €{totale_finale:.2f}")
            break
        elif scelta == '5':
            print("programma terminato")
            break    
        else:
            print("opzione non valida")

menu_principale()
