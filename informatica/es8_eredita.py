class Lavoratore:
    def __init__(self, nome):
        self.nome = nome
    def presentati(self):
        print(f'mi chiamo {self.nome}')

class Impiegato(Lavoratore):
    def __init__(self, nome, stipendio):
        super().__init__(nome)#chiama il costruttore di Persona()
        self.stipendio = stipendio
    def presentati(self):
        print(f'mi chiamo {self.nome} e guadagno {self.stipendio}€')


s = Impiegato('Giorgio', 1500)
s.presentati()
