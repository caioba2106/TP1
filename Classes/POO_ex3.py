class Produto:
    def __init__(self, nome, preço):
        self.nome = nome
        self.preço = preço


produto1 = Produto("Iphone 14", 3000.00)
print(f"Produto: {produto1.nome}, Preço: R$ {produto1.preço:.2f}")

produto1.preço = 2800.00
print(f"Produto: {produto1.nome}, Preço: R$ {produto1.preço:.2f}")
