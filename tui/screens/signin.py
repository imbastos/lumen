from textual.screen import Screen
from textual.validation import Function, Length

from tui.widgets.form import Form
from tui.widgets.form_field import FormField
from usecases.user import signin


class SigninScreen(Screen):
    DEFAULT_CSS = """
      SigninScreen {
          align: center middle;
      }
    """

    def compose(self):
        yield Form(
            title="Entrar",
            footer="Não possuo conta",
            submit_message="Entrar",
            on_footer_pressed=lambda: self.app.navigate("signup"),

            menu_message="Voltar ao menu",
            on_menu_pressed=lambda: self.app.navigate("home"),
         
            fields=[
                FormField(
                    id="email",
                    placeholder="E-mail",
                    validators=[
                        Function(
                            lambda value: "@" in value and "." in value.split("@")[-1],
                            failure_description="e-mail inválido",
                        ),
                    ],
                ),
                FormField(
                    id="password",
                    placeholder="Senha",
                    validators=[
                        Length(
                            minimum=8,
                            failure_description="mínimo de 8 caracteres",
                        ),
                    ],
                ),
            ],
            on_submit=self.handle_signin,
        )

    def handle_signin(self, form: Form):
        email = form.query_one("#email").value
        password = form.query_one("#password").value

        try:
            user = signin(email=email, password=password)
            if user:
                self.app.notify("Acesso autorizado.")
                self.app.set_session(user)
                self.app.navigate("dashboard")
            else:
                self.app.notify("Credenciais inválidas.", severity="error")
        except ValueError:
            self.app.notify("Esse e-mail não está cadastrado.", severity="error")