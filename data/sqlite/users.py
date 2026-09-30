from data.sqlite.database import get_connection


def create(user):
    conn = get_connection()
    cursor = conn.cursor()

    query = "INSERT INTO users (user_name, user_email, user_password) VALUES (?, ?, ?);"

    cursor.execute(query, (user["name"], user["email"], user["password"]))
    conn.commit()


def get_all():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users;")
    return cursor.fetchall()


def get(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    query = "SELECT * FROM users WHERE user_id = ?;"

    cursor.execute(query, (user_id,))
    return cursor.fetchone()


def find_by_email(user_email):
    conn = get_connection()
    cursor = conn.cursor()

    query = "SELECT * FROM users WHERE user_email = ?;"

    cursor.execute(query, (user_email,))
    return cursor.fetchone()


def update(user):
    conn = get_connection()
    cursor = conn.cursor()

    query = "UPDATE users SET user_name = ?, user_course = ? WHERE user_id = ?;"

    cursor.execute(query, (user["name"], user["course"], user["id"]))
    conn.commit()


def delete(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    query = "DELETE FROM users WHERE user_id = ?;"

    cursor.execute(query, (user_id))
    conn.commit()
