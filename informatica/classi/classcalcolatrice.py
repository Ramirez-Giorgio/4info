import math

class Calcolatrice(object):
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b
    def somma(self):
        return self.a + self.b
    def sottrazione(self):
        return self.a - self.b
    def moltiplicazione(self):
        return self.a * self.b
    def divisione(self):
        if self.b == 0:
            raise Exception("divisione per zero impossibile")
        return self.a / self.b
    def potenza(self):
        return self.a ** self.b
    def quadrato(self):
        return self.a ** 2
    def logaritmo(self):
        if self.a <= 0:
            raise Exception("logaritmo impossibile")
        return math.log(self.a)
    def fattoriale(self):
        if self.a < 0:
            raise Exception("fattoriale impossibile")
        return math.factorial(self.a)
    def radice(self):
        if self.a < 0:
            raise Exception("radice impossibile")
        return math.sqrt(self.a)
