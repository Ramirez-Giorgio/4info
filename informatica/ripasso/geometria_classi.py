import math

class Forma():
    def area(self): 
        pass
    def perimetro(self):
        pass
        
class Quadrato(Forma):
    def __init__(self, lato):
        self.lato = float(lato)
    def area(self):
        print(f'Area quadrato: {self.lato**2}')
    def perimetro(self):
        print(f'Perimetro quadrato: {self.lato*4}')

class Cerchio(Forma):
    def __init__(self, raggio):
        self.raggio = float(raggio)
    def area(self):
        print(f'Area cerchio: {(self.raggio**2)*math.pi:.2f}') #:.2 2decimali dopo la virgola
    def perimetro(self):
        print(f'Perimetro circonferenza: {self.raggio*math.pi*2:.2f}')

class Rettangolo(Forma):
    def __init__(self, base, altezza):
        self.base = float(base)
        self.altezza = float(altezza)
    def area(self):
        print(f'Area rettangolo: {self.base*self.altezza}') 
    def perimetro(self):
        print(f'Perimetro rettangolo: {(self.base+self.altezza)*2}')

class Rombo(Forma):
    def __init__(self, Dmag, Dmin, lo):
        self.Dmag = float(Dmag)
        self.Dmin = float(Dmin)
        self.lo = float(lo)
    def area(self):
        print(f'Area Rombo: {(self.Dmag*self.Dmin)/2}')    
    def perimetro(self):
        print(f'Perimetro rombo: {self.lo*4}')

scelta = int(input('1 quadrato - 2 cerchio - 3 rettangolo - 4 rombo: '))
a = None #variabile vuota
if scelta == 1:
    lato = float(input('Inserisci misura lato: '))
    a = Quadrato(lato)

elif scelta == 2:
    raggio = float(input('Inserisci misura raggio: '))
    a = Cerchio(raggio)

elif scelta == 3:
    base = float(input('Inserisci misura base: '))
    altezza = float(input('Inserisci misura altezza: '))
    a = Rettangolo(base, altezza)

elif scelta == 4:
    Dmag = float(input('Inserisci misura diagonale maggiore: '))
    Dmin = float(input('Inserisci misura diagonale minore: '))
    lo = float(input('Inserisci misura lato: '))
    a = Rombo(Dmag, Dmin, lo)

else:
    print('Scelta invalida')

if a: # se la variabile è piena
    print("-" * 20)
    a.area()
    a.perimetro()