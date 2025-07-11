import sqlite3
from SingeletonMeta import SingeletonMeta


class Database(metaclass=SingeletonMeta):
    def __init__(self, db_name="app.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def execute(self, query, params=None):
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        self.connection.commit()

    def fetchall(self):
        return self.cursor.fetchall()

    def close(self):
        return self.connection.close()
