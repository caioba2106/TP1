class Banco:
    
    taxa_juros = 0.05

    @staticmethod
    def calcular_juros(saldo):
        return saldo * Banco.taxa_juros

saldo_inicial = 1000
juros = Banco.calcular_juros(saldo_inicial)

print(f"Saldo Inicial: R${saldo_inicial:.2f}")
print(f"Juros calculados: R${juros:.2f}")