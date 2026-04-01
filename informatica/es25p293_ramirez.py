class Triangolo:
    def __init__(self, lato1, lato2, lato3):
        self.lato1 = lato1
        self.lato2 = lato2
        self.lato3 = lato3
    def perimetro(self):
        return self.lato1 + self.lato2 + self.lato3

class TriangoloIsoscele(Triangolo):
    def isoscele(self):
        if self.lato1 == self.lato2 or self.lato2 == self.lato3 or self.lato1 == self.lato3:
            if not (self.lato1 == self.lato2 == self.lato3):
                return self.perimetro()
        return False
class TriangoloEquilatero(TriangoloIsoscele):
    def equilatero(self):
        if self.lato1 == self.lato2 == self.lato3:
            return self.perimetro()
        return False

a = TriangoloEquilatero(2, 2, 2)

print(f'perimetro triangolo {a.perimetro()}')

if a.isoscele():
    print(f'triangolo isoscele perimetro {a.isoscele()}')
else:
    print('triangolo non isoscele')

if a.equilatero():
    print(f'triangolo equilatero perimetro {a.equilatero()}')
else:
    print('triangolo non equilatero')



# class Triangolo(object):
#     lato1:float
#     lato2:float
#     lato3:float
#     def __init__(self,lato1,lato2,lato3):
#         self.lato1 = lato1
#         self.lato2 = lato2
#         self.lato3 = lato3
#     def perimetro(self):
#         return self.lato1+self.lato2+self.lato3
# class TriangoloIsoscele(Triangolo):
#     def __init__(self,lato1,lato2,lato3):
#         super().__init__(lato1,lato2,lato3)
#     def isoscele(self):
#         if self.lato1 != self.lato2 & self.lato2 != self.lato3 & self.lato1 != self.lato3 | self.lato1==self.lato2 & self.lato2==self.lato3 :
#             return False  
#         if self.lato1==self.lato2:
#             return self.lato3+(self.lato1*2)
#         elif self.lato2==self.lato3:
#             return self.lato1+(self.lato2*2)
# class TriangoloEquilatero(TriangoloIsoscele):
#     def __init__(self,lato1,lato2,lato3):
#         super().__init__(lato1,lato2,lato3)
#     def equilatero(self):
#         if self.lato1==self.lato2 & self.lato2==self.lato3:
#             return self.lato1*3
#         else:
#             return False

# a = TriangoloEquilatero(2,2,2)
# print(f'perimetro triangolo {a.perimetro()}')
# if a.isoscele():
#     print(f'triangolo isoscele perimetro {a.isoscele()}')
# else :
#     print('triangolo non isoscele')    
# if a.equilatero():
#     print(f'triangolo equilatero perimetro {a.equilatero()}')
# else :
#     print('triangolo non equilatero')    