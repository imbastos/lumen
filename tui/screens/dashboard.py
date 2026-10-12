from textual.screen import Screen
from textual.widgets import Static


class DashboardScreen(Screen):
    def compose(self):
        yield Static("Dashboard")
