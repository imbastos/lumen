from textual.app import App

from models.user import User
from tui.screens.dashboard import DashboardScreen
from tui.screens.home import HomeScreen
from tui.screens.signin import SigninScreen
from tui.screens.signup import SignupScreen


class TextualApp(App):
    def __init__(self, **kwargs):
        self.SCREENS = {
            "home": HomeScreen,
            "signup": SignupScreen,
            "signin": SigninScreen,
            "dashboard": DashboardScreen,
        }
        self.user_session = None
        super().__init__(**kwargs)

    def on_mount(self):
        self.push_screen("home")

    def set_session(self, user: User):
        self.user_session = user

    def navigate(self, route: str):
        PUBLIC_ROUTES = ["home", "signup", "signin"]
        
        if route in PUBLIC_ROUTES or self.user_session:
            self.switch_screen(route)
        else:
            self.switch_screen("home")
