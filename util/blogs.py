#Pineapple -- Kyle Tau, Angela Tom, Mohammed Uddin, Kaitlin Wan
#SoftDev1 pd6
#P00 -- Da Art of Storytellin'(Part X)
#2018-10-15

import sqlite3

DB_FILE = "database.db"
db = sqlite3.connect(DB_FILE, check_same_thread=False)
c = db.cursor()

def addBlog(username, title, url):
    '''
    Add a new blog into the database with the params: username, title, and url.
    The blog id is unique and a number.
    '''
    maxID = c.execute("SELECT MAX(blog_id) FROM blogs").fetchone()
    blogs = c.execute("SELECT blog_id FROM blogs").fetchall()
    if len(blogs) == 0:
        blogid = 0
    else:
        blogid = maxID[0] + 1
    params = (username, title, blogid, url)
    command = "INSERT INTO blogs VALUES(?,?,?,?)"
    c.execute(command, params)

def delBlog(id):
    '''
    Delete a blog from the database with the blog id as param.
    '''
    command = "DELETE FROM blogs WHERE blog_id == ?"
    params = (id)
    c.execute(command, (id,))

def searchBlog(title):
    '''
    A list of urls would be returned based on the title.
    '''
    search_results = []
    command = "SELECT blog_name FROM blogs"
    titles = c.execute(command).fetchall()
    command = "SELECT blog_url FROM blogs"
    urls = c.execute(command).fetchall()
    for x in range(len(titles)):
        if titles[x][0] == title:
            search_results += urls[x]
    return search_results

def getEntries(id):
    '''
    Returns a list of lists with each list containing one blog id that matches given id
    '''
    command = "SELECT entry_id FROM bentries WHERE blog_id == ?"
    entries = c.execute(command, (id,)).fetchall()
    return entries

def getAuthor(id):
    '''
    Returns author of blog associated with given blog id
    '''
    command = "SELECT user FROM blogs WHERE blog_id == ?"
    author = c.execute(command, (id,)).fetchone()
    return author[0]

def getBlog(id):
    '''
    Returns name of blog associated with given blog id
    '''
    command = "SELECT blog_name FROM blogs WHERE blog_id == ?"
    name = c.execute(command, (id,)).fetchone()
    return name[0]


addBlog("AT", "Blog", "blog.html")
addBlog("Bob", "Badalog", "bob.html")
addBlog("Bobsad", "Bsdasadalog", "bobsad.html")
delBlog(1)
addBlog("Boosda", "dfwaoef", "boo.html")
addBlog("AT", "Hunger Games", "hungergames1.html")
addBlog("Stuff", "Hunger Games", "hungergames2.html")
print(searchBlog("Hunger Games"))

db.commit()
