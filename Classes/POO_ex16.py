class Carro:

    def __init__(self, modelo="Padrão", cor="Branco"):
        self.modelo = modelo
        self.cor = cor

    def detalhes_do_carro(self):
        return f"Modelo: {self.modelo}, Cor: {self.cor}"
    
carro1 = Carro()
carro2 = Carro("Sedan", "Preto")

print(carro1.detalhes_do_carro())
print(carro2.detalhes_do_carro())