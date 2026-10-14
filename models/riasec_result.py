from datetime import datetime

from attrs import define


@define
class RiasecResult:
    user_id: int
    r: int = 0
    i: int = 0
    a: int = 0
    s: int = 0
    e: int = 0
    c: int = 0
    created_at: datetime | None = None
    id: int | None = None

    def get_ranking(self):
        return {
            "R": self.r,
            "I": self.i,
            "A": self.a,
            "S": self.s,
            "E": self.e,
            "C": self.c,
        }
