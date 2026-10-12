from textual import on
from textual.screen import Screen
from textual.widgets import Button, Static


class HomeScreen(Screen):
    def compose(self):
        yield Static("Home")
        yield Button("Entrar", id="authenticate")

    @on(Button.Pressed, "#authenticate")
    def on_authenticate(self, event):
        self.app.navigate("signup")
