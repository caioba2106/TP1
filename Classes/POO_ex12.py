class Pessoa:

    @staticmethod
    def validar_idade(idade):
        if idade >= 18:
            return "True"
        else:
            return "False"
        
idadePessoa = Pessoa.validar_idade(21)
print(f"Situação: {idadePessoa}")