class Funcionario:

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def exibir_informacoes(self):
        print(f"Funcionário: {self.nome}, Salário: R${self.salario:.2f}")

class Gerente(Funcionario):

    def __init__(self, nome, salario, departamento):
        super().__init__(nome, salario)
        self.departamento = departamento

    def exibir_informacoes(self):
        print(f"Gerente: {self.nome}, Salário: R${self.salario:.2f}, Departamento: {self.departamento}")


funcionario1 = Funcionario("Caio", 3000)
gerente1 = Gerente("Wellington", 8000, "Vendas")

funcionario1.exibir_informacoes()
gerente1.exibir_informacoes()