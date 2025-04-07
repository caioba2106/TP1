class Produto:
    desconto = 0.1

    @staticmethod
    def aplcar_desconto(preco):
        return preco * (1 - Produto.desconto)
    
preco_original = 200.00
preco_com_desconto = Produto.aplcar_desconto(preco_original)

print(f"Preço original: R$ {preco_original:.2f}")
print(f"Preço com desconto: R$ {preco_com_desconto:.2f}")

Produto.desconto = 0.2
preco_com_novo_desconto = Produto.aplcar_desconto(preco_original)

print(f"Preço com novo desconto: R$ {preco_com_novo_desconto:.2f}")