class Calculadora:
    def dividir(self, a:float, b:float):
        if b == 0:
            raise ZeroDivisionError("Divisão por zero não é permitida.")
        return a / b
    

if __name__ == "__main__":
    calc = Calculadora()

    try:
        resultado = calc.dividir(10, 2)
        print(f"Resultado da divisão: {resultado}")
        resultado = calc.dividir(10, 0)
        print(f"Resultado da divisão: {resultado}")

    except ZeroDivisionError as e:
        print(f"Erro: {e}")