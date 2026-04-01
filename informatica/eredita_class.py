class Persona:
    def __init__(self,nome):
        self.nome = nome
    def saluta(self):
        print(f'ciao,sono {self.nome}')

class Studente(Persona):
    def __init__(self,nome,matricola):
        super().__init__(nome)#chiama il costruttore di Persona()
        self.matricola=matricola
    def mostra_dati(self):
        print(f'Nome:{self.nome},Matricola:{self.matricola}')
    def saluta(self):#per sovrascrivere la funzione basta che la riscrivo
        print(f'ciao,sono {self.nome} e sono uno studente')

s = Studente('Giorgio',95895)
s.saluta()
s.mostra_dati()