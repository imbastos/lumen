from textual import on
from textual.screen import Screen
from textual.widgets import Button, Static


class DashboardScreen(Screen):
    def compose(self):
        yield Static("Dashboard")
        yield Button("Teste vocacional", id="vocational")

    @on(Button.Pressed, "#vocational")
    def on_vocational(self):
        self.app.navigate("vocational")
