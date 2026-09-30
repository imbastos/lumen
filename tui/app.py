from textual.app import App

from tui.screens.hero import HeroScreen


class LumenApp(App):
    CSS_PATH = "style.tcss"
    SCREENS = {"hero": HeroScreen}  # noqa: RUF012

    def on_mount(self):
        self.push_screen("hero")
