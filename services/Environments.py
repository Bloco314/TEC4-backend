import sqlite3


class Environment:
    @staticmethod
    def initTable():
        conn = sqlite3.connect("base.db")
        cursor = conn.cursor()

        cursor.execute(
            """CREATE TABLE IF NOT EXISTS environments (
                    name TEXT PRIMARY KEY,
                    description TEXT NULL
            )"""
        )

    @staticmethod
    def create_environment(name, description=None):
        conn = sqlite3.connect("base.db")
        cursor = conn.cursor()

        cursor.execute(
            """INSERT INTO environments (name, description) VALUES (?, ?)""",
            (name, description),
        )
        conn.commit()

    @staticmethod
    def get_environment(name):
        conn = sqlite3.connect("base.db")
        cursor = conn.cursor()

        cursor.execute("""SELECT * FROM environments WHERE name=? ORDER BY name""", (name,))
        return cursor.fetchone()
    
    @staticmethod
    def nameall_environment():
        conn = sqlite3.connect("base.db")
        cursor = conn.cursor()

        cursor.execute("""SELECT name FROM environments""")
        return cursor.fetchall()

    @staticmethod
    def update_environment(name, description):
        conn = sqlite3.connect("base.db")
        cursor = conn.cursor()

        cursor.execute(
            """UPDATE environments SET description=? WHERE name=?""",
            (description, name),
        )
        conn.commit()

    @staticmethod
    def delete_environment(name):
        conn = sqlite3.connect("base.db")
        cursor = conn.cursor()

        cursor.execute("""DELETE FROM environments WHERE name=?""", (name,))
        conn.commit()
