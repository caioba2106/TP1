class NotificacaoEmail:

    def enviar(self, destinatario, mensagem):
        print(f"Enviando Email para {destinatario}: '{mensagem}' via servidor de correio eletrônico.")

class NotificacaoSMS:

    def enviar(self, destinatario, mensagem):
        print(f"Enviando SMS para {destinatario}: '{mensagem}' via rede móvel.")

class NotificacaoPush:

    def enviar(self, destinatario, mensagem):
        print(f"Enviando Push para {destinatario}: '{mensagem}' diretamente no app.")

notf_email = NotificacaoEmail()
notf_sms = NotificacaoSMS()
notf_push = NotificacaoPush()

notf_email.enviar("caio@email.com", "Você tem um novo boleto disponível.")
notf_sms.enviar("+5519999552266", "Código de verificação: 123456")
notf_push.enviar("usuario_123", "Nova mensagem recebida no chat!")