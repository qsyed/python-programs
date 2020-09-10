import sqlite3
conn = sqlite3.connect("sqlite3-python/users.db")



# query = "CREATE TABLE user (username TEXT, password TEXT) "
# c.execute(query)

# list_users = [
#     ("Roald","password123"),
#     ("Rosa", "abc123"),
# 	("Henry", "12345")
# ]

# c.executemany("INSERT INTO user VALUES (?,?)", list_users)
user_name = input("please enter username ")
password = input("please enter password ")
query = f"SELECT * FROM user WHERE username='{user_name}' and password='{password}'"

c= conn.cursor()

c.execute(query)

result = c.fetchone()
if(result):
    print("welcome back")
else:
    print("user does not exist")


conn.commit()
conn.close()