from Database import Database

if __name__ == "__main__":
    db1 = Database()
    db1.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
    db1.execute("INSERT INTO users (name) VALUES (?)", ("Alice",))

    db2 = Database()
    db2.execute("SELECT * FROM users")
    print("Users: ", db2.fetchall())

    print("Same instance:", db1 is db2)

    db1.close()
