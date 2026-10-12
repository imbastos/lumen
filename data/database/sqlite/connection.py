import sqlite3

from config import SQLITE_FILE


def get_connection() -> sqlite3.Connection:
    return sqlite3.connect(SQLITE_FILE)
