from textual.containers import Container
from textual.widgets import Static


class ScaleButton(Container):
    DEFAULT_CSS = """
        .index--1, .index--2 {
            color: $error;
        }
        
        .index-1, .index-2 {
            color: $success;
        }
    """

    NOT_FILLED = ".--.\n|    |\n`--´"
    FILLED = ".aa.\n|@@@@|\n`aa´"

    def __init__(self, index: int, **kwargs):
        self.index = index
        self.state = False

        super().__init__(**kwargs)

    def compose(self):
        yield Static(self.NOT_FILLED, classes=f"index-{self.index}")

    def on_click(self):
        buttons = self.parent.query(ScaleButton)
        for button in buttons:
            if button.state == True:
                button.disable()

        self.enable()
        self.parent.parent.set_score(self.index)
        self.screen.query_one("#vocational_test").update_submit_state()

    def enable(self):
        self.state = True
        self.query_one(Static).update(self.FILLED)

    def disable(self):
        self.state = False
        self.query_one(Static).update(self.NOT_FILLED)
