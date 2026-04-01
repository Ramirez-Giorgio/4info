#random.choice() per scegliere valore casuale

import random
NUMERICHE = '0123456789'
MAIUSCOLE = 'ABCDEFGHIJKLMNOPQRSTU-VWXYZ'
MINUSCOLE = 'abcdefghijklmnopqrstuvwxyz'

print(random.choice(NUMERICHE),random.choice(MAIUSCOLE),random.choice(MINUSCOLE),random.choice(NUMERICHE),random.choice(MAIUSCOLE),random.choice(MINUSCOLE),random.choice(NUMERICHE),random.choice(MAIUSCOLE),random.choice(MINUSCOLE),random.choice(NUMERICHE))