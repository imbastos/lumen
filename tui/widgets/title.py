from pyfiglet import Figlet
from textual.widgets import Static


class Title(Static):
    DEFAULT_CSS = """
    Title{
        color: $primary;
        width: 100%;
    }
    """
    cybermedium = Figlet(font="cybermedium")

    def __init__(self, content: str, **kwargs):
        formatted_content = "[b]" + self.cybermedium.renderText(content) + "[/]"
        super().__init__(formatted_content, classes="title", **kwargs)
