class ContaBancaria:
    
    def __init__(self, titular):
        self.titular = titular
        self.__saldo = 0

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso!")
        else:
            print("O valor do depósito deve ser positivo.")

    def consultar_saldo(self):
        return self.__saldo

conta = ContaBancaria("Ana")

print(f"Titular: {conta.titular}")
print(f"Saldo inicial: R${conta.consultar_saldo():.2f}")

conta.depositar(500)

print(f"Saldo atualizado: R${conta.consultar_saldo():.2f}")
