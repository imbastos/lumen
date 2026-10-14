from data.database.sqlite.connection import get_connection
from models.riasec_result import RiasecResult


def create(riasec_result: RiasecResult):
    conn = get_connection()
    try:
        cursor = conn.cursor()

        query = "INSERT INTO riasec_results (user_id, r, i, a, s, e, c) VALUES (?, ?, ?, ?, ?, ?, ?);"

        cursor.execute(
            query,
            (
                riasec_result.user_id,
                riasec_result.r,
                riasec_result.i,
                riasec_result.a,
                riasec_result.s,
                riasec_result.e,
                riasec_result.c,
            ),
        )
        conn.commit()
    finally:
        if conn is not None:
            conn.close()


def get_latest_by_user_id(user_id: int):
    conn = get_connection()
    try:
        cursor = conn.cursor()

        query = "SELECT id, r, i, a, s, e, c FROM riasec_results WHERE user_id = ? ORDER BY id DESC LIMIT 1;"

        row = cursor.execute(query, (user_id,)).fetchone()

        if row is None:
            return None

        return RiasecResult(
            id=row[0],
            r=row[1],
            i=row[2],
            a=row[3],
            s=row[4],
            e=row[5],
            c=row[6],
            user_id=user_id
        )
    finally:
        conn.close()


def get_all_by_user_id(user_id: int):
    conn = get_connection()

    try:
        cursor = conn.cursor()

        query = "SELECT id, user_id, r, i, a, s, e, c, created_at FROM riasec_results WHERE user_id = ? ORDER BY id DESC;"

        cursor.execute(query, (user_id,))
        rows = cursor.fetchall()

        return [
            RiasecResult(
                id=row[0],
                r=row[1],
                i=row[2],
                a=row[3],
                s=row[4],
                e=row[5],
                c=row[6],
            )
            for row in rows
        ]
    finally:
        conn.close()
