from attrs import define


@define
class User:
    name: str
    email: str
    hashed_password: str
    newsletter_subscribed: bool = False
    id: int | None = None
