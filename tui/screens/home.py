from pyfiglet import figlet_format
from textual import on
from textual.containers import Center, Container, VerticalScroll
from textual.screen import Screen
from textual.widgets import Button, Static
from pathlib import Path

class HomeScreen(Screen):
    DEFAULT_CSS = """
        HomeScreen {
            align: center middle;
        }

        #home_container {
            border: round $surface;
            height: 90%;
            width: 0.4fr;
            padding: 1 0;
            align: center middle;
        }

        #home_scroll {
            width: 100%;
            height: 1fr;
        }

        #star {
            width: 100%;
            height: auto;
            text-align: center;
            color: $secondary;
            margin: 0;
            padding: 0;
        }

        #title {
            width: 100%;
            height: auto;
            text-align: center;
            color: $primary;
            margin-top: 0;
        }

        #description {
            width: 100%;
            height: auto;
            text-align: center;
            margin: 0 0 2 0;
        }

        #signup_prompt {
            width: 100%;
            text-align: center;
            margin-bottom: 1;
        }

        #authenticate_signup {
            width: 24;
            margin-bottom: 2;
        }

        #login_prompt {
            width: 100%;
            text-align: center;
            margin-bottom: 1;
        }

        #authenticate_login {
            width: 24;
        }
    """

    def compose(self):

        star_path = (
            Path(__file__).resolve().parents[1]
            / "assets"
            / "stars.txt"
        )

        star_art = star_path.read_text(
            encoding="utf-8"
        ).strip("\n")

        with Container(id="home_container"):

            # Coloca todos os componentes dentro da área rolável.
            with VerticalScroll(id="home_scroll"):

                yield Static(
                    star_art,
                    id="star",
                )

                yield Static(
                    figlet_format("LUMEN", font="standard"),
                    id="title",
                )

                yield Static(
                    "Estudante, seu caminho para a universidade "
                    "começa aqui!\n"
                    "Explore cursos, descubra suas afinidades "
                    "e planeje seu futuro acadêmico.",
                    id="description",
                )

                yield Static(
                    "Não possui cadastro? Crie sua conta:",
                    id="signup_prompt",
                )

                with Center():
                    yield Button(
                        "Cadastrar",
                        id="authenticate_signup",
                        variant="primary",
                    )

                yield Static(
                    "Já é cadastrado? Faça login:",
                    id="login_prompt",
                )

                with Center():
                    yield Button(
                        "Login",
                        id="authenticate_login",
                        variant="primary",
                    )

    @on(Button.Pressed, "#authenticate_signup")
    def on_authenticate_signup(self, event: Button.Pressed):
        self.app.navigate("signup")

    @on(Button.Pressed, "#authenticate_login")
    def on_authenticate_login(self, event: Button.Pressed):
        self.app.navigate("signin")
