def dividir_numeros(a, b):
    try:
        resultado = a / b
        return f"O resultado da divisão é: {resultado}"
    
    except ZeroDivisionError:
        return "Erro: Não é possível dividir por zero."
    
print(dividir_numeros(10, 0))