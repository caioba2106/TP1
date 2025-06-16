import math

class Forma:

    def calcular_area(self):
        raise NotImplementedError("O método calcular_area() deve ser implementado pelas subclasses.")
    
class Quadrado(Forma):

    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2
    
class Circulo(Forma):

    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return math.pi * (self.raio ** 2)


quadrado1 = Quadrado(4)
circulo1 = Circulo(5)

print(f"Área do quadrado: {quadrado1.calcular_area():.2f}")
print(f"Área do círculo: {circulo1.calcular_area():.2f}")