#Pineapple -- Kyle Tau, Angela Tom, Mohammed Uddin, Kaitlin Wan
#SoftDev1 pd6
#P00 -- Da Art of Storytellin'(Part X)
#2018-10-15

import sqlite3

DB_FILE = "database.db"
db = sqlite3.connect(DB_FILE)
c = db.cursor()

def addBlog(username, title):
    blogs = c.execute("SELECT blog_id FROM blogs").fetchall()
    blogid = len(blogs)
    params = (username, title, blogid)
    command = "INSERT INTO blogs VALUES(?,?,?)"
    c.execute(command, params)


def delBlog(id):
    command = "DELETE FROM blogs WHERE blog_id == ?"
    params = (id)
    c.execute(command, (id,))

addBlog("AT", "Blog")
addBlog("Bob", "Badalog")
delBlog(0)

db.commit()
db.close()
