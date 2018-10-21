#Pineapple -- Kyle Tau, Angela Tom, Mohammed Uddin, Kaitlin Wan
#SoftDev1 pd6
#P00 -- Da Art of Storytellin'(Part X)
#2018-10-15

import sqlite3
DB_FILE = "database.db"
db = sqlite3.connect(DB_FILE)
c = db.cursor()


def addEntry( text):
    pass


db.commit()
db.close()
