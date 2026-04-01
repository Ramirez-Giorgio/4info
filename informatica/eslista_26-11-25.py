import eslistecalc

def main():
    while True:
        print("-"*30)
        print("1. Visualizza lista")
        print("2. Aggiungere")
        print("3. Cercare ")
        print("4. Uscire")
        print("-"*30)

        try:
            s = input("Scegli un'opzione (1-4): ")
            if s == '1':
                eslistecalc.vedi_inventario()
            elif s == '2':
                oggetto = input("Inserisci nome: ")
                eslistecalc.aggiungi(oggetto)
            elif s == '3':
                keyword = input("Inserisci ricerca: ")
                eslistecalc.ricerca(keyword)
            elif s == '4':
                break
            else:
                print("\nScelta non valida")
        except ValueError:
            print("valore non valido")
        except Exception as e:
            print(f"\nerrore: {e}")

if __name__ == "__main__":
    main()