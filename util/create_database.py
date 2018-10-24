#Pineapple -- Kyle Tau, Angela Tom, Mohammed Uddin, Kaitlin Wan
#SoftDev1 pd6
#P00 -- Da Art of Storytellin'(Part X)
#2018-10-15

import sqlite3

DB_FILE = "database.db"
db = sqlite3.connect(DB_FILE, check_same_thread=False)
c = db.cursor()

'''
Creating the database tables: accts, blogs, and bentries.
'''

command = "CREATE TABLE accts(user TEXT PRIMARY KEY, password TEXT);"
c.execute(command)

command = "CREATE TABLE blogs(user TEXT, blog_name TEXT, blog_id INTEGER PRIMARY KEY, blog_url TEXT);"
c.execute(command)

command = "CREATE TABLE bentries(blog_id INTEGER, entry_id INTEGER PRIMARY KEY, blog_entry TEXT);"
c.execute(command)

db.commit()
