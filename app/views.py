from flask import render_template
from app import app

import datetime
import pytz

TZ = pytz.timezone('US/Pacific')

@app.route('/')
def index():
	now = datetime.datetime.now(tz=pytz.utc).astimezone(TZ)
	return render_template('index.html',
		location='San Francisco, CA',
		date=now.strftime('%A, %B %d %Y'),
		hours=now.strftime('%I:%M %p'))
