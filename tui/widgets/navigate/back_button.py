from textual.widgets import Button


class BackButton(Button):
    def __init__(self):
        super().__init__(flat=True, label="‹")

    def on_click(self):
        self.app.navigate("home")
