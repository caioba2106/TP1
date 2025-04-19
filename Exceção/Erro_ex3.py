def solicitar_numero_inteiro():
    while True:
        try:
            numero = int(input("Digite um número inteiro: "))
            print(f"Você digitou o número {numero}.")
            break

        except ValueError:
            print("Erro: Valor inválido. Por favor, digite apenas números inteiros.")

solicitar_numero_inteiro()