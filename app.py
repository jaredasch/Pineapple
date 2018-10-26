#Pineapple -- Kyle Tau, Angela Tom, Mohammed Uddin, Kaitlin Wan
#SoftDev1 pd6
#P00 -- Da Art of Storytellin'(Part X)
#2018-10-15

from flask import Flask,request,render_template,session,url_for,redirect,flash
import os
from util import auth, blogs
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
    id = int(que['id'])
    name = blogs.getBlog(id)
    user = blogs.getAuthor(id)
    entries = blogs.getEntries(id)
    return render_template("blog.html", blog_title = name, author = user, entry_list = entries)

@app.route("/display_entry")
def display_entry():
    que = request.args
    id = int(que['entry_id'])
    text = entries.viewEntry(id)
    return render_template("entry.html", entry_text=text)



@app.route("/logout")
def logout():
    session.pop('username', None)
    return render_template("landing.html", loginStatus = "Logged Out.")

if __name__ == '__main__':
    app.debug = True
    app.run()
