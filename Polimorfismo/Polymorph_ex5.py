import math

class FormaGeometrica:

    def calcular_area(self):
        raise NotImplementedError("Este método deve ser implementado pelas subclasses.")
    
class Quadrado(FormaGeometrica):

    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2
    
class Circulo(FormaGeometrica):

    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return math.pi * (self.raio ** 2)
    

forma1 = Quadrado(4)
forma2 = Circulo(3)

print(f"Área do quadrado: {forma1.calcular_area():.2f}")
print(f"Área do círculo: {forma2.calcular_area():.2f}")