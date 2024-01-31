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


def createDB():
    User.createUser()
    Environment.createEnvironment()
    Equipment.createEquipment()

createDB()
