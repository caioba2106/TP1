class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def verificar_maioridade(self):
        if self.idade >= 18:
            return f"{self.nome} é maior de idade."
        else:
            return f"{self.nome} é menor de idade."

pessoa1 = Pessoa("Alice", 5)
pessoa2 = Pessoa("Carol", 22)

print(pessoa1.verificar_maioridade())
print(pessoa2.verificar_maioridade())