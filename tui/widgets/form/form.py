from collections.abc import Callable, Iterable

from textual import on
from textual.containers import Container
from textual.widget import Widget
from textual.widgets import Button, Input, Label

from tui.widgets.form.field import FormField


class Form(Container):
    def __init__(
        self,
        title: str,
        fields: Iterable[FormField],
        on_submit: Callable[["Form"], None],
        footer: list[Widget] | None = None,
        submit_message: str = "Confirmar",
        **kwargs,
    ):
        self.filled = False
        self.fields = fields
        self.title = title
        self.footer = footer
        self.on_submit = on_submit
        self.submit_message = submit_message

        super().__init__(classes="box", **kwargs)

    def compose(self):
        yield Container(
            Label(self.title, classes="title"),
            *self.fields,
            Button(
                self.submit_message, variant="primary", disabled=True, classes="submit"
            ),
        )
        if self.footer != None:
            yield Container(*self.footer)

    def on_mount(self):
        self.update_submit_state()

    def update_submit_state(self):
        fields = self.query(FormField)
        all_valid = all(field.is_valid() for field in fields)

        self.query_one(".submit", Button).disabled = not all_valid

    @on(Input.Changed)
    def on_input_changed(
        self,
    ):
        self.update_submit_state()

    @on(Button.Pressed, ".submit")
    def on_form_submit(self):
        self.on_submit(self.get_values())

    def get_values(self):
        values = {}
        for field in self.query(FormField):
            values[field.id] = field.value
        return values
