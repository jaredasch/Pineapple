#Pineapple -- Kyle Tau, Angela Tom, Mohammed Uddin, Kaitlin Wan
#SoftDev1 pd6
#P00 -- Da Art of Storytellin'(Part X)
#2018-10-15

import sqlite3
from random import randint

DB_FILE = "database.db"
db = sqlite3.connect(DB_FILE)
c = db.cursor()


def addEntry(blog_id, text):
    '''

    '''
    id  = genId();
    while id in entry_id:
        id =
    params = (blog_id, text,)
    command = "INSERT INTO bentries VALUES(?,?,?)"
    c.execute(command, params)

def removeEntry(entry_id):
    '''

    '''
    command = "DELETE FROM bentries WHERE entry_id == ?"
    c.execute(command, (entry_id,))

def viewEntry(entry_id):
    '''
    
    '''
    command = "SELECT text"

def editEntry(entry_id):
    '''
    
    '''
    command = ""

def genId():
    '''

    '''
    command = "SELECT entry_id FROM bentries"
    ids = c.execute(command).fetchall()
    id = randint(0,999999999)
#idk above and below this point

def makeGood(id):
    '''

    '''
    bad = False
    for row in ids:
        if id == row[0]:
            bad = True
            break
    if bad:

    return id


db.commit()
db.close()
