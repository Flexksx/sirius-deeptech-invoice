import sqlite3
from datetime import datetime
import os


class Database:
    def __init__(self) -> None:
        # '../../database/database.db'
        self.database_path = os.path.join(
            os.path.dirname(__file__), '../../database/database.db')

        self.conn = sqlite3.connect(self.database_path)
        self.cursor = self.conn.cursor()
        self.conn.execute('PRAGMA foreign_keys = ON;')
        self.log('Database connected successfully')

    def log(self, message):
        header = "[DATABASE]"
        currentTime = datetime.now()
        print(f'{header} {currentTime} {message}')

    def __del__(self) -> None:
        self.conn.close()

    def init_tables(self, conn, cursor):
        if conn is None:
            conn = self.conn
        if cursor is None:
            cursor = self.cursor
        query = open('./sql/create_tables.sql', 'r').read()
        cursor.executescript(query)
        conn.commit()
        self.log('Tables created successfully')

    def drop_tables(self, conn, cursor):
        if conn is None:
            conn = self.conn
        if cursor is None:
            cursor = self.cursor
        query = open('./sql/drop_tables.sql', 'r').read()
        cursor.executescript(query)
        conn.commit()
        self.log('Tables dropped successfully')
