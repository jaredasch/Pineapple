#Pineapple -- Kyle Tau, Angela Tom, Mohammed Uddin, Kaitlin Wan
#SoftDev1 pd6
#P00 -- Da Art of Storytellin'(Part X)
#2018-10-15

import sqlite3
DB_FILE = "database.db"

def addEntry(blog_id, text):
    db = sqlite3.connect(DB_FILE, check_same_thread=False)
    c = db.cursor()
    maxID = c.execute("SELECT MAX(entry_id) FROM bentries").fetchone()
    entries = c.execute("SELECT entry_id FROM bentries").fetchall()
    if len(entries) == 0:
        entry_id = 0
    else:
        entry_id = maxID[0] + 1
    params = (blog_id, entry_id, text)
    command = "INSERT INTO bentries VALUES(?,?,?)"
    c.execute(command, params)   
    db.commit()
    db.close()

def removeEntry(entry_id):
    db = sqlite3.connect(DB_FILE, check_same_thread=False)
    c = db.cursor()
    command = "DELETE FROM bentries WHERE entry_id == ?"
    c.execute(command, (entry_id,))
    db.commit()
    db.close()

def viewEntry(entry_id):
    db = sqlite3.connect(DB_FILE, check_same_thread=False)
    c = db.cursor()
    command = "SELECT blog_entry FROM bentries WHERE entry_id == ?"
    text = c.execute(command, (entry_id,)).fetchone()
    db.commit()
    db.close()
    return text[0]

def editEntry(entry_id, text):
    db = sqlite3.connect(DB_FILE, check_same_thread=False)
    c = db.cursor()
    command = "UPDATE bentries SET blog_entry = ? WHERE entry_id == ?"
    params = (text, entry_id)
    c.execute(command, params)
    db.commit()
    db.close()

def getBlog(entry_id):
    db = sqlite3.connect(DB_FILE, check_same_thread=False)
    c = db.cursor()
    command = "SELECT blog_id FROM bentries WHERE entry_id == ?"
    blog = c.execute(command, (entry_id,)).fetchone()
    db.commit()
    db.close()
    return blog[0]

