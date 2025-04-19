class Produto:
    def __init__(self, nome:str, preco:float):
        if preco < 0:
            raise ValueError("O preço não pode ser negativo.")
        self.nome = nome
        self.preco = preco

    def exibir_info(self):
        print(f"Produto: {self.nome} | Preço: R$ {self.preco:.2f}")


if __name__ == "__main__":
    try:
        produto1 = Produto("Camiseta (Hering)", 49.90)
        produto1.exibir_info()
        produto2 = Produto("Tênis (Puma)", -120.00)
        produto2.exibir_info()

    except ValueError as e:
        print(f"Erro ao criar o produto: {e}")