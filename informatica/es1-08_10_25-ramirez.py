print("inserisci 0 per uscire\n")
while True:
    try:        
        n = int(input("inserisci un numero intero positivo maggiore di 1:"))
        if n == 0: 
            break
        elif n <= 1:
            print('Devi inserire un numero maggiore di 1')
        else:
            div, c = 2, 0
            while div <= n / 2 and c == 0:
                if n % div == 0:
                    c += 1
                div += 1
            if c == 0:
                print('Numero primo!')
            else:
                print('Il numero non è primo!')
    except ValueError:
        print("errore, valore non valido!")