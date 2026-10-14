from textual import on
from textual.screen import Screen
from textual.widgets import Button

from exceptions.auth import AuthError
from tui.forms.auth_fields import email_field, name_field, password_field
from tui.widgets.form.form import Form
from tui.widgets.navigate.back_button import BackButton
from usecases.user import signup


class SignupScreen(Screen):
    def compose(self):
        signin_button = Button("Já possuo uma conta", id="signin_button")

        yield BackButton()
        yield Form(
            title="Cadastro de Usuário",
            footer=[signin_button],
            submit_message="Criar conta",
            fields=[name_field(), email_field(), password_field()],
            on_submit=self.handle_signup,
        )

    def handle_signup(self, values: dict):
        name = values["name"]
        email = values["email"]
        password = values["password"]

        try:
            user = signup(name=name, email=email, password=password)
            self.app.set_current_user(user)
            self.app.notify("Conta criada com sucesso.")

            self.app.navigate("dashboard")
        except AuthError as e:
            self.app.notify(e.message, severity="error")

    @on(Button.Pressed, "#signin_button")
    def on_signin_button(self):
        self.app.navigate("signin")
