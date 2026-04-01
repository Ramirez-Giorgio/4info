def perpendicolari(m1, q1, m2, q2):
    return m1 == -(1/m2)


print("Controllo se due rette sono perpendicolari.")
m1 = float(input("Inserisci il coefficiente angolare m1: "))
q1 = float(input("Inserisci il termine noto q1: "))
m2 = float(input("Inserisci il coefficiente angolare m2: "))
q2 = float(input("Inserisci il termine noto q2: "))

if perpendicolari(m1, q1, m2, q2):#controlla se il return 
    print("Le due rette sono perpendicolari.")
else:
    print("Le due rette NON sono perpendicolari.")
