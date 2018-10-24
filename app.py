#Pineapple -- Kyle Tau, Angela Tom, Mohammed Uddin, Kaitlin Wan
#SoftDev1 pd6
#P00 -- Da Art of Storytellin'(Part X)
#2018-10-15

from flask import Flask,request,render_template,session,url_for,redirect,flash
import os
from util import auth,entries

app = Flask(__name__)
# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = "supersecretkey"

@app.route("/")
def home():

    if 'user' in session: #ALREADY LOGGED IN NEVER LOGGED OUT
        print("user in ses")
        return redirect("dash.html")

    if not("user" in request.args): #NOT LOGGED IN NEW USER FIRST TIME
        return render_template("landing.html")

    login = auth.login(request.args['user'],request.args['pass'])
    print(login)
    if login == 0: #Page with error msg
        return render_template("template.html", loginStatus = "unsucessful")
    else:
        session['user'] = request.args["user"]
        return redirect('/landing.html')
    return render_template("landing.html")



@app.route("/login")
def login():
    que = request.args
    print(que)
    return render_template("dash.html")

@app.route("/register")
def reg():
    que = request.args
    auth.register(que['user'],que['pass'])
    return render_template("landing.html")

@app.route("/display_entry")
def display_entry():
    que = request.args
    text = entries.viewEntry(que['entry_id'])
    return render_template("entry.html", entry_text=text)


if __name__ == '__main__':
    app.debug = True
    app.run()
