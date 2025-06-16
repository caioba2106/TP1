class Funcionario:

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def exibir_informacoes(self):
        print(f"Funcionário: {self.nome}, Salário: R${self.salario:.2f}.")

class Programador(Funcionario):

    def __init__(self, nome, salario, linguagem):
        super().__init__(nome, salario)
        self.linguagem = linguagem

    def exibir_informacoes(self):
        print(f"Programador: {self.nome}, Salário: R${self.salario:.2f}, Linguagem: {self.linguagem}.")


funcionario1 = Funcionario("Lucas", 4000)
programador1 = Programador("Renata", 7500, "Python")

funcionario1.exibir_informacoes()
programador1.exibir_informacoes()