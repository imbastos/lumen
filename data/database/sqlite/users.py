import sqlite3

from data.database.sqlite.connection import get_connection
from exceptions.auth import AuthError, EmailAlreadyInUseError, UserNotFoundByEmailError
from models.user import User


def create(user: User):
    conn = get_connection()
    try:
        cursor = conn.cursor()

        query = "INSERT INTO users (name, email, hashed_password) VALUES (?, ?, ?);"

        cursor.execute(query, (user.name, user.email, user.hashed_password))
        conn.commit()
    except sqlite3.IntegrityError as e:
        raise EmailAlreadyInUseError() from e
    except sqlite3.Error as e:
        raise AuthError() from e
    finally:
        if conn is not None:
            conn.close()


def get_all():
    conn = get_connection()
    try:
        cursor = conn.cursor()

        query = "SELECT * FROM users;"

        cursor.execute(query)
        return cursor.fetchall()
    finally:
        conn.close()


def get_by_id(user_id: int):
    conn = get_connection()
    try:
        cursor = conn.cursor()

        query = "SELECT * FROM users WHERE id = ?;"

        cursor.execute(query, (user_id,))
        return cursor.fetchone()
    finally:
        conn.close()


def find_by_email(email: str):
    conn = get_connection()

    try:
        cursor = conn.cursor()

        query = "SELECT id, name, email, hashed_password FROM users WHERE email = ?;"

        cursor.execute(query, (email,))
        row = cursor.fetchone()
    finally:
        conn.close()

    if row is None:
        raise UserNotFoundByEmailError()

    return User(
        id=row[0],
        name=row[1],
        email=row[2],
        hashed_password=row[3],
    )


def update(user):
    conn = get_connection()

    try:
        query = "UPDATE users SET name = ?, course = ? WHERE id = ?;"

        conn.execute(query, (user["name"], user["course"], user["id"]))
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def delete(user_id: int):
    conn = get_connection()

    try:
        query = "DELETE FROM users WHERE id = ?;"

        conn.execute(query, (user_id,))
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()
