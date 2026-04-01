class Nuotatore:
    def __init__(self,nome):
        self.nome=nome
    def nuota(self):
        print(f'{self.nome} sta nuotando')

class Corridore:
    def __init__(self,nome):
        self.nome=nome
    def corre(self):
        print(f'{self.nome} sta correndo')

class Atleta(Nuotatore,Corridore):
    pass

a = Atleta('Giorgio')
a.nuota()
a.corre()