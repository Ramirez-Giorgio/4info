class Anagrafica:
    def __init__(self, nome, cognome, indirizzo):
        self.nome = nome
        self.cognome = cognome
        self.indirizzo = indirizzo
    def registrazione(self):
        print(f"Nome: {self.nome}")
        print(f"Cognome: {self.cognome}")
        print(f"Indirizzo: {self.indirizzo}")
class Cliente(Anagrafica):
    def __init__(self, nome, cognome, indirizzo, telefono, partita_iva):
        super().__init__(nome, cognome, indirizzo)
        self.telefono = telefono
        self.partita_iva = partita_iva
    def registrazione(self):
        super().registrazione()
        print(f"Telefono: {self.telefono}")
        print(f"Partita IVA: {self.partita_iva}")
a = Cliente("giorio","negro","Via Roma 10","3331234567","IT12345678901")
a.registrazione()
