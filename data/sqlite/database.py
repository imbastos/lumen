import sqlite3

from src.config import SQLITE_FILE


def get_connection() -> sqlite3.Connection:
    return sqlite3.connect(SQLITE_FILE)


def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS `users`(
            `user_id` INTEGER PRIMARY KEY AUTOINCREMENT,
            `user_name` VARCHAR(32) NOT NULL,
            `user_email` VARCHAR(64) NOT NULL,
            `user_password` VARCHAR(60) NOT NULL
            );"""
    )
    conn.commit()
