class Persona():
    nome:str
    altezza:int
    pigmentazione:str
    eta:int
    def __init__(self,nome,altezza,pigmentazione,eta):
        self.nome = nome
        self.eta = eta
        self.pigmentazione = pigmentazione
        self.altezza = altezza
    def descrizione(self):
        print(f"nome: {self.nome}, altezza: {self.altezza},pigmentazione: {self.pigmentazione},eta: {self.eta}")

def main():
    persona1 = Persona("Giorgio",175,"neGro",17)
    persona2 = Persona("Marco",161,"gringo",17)
    persona3 = Persona("Daniele",179,"gringo",17)

    persona1.descrizione()
    persona2.descrizione()
    persona3.descrizione()

main()