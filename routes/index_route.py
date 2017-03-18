from flask import render_template, session
from run import app

#server/
@app.route("/")
def index():
	title = "Index"
	template_vars = {
		"title" : title
	}
	
	return render_template("index.html",vars = template_vars)