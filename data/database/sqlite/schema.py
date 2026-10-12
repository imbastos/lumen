from .connection import get_connection


def initialize_database() -> None:
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL CHECK(length(name) <= 32),
                email TEXT NOT NULL UNIQUE
                    CHECK(length(email) <= 64),
                hashed_password TEXT NOT NULL
            );
        """)
