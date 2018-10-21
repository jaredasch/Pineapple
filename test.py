#Team Pineapple


from flask import Flask,request,render_template,session,url_for,redirect,flash
import os

app = Flask(__name__)
# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = "supersecretkey123"

@app.route('/')
def home():
    return render_template("landing.html")

if __name__ == '__main__':
    app.debug = True
    app.run()
