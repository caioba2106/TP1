import re

class Cliente:

    def __init__(self, nome):
        self.nome = nome
        self.cpf = None

    @staticmethod
    def validar_cpf(cpf):
        padrao_cpf = r"^\d{3}\.\d{3}\.\d{3}-\d{2}$"
        return bool(re.match(padrao_cpf, cpf))
    
    def cadastrar_cliente(self, cpf):
        if Cliente.validar_cpf(cpf):
            self.cpf = cpf
            return f"Cliente {self.nome} cadastrado com sucesso com CPF {self.cpf}!"
        else:
            return "CPF inválido. Não foi possível cadastrar o cliente."

cliente1 = Cliente("Alice")
cliente2 = Cliente("Carlos")

print(cliente1.cadastrar_cliente("123.456.789-00"))  
print(cliente2.cadastrar_cliente("12345678900"))