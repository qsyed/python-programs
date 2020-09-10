import sqlite3
conn = sqlite3.connect("sqlite3-python/users.db")

c= conn.cursor()
query = "CREATE TABLE user (username TEXT, password TEXT) "

c.execute(query)
conn.commit()
conn.close()