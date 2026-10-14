from pyfiglet import figlet_format
from textual import on
from textual.containers import Center, Container, Vertical
from textual.screen import Screen
from textual.widgets import Button, Label

from data.database.sqlite.users import update_newsletter_subscription
from models.user import User


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
                    "Faça o teste vocacional e descubra seus principais perfis de interesse.",
                ),
            ),
            Vertical(
                Button(
                    "📰 Assinar a Newsletter",
                    id="newsletter_button",
                    variant="primary",
                ),
                Label(
                    "Receba conteúdos exclusivos direto na sua caixa de entrada.",
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

    @on(Button.Pressed, "#newsletter_button")
    def on_newsletter(self, event: Button.Pressed):
        self.update_newsletter_button()

    def update_newsletter_button(self):
        user: User = self.app.current_user
        button = self.query_one("#newsletter_button", Button)

        subscribed = not user.newsletter_subscribed

        update_newsletter_subscription(
            user_id=user.id,
            subscribed=subscribed,
        )

        user.newsletter_subscribed = subscribed

        if subscribed:
            button.label = "❌ Cancelar a Newsletter"
            button.variant = "error"
        else:
            button.label = "📰 Assinar a Newsletter"
            button.variant = "primary"

    @on(Button.Pressed, "#logout")
    def on_logout(self):
        self.app.set_current_user(None)
        self.app.navigate("home")
