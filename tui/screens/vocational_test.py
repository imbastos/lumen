from textual import on
from textual.containers import Container, Horizontal
from textual.screen import Screen
from textual.widgets import Button, Select, Static

from usecases.vocational_test_auth import (
    AREA_QUESTION,
    QUESTIONS,
    RIASEC_PROFILES,
    SCALE_OPTIONS,
    calculate_profile_scores,
    valid_area_interest,
)

class VocationalTestScreen(Screen):
    CSS_PATH = "vocational_test.tcss"

def __init__(self, **kwargs):
    super().__init__(**kwargs)

    self.current_index = 0
    self.responses = {}
    self.area_interest = None

    def compose(self):
        with Container(id="test_container"):
            yield Static("Teste Vocacional", id="screen_title")
            yield Static("", id="progress")
            yield Static("", id="question_text")

            yield Select(
            [],
            prompt="Selecione uma resposta",
            allow_blank=True,
            id="answer",
        )
