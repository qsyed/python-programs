import sqlite3
conn = sqlite3.connect("sqlite3-python/users.db")

c= conn.cursor()


conn.commit()
conn.close()