from pyfiglet import figlet_format
from textual import on
from textual.containers import Center, Container, Vertical
from textual.screen import Screen
from textual.widgets import Button, Label


class DashboardScreen(Screen):
    def compose(self):
        user = self.app.current_user

        if user.name:
            welcome_message = f"Bem-vindo(a) ao menu, [$secondary]{user.name}!"
        else:
            welcome_message = "Bem-vindo(a) ao menu!"

        yield Container(
            Center(
                Label(f"[$primary]{figlet_format('Lumen')}"),
                Label(welcome_message),
                Label(
                    "[$foreground-muted]Explore possibilidades para seu futuro profissional!"
                ),
            ),
            Vertical(
                Button(
                    "Teste vocacional",
                    id="vocational_button",
                    variant="primary",
                ),
                Label(
                    "Faça o teste vocacional e descubra seus "
                    "principais perfis de interesse.",
                    id="vocational_description",
                ),
            ),
            Button("🔒 Guia de cursos", disabled=True),
            Button("🔒 Plano de estudos", disabled=True),
            Button("🔒 Ingresso na universidade", disabled=True),
            Button("⇥ Sair", variant="error", id="logout"),
            classes="box",
        )

    @on(Button.Pressed, "#vocational_button")
    def on_vocational(self):
        self.app.navigate("vocational")

    @on(Button.Pressed, "#logout")
    def on_logout(self):
        self.app.set_current_user(None)
        self.app.navigate("home")
