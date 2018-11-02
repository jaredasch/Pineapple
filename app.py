#Pineapple -- Kyle Tau, Angela Tom, Mohammed Uddin, Kaitlin Wan
#SoftDev1 pd6
#P00 -- Da Art of Storytellin'(Part X)
#2018-10-15

from flask import Flask,request,render_template,session,url_for,redirect,flash
import os
from util import auth, blogs, entries
import sqlite3
app = Flask(__name__)
# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = "supersecretkey"

@app.route("/")
def home():
    #If there is a session: take user to dashbaord
    if 'username' in session:
      return redirect("/homepage")
    return render_template("landing.html")


@app.route("/login")
def login():
    que = request.args
    login = auth.login(request.args['user'],request.args['pass'])
    if (login == 0):
        return render_template("landing.html", loginStatus = "Invalid Login.")
    session['username'] = request.args['user']
    return redirect('/homepage')

@app.route("/register")
def reg():
    que = request.args
    if (auth.register(que['user'],que['pass']) == 0):
        return render_template("landing.html", loginStatus = "Nope. Try again. Already registered")
    else:
        return render_template("landing.html", loginStatus = "Sucessfully Registered.")

@app.route("/homepage")
def homepage():
    que = request.args
    return render_template("dash.html", LoggedUser = session['username'], blogs = blogs.getBlogsList(session['username']))
    #Getting Which Blog as a number

@app.route("/newBlog")
def newBlog():
    que = request.args
    blogs.addBlog(session['username'], que['blogName'])
    return render_template("dash.html", LoggedUser = session['username'], blogs =  blogs.getBlogsList(session['username']))

@app.route("/display_blog")
def display_blog():
    que = request.args
    blog_id = int(que['blog_id'])
    name = blogs.getBlog(blog_id)
    user = blogs.getAuthor(blog_id)
    entries = blogs.getEntries(blog_id)
    if user == session['username']:
        return render_template("blog.html", blog_id = blog_id, blog_title = name, author = user, entry_list = entries)
    else:
        return render_template("blogview.html", blog_id = blog_id, blog_title = name, author = user, entry_list = entries)
@app.route("/remove_blog")
def remove_blog():
    que = request.args
    blog_id = int(que['blog_id'])
    blogs.delBlog(blog_id)
    return render_template("dash.html", LoggedUser = session['username'], blogs =  blogs.getBlogsList(session['username']))

@app.route("/search_blog")
def search_blog():
    que = request.args
    searches = blogs.searchBlog(que["blog_title"])
    bloglist = blogs.getBlogsList(session['username'])
    return render_template("dash.html", LoggedUser = session['username'], blogs =  bloglist, searchlist = searches)

@app.route("/new_entry")
def add_entry():
    que = request.args
    blog_id = int(que['blog_id'])
    name = blogs.getBlog(blog_id)
    user = blogs.getAuthor(blog_id)    
    entries.addEntry(blog_id,"")
    entries_list = blogs.getEntries(blog_id)
    return render_template("blog.html", blog_id = blog_id, blog_title = name, author = user, entry_list = entries_list)

@app.route("/remove_entry")
def remove_entry():
    que = request.args
    entry_id = int(que['entry_id'])
    blog_id = int(que['blog_id'])
    name = blogs.getBlog(blog_id)
    user = blogs.getAuthor(blog_id)
    entries.removeEntry(entry_id)
    entries_list = blogs.getEntries(blog_id)
    return render_template("blog.html", blog_id = blog_id, blog_title = name, author = user, entry_list = entries_list)

@app.route("/display_entry")
def display_entry():
    que = request.args
    entry_id = int(que['entry_id'])
    blog_id = int(que['blog_id'])
    name = blogs.getBlog(blog_id)
    user = blogs.getAuthor(blog_id)
    text = entries.viewEntry(entry_id)
    if user == session['username']:
        return render_template("entry.html", entry_id = entry_id, blog_id = blog_id, entry_text=text, blog_title = name, author = user)
    else:
        return render_template("entryview.html", entry_id = entry_id, blog_id = blog_id, entry_text=text, blog_title = name, author = user)
@app.route("/edit_mode")
def edit_mode():
    que = request.args
    entry_id = int(que['entry_id'])
    blog_id = int(que['blog_id'])
    name = blogs.getBlog(blog_id)
    user = blogs.getAuthor(blog_id)  
    text = entries.viewEntry(entry_id)
    return render_template("edit.html", blog_id = blog_id, entry_id = entry_id, entry_text=text, blog_title = name, author = user)

@app.route("/edit_entry")
def edit_entry():
    que = request.args
    entry_id = int(que['entry_id'])
    blog_id = int(que['blog_id'])
    name = blogs.getBlog(blog_id)
    user = blogs.getAuthor(blog_id)
    text = que['content']
    entries.editEntry(entry_id,text)
    return render_template("entry.html", blog_id = blog_id, entry_id = entry_id, entry_text=text, blog_title = name, author = user)

@app.route("/logout")
def logout():
    session.pop('username', None)
    return render_template("landing.html", loginStatus = "Logged Out.")

if __name__ == '__main__':
    app.debug = True
    app.run()
