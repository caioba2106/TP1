class Onibus:

    def __init__(self, tarifa_fixa=4.50):
        self.tarifa_fixa = tarifa_fixa

    def custo_viagem(self, distancia):
        print(f"Custo da viagem de ônibus: R${self.tarifa_fixa:.2f} (tarifa fixa)")

class Bicicleta:

    def custo_viagem(self, distancia):
        print(f"Custo da viagem de bicicleta: R$0.00 (modo ecologicamente correto)")

class Carro:

    def __init__(self, preco_combustivel=6.00, consumo_km_litro=10):
        self.preco_combustivel = preco_combustivel
        self.consumo_km_litro = consumo_km_litro

    def custo_viagem(self, distancia):
        litros_usados = distancia / self.consumo_km_litro
        custo = litros_usados * self.preco_combustivel
        print(f"Custo da viagem de carro: R${custo:.2f} (para {distancia} km)")


veiculos = [Onibus(), Bicicleta(), Carro()]

distancia = 15
for veiculo in veiculos:
    veiculo.custo_viagem(distancia)
