class Email:

    def enviar_mensagem(self, destinatario, mensagem):
        print(f"Enviando Email para {destinatario}: '{mensagem}' via servidor SMTP... ")

class SMS:

    def enviar_mensagem(self, destinatario, mensagem):
        print(f"Enviando SMS para {destinatario}: '{mensagem}' usando operadora de telefonia... ")

class Whatsapp:

    def enviar_mensagem(self, destinatario, mensagem):
        print(f"Enviando WhatsApp para {destinatario}: '{mensagem}' com notificação via app... ")
    

mensagem1 = Email()
mensagem2 = SMS()
mensagem3 = Whatsapp()

mensagem1.enviar_mensagem("caio@example.com", "Olá Caio, tudo bem?")
mensagem2.enviar_mensagem("+5511999999999", "Não esqueça da reunião às 15h!")
mensagem3.enviar_mensagem("+5511988888888", "Já chegou em casa?")