class Auto(object):
    marca:str
    modello:str
    colore:str
    def __init__(self, marca, modello ,colore):
        self.marca = marca
        self.modello = modello
        self.colore = colore
    def descrizione(self):
        print(f"{self.marca}, {self.modello}, {self.colore}")

def main():
    auto1 = Auto("fiat","500L","nero")
    auto2 = Auto("fiat","panda","giallo")
    auto3 = Auto("fiat","punto","blu")
    
    auto1.descrizione()
    auto2.descrizione()
    auto3.descrizione()

main()