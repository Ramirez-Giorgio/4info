class Persona:
    def __init__(self, nome):
        self.nome = nome

    def descrizione(self):
        print("Sono una persona")


class Studente(Persona):
    def __init__(self, nome, voto):
        super().__init__(nome)
        self.voto = voto

    def descrizione(self):
        print(f"Sono uno studente e ho {self.voto}")


class Professore(Persona):
    def descrizione(self):
        print("Sono un professore")


persone = [
    Studente("Gio", 8),
    Professore("Rossi")
]

for p in persone:
    p.descrizione()
