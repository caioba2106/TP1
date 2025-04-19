class SaldoInsuficienteError(Exception):
    def __init__(self, saldo, valor_saque):
        super().__init__(f"Saque de R$ {valor_saque:.2f} não permitido. Saldo disponível: R$ {saldo:.2f}.")

class ContaBancaria:
    def __init__(self, titular:str, saldo_inicial:float=0.0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, valor:float):
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser positivo.")
        self.saldo += valor
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso. Saldo atual: R$ {self.saldo:.2f}")

    def sacar(self, valor:float):
        if valor <= 0:
            raise ValueError("O valor do saque deve ser positivo.")
        
        if valor > self.saldo:
            raise SaldoInsuficienteError(self.saldo, valor)
        self.saldo -= valor
        print(f"Saque de R$ {valor:.2f} realizado com sucesso. Saldo atual: R$ {self.saldo:.2f}")

    def exibir_saldo(self):
        print(f"Titular: {self.titular} | Saldo: R$ {self.saldo:.2f}")


if __name__ == "__main__":
    conta = ContaBancaria("Caio", 7400.00)

    try:
        conta.depositar(50)
        conta.sacar(30)
        conta.sacar(150)

    except (ValueError, SaldoInsuficienteError) as e:
        print(f"Erro: {e}")

    finally:
        conta.exibir_saldo()