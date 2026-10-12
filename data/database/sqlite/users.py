from data.database.sqlite.connection import get_connection
from models.user import User


def create(user: User):
    conn = get_connection()
    cursor = conn.cursor()

    query = "INSERT INTO users (name, email, hashed_password) VALUES (?, ?, ?);"

    cursor.execute(query, (user.name, user.email, user.hashed_password))
    conn.commit()


def get_all():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users;")
    return cursor.fetchall()


def get(id):
    conn = get_connection()
    cursor = conn.cursor()

    query = "SELECT * FROM users WHERE id = ?;"

    cursor.execute(query, (id,))
    return cursor.fetchone()


def find_by_email(email):
    conn = get_connection()
    cursor = conn.cursor()

    query = "SELECT * FROM users WHERE email = ?;"
    cursor.execute(query, (email,))

    row = cursor.fetchone()
    conn.close()

    if row is None:
        return None

    return User(id=row[0], name=row[1], email=row[2], hashed_password=row[3])


def update(user):
    conn = get_connection()
    cursor = conn.cursor()

    query = "UPDATE users SET name = ?, course = ? WHERE id = ?;"

    cursor.execute(query, (user["name"], user["course"], user["id"]))
    conn.commit()


def delete(id):
    conn = get_connection()
    cursor = conn.cursor()

    query = "DELETE FROM users WHERE id = ?;"

    cursor.execute(query, (id))
    conn.commit()
