from textual import on
from textual.containers import Vertical
from textual.validation import Length, Regex
from textual.widgets import Button, Input, Static


class SigninForm(Vertical):
    def __init__(self, on_signup, on_submit=None, **kwargs):
        super().__init__(**kwargs)
        self.on_submit = on_submit
        self.on_signup = on_signup

    def compose(self):
        yield Input(
            placeholder="E-mail",
            id="email",
            validators=[
                Length(
                    minimum=4,
                    maximum=32,
                    failure_description="ter entre 4 e 32 caracteres",
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
        yield Button(label="Entrar", id="submit", disabled=True)
        yield Button(label="Não possuo conta", id="signup", flat=True)

    @on(Input.Changed)
    def show_invalid_reasons(self, event: Input.Changed) -> None:
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
        # found_user("")
        if self.on_submit:
            self.on_submit()

    @on(Button.Pressed, "#signup")
    def signup_button(self):
        self.on_signup()
