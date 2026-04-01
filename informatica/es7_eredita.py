class Lavoratore:
    def __init__(self, nome):
        self.nome = nome
    def presentati(self):
        print(f'mi chiamo {self.nome}')

class Impiegato(Lavoratore):
    def __init__(self, nome, stipendio):
        Lavoratore.__init__(self, nome)  # chiamata diretta al padre senza usare super
        self.stipendio = stipendio


s = Impiegato('Giorgio', 1500)
s.presentati()
