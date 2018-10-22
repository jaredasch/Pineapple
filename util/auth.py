#Pineapple -- Kyle Tau, Angela Tom, Mohammed Uddin, Kaitlin Wan
#SoftDev1 pd6
#P00 -- Da Art of Storytellin'(Part X)
#2018-10-15

import sqlite3

DB_FILE = "database.db"
db = sqlite3.connect(DB_FILE)
c = db.cursor()

USER = "123"
PASS = "123"

def register(username, password):
    command = "SELECT user FROM accts"
    users = c.execute(command).fetchall()
    if username in users:
        return 0
    else:
        params = (username, password)
        command = "INSERT INTO accts VALUES(?,?)"
        c.execute(command, params)
    return 1

def login(username, password):
    command = "SELECT user, password FROM accts"
    accts = c.execute(command).fetchall()
    login = {}
    for acct in accts:
        login[acct[0]] = acct[1]
    if user in login.keys():
        if password == login[user]:
            return 1
        else:
            return 0
    return 0

register("Bob", "pass")
register("James", "hello")


##THIS IS JUST FOR KAITLIN FOR EZ TESTING
def checkInfo(user,pswd):
    if(user == USER and pswd == PASS):
        return "Login Successful"
    elif(user != USER):
        return "ERROR: Invalid Username"
    else:
        return "ERROR: Invalid Password"



db.commit()
db.close()
