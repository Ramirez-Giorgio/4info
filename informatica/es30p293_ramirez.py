class Veicolo:
    def __init__(self, marca, modello, anno):
        self.marca = marca
        self.modello = modello
        self.anno = anno
    def mostra_dati(self):
        print(f"marca{self.marca}, modello {self.modello}, anno {self.anno}")


class Automobile(Veicolo):
    def __init__(self, marca, modello, anno, numero_porte, km):
        super().__init__(marca, modello, anno)
        self.numero_porte = numero_porte
        self.km = km
    def mostra_dati(self):
        super().mostra_dati()
        print(f"n porte {self.numero_porte}, km {self.km}")


class Autobus(Veicolo):
    def __init__(self, marca, modello, anno, posti, linea):
        super().__init__(marca, modello, anno)
        self.posti = posti
        self.linea = linea
    def mostra_dati(self):
        super().mostra_dati()
        print(f"Posti {self.posti}, linea {self.linea}")


auto = Automobile("Fiat", "Panda", 2020, 5, 2000)
bus = Autobus("Iveco", "gtt", 2019, 80, "Linea 10")
auto.mostra_dati()
bus.mostra_dati()
