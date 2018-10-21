#Pineapple -- Kyle Tau, Angela Tom, Mohammed Uddin, Kaitlin Wan
#SoftDev1 pd6
#P00 -- Da Art of Storytellin'(Part X)
#2018-10-15

from flask import Flask,request,render_template,session,url_for,redirect,flash
import os

app = Flask(__name__)
# Set the secret key to some random bytes. Keep this really secret!
#app.secret_key = open("secret.txt","r").read()

@app.route("/")
def register():
    return render_template("landing.html")

if __name__ == '__main__':
    app.debug = True
    app.run()
