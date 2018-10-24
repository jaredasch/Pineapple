#Pineapple -- Kyle Tau, Angela Tom, Mohammed Uddin, Kaitlin Wan
#SoftDev1 pd6
#P00 -- Da Art of Storytellin'(Part X)
#2018-10-15

import sqlite3


#params = ("Kaitlin", "123")
#command = "INSERT INTO accts VALUES(?,?)"
#c.execute(command, params)

def register(username,password):
    DB_FILE = "../database.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "SELECT user FROM accts"
    users = c.execute(command).fetchall()
    print(users)
    if username in users:
        db.commit()
        db.close()
        return 0
    else:
        params = (username, password)
        command = "INSERT INTO accts VALUES(?,?)"
        c.execute(command, params)
        db.commit()
        db.close()
    return 1

def login(username, password):
    DB_FILE = "../database.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "SELECT user, password FROM accts"
    accts = c.execute(command).fetchall()
    login = {}
    for acct in accts:
        login[acct[0]] = acct[1]
    print(login)
    if username in login.keys():
        if password == login[username]:
            db.commit()
            db.close()
            return 1
        else:
            db.commit()
            db.close()
            return 0
    db.commit()
    db.close()
    return 0
#print("printing all past users:")
#users = c.execute("SELECT user FROM accts").fetchall()
#print(users)
