class Veiculo:
    def __init__(self, marca:str, modelo:str):
        self.marca = marca
        self.modelo = modelo

    def exibir_info(self):
        print(f"Veículo: {self.marca} | Modelo: {self.modelo}")

class Carro(Veiculo):
    def __init__(self, marca:str, modelo:str, portas:int):
        super().__init__(marca, modelo)

        if not isinstance(portas, int) or portas <= 0:
            raise ValueError("A quantidade de portas deve ser um número inteiro maior que zero.")
        
        self.portas = portas

    def exibir_info(self):
        super().exibir_info()
        print(f"Tipo: Carro | Portas: {self.portas}")


if __name__ == "__main__":
    try:
        carro1 = Carro("Lamborghini", "Esportivo", 2)
        carro1.exibir_info()
        carro2 = Carro("BYD", "Sedan", 0)
        carro2.exibir_info()

    except ValueError as e:
        print(f"Erro ao criar carro: {e}")