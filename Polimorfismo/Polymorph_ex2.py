class Funcionario:

    def __init__(self, nome, salario_base):
        self.nome = nome
        self.salario_base = salario_base

    def calcular_salario(self):
        raise NotImplementedError("Este método deve ser implementado pelas subclasses.")

class Funcionario_CLT(Funcionario):

    def calcular_salario(self):
        return self.salario_base * 0.8
    
class Funcionario_PJ(Funcionario):

    def calcular_salario(self):
        return self.salario_base


func1 = Funcionario_CLT("Ana", 5000)
func2 = Funcionario_PJ("Carlos", 5000)

print(f"{func1.nome} (CLT) recebe: R${func1.calcular_salario():.2f}")
print(f"{func2.nome} (PJ) recebe: R${func2.calcular_salario():.2f}")