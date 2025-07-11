import sqlite3


class Database:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            print("Creating new database connection instance...")
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance._initialized = False
        else:
            print("Reusing Existing instance...")

    def __init__(self, dbname="app.db"):
        if not self._initialized:
            self.connection = sqlite3.connect(dbname)
            self.cursor = self.connection.cursor()
            self._initialized = True


db1 = (
    Database()
)  
"""this will call __new__ method of Database, 
where it checks if its has the shared instance (which is a class based property),
the super(Database, cls).__new__(cls) resolves the dependency then __init__ method is called

"""