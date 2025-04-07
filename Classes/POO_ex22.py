class Pessoa:
    total_pessoas = 0

    def __init__(self, nome):
        self.nome = nome
        Pessoa.total_pessoas += 1

    @classmethod
    def mostrar_total_pessoas(cls):
        return f"Total de pessoas: {cls.total_pessoas}"
    
pessoa1 = Pessoa("Alice")
pessoa2 = Pessoa("Bruno")
pessoa3 = Pessoa("Carla")

print(Pessoa.mostrar_total_pessoas())

pessoa4 = Pessoa("Diego")

print(Pessoa.mostrar_total_pessoas())