class Aluno:

    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def detalhes_aluno(self):
        return f"Nome do aluno: {self.nome}, Nota: {self.nota}"
    
aluno1 = Aluno("Caio", 8.5)
aluno2 = Aluno("Nicholas", 7.0)
aluno3 = Aluno("Lucas", 9.2)

print(aluno1.detalhes_aluno())
print(aluno2.detalhes_aluno())
print(aluno3.detalhes_aluno())

aluno1.nota = 9.0
aluno2.nome = "Bruno"
aluno3.nota = 10.0

print(aluno1.detalhes_aluno())
print(aluno2.detalhes_aluno())
print(aluno3.detalhes_aluno())