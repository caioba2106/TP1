class Carro:

    def acelerar(self):
        print("O carro está acelerando suavemente na estrada!")

class Moto:

    def acelerar(self):
        print("A moto dispara com velocidade e emoção!")


veiculos = [Carro(), Moto()]

for veiculo in veiculos:
    veiculo.acelerar()