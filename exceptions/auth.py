class AuthError(Exception):
    def __init__(self, message="A operação de autenticação falhou"):
        super().__init__(message)


class EmailAlreadyInUseError(AuthError):
    message = "O e-mail informado já está em uso"

    def __init__(self):
        super().__init__()


class UserNotFoundByEmailError(AuthError):
    message = "Nenhum usuário registrado com esse e-mail"

    def __init__(self):
        super().__init__(self.message)


class InvalidPasswordError(AuthError):
    message = "Senha inválida"

    def __init__(self):
        super().__init__(self.message)
