class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def aplicar_desconto(self, desconto):
        if 0 <= desconto <= 1:
            self.preco *= (1 - desconto)
            print(f"Desconto de {desconto * 100:.0f}% aplicado! Preço atualizado: R${self.preco:.2f}")
        else:
            print("O desconto deve ser um valor entre 0 e 1 (0% a 100%).")

acessorio = Produto("Calça", 1500)
print(f"Produto: {acessorio.nome}, Preço inicial: R${acessorio.preco:.2f}")

acessorio.aplicar_desconto(0.2)
print(f"Preço após desconto: R${acessorio.preco:.2f}")