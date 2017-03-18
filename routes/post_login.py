from flask import render_template, session, redirect, request
from run import app
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

@app.route("/post-login",methods=['GET', 'POST'])
def post_login():
		
	auth = firebase.auth()	
	user_data = auth.sign_in_with_email_and_password(request.form["email"], request.form["password"])
		
	
	return str("done")