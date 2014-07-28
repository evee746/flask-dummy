from flask import render_template
from app import app

@app.route('/')
def index():
	return render_template('index.html',
		location='San Francisco, CA',
		date='Sunday 2014/07/27')
