import sqlite3
import os
import datetime


class DBContracts:
    def __init__(self, conn) -> None:
        self.conn = conn
        self.log('DBContracts initialized')
        getPath = os.path.join(os.path.dirname(__file__), 'sql/get.sql')
        insertPath = os.path.join(os.path.dirname(__file__), 'sql/insert.sql')
        self.queries = {
            "get": open(getPath).read(),
        }

    def log(self, message):
        header = "[DATABASE][CONTRACTS]"
        currentTime = datetime.datetime.now()
        print(f'{header} {currentTime} {message}')

    def get(self, id: str):
        cursor = self.conn.cursor()
        cursor.execute(self.queries["get"], (id,))
        contract = cursor.fetchone()
        if contract is None:
            self.log(f'Contract not found: {id}')
            return None
        self.log(f'Contract fetched: {contract}')
        return contract
