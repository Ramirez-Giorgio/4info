class trapezio(object):
    bmaggiore: float
    bminore: float
    altezza: float
    diagonale: float
    def __init__(self,bmaggiore,bminore,altezza,diagonale):
        self.bmaggiore = bmaggiore
        self.bminore = bminore
        self.altezza = altezza
        self.diagonale = diagonale
    def perimetro(self):
        return self.bmaggiore+self.bminore+(self.diagonale*2)
    def area(self):
        return ((self.bmaggiore+self.bminore)*self.altezza)/2

a = trapezio(5,2,3,6)
print(f'perimetro {a.perimetro()}, area {a.area()}')
