from .connection import get_connection


def initialize_database() -> None:
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL CHECK(length(name) <= 32),
                email TEXT NOT NULL UNIQUE
                    CHECK(length(email) <= 64),
                hashed_password TEXT NOT NULL,
                newsletter_subscribed INTEGER NOT NULL DEFAULT 0
                    CHECK(newsletter_subscribed IN (0, 1))
            );
        """)

        conn.execute("""
            CREATE TABLE IF NOT EXISTS riasec_results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                r INTEGER NOT NULL,
                i INTEGER NOT NULL,
                a INTEGER NOT NULL,
                s INTEGER NOT NULL,
                e INTEGER NOT NULL,
                c INTEGER NOT NULL,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,

                FOREIGN KEY (user_id)
                    REFERENCES users(id)
                    ON DELETE CASCADE
            );
        """)
