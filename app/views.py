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

PHONE_MAC_SUFFIX = '7b:5b:3c'
TZ = pytz.timezone('US/Pacific')

# def check_away():
#     lines = subprocess.check_output(['netstat', '-nr']).splitlines()
#     for line in lines:
#         if line.startswith('192.168.1.') and len(line.split()) > 1:
#             ip, mac = line.split()[:2]
#             if mac.endswith(PHONE_MAC_SUFFIX):
#                 try:
#                     x = subprocess.check_output(['ping', '-c1', '-t', '1', ip])
#                     return False
#                 except subprocess.CalledProcessError:
#                     return True
#     return True

def check_away():
    try:
        x = subprocess.check_output(
            ['ping', '-c1', '-t', '1', '192.168.1.107'])
        return False
    except subprocess.CalledProcessError:
        return True

@app.route('/')
def index():
    away = check_away()
    now = datetime.datetime.now(tz=pytz.utc).astimezone(TZ)
    datestr = now.strftime('%A, %B %d %Y')
    hourstr = now.strftime('%I:%M %p')
    logging.info('Everett is %s', 'away' if away else 'home')
    return render_template('index.html',
        date=datestr,
        hours=hourstr,
        away=away)
