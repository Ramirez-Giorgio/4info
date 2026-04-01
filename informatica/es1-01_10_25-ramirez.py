#scrivi un programma che 
#1 chiede un n intero all'utente 
#2 chiede in quale base convertire(bin ot ex) 
#3 mostra la conversione corrispondente
#4 gestire gli errori con try execpt
print("inserisci 0 per uscire\n")
while True :
    try:
        n = int(input(print("inserisci un numero intero: ")))
        if n == 0:
            break
        conv = input("inserisci la base di conversione(bin, oct, hex): ")
        if conv.lower() == "bin":  #in caso l'utente inserisce in maiuscolo o minuscolo viene tutto convertito in minuscolo
            print("il numero convertito è ",bin(n)) # converte in questo caso in bin in l.16 oct e l.18 hex
        elif conv.lower() == "oct":
            print("il numero convertito è ",oct(n))
        elif conv.lower() == "hex":
            print("il numero convertito è ", hex(n) )
        else: 
            print("valore non valido!")# se non viene inserito bin hex o oct stampa questo
    except ValueError:#gestione errori
        print("valore non valido")
