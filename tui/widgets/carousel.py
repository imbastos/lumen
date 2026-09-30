from textual.containers import Container
from textual.widgets import Static


class Carousel(Container):
    DEFAULT_CSS = """
      #progress{
        color: $primary;
      }
    """

    symbols = ("▫", "▪", "■")
    current = 0

    def __init__(self, elements, **kwargs):
        super().__init__(classes="carousel", **kwargs)
        self.elements: list = elements

    def compose(self):
        yield Container(id="content")
        yield Static("", id="progress")

    def on_mount(self):
        self.update_carousel()
        self.set_interval(5.0, self.next_carousel)

    def next_carousel(self):
        self.current = (self.current + 1) % len(self.elements)
        self.update_carousel()

    def update_carousel(self):
        symbols = (
            [self.symbols[1]] * self.current
            + [self.symbols[2]]
            + [self.symbols[0]] * (len(self.elements) - self.current - 1)
        )
        self.query_one("#progress").update(" ".join(symbols))

        content = self.query_one("#content")
        content.remove_children()
        for widget in self.elements[self.current]:
            content.mount(widget)
