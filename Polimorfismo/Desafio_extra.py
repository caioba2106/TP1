class Pagamento:
    
    def __init__(self, valor):
        self.valor = valor

    def processar(self):
        raise NotImplementedError("Este método deve ser implementado pelas subclasses.")

class PagamentoCartao(Pagamento):

    def processar(self):
        print(f"Pagamento de R${self.valor:.2f} processado com sucesso no cartão!")

class PagamentoPix(Pagamento):

    def processar(self):
        print(f"Pagamento de R${self.valor:.2f} via Pix concluído instantaneamente!")

class PagamentoBoleto(Pagamento):

    def processar(self):
        print(f"Boleto gerado no valor de R${self.valor:.2f}. Aguarde a compensação bancária.")

print("Bem-vindo ao sistema de pagamentos!")
valor = float(input("Informe o valor do pagamento: R$"))
print("Escolha o método de pagamento:")
print("1 - Cartão")
print("2 - Pix")
print("3 - Boleto")

opcao = input("Opção: ")

if opcao == "1":
    pagamento = PagamentoCartao(valor)
elif opcao == "2":
    pagamento = PagamentoPix(valor)
elif opcao == "3":
    pagamento = PagamentoBoleto(valor)
else:
    print("Opção inválida.")
    pagamento = None

if pagamento:
    pagamento.processar()
