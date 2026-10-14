from textual import on
from textual.screen import Screen
from textual.widgets import Button

from exceptions.auth import AuthError
from tui.forms.auth_fields import email_field, password_field
from tui.widgets.form.form import Form
from tui.widgets.navigate.back_button import BackButton
from usecases.user import signin


class SigninScreen(Screen):
    def compose(self):
        signup_button = Button("Não possuo uma conta", id="signup_button")

        yield BackButton()
        yield Form(
            title="Fazer Login",
            footer=[signup_button],
            submit_message="Entrar",
            fields=[email_field(), password_field()],
            on_submit=self.handle_signin,
        )

    def handle_signin(self, values: dict):
        email = values["email"]
        password = values["password"]

        try:
            user = signin(email=email, password=password)
            self.app.set_current_user(user)
            self.app.notify("Acesso autorizado.")

            self.app.navigate("dashboard")
        except AuthError as e:
            self.app.notify(e.message, severity="error")

    @on(Button.Pressed, "#signup_button")
    def on_signup_button(self):
        self.app.navigate("signup")
