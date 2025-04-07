class ContaBancaria:

    def __init__(self, saldo):
        self.saldo = saldo

    def saque(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return f"Saque de R$ {valor:.2f} realizado com sucesso! Saldo restante: R$ {self.saldo:.2f}"
        else:
            return f"saque de R$ {valor:.2f} não pode ser realizado. Saldo insuficiente: R$ {self.saldo:.2f}"
        
conta = ContaBancaria(500.00)

print(conta.saque(100.00))
print(conta.saque(600.00))
print(conta.saque(200.00))