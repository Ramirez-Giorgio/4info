frase = 'frase con elenco: 1, 2, 3, 4'
frase_s = frase.split()
print(frase_s)

frase2 = '1, 2, 3, 4'
frase_S2 = frase2.split(', ')
print(frase_S2)

frase3 = '1 /2 /3 /4'
frase_S3 = frase3.split('/')
print(frase_S3)

parolas = 'parola : '

parolas_1 = parolas.strip()#toglie solo gli spazi finali
print(parolas_1)

parolas_2 = parolas.strip(':')
print(parolas_2)