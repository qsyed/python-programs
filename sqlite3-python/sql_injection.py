import sqlite3
conn = sqlite3.connect("sqlite3-python/users.db")

c= conn.cursor()

# query = "CREATE TABLE user (username TEXT, password TEXT) "
# c.execute(query)

list_users = [
    ("Roald","password123"),
    ("Rosa", "abc123"),
	("Henry", "12345")
]

c.executemany("INSERT INTO user VALUES (?,?)", list_users)


conn.commit()
conn.close()