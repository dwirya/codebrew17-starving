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

@app.route("/sign-up",methods=['GET', 'POST'])
def post_sign_up():
		
	

	
		
	auth = firebase.auth()
		#user register in authentication database
	#print(request.form["email"])
		
	user_data = auth.create_user_with_email_and_password(request.form["email"], request.form["password"])
		
	
	# #have to store user in user database	
	data = {
	    "firstName" : request.form["firstname"],
		"lastName" : request.form["lastname"],
	    "email" : request.form["email"],
	    	
	}

	db.child('User').child(user_data['localId']).set(data)

	#session['uid_email_verified'] = user_data['localId']		
	#session['logged_in'] = True

		
	return str("done")
