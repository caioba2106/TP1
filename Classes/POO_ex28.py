class ContaBancaria:
    taxa_juros = 0.05

    @staticmethod
    def calcular_juros(saldo):
        return saldo * ContaBancaria.taxa_juros
    
saldo = 1000.00
juros = ContaBancaria.calcular_juros(saldo)

print(f"Saldo: R$ {saldo:.2f}")
print(f"Juros calculados: R$ {juros:.2f}")

ContaBancaria.taxa_juros = 0.08

novos_juros = ContaBancaria.calcular_juros(saldo)
print(f"Juros calculados com nova taxa: R$ {novos_juros:.2f}")