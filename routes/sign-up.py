from flask import render_template, session, redirect, request
from main import app
import pyrebase


config = {
    "apiKey": "AIzaSyB5lNPIMw2taY-RqTAH39NUquFVn54ECLk",
    "authDomain": "codebrew2k17.firebaseapp.com",
    "databaseURL": "https://codebrew2k17.firebaseio.com",
    "storageBucket": "codebrew2k17.appspot.com",
    "serviceAccount": "codebrew2k17-firebase-adminsdk-pv7y6-8935885448.json"
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()

@app.route("/sign-up")
def sign_up():
	print(db.child("User").get().val())


	return str("hi")