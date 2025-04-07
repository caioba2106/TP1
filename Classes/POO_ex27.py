class Produto:

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def mostrar_info(self):
        return f"Produto: {self.nome}, Preço: R$ {self.preco:.2f}"
    
produto1 = Produto("Notebook Gamer", 3500.00)
produto2 = Produto("Iphone 12", 1500.00)

print(produto1.mostrar_info())
print(produto2.mostrar_info())