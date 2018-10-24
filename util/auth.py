#Pineapple -- Kyle Tau, Angela Tom, Mohammed Uddin, Kaitlin Wan
#SoftDev1 pd6
#P00 -- Da Art of Storytellin'(Part X)
#2018-10-15

import sqlite3

DB_FILE = "database.db"
db = sqlite3.connect(DB_FILE, check_same_thread=False)
c = db.cursor()

def register(username, password):
    '''
    Adds the user and password into the database if it does not already exist
    Returns 0 if username already exists
    Returns 1 if successful
    '''
    command = "SELECT user FROM accts"
    users = c.execute(command).fetchall()
    if username in users:
        return 0
    else:
        try:
            params = (username, password)
            command = "INSERT INTO accts VALUES(?,?)"
            c.execute(command, params)
        except:
            #If it is already registered
            return 0
    return 1

def login(username, password):
    '''
    Returns 0 if login failed
    Returns 1 if login is successful
    '''
    command = "SELECT user, password FROM accts"
    accts = c.execute(command).fetchall()
    login = {}
    for acct in accts:
        login[acct[0]] = acct[1]
    if username in login.keys():
        if password == login[username]:
            return 1
        else:
            return 0
    return 0

db.commit()
