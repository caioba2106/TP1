class Livro:

    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    @classmethod
    def criar_livro(cls, titulo, autor):
        return cls(titulo, autor)
    
    def detalhes_livro(self):
        return f"Título: {self.titulo}, Autor: {self.autor}"
    
livro1 = Livro.criar_livro("1984", "George Orwell")
livro2 = Livro.criar_livro("Dom Casmurro", "Machado de Assis")

print(livro1.detalhes_livro())
print(livro2.detalhes_livro())