import data.database.sqlite as db
from models.riasec_result import RiasecResult


def create(user_id: int, r: int, i: int, a: int, s: int, e: int, c: int):
    riasec_result = RiasecResult(user_id=user_id, r=r, i=i, a=a, s=s, e=e, c=c)
    return db.riasec_results.create(riasec_result)


def get_latest_by_user_id(user_id: int):
    return db.riasec_results.get_latest_by_user_id(user_id)
