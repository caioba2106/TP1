class Conta:
    def __init__(self, saldo):
        self.saldo = saldo

    def verificar_saldo(self):
        if self.saldo < 0:
            return "Saldo negativo. Você está no vermelho!"
        
        elif self.saldo == 0:
            return "Saldo zerado. Cuidado com seus gastos!"
        
        elif self.saldo > 0 and self.saldo <= 1000:
            return "Saldo positivo, mas você pode economizar mais."
        
        else:
            return "Saldo saudável! Continue assim!"
        
conta1 = Conta(-50)
conta2 = Conta(0)
conta3 = Conta(500)
conta4 = Conta(1500)

print(conta1.verificar_saldo())
print(conta2.verificar_saldo())
print(conta3.verificar_saldo())
print(conta4.verificar_saldo())