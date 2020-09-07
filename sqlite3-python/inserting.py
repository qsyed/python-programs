import sqlite3

""" 
to check if connection is working do: sqlite3 my_friends.db 

check: .tables
check: .schema + table_name

"""


conn = sqlite3.connect("sqlite3-python/my_freinds.db")

# create cursor obj  and execute sql commands

c = conn.cursor()
# c.execute("CREATE TABLE friends (first_name TEXT, last_name TEXT, closeness INTEGER);")

# insert = '''INSERT INTO friends 
#             VALUES ('Marry', 'Lewis', 7)'''

form_first = "Marry-Todd"
query = f"INSERT INTO friends (first_name) VALUES (?)"
c.execute(query, (form_first,))

conn.commit()

conn.close()



