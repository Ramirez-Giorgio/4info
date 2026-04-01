#inserire un n da tastiera e dimmi se pari e multiplo di 3 
n = int(input("inserisci un numero intero: "))
if n%2==0 and n%3==0:
    print("numero pari e divisibile per 3")
elif n%2==0 and n%3!=0:
    print("numero pari ma non divisibile per 3")
elif n%3==0 and n%2!=0:
    print("numero dispari ma divisibile per 3")
else:
    print("numero non divisibile per 3 e/o pari")