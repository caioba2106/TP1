class Pessoa:
 
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_pessoa(cls):
        print("Cria o nome e a idade da pessoa")
        return cls("Caio", 21)
    
pessoa_padrao = Pessoa.criar_pessoa()

print(f"Nome: {pessoa_padrao.nome}")
print(f"Idade: {pessoa_padrao.idade}")