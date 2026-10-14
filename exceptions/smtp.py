class SmtpError(Exception):
    message = "Não foi possível enviar o email"

    def __init__(self):
        super().__init__(self.message)
