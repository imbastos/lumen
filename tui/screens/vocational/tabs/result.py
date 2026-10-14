from textual.containers import Center, Container
from textual.widgets import Label, Static

from enums.riasec_profile import RiasecProfile
from usecases.riasec_result import get_latest_by_user_id


class VocationalResult(Container):
    def __init__(self):
        self.latest_test = None
        super().__init__(id="result")

    def compose(self):
        yield Static(
            "[$secondary]Para obter resultados, é necessário realizar o teste",
            classes="hidden" if self.latest_test is None else "",
            id="empty-message",
        )
        yield Center(
            Label(
                "Seu perfil é",
                classes="hidden" if self.latest_test is not None else "",
            )
        )
        yield Static(
            id="profile-description",
            classes="hidden" if self.latest_test is not None else "",
        )

    def on_mount(self):
        self.update_result()

    def update_result(self):
        user = self.app.current_user
        self.latest_test = get_latest_by_user_id(user.id)

        if not self.latest_test:
            return
        ranking = self.latest_test.get_ranking()

        main_profile = RiasecProfile[max(ranking, key=ranking.get)]

        if main_profile != None:
            self.query_one("#profile-description", Static).update(main_profile.value[1])
