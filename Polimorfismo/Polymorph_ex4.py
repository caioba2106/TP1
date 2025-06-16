class Passaro:

    def movimentar(self):
        print("O pássaro voa pelos céus com graciosidade!")

class Peixe:

    def movimentar(self):
        print("O peixe nada silenciosamente pelas águas!")


bichos = [Passaro(), Peixe()]

for bicho in bichos:
    bicho.movimentar()