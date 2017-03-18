from flask import render_template, session
from main import app

#server/
@app.route("/")
def index():
	title = "Index"
	template_vars = {
		"title" : title
	}
	
	return render_template("index.html",vars = template_vars)