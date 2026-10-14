from textual import on
from textual.containers import Container, VerticalScroll
from textual.widgets import Button, Label, TabbedContent

from data.riasec.questions import questions
from tui.widgets.vocational.question import VocationalQuestion
from usecases.riasec_result import create


class VocationalTest(Container):
    def __init__(self):
        super().__init__(id="vocational_test")

    def compose(self):
        yield Label("Teste Vocacional", classes="title")
        yield VerticalScroll(
            *[VocationalQuestion(question) for question in questions],
            Button("Concluir", disabled=True, variant="primary", classes="submit"),
            id="questions-scroll",
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
            user_id = self.app.current_user.id
            r = sum(q.score for q in self.query(".profile-r"))
            i = sum(q.score for q in self.query(".profile-i"))
            a = sum(q.score for q in self.query(".profile-a"))
            s = sum(q.score for q in self.query(".profile-s"))
            e = sum(q.score for q in self.query(".profile-e"))
            c = sum(q.score for q in self.query(".profile-c"))
            create(user_id=user_id, r=r, i=i, a=a, s=s, e=e, c=c)
            self.app.notify("Teste concluido.")

            self.screen.query_one(TabbedContent).active = "result_tab"
            self.screen.query_one("#result").update_result()
        else:
            self.app.notify("Conclua o teste.", severity="error")
