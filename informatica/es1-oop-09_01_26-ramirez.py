class Atleta:
    def __init__(self, nome):
        self.nome = nome
        self.squadra = None
        self.visitaMedica = False

    def assegna_squadra(self, squadra):
        self.squadra = squadra

    def effettua_visita(self):
        self.visitaMedica = True

    def mostra_dati(self):
        print("Nome:", self.nome)
        print("Squadra:", self.squadra)
        print("Visita medica:", self.visitaMedica)
