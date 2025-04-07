class Calculadora:

    @staticmethod
    def somar(a, b):
        return a + b
    
totalSoma = Calculadora.somar(2, 4)
print(f"O total da soma foi: {totalSoma}")