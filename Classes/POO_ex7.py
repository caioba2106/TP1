class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def situacao(self):
        if self.nota >= 6:
            return "Aprovado"
        else:
            return "Reprovado"

aluno1 = Aluno("Carlos", 9.4)
aluno2 = Aluno("André", 8.5)
aluno3 = Aluno("Sérgio", 5.9)

print(f"Aluno: {aluno1.nome}, Nota: {aluno1.nota}, Situação: {aluno1.situacao()}")
print(f"Aluno: {aluno2.nome}, Nota: {aluno2.nota}, Situação: {aluno2.situacao()}")
print(f"Aluno: {aluno3.nome}, Nota: {aluno3.nota}, Situação: {aluno3.situacao()}")