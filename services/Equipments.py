import sqlite3


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
            (name, description, tag, env_name),
        )
        conn.commit()

    @staticmethod
    def get_equipment(name):
        conn = sqlite3.connect("base.db")
        cursor = conn.cursor()

        cursor.execute("""SELECT * FROM equipments WHERE name=?""", (name,))
        return cursor.fetchone()

    @staticmethod
    def update_equipment(name, description, tag, env_name):
        conn = sqlite3.connect("base.db")
        cursor = conn.cursor()

        cursor.execute(
            """UPDATE equipments SET description=?, tag=?, env_name=? WHERE name=?""",
            (description, tag, env_name, name),
        )
        conn.commit()

    @staticmethod
    def delete_equipment(name):
        conn = sqlite3.connect("base.db")
        cursor = conn.cursor()

        cursor.execute("""DELETE FROM equipments WHERE name=?""", (name,))
        conn.commit()
