import datetime
import hashlib
import logging
import os
import subprocess

from flask import render_template
import pytz
import redis

from app import app

logging.basicConfig(
    filename='views.log',
    level=logging.DEBUG,
    format='%(asctime)s:%(levelname)s:%(message)s')

TZ = pytz.timezone('US/Pacific')
REDIS = redis.from_url(os.getenv('REDISTOGO_URL'))

@app.route('/')
def index():
    everett_is = REDIS.get('everett_is') or 'unknown'
    now = datetime.datetime.now(tz=pytz.utc).astimezone(TZ)
    datestr = now.strftime('%A, %B %d %Y')
    hourstr = now.strftime('%I:%M %p')
    logging.info('Everett is %s', everett_is)
    return render_template('index.html',
        date=datestr,
        hours=hourstr,
        everett_is=everett_is)
