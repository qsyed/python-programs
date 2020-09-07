import sqlite3
conn = sqlite3.connect("sqlite3-python/my_freinds.db")


"""

to check if connection is working do: sqlite3 my_friends.db 

check: .tables
check. schema + table_name


the db most already be creat inorder for code to run; first run learning_to_insert.py




"""
# create cursor object
c = conn.cursor()

people = [
	("Roald","Amundsen", 5),
	("Rosa", "Parks", 8),
	("Henry", "Hudson", 7),
	("Neil","Armstrong", 7),
	("Daniel", "Boone", 3)]



# for person in people:
# 	c.execute("INSERT INTO friends VALUES (?,?,?)", person)



# Insert all at once
c.executemany("INSERT INTO friends VALUES (?,?,?)", people)


	

# commit changes
conn.commit()
conn.close()



