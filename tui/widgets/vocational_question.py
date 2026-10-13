from textual.containers import Container, Horizontal
from textual.widgets import Static

from models.riasec_question import RiasecQuestion
from tui.widgets.scale_button import ScaleButton


class VocationalQuestion(Container):
    DEFAULT_CSS = """
      VocationalQuestion Horizontal{
        margin-top: 1;
      }
    """

    def __init__(self, riasec_question: RiasecQuestion, **kwargs):
        self.riasec_question = riasec_question
        self.score: int | None = None
        super().__init__(**kwargs)

    def set_score(self, score):
        self.score = score

    def compose(self):
        yield Static(self.riasec_question.text, id="text")
        yield Horizontal(
            *[
                ScaleButton(
                    index=i - 3,
                )
                for i in range(1, 6)
            ]
        )
