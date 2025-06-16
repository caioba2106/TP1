class Pagamento:

    def __init__(self, valor):
        self.valor = valor

    def processar(self):
        raise NotImplementedError("Este método deve ser implementado pelas subclasses.")

class PagamentoCartao(Pagamento):

    def processar(self):
        print(f"Processando pagamento de R${self.valor:.2f} no cartão de crédito.")

class PagamentoPix(Pagamento):

    def processar(self):
        print(f"Pagamento de R${self.valor:.2f} via Pix concluído instantaneamente.")

class PagamentoBoleto(Pagamento):

    def processar(self):
        print(f"Gerando boleto bancário no valor de R${self.valor:.2f}. Aguardando compensação...")

pagamentos = [
    PagamentoCartao(150.00),
    PagamentoPix(80.50),
    PagamentoBoleto(200.00),
    PagamentoPix(35.75)
]

for pagamento in pagamentos:
    pagamento.processar()
