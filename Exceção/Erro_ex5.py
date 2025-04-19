class CPFInvalidoError(Exception):
    pass

def validar_cpf(CPF):
    if len(CPF) < 11:
        raise CPFInvalidoError("Erro: O CPF deve conter pelo menos 11 caracteres.")
    
    elif not CPF.isdigit():
        raise CPFInvalidoError("Erro: O CPF deve conter apenas números.")
    
    else:
        print("CPF válido")

try:
    CPF = "12345678"
    validar_cpf(CPF)

except CPFInvalidoError as e:
    print(f"Exceção capturada -- {e}")