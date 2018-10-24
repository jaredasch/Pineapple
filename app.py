#Pineapple -- Kyle Tau, Angela Tom, Mohammed Uddin, Kaitlin Wan
#SoftDev1 pd6
#P00 -- Da Art of Storytellin'(Part X)
#2018-10-15

from flask import Flask,request,render_template,session,url_for,redirect,flash
import os
from util import auth
import sqlite3

app = Flask(__name__)
# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = "supersecretkey"

@app.route("/")
def home():
    #If there is a session: take user to dashbaord
    if 'user' in session: #ALREADY LOGGED IN NEVER LOGGED OUT
        print("user in ses")
        return redirect("dash.html")
    return render_template("landing.html")


@app.route("/login")
def login():
    que = request.args
    login = auth.login(request.args['user'],request.args['pass'])
    if (login == 0):
        return render_template("landing.html", loginStatus = "Invalid Login.")
    return render_template("dash.html")

@app.route("/register")
def reg():
    que = request.args
    if (auth.register(que['user'],que['pass']) == 0):
        return render_template("landing.html", loginStatus = "Nope. Try again. Already registered")
    else:
        return render_template("landing.html", loginStatus = "Sucessfully Registered.")

if __name__ == '__main__':
    app.debug = True
    app.run()
