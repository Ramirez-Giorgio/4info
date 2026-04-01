#dizionario
#in coppia [chiave: valore] 
settimana = {'Lun': 'Mon', 
            'Mar': 'Tue',  
            'Mer': 'Wed', 
            'Gio': 'Thu',  
            'Ven': 'Fri', 
            'Sab': 'Sat',  
            'Dom': 'Sun'}
diz = dict(a=1,b=2)
d = {}
print(settimana['Lun'])#metto la chiave e mi stampera il valore [], se chiave non presente va in errore
print(settimana.get('Mar','Non disponibile'))#uso di get che funziona come un if  (chiave,messaggio se non disponibile) gestito l'errore dal get

s = "banana"
conta = {}

for lettera in s:
    conta[lettera] = conta.get(lettera, 0) + 1#cerca e conta il n di lettere presenti

print(conta)
# {'b': 1, 'a': 3, 'n': 2} crea il dizionario

stud = {
    "nome": "Marco",
    "età": 17,
    "indirizzo": {"via": "Roma", "numero": 12}#dizionario dentro un altro dizionario
}

print(stud.get("indirizzo", {}).get("via", "Sconosciuta")) # nel primo get se l'indirizzo è vuoto restituisce un dizionario vuoto per questo uso un altro .get
#  'Roma'

#dizionari modificabili
stud["età"] = 18
#Aggiunta:
stud["classe"] = "4B ITT"
#Rimozione elementi
del stud["età"]
#Per svuotare il dizionario:
stud.clear()
#.keys() Restituisce tutte le chiavi
#.values() Tutti i valori
#.items() Coppie chiave/valore
#.update() Unisce o aggiorna
classe = {
"stud1": {"nome": "Luca", "età": 17},
"stud2": {"nome": "Anna", "età": 18}
}
#Accesso:
print(classe["stud2"]["nome"])


# try modulo e metti import error nel exception

#nelle liste uso set per togliere i duplicati