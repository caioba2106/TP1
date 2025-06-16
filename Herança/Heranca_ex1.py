class Animal:

    def falar(self):
        return "Som genérico de um animal"
    
class Cachorro(Animal):

    def falar(self):
        return "Au Au!"
    
class Gato(Animal):

    def falar(self):
        return "Miau!"


animais = [Cachorro(), Gato()]

for animal in animais:
    print(animal.falar())