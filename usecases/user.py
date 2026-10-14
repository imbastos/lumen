import data.database.sqlite as db
import utils
from exceptions.auth import InvalidPasswordError
from models.user import User


def signup(name: str, email: str, password: str) -> User:
    user = User(name, email, utils.hash_password(password))
    db.users.create(user)

    return user


def signin(email: str, password: str) -> User:
    found_user = db.users.find_by_email(email)

    if utils.check_password(password, found_user.hashed_password):
        return found_user
    else:
        raise InvalidPasswordError()
