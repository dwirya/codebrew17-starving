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

	form = RegisterForm()

		
	auth = firebase.auth()
		#user register in authentication database
		
	
	user_data = auth.create_user_with_email_and_password(request.form["email"], request.form["password"])
		
	
	#have to store user in user database	
	data = {
	    "firstName" : request.form["firstname"],
		"lastName" : request.form["lastname"],
	    "email" : request.form["email"],
	    "emailVerified" : "false"
	}

	db.child('Users').child(user_data['localId']).child('UserDetails').set(data)
	
	session['logged_in'] = True

		
	return render_template("register.html",vars = template_vars, form=form)
