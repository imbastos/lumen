from pyfiglet import figlet_format
from textual import on
from textual.containers import Center, Container
from textual.screen import Screen
from textual.widgets import Button, Static


class HomeScreen(Screen):
    DEFAULT_CSS = """
        HomeScreen {
            align: center middle;
        }

        #home_container {
            width: 90%;
            height: auto;
            border: round $surface;
            padding: 1 3;
            align: center middle;
        }

        #star {
            width: 100%;
            height: auto;
            text-align: center;
            color: #FACC15;
            margin: 0;
            padding: 0;
        }

        #title {
            width: 100%;
            height: auto;
            text-align: center;
            color: #A78BFA;
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
            background: #7651A8;
            color: #FFFFFF;
            margin-bottom: 2;
        }

        #login_prompt {
            width: 100%;
            text-align: center;
            margin-bottom: 1;
        }

        #authenticate_login {
            width: 24;
            background: #7651A8;
            color: #FFFFFF;
        }
    """

    def compose(self):
        with Container(id="home_container"):
            yield Static(
                r"""
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⣠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⡏⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠤⣤⣤⣤⣤⣤⣤⣤⣤⣿⣿⠇⠀⢿⣿⣷⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⡶⠶⠶⠶⠶⠶⠶⠶⠶⠖⠒⠒⠒⠒⠒⠒⠒⠂⠀⠀⠀⠀
⠀⠀⠘⢿⣿⣿⣟⠛⠛⠛⠛⠀⠀⠀⠛⠛⠛⠛⠋⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠛⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢹⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣾⣿⠁⢀⣤⣾⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣸⣿⢇⣶⣿⠟⠙⠻⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢠⣿⣿⠿⠋⠁⠀⠀⠀⠀⠉⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                """,
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
