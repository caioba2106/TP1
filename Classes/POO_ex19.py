class Curso:
    quantidade_cursos = 0

    def __init__(self, nome):
        self.nome = nome
        Curso.quantidade_cursos += 1

    @classmethod
    def alterar_quantidade_cursos(cls, nova_quantidade):
        cls.quantidade_cursos = nova_quantidade

    @classmethod
    def mostrar_quantidade_cursos(cls):
        return f"Quantidade de curso: {cls.quantidade_cursos}"
    
curso1 = Curso("Redes de Computadores")
curso2 = Curso("Desenvolvimento de Software Multiplataforma")

print(Curso.mostrar_quantidade_cursos())

Curso.alterar_quantidade_cursos(5)

print(Curso.mostrar_quantidade_cursos())