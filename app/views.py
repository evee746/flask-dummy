import datetime
import hashlib
import logging
import os
import subprocess

from flask import render_template
import pytz

from app import app

logging.basicConfig(
    filename='example.log',
    level=logging.DEBUG,
    format='%(asctime)s:%(levelname)s:%(message)s')

TZ = pytz.timezone('US/Pacific')
REDIS = redis.from_url(os.getenv('REDISTOGO_URL'))

# def check_away():
#     try:
#         x = subprocess.check_output(
#             ['ping', '-c1', '-t', '1', '192.168.1.107'])
#         return False
#     except subprocess.CalledProcessError:
#         return True

@app.route('/')
def index():
    away = check_away()
    REDIS.get('everett_away', True)
    now = datetime.datetime.now(tz=pytz.utc).astimezone(TZ)
    datestr = now.strftime('%A, %B %d %Y')
    hourstr = now.strftime('%I:%M %p')
    logging.info('Everett is %s', 'away' if away else 'home')
    return render_template('index.html',
        date=datestr,
        hours=hourstr,
        away=away)
