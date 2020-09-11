import sqlite3
conn = sqlite3.connect("sqlite3-python/users.db")

"""
this execrise wa meant to show how sql injection can work if the query strings are not set up properly
first we have to set up a data base and enter in seed data. 

    the data base was created by using 
     query = "CREATE TABLE user (username TEXT, password TEXT) "
    and 

    c.execute(query

    I then created a list of users:
        list_users = [
         ("Roald","password123"),
         ("Rosa", "abc123"),
 	     ("Henry", "12345")
         ]

    the seed data was executed by using:
    c.executemany("INSERT INTO user VALUES (?,?)", list_users)
    



"""


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

""" 
when using f string the query can manipulated using sql:
enter a name of a user as is and to inject in password field type ' or 1=1--


the coorect way to ask a user for input is the following:
 query = f"SELECT * FROM user WHERE username=? and password=?"
 followed by c.execute(query,(user_name, password))

"""