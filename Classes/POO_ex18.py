class Funcionario:

    def __init__(self, nome, salario_base):
        self.nome = nome
        self.salario_base = salario_base

    def salario(self):
        return f"Funcionário {self.nome}: Salário R$ {self.salario_base:.2f}"
    
class Gerente(Funcionario):

    def __init__(self, nome, salario_base, bonus):
        super().__init__(nome, salario_base)
        self.bonus = bonus

    def salario(self):
        salario_total = self.salario_base + self.bonus
        return f"Gerente {self.nome}: Salário R$ {salario_total:.2f}"
    
funcionario = Funcionario("Carlos", 3000.00)
gerente = Gerente("Wellington", 5000.00, 2000.00)

print(funcionario.salario())
print(gerente.salario())