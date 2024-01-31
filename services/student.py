import sqlite3


class Student:
    @staticmethod
    def createStudent():
        conn = sqlite3.connect("base.db")
        cursor = conn.cursor()

        cursor.execute(
            """CREATE TABLE IF NOT EXISTS student (
                    matricula TEXT PRIMARY KEY,
                    name TEXT
            )"""
        )

    @staticmethod
    def create_student(matricula, name):
        conn = sqlite3.connect("base.db")
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO TABLE (matricula,name) student values(?,?)
        """,
            (matricula, name),
        )

    @staticmethod
    def update_student(matricula, name):
        conn = sqlite3.connect("base.db")
        cursor = conn.cursor()

        cursor.execute(
            """UPDATE users SET name=? WHERE matricula=?""", (name, matricula)
        )
        conn.commit()

    @staticmethod
    def delete_student(matricula):
        conn = sqlite3.connect("base.db")
        cursor = conn.cursor()

        cursor.execute("""DELETE FROM users WHERE email=?""", (matricula,))
        conn.commit()
