class Carro:
    def __init__(self, modelo, ano):
        self.modelo = modelo
        self.ano = ano

    def exibir(self):
        print(f"Modelo: {self.modelo} - Ano: {self.ano}")

carro1 = Carro("Corvette C7", 2014)
carro2 = Carro("Ford GT (GEN2)", 2016)

carro1.exibir()
carro2.exibir()