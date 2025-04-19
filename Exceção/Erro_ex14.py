def dividir_numeros():
    try:
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        resultado = a / b

    except ValueError:
        print("Erro: Você deve digitar números válidos.")

    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida.")

    else:
        print(f"Resultado da divisão: {resultado:.2f}")

    finally:
        print("Operação finalizada.")


if __name__ == "__main__":
    dividir_numeros()