class ErroSaldoInsuficiente(Exception):
    def __init__(self, saldo, valor_saque):
        mensagem = f"Saldo insuficiente. Saldo atual: R$ {saldo:.2f}, tentativa de saque: R$ {valor_saque:.2f}."
        super().__init__(mensagem)

class ContaBancaria:
    def __init__(self, titular:str, saldo_inicial:float = 0.0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, valor:float):
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser positivo.")
        self.saldo += valor
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")

    def sacar(self, valor:float):
        if valor <= 0:
            raise ValueError("O valor do saque deve ser positivo.")
        if valor > self.saldo:
            raise ErroSaldoInsuficiente(self.saldo, valor)
        self.saldo -= valor
        print(f"Saque de R$ {valor:.2f} realizado com sucesso.")

    def exibir_saldo(self):
        print(f"Titular: {self.titular} | Saldo atual: R$ {self.saldo:.2f}")


if __name__ == "__main__":
    conta = ContaBancaria("Otavio", 100)

    try:
        conta.depositar(50)
        conta.sacar(200)
    
    except ErroSaldoInsuficiente as e:
        print(f"Erro personalizado: {e}")

    except ValueError as ve:
        print(f"Erro de valor: {ve}")

    finally:
        conta.exibir_saldo()