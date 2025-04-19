class Pessoa:
    def __init__(self, nome:str, idade):
        self.nome = nome
        self.idade = idade

    def verificar_maioridade(self):
        try:
            idade_int = int(self.idade)
            if idade_int >= 18:
                print(f"{self.nome} é maior de idade ({idade_int} anos).")
            else:
                print(f"{self.nome} é menor de idade ({idade_int} anos).")

        except ValueError:
            print(f"Erro: A idade fornecida para {self.nome} não é um número inteiro válido.")


if __name__ == "__main__":
    pessoa1 = Pessoa("Lucas", "21")
    pessoa2 = Pessoa("João", 17)
    pessoa3 = Pessoa("Fernanda", "dezesseis")

    pessoa1.verificar_maioridade()
    pessoa2.verificar_maioridade()
    pessoa3.verificar_maioridade()