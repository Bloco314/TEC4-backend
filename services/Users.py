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
                    name TEXT
            )"""
        )

    @staticmethod
    def create_user(email, senha, name):
        conn = sqlite3.connect("base.db")
        cursor = conn.cursor()

        cursor.execute(
            """INSERT INTO users (email, senha, name) VALUES (?, ?, ?)""",
            (email, senha, name),
        )
        conn.commit()

    @staticmethod
    def get_user(email):
        conn = sqlite3.connect("base.db")
        cursor = conn.cursor()

        cursor.execute("""SELECT * FROM users WHERE email=?""", (email,))
        return cursor.fetchone()
    
    @staticmethod
    def listall_user():
        conn = sqlite3.connect("base.db")
        cursor = conn.cursor()

        cursor.execute("""SELECT * FROM users""")
        return cursor.fetchall()
    

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
