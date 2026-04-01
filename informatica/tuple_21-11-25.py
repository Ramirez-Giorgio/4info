nascita = (25, 'marzo', 1995)
giorni = ('Lun', 'Mar', 'Mer', 'Gio', 'Ven', 'Sab', 'Dom') #con () è una tupla, con [] lista
colori = ('rosso', 'giallo', 'blu')
print(giorni[2:3    ] + nascita) # unisce il dato mer con nascita intera
tupla3 = tuple(range(9,15)) # prende i numeri da 9 a 15 e mi crea una tupla con essi
print(tupla3)
tupla4 = tuple(range(1,9))
print('somma tuple 3,4',tupla4+tupla3)

lista = ['a', 'e', 'i', 'o', 'u'] # inizializzo una lista
tupla_list = tuple(lista)#faccio una tupla con gli elementi di lista
print(tupla_list)
list_tuple = list(tupla_list)
print(list_tuple)


#insiemi
#messi con {}
set1 = set('banana')
print(set1)

#dizionario
#in coppia [chiave: valore] 
settimana = {'Lun': 'Mon', 'Mar': 'Tue',  'Mer': 'Wed', 'Gio': 'Thu',  'Ven': 'Fri', 'Sab': 'Sat',  'Dom': 'Sun'}