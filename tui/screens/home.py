from pathlib import Path

from pyfiglet import figlet_format
from textual import on
from textual.containers import (
    Center,
    Container,
    Horizontal,
    Middle,
    Vertical,
    VerticalScroll,
)
from textual.screen import Screen
from textual.widgets import Button, Label


class HomeScreen(Screen):
    DEFAULT_CSS = """
    #star{
        text-align: center;
        width: 1fr;
    }
    
    .title{
        margin-top: 8;
        offset-y: -7;
    }
    
    Middle{
        max-height: 15;
    }
    """

    def compose(self):
        star_path = Path(__file__).resolve().parents[1] / "assets" / "stars.txt"

        star_art = star_path.read_text(encoding="utf-8").strip("\n")

        yield Container(
            Middle(
                Label(f"[$secondary]{star_art}", id="star"),
                Label(f"[$primary]{figlet_format('Lumen')}", classes="title"),
            ),
            VerticalScroll(
                Center(
                    Label(
                        "Estudante, seu caminho para a universidade começa [bold $secondary]aqui![/bold $secondary]"
                    ),
                    Label(
                        "[$foreground-muted]Explore cursos, descubra suas afinidades e planeje seu futuro acadêmico."
                    ),
                ),
                Horizontal(
                    Vertical(
                        Center(
                            Label("[$foreground-muted]Não possuo cadastro"),
                            Button(
                                variant="primary",
                                label="Crie sua conta",
                                id="signup_button",
                            ),
                        )
                    ),
                    Vertical(
                        Center(
                            Label("[$foreground-muted]Já tenho uma conta"),
                            Button(label="Entrar", id="signin_button"),
                        )
                    ),
                ),
            ),
            classes="box",
        )

    @on(Button.Pressed, "#signup_button")
    def on_authenticate_signup(self, event: Button.Pressed):
        self.app.navigate("signup")

    @on(Button.Pressed, "#signin_button")
    def on_authenticate_login(self, event: Button.Pressed):
        self.app.navigate("signin")
