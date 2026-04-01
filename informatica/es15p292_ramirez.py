class Automobile(object):
    kilometri:float
    litri:float
    def __init__(self,kilometri,litri):
        self.litri = litri
        self.kilometri = kilometri
    def calcolo_media(self):
        return self.kilometri/self.litri

a = Automobile(5000,30)
print(f'la media di kilometri fatti per litro di benzina è {a.calcolo_media()}')
