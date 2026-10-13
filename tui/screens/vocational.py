from textual import on
from textual.containers import Container, Horizontal, VerticalScroll
from textual.screen import Screen
from textual.widgets import Button, Static

from data.riasec_questions import questions
from tui.widgets.vocational_question import VocationalQuestion


class VocationalScreen(Screen):
    DEFAULT_CSS = """
      VocationalScreen {
        align: center middle;
      }

      #vocational {
          border: round $surface;
          height: 80%;
          width: 0.3fr;
      }

      #questions-scroll {
          width: 100%;
      }

      #vocational Static {
        text-align: center;
      }
      
      #vocational #header{
        margin: 0 6;
        height: auto;
      }
      
      #vocational #header Button{
        max-width: 5;
        margin-right: 1;
      }
      
      #vocational #title{
        text-align: left;
        margin: 1 0 2 0;
        width: 1fr;
      }

      #questions-scroll VocationalQuestion {
          height: 8;
          margin-bottom: 1;
          padding: 0 6;
      }
      
      #questions-scroll #submit {
          width: 1fr;
          margin: 2 8;
      }
    """

    def compose(self):
        yield Container(
            Horizontal(
                Button("<", flat=True, id="back"),
                Static("Teste Vocacional", id="title"),
                id="header",
            ),
            VerticalScroll(
                *[VocationalQuestion(question) for question in questions],
                Button("Concluir", disabled=True, variant="primary", id="submit"),
                id="questions-scroll",
            ),
            id="vocational",
        )

    def _is_filled(self):
        return all(
            question.score is not None for question in self.query(VocationalQuestion)
        )

    def update_submit_state(self):
        self.query_one("#submit").disabled = not self._is_filled()

    @on(Button.Pressed, "#submit")
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

    @on(Button.Pressed, "#back")
    def on_back(self):
        self.app.navigate("dashboard")
