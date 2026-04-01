class Atleta():
    def __init__(self, nome, nazione, tempo):
        self.nome = str(nome)
        self.nazione = str(nazione)
        self.tempo = float(tempo)
    def descrizione(self):
        return f'{self.nome.upper()}({self.nazione.upper()})-{self.tempo}s'

class AtletaAmatore(Atleta):
    def __init__(self, nome, nazione, tempo, categoria):
        super().__init__(nome, nazione, tempo)
        self.categoria = str(categoria)
    def __str__(self):
        return f'{self.nome.upper()};{self.nazione.upper()};{self.tempo};{self.categoria.upper()}'
    def descrizione(self):
        return f'{super().descrizione()}-categoria:{self.categoria}'

class AtletaProfessionista(Atleta):
    def __init__(self, nome, nazione, tempo, sponsor):
        super().__init__(nome, nazione, tempo)
        self.sponsor = str(sponsor)
    def __str__(self):
        return f'{self.nome.upper()};{self.nazione.upper()};{self.tempo};{self.sponsor.upper()}'
    def descrizione(self):
        return f'{super().descrizione()}-sponsor:{self.sponsor.capitalize()}'

atleti = {
    'gianni': AtletaAmatore('gianni', 'italia', 20, 'senior'),
    'Raul': AtletaProfessionista('Raul', 'stati uniti', 30, 'nike'),
    'pablo': AtletaAmatore('pablo', 'colombia', 25, 'junior'),
    'jose': AtletaProfessionista('jose', 'messico', 30, 'adidas'),
    'rosalia': AtletaAmatore('rosalia', 'puerto rico', 35, 'veterano')
}

for a in atleti.values():
    print(a.descrizione(),'\n'+'-'*30)

print('scrittura nel file')
with open('gara.txt','w') as f:
    for a in atleti.values():
        f.write(str(a)+'\n')
print('dati salvati')