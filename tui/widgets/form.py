from collections.abc import Callable, Iterable

from textual import on
from textual.containers import Container
from textual.widgets import Button, Input, Static

from tui.widgets.form_field import FormField


class Form(Container):
    DEFAULT_CSS = """
    Form{
      border: round $surface;
      height: auto;
      width: 0.3fr;
    }

    Form FormField{
      margin-bottom: 1;
    }
    
    Form Button{
      margin: 0 1;
      width: 1fr;
    }
    
    Form #submit{
      background: $primary;
    }
    
    Form #footer{
      margin: 1 1 0 1;
    }
    
    Form #title{
      text-align: center;
      margin: 1 0 2 0;
      width: 1fr;
    }
    """

    def __init__(
        self,
        title: str,
        fields: Iterable[FormField],
        on_submit: Callable[["Form"], None],
        submit_message: str = "Confirmar",
        footer: str | None = None,
        on_footer_pressed: Callable[[], None] | None = None,
        **kwargs,
    ):
        self.filled = False
        self.fields = fields
        self.title = title
        self.footer = footer
        self.on_submit = on_submit
        self.on_submit = on_submit
        self.submit_message = submit_message
        self.on_footer_pressed = on_footer_pressed
        super().__init__(**kwargs)

    def compose(self):
        yield Static(self.title, id="title")
        yield from self.fields
        yield Button(self.submit_message, disabled=True, id="submit")
        if self.footer:
            yield Button(self.footer, id="footer")

    def on_mount(self):
        self.update_submit_state()

    @on(Input.Changed)
    def on_input_changed(self, event: Input.Changed):
        self.update_submit_state()

    def update_submit_state(self):
        fields = self.query(FormField)
        all_valid = all(field.is_valid() for field in fields)

        self.query_one("#submit", Button).disabled = not all_valid

    @on(Button.Pressed, "#submit")
    def on_form_submit(self, event: Button.Pressed):
        self.on_submit(self)

    @on(Button.Pressed, "#footer")
    def on_footer_pressed(self, event: Button.Pressed):
        self.on_footer_pressed()
