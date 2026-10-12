from attrs import define


@define
class User:
    name: str
    email: str
    hashed_password: str
    id: str | None = None
