while True:
    try: 
        d= int(input(print("""inserisci:
            1 per calcolare l'area di un cerchio
            2 per calcolare l'area di un quadrato
            3 per calcolare l'area di un rettangolo
            4 per calcolare l'area di un triangolo
            0 per uscire dal programma : """)))
        if d == 0:
            break
        elif d == 1:
            r = int(input("inserisci il raggio:"))
            Ar = 3.14*(r**2)
            print(f"l'area del cerchio è {Ar}")
        elif d == 2:
            l = int(input("inserisci il lato:"))
            Aq = l**2
            print(f"l'area del quadrato è {Aq}")
        elif d == 3:
            b = int(input("inserisci la base :"))
            h = int(input("inserisci l'altezza :"))
            Ar = b*h
            print(f"l'area del rettangolo è {Ar}")
        elif d == 4:
            b = int(input("inserisci la base :"))
            h = int(input("inserisci l'altezza :"))
            At = (b*h)/2
            print(f"l'area del triangolo è {At}")
    except ValueError:
        print("inserisci un numero valido")