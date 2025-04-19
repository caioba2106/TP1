class Aluno:
    def __init__(self, nome:str, nota:float):
        self.nome = nome
        self.set_nota(nota)

    def set_nota(self, nota:float):
        if not isinstance(nota, (int, float)):
            raise TypeError("A nota deve ser um número.")
        
        if nota < 0 or nota > 10:
            raise ValueError("A nota deve estar entre 0 e 10.")
        self.nota = nota

    def exibir_dados(self):
        print(f"Aluno: {self.nome} | Nota: {self.nota}")


if __name__ == "__main__":
    try:
        aluno1 = Aluno("Caio", 8.5)
        aluno1.exibir_dados()
        aluno2 = Aluno("João", 12)
        aluno2.exibir_dados()

    except (ValueError, TypeError) as e:
        print(f"Erro ao criar aluno: {e}")