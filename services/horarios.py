import sqlite3


class Horarios:
    def initTable():
        conn = sqlite3.connect("base.db")
        cursor = conn.cursor()

        cursor.execute(
            """CREATE TABLE IF NOT EXISTS horarios (
                valor TEXT,
                env_name TEXT,
                FOREIGN KEY (env_name) REFERENCES environments(name)
                PRIMARY KEY (valor,env_name))"""
        )

    def createHorarios(list, env):
        conn = sqlite3.connect("base.db")
        cursor = conn.cursor()

        for i in list:
            cursor.execute(
                """
                INSERT INTO horarios (valor,env_name) VALUES (?,?) 
            """,
                (i, env),
            )

        conn.commit()

    def getHorarios(env):
        conn = sqlite3.connect("base.db")
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT valor FROM horarios WHERE env_name = ? ORDER BY env_name 
        """,
            (env,),
        )
        return cursor.fetchall()

    def clearEnv(env):
        conn = sqlite3.connect("base.db")
        cursor = conn.cursor()

        cursor.execute(
            """
            DELETE FROM horarios WHERE env_name = ? 
        """,
            (env,),
        )

        conn.commit()
