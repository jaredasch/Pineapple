#Pineapple -- Kyle Tau, Angela Tom, Mohammed Uddin, Kaitlin Wan
#SoftDev1 pd6
#P00 -- Da Art of Storytellin'(Part X)
#2018-10-15

from flask import Flask,request,render_template,session,url_for,redirect,flash

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = open("secret.txt","r").read()

@app.route("/")
def register():
    
