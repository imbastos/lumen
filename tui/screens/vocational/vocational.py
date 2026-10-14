from textual.containers import Container
from textual.screen import Screen
from textual.widgets import TabbedContent, TabPane

from tui.screens.vocational.tabs.result import VocationalResult
from tui.screens.vocational.tabs.test import VocationalTest
from tui.widgets.navigate.back_button import BackButton


class VocationalScreen(Screen):
    def compose(self):
        yield BackButton()
        with Container(classes="box"), TabbedContent(id="test_tab"):
            yield TabPane("Teste Vocacional", VocationalTest(), id="test_tab")
            yield TabPane("Resultados", VocationalResult(), id="result_tab")
