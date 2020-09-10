import sqlite3
conn = sqlite3.connect("sqlite3-python/my_friends.db")

c = conn.cursor()
c.execute("SELECT * FROM friends")

for result in c:
    print(result)

conn.commit()
conn.close()