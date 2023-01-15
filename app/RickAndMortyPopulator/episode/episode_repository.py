import random
import string
import sqlite3 as sql
from config import Config


class EpisodeRepository:
    def __init__(self):
        pass

    @staticmethod
    def get_db():
        conn = sql.connect(Config.DATABASE_URI)
        return conn

    @staticmethod
    def create_tables():
        # Las tablas son una lista de sentencias
        tables = [
            """CREATE TABLE IF NOT EXISTS episodes(
            uuid TEXT PRIMARY KEY NOT NULL,
            name TEXT NOT NULL)""",
        ]
        db = EpisodeRepository.get_db()
        cursor = db.cursor()
        for table in tables:
            cursor.execute(table)

    @staticmethod
    def get_uuid(num_dig):
        uuid = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(num_dig))
        return uuid

    @staticmethod
    def insert_episode(uuid, name):
        db = EpisodeRepository.get_db()
        cursor = db.cursor()
        statement = "INSERT INTO episodes (uuid, name) VALUES (?,?)"
        cursor.execute(statement, [uuid, name])
        db.commit()

