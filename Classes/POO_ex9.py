class Loja:

    desconto = 0.25

    @classmethod
    def aplicar_desconto(cls, novo_desconto):
        cls.desconto = novo_desconto
        print(f"Desconto atualizado para: {cls.desconto * 100:.0f}%")

print(f"Desconto inicial: {Loja.desconto * 100:.0f}%")

Loja.aplicar_desconto(0.75)
