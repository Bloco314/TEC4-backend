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
            (email, senha, name)
        )
        conn.commit()

    @staticmethod
    def get_user(email):
        conn = sqlite3.connect("base.db")
        cursor = conn.cursor()

        cursor.execute(
            """SELECT * FROM users WHERE email=?""",
            (email,)
        )
        return cursor.fetchone()

    @staticmethod
    def update_user(email, senha, name):
        conn = sqlite3.connect("base.db")
        cursor = conn.cursor()

        cursor.execute(
            """UPDATE users SET senha=?, name=? WHERE email=?""",
            (senha, name, email)
        )
        conn.commit()

    @staticmethod
    def delete_user(email):
        conn = sqlite3.connect("base.db")
        cursor = conn.cursor()

        cursor.execute(
            """DELETE FROM users WHERE email=?""",
            (email,)
        )
        conn.commit()


class Environment:
    @staticmethod
    def createEnvironment():
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
            (name, description)
        )
        conn.commit()

    @staticmethod
    def get_environment(name):
        conn = sqlite3.connect("base.db")
        cursor = conn.cursor()

        cursor.execute(
            """SELECT * FROM environments WHERE name=?""",
            (name,)
        )
        return cursor.fetchone()

    @staticmethod
    def update_environment(name, description):
        conn = sqlite3.connect("base.db")
        cursor = conn.cursor()

        cursor.execute(
            """UPDATE environments SET description=? WHERE name=?""",
            (description, name)
        )
        conn.commit()

    @staticmethod
    def delete_environment(name):
        conn = sqlite3.connect("base.db")
        cursor = conn.cursor()

        cursor.execute(
            """DELETE FROM environments WHERE name=?""",
            (name,)
        )
        conn.commit()



class Equipment:
    @staticmethod
    def createEquipment():
        conn = sqlite3.connect("base.db")
        cursor = conn.cursor()

        cursor.execute(
            """CREATE TABLE IF NOT EXISTS equipments (
                    name TEXT PRIMARY KEY,
                    description TEXT NULL,
                    tag TEXT,
                    env_name TEXT,
                    FOREIGN KEY (env_name) REFERENCES environments(name)
            )"""
        )

    @staticmethod
    def create_equipment(name, description=None, tag=None, env_name=None):
        conn = sqlite3.connect("base.db")
        cursor = conn.cursor()

        cursor.execute(
            """INSERT INTO equipments (name, description, tag, env_name) VALUES (?, ?, ?, ?)""",
            (name, description, tag, env_name)
        )
        conn.commit()

    @staticmethod
    def get_equipment(name):
        conn = sqlite3.connect("base.db")
        cursor = conn.cursor()

        cursor.execute(
            """SELECT * FROM equipments WHERE name=?""",
            (name,)
        )
        return cursor.fetchone()

    @staticmethod
    def update_equipment(name, description, tag, env_name):
        conn = sqlite3.connect("base.db")
        cursor = conn.cursor()

        cursor.execute(
            """UPDATE equipments SET description=?, tag=?, env_name=? WHERE name=?""",
            (description, tag, env_name, name)
        )
        conn.commit()

    @staticmethod
    def delete_equipment(name):
        conn = sqlite3.connect("base.db")
        cursor = conn.cursor()

        cursor.execute(
            """DELETE FROM equipments WHERE name=?""",
            (name,)
        )
        conn.commit()


def createDB():
    User.createUser()
    Environment.createEnvironment()
    Equipment.createEquipment()

createDB()
