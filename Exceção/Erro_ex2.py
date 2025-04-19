def calcular_media(numeros):
    try:
        media = sum(numeros) / len(numeros)

    except:
        return "Erro: A lista deve conter apenas números."
    
    else:
        return f"A média dos números é: {media}"
    
numeros_corretos = [10, 20, 30, 40, 50]
numeros_errados = [10, 20, 30, 40, 'cinquenta']

print(calcular_media(numeros_corretos))
print(calcular_media(numeros_errados))