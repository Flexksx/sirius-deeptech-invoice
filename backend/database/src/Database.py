import sqlite3
from datetime import datetime
from contracts.DBContracts import DBContracts
import os


class Database:
    def __init__(self) -> None:
        # '../../database/database.db'
        self.database_path = os.path.join(
            os.path.dirname(__file__), '../../database/database.db')

        self.conn = sqlite3.connect(self.database_path)
        self.log('Database connected successfully')

        self.cursor = self.conn.cursor()
        self.conn.execute('PRAGMA foreign_keys = ON;')
        self.contract = DBContracts(self.conn)

        initTablesPath = os.path.join(
            os.path.dirname(__file__), 'sql/create_tables.sql')
        dropTablesPath = os.path.join(
            os.path.dirname(__file__), 'sql/drop_tables.sql')

        self.queries = {
            "init_tables": open(initTablesPath).read(),
            "drop_tables": open(dropTablesPath).read()
        }

    def log(self, message):
        currentTime = datetime.now()
        header = "[DATABASE]"
        print(f'{header} {currentTime} {message}')

    def __del__(self) -> None:
        self.conn.close()

    def init_tables(self, conn=None, cursor=None):
        if conn is None:
            conn = self.conn
        if cursor is None:
            cursor = self.cursor
        cursor.executescript(self.queries["init_tables"])
        conn.commit()
        self.log('Tables created successfully')

    def drop_tables(self, conn=None, cursor=None):
        if conn is None:
            conn = self.conn
        if cursor is None:
            cursor = self.cursor
        cursor.executescript(self.queries["drop_tables"])
        conn.commit()
        self.log('Tables dropped successfully')
