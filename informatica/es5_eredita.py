class Veicolo:
    def __init__(self,marca):
        self.marca = marca
    def descrizione(self):
        print(f'veicola di marca {self.marca}')

class Auto(Veicolo):
    def __init__(self,marca,n_porte):
        super().__init__(marca)#chiama il costruttore di Persona()
        self.n_porte=n_porte
    def descrizione(self):
        print(f'veicola di marca {self.marca} e con {self.n_porte} porte')
s = Auto('fiat',4)
s.descrizione()#es 5-6