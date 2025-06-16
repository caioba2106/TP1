class Professor:

    def ensinar(self):
        print(f"Ministrando aulas e orientando alunos.")

class Pesquisador:

    def pesquisar(self):
        print(f"Conduzindo pesquisas e publicando artigos científicos.")

class Cientista(Professor, Pesquisador):

    def trabalhar(self):
        print(f"{self.ensinar()} {self.pesquisar()}")


cientista1 = Cientista()
cientista1.trabalhar()