from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
	return render_template('index.html',
		location='San Francisco, CA',
		date='Sunday 2014/07/27')
