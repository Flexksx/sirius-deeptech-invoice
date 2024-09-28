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
        checkTablesPath = os.path.join(
            os.path.dirname(__file__), 'sql/check_tables.sql')
        restartTablesPath = os.path.join(
            os.path.dirname(__file__), 'sql/restart_database.sql')
               
        
        self.queries = {
            "init_tables": open(initTablesPath).read(),
            "drop_tables": open(dropTablesPath).read(),
            "check_tables": open(checkTablesPath).read(),
            "restart_database": open(restartTablesPath).read()
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


    def check_tables(self, conn=None, cursor=None):
        if conn is None:
            conn = self.conn
        if cursor is None:
            cursor = self.cursor

        cursor.execute(self.queries['check_tables'])
        tables = cursor.fetchall()

        conn.commit()

        if tables:
            table_names = [table[0] for table in tables]  # Extract table names from the tuples
            self.log(f"Existing tables: {', '.join(table_names)}")
        else:
            self.log("No existing tables found")


    def drop_tables(self, conn=None, cursor=None):
        if conn is None:
            conn = self.conn
        if cursor is None:
            cursor = self.cursor
        cursor.executescript(self.queries["drop_tables"])
        conn.commit()
        self.log('Tables dropped successfully')


    def restart_database(self, conn=None, cursor=None):
        if conn is None:
            conn = self.conn
        if cursor is None:
            cursor = self.cursor
# Fetching all the tables
        self.log("Fetching the tables for deletion..")
        cursor.execute(self.queries["restart_database"])        
        tables = cursor.fetchall()
# Drop tables
        if tables:
            self.drop_tables()
            self.log("All tables dropped successfully.")
        else:
            self.log("No existing tables found to drop.")
# Reinitialozation
        self.log("Reinitializing tables...")
        self.init_tables()