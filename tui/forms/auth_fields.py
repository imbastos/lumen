from textual.validation import Length, Regex

from tui.widgets.form.field import FormField


def name_field():
    return FormField(
        id="name",
        placeholder="Nome",
        validators=[
            Length(
                minimum=3,
                maximum=64,
                failure_description="tamanho inválido",
            ),
        ],
    )


def email_field():
    return FormField(
        id="email",
        placeholder="E-mail",
        validators=[
            Regex(
                r"(?i)^[a-z0-9.]+@[a-z0-9]+\.[a-z]+(\.[a-z]+)?$",
                failure_description="formato inválido",
            ),
        ],
    )


def password_field():
    return FormField(
        id="password",
        placeholder="Senha",
        password=True,
        validators=[
            Length(
                minimum=8,
                failure_description="mínimo de 8 caracteres",
            ),
        ],
    )
