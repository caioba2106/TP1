class Veiculo:

    def __init__(self, marca, ano):
        self.marca = marca
        self.ano = ano

    def exibir_informacoes(self):
        print(f"Veículo: {self.marca}, Ano: {self.ano}")

class Carro(Veiculo):

    def __init__(self, marca, ano, portas):
        super().__init__(marca, ano)
        self.portas = portas

    def exibir_informacoes(self):
        print(f"Carro: {self.marca}, Ano: {self.ano}, Portas: {self.portas}")

class Moto(Veiculo):

    def __init__(self, marca, ano, cilindradas):
        super().__init__(marca, ano)
        self.cilindradas = cilindradas

    def exibir_informacoes(self):
        print(f"Moto: {self.marca}, Ano: {self.ano}, Cilindradas: {self.cilindradas}cc")


carro1 = Carro("Bugatti Chiron", 2016, 2)
moto1 = Moto("Kawasaki Ninja H2R", 2014, 998)

carro1.exibir_informacoes()
moto1.exibir_informacoes()