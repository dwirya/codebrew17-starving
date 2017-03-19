from flask import render_template, session, redirect, url_for, render_template, request
from . import main
from .forms import LoginForm
# from chat import app
import pyrebase


@main.route('/', methods=['GET', 'POST'])
def index():
    """"Login form to enter a room."""
    form = LoginForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        # session['room'] = form.room.data
        return redirect(url_for('.chat'))
    elif request.method == 'GET':
        form.name.data = session.get('name', '')
        # form.room.data = session.get('room', '')
    return render_template('front_page.html', form=form)


@main.route('/chat')
def chat():
    """Chat room. The user's name and room must be stored in
    the session."""
    name = session.get('name', '')
    room = session.get('room', '')
    if name == '' or room == '':
        return redirect(url_for('.index'))
    return render_template('chatroom.html', name=name, room=room)


config = {
    "apiKey": "AIzaSyB5lNPIMw2taY-RqTAH39NUquFVn54ECLk",
    "authDomain": "codebrew2k17.firebaseapp.com",
    "databaseURL": "https://codebrew2k17.firebaseio.com",
    "storageBucket": "codebrew2k17.appspot.com",
    "serviceAccount": "codebrew2k17-firebase-adminsdk-pv7y6-8935885448.json"
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()

@main.route("/login",methods=['GET', 'POST'])
def login():
    return render_template("login.html")

@main.route("/post-login",methods=['GET', 'POST'])
def post_login():
        
    auth = firebase.auth()  
    user_data = auth.sign_in_with_email_and_password(request.form["email"], request.form["password"])
        
    
    return str("done")

@main.route("/post-sign-up",methods=['GET', 'POST'])
def post_sign_up():

    auth = firebase.auth()  
    user_data = auth.create_user_with_email_and_password(request.form["email"], request.form["password"])
        
    
    # #have to store user in user database  
    data = {
        "firstName" : request.form["firstname"],
        "lastName" : request.form["lastname"],
        "email" : request.form["email"],
            
    }

    db.child('User').child(user_data['localId']).set(data)
    
    return str("done")



@main.route("/sign-up",methods=['GET', 'POST'])
def sign_up():
    return render_template("sign-up.html")







