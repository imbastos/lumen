from textual import on
from textual.containers import Center, Container, VerticalScroll
from textual.screen import Screen
from textual.widgets import Button, Static

from data.riasec_questions import questions
from tui.widgets.navigate.back_button import BackButton
from tui.widgets.vocational.question import VocationalQuestion


class VocationalScreen(Screen):
    def compose(self):
        yield BackButton()
        yield Container(
            Center(Static("Teste Vocacional", classes="title")),
            VerticalScroll(
                *[VocationalQuestion(question) for question in questions],
                Button("Concluir", disabled=True, variant="primary", classes="submit"),
                id="questions-scroll",
            ),
            classes="box",
        )

    def _is_filled(self):
        return all(
            question.score is not None for question in self.query(VocationalQuestion)
        )

    def update_submit_state(self):
        self.query_one(".submit").disabled = not self._is_filled()

    @on(Button.Pressed, ".submit")
    def on_submit(self, event: Button.Pressed):
        if self._is_filled():
            scores = {}
            for question in self.query(VocationalQuestion):
                profile = question.riasec_question.profile.name
                scores[profile] = scores.get(profile, 0) + question.score

            top_3 = sorted(scores, key=scores.get, reverse=True)[:3]
            self.app.notify(str(top_3))
        else:
            self.app.notify("Conclua o teste.", severity="error")