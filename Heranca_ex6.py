class SerVivo:

    def __init__(self, nome):
        self.nome = nome

    def identificar(self):
        print(f"Sou um ser vivo chamado {self.nome}.")

class Animal(SerVivo):

    def __init__(self, nome, especie):
        super().__init__(nome)
        self.especie = especie

    def identificar(self):
        print(f"Sou um animal da espécie {self.especie} chamado {self.nome}.")

class Passaro(Animal):

    def __init__(self, nome, especie, cor_penas):
        super().__init__(nome, especie)
        self.cor_penas = cor_penas

    def identificar(self):
        print(f"Sou um pássaro da espécie {self.especie}, chamado {self.nome}, com penas da cor {self.cor_penas}.")


ser_vivo1 = SerVivo("Organismo desconhecido")
animal1 = Animal("Leão", "Felino")
passaro1 = Passaro("Canário", "Ave", "amarelas")

ser_vivo1.identificar()
animal1.identificar()
passaro1.identificar()