def fattoriale(n): #per definire una funzione
    if n == 0 or n == 1:
        return 1
    else:
        return n * fattoriale(n-1)
    
while True:
    try:
        numero = int(input("inserisci un numero intero: "))
        
