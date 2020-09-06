import sqlite3

""" 
to check if connection is working do: sqlite3 my_friends.db 

check: .tables
check. schema + table_name

"""


conn = sqlite3.connect("sqlite3-python/my_freinds.db")

# create cursor obj  and execute sql commands

c = conn.cursor()
c.execute("CREATE TABLE friends (first_name TEXT, last_name TEXT, closeness INTEGER);")



c.execute()

conn.commit()
# must close connection
conn.close()



