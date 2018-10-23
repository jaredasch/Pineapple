#Pineapple -- Kyle Tau, Angela Tom, Mohammed Uddin, Kaitlin Wan
#SoftDev1 pd6
#P00 -- Da Art of Storytellin'(Part X)
#2018-10-15

import sqlite3

DB_FILE = "database.db"
db = sqlite3.connect(DB_FILE)
c = db.cursor()

def addBlog(username, title):
    maxID = c.execute("SELECT MAX(blog_id) FROM blogs").fetchone()
    blogs = c.execute("SELECT blog_id FROM blogs").fetchall()
    if len(blogs) == 0:
        blogid = 0
    else:
        blogid = maxID[0] + 1
    params = (username, title, blogid)
    command = "INSERT INTO blogs VALUES(?,?,?)"
    c.execute(command, params)


def delBlog(id):
    command = "DELETE FROM blogs WHERE blog_id == ?"
    params = (id)
    c.execute(command, (id,))

def searchBlog(title):
    command = "SELECT ?"

addBlog("AT", "Blog")
addBlog("Bob", "Badalog")
addBlog("Bobsad", "Bsdasadalog")
delBlog(1)
addBlog("Boosda", "dfwaoef")

db.commit()
db.close()
