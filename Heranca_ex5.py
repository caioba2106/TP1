class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}, Idade: {self.idade} anos")

class Aluno(Pessoa):

    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula

    def exibir_informacoes(self):
        print(f"Aluno: {self.nome}, Idade: {self.idade} anos, Matrícula: {self.matricula}")


pessoa1 = Pessoa("Giovana", 35)
aluno1 = Aluno("Caio", 21, "20251234")

pessoa1.exibir_informacoes()
aluno1.exibir_informacoes()