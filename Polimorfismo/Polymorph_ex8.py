class Filme:

    def __init__(self, titulo, duracao):
        self.titulo = titulo
        self.duracao = duracao

    def reproduzir(self):
        print(f"Reproduzindo o filme '{self.titulo}' ({self.duracao} minutos). Pipoca pronta?")

class Musica:

    def __init__(self, titulo, artista):
        self.titulo = titulo
        self.artista = artista

    def reproduzir(self):
        print(f"Tocando '{self.titulo}' por {self.artista}. Aperte o play e curta o som!")

streamings = [Filme("A Origem", 148), Musica("Bohemian Rhapsody", "Queen")]

for streaming in streamings:
    streaming.reproduzir()