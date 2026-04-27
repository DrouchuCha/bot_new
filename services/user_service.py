import sqlite3
from pathlib import Path

DB_PATH = Path("bot.db")


def get_connection():
    return sqlite3.connect(DB_PATH)


def init_db():
    with get_connection() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS user_stats (
                user_id INTEGER PRIMARY KEY,
                messages_count INTEGER NOT NULL
            )
            """
        )
        conn.commit()


def register_user_message(user_id: int) -> None:
    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute(
            "SELECT messages_count FROM user_stats WHERE user_id = ?",
            (user_id,),
        )
        row = cursor.fetchone()

        if row is None:
            cursor.execute(
                "INSERT INTO user_stats (user_id, messages_count) VALUES (?, 1)",
                (user_id,),
            )
        else:
            cursor.execute(
                "UPDATE user_stats SET messages_count = messages_count + 1 WHERE user_id = ?",
                (user_id,),
            )

        conn.commit()


def get_user_stats(user_id: int) -> int:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT messages_count FROM user_stats WHERE user_id = ?",
            (user_id,),
        )
        row = cursor.fetchone()
        return row[0] if row else 0