# restituisce la stringa ordinata
def ordina(stringa):
    lis = list(stringa)    
    lis.sort()
    for j in range(1, len(lis)):
        lis[0] += lis[j]
        return lis[0]

#restituisce la stringa ordinata con i caratteridi stringa1 e stringa2
def fondi(stringa1, stringa2):
    stringa = ordina(stringa1 + stringa2)
    return stringa
