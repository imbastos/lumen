from textual import on
from textual.containers import Vertical
from textual.validation import Length, Regex
from textual.widgets import Button, Input, Static

from usecases.auth import signup


class SignupForm(Vertical):
    def __init__(self, on_signin, on_submit=None, **kwargs):
        super().__init__(**kwargs)
        self.on_submit = on_submit
        self.on_signin = on_signin

    def compose(self):
        yield Input(
            placeholder="Nome de usuário",
            id="name",
            validators=[
                Length(
                    minimum=3,
                    maximum=32,
                    failure_description="ter entre 3 e 32 caracteres",
                ),
            ],
        )
        yield Input(
            placeholder="E-mail",
            id="email",
            validators=[
                Length(
                    minimum=8,
                    maximum=64,
                    failure_description="ter entre 8 e 64 caracteres",
                ),
                Regex(
                    regex=r"^\S+@\S+\.\S+$",
                    failure_description="ser um e-mail válido",
                ),
            ],
        )
        yield Input(
            placeholder="Senha",
            id="password",
            password=True,
            validators=[
                Length(
                    minimum=8,
                    maximum=64,
                    failure_description="ter no mínimo 8 caracteres",
                )
            ],
        )
        yield Static(id="error_message")
        yield Button(label="Criar", id="submit", disabled=True)
        yield Button(label="Já possuo conta", id="signin", flat=True)

    @on(Input.Changed)
    def show_invalid_reasons(self, event: Input.Changed) -> None:
        # TODO: Refazer lógica de validar os campos, não funciona bem.
        fields = [
                    self.query_one("#name"),
                    self.query_one("#email"),
                    self.query_one("#password"),
                ]
                
        if all(field.is_valid for field in fields):
            self.query_one("#submit").disabled = False
        else:
            self.query_one("#submit").disabled = True

        if not event.validation_result.is_valid:
            self.query_one("#error_message").update(
                "O campo deve "
                + " e deve ".join(event.validation_result.failure_descriptions)
                + "."
            )
        else:
            self.query_one("#error_message").update("")

    @on(Button.Pressed, "#submit")
    def submit_button(self):
        fields = [
            self.query_one("#name"),
            self.query_one("#email"),
            self.query_one("#password"),
        ]
        
        if all(field.is_valid for field in fields):
            signup(fields[0].value, fields[1].value, fields[2].value)
            
        if self.on_submit:
            self.on_submit()

    @on(Button.Pressed, "#signin")
    def signin_button(self):
        self.on_signin()
