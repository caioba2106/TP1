class Funcionario:
    
    bonus = 1000

    @classmethod
    def modificar_bonus(cls, valor):
        cls.bonus = valor
        print(f"Bônus alterado para: R${cls.bonus:.2f}")

print(f"Bônus inicial: R${Funcionario.bonus:.2f}")

Funcionario.modificar_bonus(2000)
