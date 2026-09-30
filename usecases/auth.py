import bcrypt

import data.sqlite as db


def signup(email, password, name):
    user = {"email": email, "password": _hash(password), "name": name}

    db.users.create(user=user)


def signin(email, anPassword):
    found_user = db.users.find_by_email(email)
    if not found_user:
        raise ValueError()

    print(found_user)
    # if _hash(anPassword) == found_user


def _hash(password):
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
