class Venda:

    @staticmethod
    def calcular_imposto(valor, taxa=0.1):
        return valor * taxa
    
valor_venda = 500.00
imposto = Venda.calcular_imposto(valor_venda)
print(f"O imposto sobre a venda de R$ {valor_venda:.2f} é R$ {imposto:.2f}")

imposto_personalizado = Venda.calcular_imposto(valor_venda, taxa=0.2)
print(f"O imposto com taxa personalizada sobre a venda de R$ {valor_venda:.2f} é R$ {imposto_personalizado:.2f}")