class Personagem:

    def __init__(self, nome, vida, forca):
        self.nome = nome
        self.vida = vida
        self.forca = forca

    def status(self):
        print(f"{self.nome} - Vida: {self.vida}, Força: {self.forca}")

class Guerreiro(Personagem):

    def __init__(self, nome, vida, forca):
        super().__init__(nome, vida, forca)

    def usar_habilidade(self):
        print(f"{self.nome} usa Ataque Poderoso! Dano causado: {self.forca * 2}")

class Mago(Personagem):

    def __init__(self, nome, vida, forca):
        super().__init__(nome, vida, forca)

    def usar_habilidade(self):
        print(f"{self.nome} lança Bola de Fogo! Dano mágico: {self.forca * 1.5:.1f}")


char_guerreiro = Guerreiro("Thorin", 100, 20)
char_mago = Mago("Elena", 80, 25)

char_guerreiro.status()
char_guerreiro.usar_habilidade()
print()
char_mago.status()
char_mago.usar_habilidade()
