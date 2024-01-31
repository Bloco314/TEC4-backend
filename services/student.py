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