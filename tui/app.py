from textual.app import App

from models.user import User
from tui.screens.dashboard import DashboardScreen
from tui.screens.home import HomeScreen
from tui.screens.signin import SigninScreen
from tui.screens.signup import SignupScreen
from tui.screens.vocational.vocational import VocationalScreen
from tui.theme import lumen_theme


class TextualApp(App):
    def __init__(self, **kwargs):
        self.CSS_PATH = ["styles/app.tcss"]
        self.SCREENS = {
            "home": HomeScreen,
            "signup": SignupScreen,
            "signin": SigninScreen,
            "dashboard": DashboardScreen,
            "vocational": VocationalScreen,
        }
        self.current_user = None
        super().__init__(**kwargs)

    def on_mount(self):
        self.register_theme(lumen_theme)
        self.theme = "lumen"

        self.push_screen("home")

    def set_current_user(self, user: User):
        self.current_user = user

    def navigate(self, route: str):
        PUBLIC_ROUTES = ["home", "signup", "signin"]
        if route in PUBLIC_ROUTES:
            if self.current_user is not None:
                self.switch_screen("dashboard")
            else:
                self.switch_screen(route)

        elif self.current_user is not None:
            self.switch_screen(route)

        else:
            self.switch_screen("home")

        self.last_page = self.screen.name
