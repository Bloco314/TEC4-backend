import sqlite3


class User:
    @staticmethod
    def createUser():
        conn = sqlite3.connect("base.db")
        cursor = conn.cursor()

        cursor.execute(
            """CREATE TABLE IF NOT EXISTS users (
                    email TEXT PRIMARY KEY,
                    senha TEXT,
                    name TEXT,
                    tipo TEXT
            )"""
        )

    @staticmethod
    def login(email, senha):
        conn = sqlite3.connect("base.db")
        cursor = conn.cursor()

        cursor.execute(
            """SELECT * FROM users WHERE email = ? AND senha = ?""", (email, senha)
        )

        return cursor.fetchone()

    @staticmethod
    def create_user(email, senha, name, tipo):
        conn = sqlite3.connect("base.db")
        cursor = conn.cursor()

        cursor.execute(
            """INSERT INTO users (email, senha, name, tipo) VALUES (?, ?, ?, ?)""",
            (email, senha, name, tipo),
        )
        conn.commit()

    @staticmethod
    def update_user(email, senha, name):
        conn = sqlite3.connect("base.db")
        cursor = conn.cursor()

        cursor.execute(
            """UPDATE users SET senha=?, name=? WHERE email=?""", (senha, name, email)
        )
        conn.commit()

    @staticmethod
    def delete_user(email):
        conn = sqlite3.connect("base.db")
        cursor = conn.cursor()

        cursor.execute("""DELETE FROM users WHERE email=?""", (email,))
        conn.commit()
