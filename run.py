from flask import Flask, render_template, session
app = Flask(__name__, static_folder='.', static_url_path='')
WTF_CSRF_ENABLED = True
from gevent import monkey
#from socketio.server import SocketIOServer


#import all routes from routes directory
from routes import *

monkey.patch_all()

if __name__ == "__main__":
    app.run(debug=True, port=2526)
