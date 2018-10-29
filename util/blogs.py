#Pineapple -- Kyle Tau, Angela Tom, Mohammed Uddin, Kaitlin Wan
#SoftDev1 pd6
#P00 -- Da Art of Storytellin'(Part X)
#2018-10-15

import sqlite3



def addBlog(username, title):
    ''' 
    Add a new blog into the database with the params: username, title, and url.
    The blog id is unique and a number.
    The url is the the title and the number. Ex: "hungergames1"
    ''' 
    
    DB_FILE = "database.db"
    db = sqlite3.connect(DB_FILE, check_same_thread=False)
    c = db.cursor()
    maxID = c.execute("SELECT MAX(blog_id) FROM blogs").fetchone()
    blogs = c.execute("SELECT blog_id FROM blogs").fetchall()
    if len(blogs) == 0:
        blogid = 0
    else:
        blogid = maxID[0] + 1
#    url = title + blogid
    params = (username, title, blogid)
    command = "INSERT INTO blogs VALUES(?,?,?)"
    c.execute(command, params)
    db.commit()
    db.close()


def delBlog(id):
    '''
    Delete a blog from the database with the blog id as param.
    '''
    
    DB_FILE = "database.db"
    db = sqlite3.connect(DB_FILE, check_same_thread=False)
    c = db.cursor()
    command = "DELETE FROM blogs WHERE blog_id == ?"
    params = (id)
    c.execute(command, (id,))
    db.commit()
    db.close()

def searchBlog(title):
    '''
    A list of urls would be returned based on the title.
    '''
    DB_FILE = "database.db"
    db = sqlite3.connect(DB_FILE, check_same_thread=False)
    c = db.cursor()
    search_results = []
    command = "SELECT blog_name FROM blogs"
    titles = c.execute(command).fetchall()
    command = "SELECT blog_id FROM blogs"
    urls = c.execute(command).fetchall()
    for x in range(len(titles)):
        if titles[x][0] == title:
            search_results += urls[x]
    db.commit()
    db.close()       
    return search_results

def getEntries(id):
    '''
    Returns a list of lists with each list containing one blog id that matches given id
    '''
    DB_FILE = "database.db"
    db = sqlite3.connect(DB_FILE, check_same_thread=False)
    c = db.cursor()
    command = "SELECT entry_id FROM bentries WHERE blog_id == ?"
    entries = c.execute(command, (id,)).fetchall()
    db.commit()
    db.close()
    return entries

def getAuthor(id):
    '''
    Returns author of blog associated with given blog id
    '''
    
    DB_FILE = "database.db"
    db = sqlite3.connect(DB_FILE, check_same_thread=False)
    c = db.cursor()
    command = "SELECT user FROM blogs WHERE blog_id == ?"
    author = c.execute(command, (id,)).fetchone()

    db.commit()
    db.close()
    return author[0]

def getBlog(id):
    '''
    Returns name of blog associated with given blog id
    '''

    DB_FILE = "database.db"
    db = sqlite3.connect(DB_FILE, check_same_thread=False)
    c = db.cursor()
    command = "SELECT blog_name FROM blogs WHERE blog_id == ?"
    name = c.execute(command, (id,)).fetchone()
    db.commit()
    db.close()
    return name[0]

def getBlogsList(gettingUser):
    '''
    Returns a list of blogs name assosiated with user
    '''
    DB_FILE = "database.db"
    db = sqlite3.connect(DB_FILE, check_same_thread=False)
    c = db.cursor()
    command = "SELECT blog_name,blog_id FROM blogs WHERE user == ?"
    name = c.execute(command, (gettingUser,)).fetchall()
    db.commit()
    db.close()
    return name
