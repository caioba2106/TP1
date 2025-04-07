class Aluno:

    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    @classmethod
    def alterar_nome(cls, lista_alunos, novo_nome):
        for aluno in lista_alunos:
            aluno.nome = novo_nome

    def detalhes_aluno(self):
        return f"Nome: {self.nome}, Nota: {self.nota}"
    
aluno1 = Aluno("Caio", 8.5)
aluno2 = Aluno("Nicholas", 7.0)
aluno3 = Aluno("Lucas", 9.2)

lista_alunos = [aluno1, aluno2, aluno3]

print("Antes de alterar os nomes:")
for aluno in lista_alunos:
    print(aluno.detalhes_aluno())

Aluno.alterar_nome(lista_alunos, "Estudante")

print("\nApós alterar os nomes:")
for aluno in lista_alunos:
    print(aluno.detalhes_aluno())