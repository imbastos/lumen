from textual import on
from textual.containers import Container, Horizontal, VerticalScroll
from textual.screen import Screen
from textual.widgets import Button, Static


class DashboardScreen(Screen):
    # o temo DEFAULT_CSS define a aparência dos componentes da tela.

    DEFAULT_CSS = """     
        DashboardScreen {
            align: center middle;
        }

        #dashboard {
            border: round $surface;
            height: 80%;
            width: 0.3fr;
        }

        #menu_scroll {
            width: 100%;
            height: 1fr;
        }

        #dashboard Static {
            text-align: center;
        }

        #dashboard #header {
            margin: 0 6;
            height: auto;
        }

        #dashboard #header Button {
            width: 8;
            max-width: 8;
            margin-right: 1;
        }

        #dashboard #title_header {
            text-align: left;
            margin: 1 0 2 0;
            width: 1fr;
            height: auto;
            color: $primary;
        }

        #menu_scroll #welcome {
            margin: 1 2;
            height: auto;
        }

        #menu_scroll #description  {
            margin: 0 2 2 2;
            height: auto;
        }

        #menu_scroll Button {
            width: 1fr;
            margin: 1 5;
        }
        
        #menu_scroll #vocational_description {
            margin: 0 4 2 4;
            height: auto;
         }
    """

    def compose(self):
        user = self.app.user_session
        name = getattr(user, "name", None) if user else None

        if name:
            welcome_message = f"Bem-vindo(a) ao menu, {name}!"
        else:
            welcome_message = "Bem-vindo(a) ao menu!"

        yield Container(
            Horizontal(
                Static("LUMEN", id="title_header"),
                Button("Sair", flat=True, id="logout"),
                id="header",
            ),
            VerticalScroll(
                Static(
                    welcome_message,
                    id="welcome",
                ),
                Static(
                    "Explore possibilidades para seu futuro profissional!",
                    id="description",
                ),
                Button(
                    "Teste vocacional",
                    id="vocational_button",
                    variant="primary",
                ),
                Static(
                    "Faça o teste vocacional e descubra seus "
                    "principais perfis de interesse.",
                    id="vocational_description",
                ),
                Button(
                    "🔒 Guia de cursos",
                    id="courses",
                    disabled=True,
                ),
                Button(
                    "🔒 Plano de estudos",
                    id="study_plan",
                    disabled=True,
                ),
                Button(
                    "🔒 Ingresso na universidade",
                    id="admission",
                    disabled=True,
                ),
                id="menu_scroll",
            ),
            id="dashboard",
        )

    @on(Button.Pressed, "#vocational_button")
    def on_vocational(self, event: Button.Pressed):
        self.app.navigate("vocational")

    @on(Button.Pressed, "#logout")
    def on_logout(self, event: Button.Pressed):
        self.app.set_session(None)
        self.app.navigate("home")
