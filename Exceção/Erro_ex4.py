class IdadeInvalidaError(Exception):
    pass

def verificar_idade(idade):
    if idade < 0:
        raise IdadeInvalidaError("Erro: A idade não pode ser menor que 0.")
    else:
        print(f"A idade fornecida é válida: {idade} anos.")

try:
    verificar_idade(-5)

except IdadeInvalidaError as e:
    print(f"Exceção capturada -- {e}")