import sqlite3
conn = sqlite3.connect("my_friends.db")

c = conn.cursor()


conn.commit()
conn.close()