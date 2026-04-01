# rettangolo.py: area del rettangolo# definizione della classe
class Rettangolo(object):
    base = 0.0    
    altezza = 0.0
    def assegna(self, b, h):        
        self.base = b        
        self.altezza = h
    def area(self):
        return self.base * self.altezza
        # funzione principale
    def perimetro(self):
        return ((self.base*2)+(self.altezza*2))

def main():    
    tovaglia1 = Rettangolo()
    tovaglia2 = Rettangolo()
    tovaglia3 = Rettangolo()
    
    tovaglia1.assegna(2, 1)
    tovaglia2.assegna(3, 4)
    tovaglia3.assegna(2, 4)
    
    print("Area1 =", tovaglia1.area())
    print("Perimetro1 =", tovaglia1.perimetro())
    print("Area2 =", tovaglia2.area())
    print("Perimetro2 =", tovaglia2.perimetro())
    print("Area3 =", tovaglia3.area())
    print("Perimetro3 =", tovaglia3.perimetro())
    
# istruzione di avvio del programma
main()