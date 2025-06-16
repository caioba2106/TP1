class Conta:

    def __init__(self, saldo=0):
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}.")
        else:
            print(f"Valor de depósito inválido.")

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado. Saldo restante: R${self.saldo:.2f}.")
        else:
            print(f"Saldo insuficiente ou valor inválido.")


class ContaCorrente(Conta):

    def __init__(self, saldo=0, limite=500):
        super().__init__(saldo)
        self.limite = limite

    def sacar(self, valor):
        if 0 < valor <= (self.saldo + self.limite):
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado (com limite). Saldo atual: R${self.saldo:.2f}.")
        else:
            print(f"Limite excedido ou valor inválido.")


conta1 = Conta(1000)
conta_corrente1 = ContaCorrente(500, 300)

conta1.depositar(200)
conta1.sacar(500)
conta_corrente1.sacar(700)
conta_corrente1.sacar(200)