class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso!")
        else:
            print("O valor do depósito deve ser positivo.")

conta = ContaBancaria("João", 100) 

print(f"Titular: {conta.titular}")
print(f"Saldo inicial: R${conta.saldo:.2f}")

conta.depositar(50)

print(f"Saldo após depósito: R${conta.saldo:.2f}")