from collections.abc import Iterable

from textual import on
from textual.containers import Vertical
from textual.validation import Validator
from textual.widgets import Input, Static


class FormField(Vertical):
    def __init__(
        self,
        id: str,
        placeholder: str,
        validators: Validator | Iterable[Validator],
        password: bool = False,
        **kwargs,
    ):
        self.password = password
        self.placeholder = placeholder
        self.validators = validators
        super().__init__(classes="h_auto", id=id, **kwargs)

    def compose(self):
        yield Input(
            placeholder=self.placeholder,
            validators=self.validators,
            password=self.password,
        )
        yield Static(classes="error")

    def is_valid(self):
        input = self.query_one(Input)
        return input.is_valid and bool(input.value.strip())

    @on(Input.Changed)
    def show_invalid_reason(self, event: Input.Changed):
        error: Static = self.query_one(".error")
        failure_descriptions = event.validation_result.failure_descriptions

        if failure_descriptions:
            error_message = (
                "* Esse campo possui " + " e ".join(failure_descriptions) + "."
            )
            error.update(error_message)
        else:
            error.update("")

    @property
    def value(self):
        return self.query_one(Input).value
