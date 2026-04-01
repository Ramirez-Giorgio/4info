class Eroe:
    def __init__(self, nome, salute):
        self.nome = str(nome)
        self.salute = int(salute)
        print(f"L'eroe {self.nome} è entrato nel mondo!")

    def __del__(self):
        # Questo è il distruttore
        print(f"L'eroe {self.nome} è stato rimosso dalla memoria (o è morto in battaglia).")

# Se nel main scriviamo:
eroe_test = Eroe("Sblao", 100)
del eroe_test  # Chiamata manuale al distruttore
