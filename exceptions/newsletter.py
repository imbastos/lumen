class UserNotFoundByIdError(Exception):
    message = "Usuário não encontrado"

    def __init__(self):
        super().__init__(self.message)
