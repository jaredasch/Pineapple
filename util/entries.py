#Pineapple -- Kyle Tau, Angela Tom, Mohammed Uddin, Kaitlin Wan
#SoftDev1 pd6
#P00 -- Da Art of Storytellin'(Part X)
#2018-10-15

import sqlite3
DB_FILE = "database.db"
db = sqlite3.connect(DB_FILE)
c = db.cursor()


def addEntry(blog_id, text):
    params = (blog_id, text)
    command = "INSERT INTO bentries VALUES(?,?,?)"
    c.execute(command, params)

def removeEntry(entry_id):
    command = "DELETE FROM bentries WHERE entry_id == ?"
    c.execute(command, (entry_id))

def editEntry(entry_id):
    command = ""

db.commit()
db.close()


