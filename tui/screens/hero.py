from textual.containers import Container
from textual.screen import Screen
from textual.widgets import Static

from tui.widgets.carousel import Carousel
from tui.widgets.signin_form import SigninForm
from tui.widgets.signup_form import SignupForm
from tui.widgets.title import Title


class HeroScreen(Screen):
    CSS_PATH = "hero.tcss"

    def compose(self):
        with Container(classes="hero"):
            yield IntroPanel(id="intro_panel", classes="hero_panel")
            yield AuthPanel(id="auth_panel", classes="hero_panel")


class IntroPanel(Container):
    def compose(self):
        elements = [
            [
                Title("Teste Vocacional"),
                Static("Encontre o curso que você deseja."),
            ],
            [
                Title("Guia de Cursos"),
                Static("Entenda o que cada curso faz."),
            ],
        ]

        yield Carousel(elements=elements)


class AuthPanel(Container):
    def compose(self):
        yield Title("Lumen")
        yield Static("Trilhe o seu caminho até a universidade.")

        yield SigninForm(on_signup=self.show_signup)

    def show_signup(self):
        self.query_one(SigninForm).remove()

        self.mount(
            SignupForm(
                on_signin=self.show_signin,
            )
        )

    def show_signin(self):
        self.query_one(SignupForm).remove()

        self.mount(
            SigninForm(
                on_signup=self.show_signup,
            )
        )
