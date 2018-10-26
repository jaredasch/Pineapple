#Pineapple -- Kyle Tau, Angela Tom, Mohammed Uddin, Kaitlin Wan
#SoftDev1 pd6
#P00 -- Da Art of Storytellin'(Part X)
#2018-10-15

import sqlite3

DB_FILE = "database.db"
db = sqlite3.connect(DB_FILE, check_same_thread=False)
c = db.cursor()

def getBlogsList(gettingUser):
    '''
    Returns a list of blogs name assosiated with user
    '''
    command = "SELECT blog_name FROM blogs WHERE id == ?"
    name = c.execute(command, (gettingUser,)).fetchall()
    return name

db.commit()
