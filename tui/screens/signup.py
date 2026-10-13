import sqlite3

from textual.screen import Screen
from textual.validation import Length, Regex

from tui.widgets.form import Form
from tui.widgets.form_field import FormField
from usecases.user import signup


class SignupScreen(Screen):
    DEFAULT_CSS = """
      SignupScreen {
          align: center middle;
      }
    """

    def compose(self):
        yield Form(
            title="Criar conta",
            footer="Já possuo conta",
            submit_message="Criar conta",
            on_footer_pressed=lambda: self.app.navigate("signin"),
            menu_message="Voltar ao menu",
            on_menu_pressed=lambda: self.app.navigate("home"),
            fields=[
                FormField(
                    id="name",
                    placeholder="Nome",
                    validators=[
                        Length(
                            minimum=3,
                            maximum=64,
                            failure_description="tamanho inválido",
                        ),
                    ],
                ),
                FormField(
                    id="email",
                    placeholder="E-mail",
                    validators=[
                        Regex(
                            r"(?i)^[a-z0-9.]+@[a-z0-9]+\.[a-z]+(\.[a-z]+)?$",
                            failure_description="formato inválido",
                        ),
                    ],
                ),
                FormField(
                    id="password",
                    placeholder="Senha",
                    password=True,
                    validators=[
                        Length(
                            minimum=8,
                            failure_description="mínimo de 8 caracteres",
                        ),
                    ],
                ),
            ],
            on_submit=self.handle_signup,
        )

    def handle_signup(self, form: Form):
        name = form.query_one("#name").value
        email = form.query_one("#email").value
        password = form.query_one("#password").value

        try:
            user = signup(name=name, email=email, password=password)
            if user:
                self.app.notify("Conta criada com sucesso.")
                self.app.set_session(user)
                self.app.navigate("dashboard")
            else:
                self.app.notify("Não foi possível criar a sua conta.", severity="error")
        except sqlite3.IntegrityError:
            self.app.notify("Esse e-mail já está sendo utilizado", severity="error")
        except sqlite3.OperationalError:
            self.app.notify("Limite de requisições atingido", severity="error")
