import sqlite3


class DBContracts:
    def __init__(self, conn) -> None:
        self.conn = conn
        self.queries = {
            "get": open('./sql/get.sql').read(),
            "create": open('./sql/create.sql').read(),
        }

    def get(self, id: str):
        cursor = self.conn.cursor()
        cursor.execute(self.queries["get"], (id,))
        contract = cursor.fetchone()
        cursor.close()
        return contract
