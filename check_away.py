#!/usr/bin/python
import datetime
import logging
import os
import redis
import subprocess

import pytz

tries=3
everett_is = 'away'
while tries:
    tries -= 1
    try:
        x = subprocess.check_output(
            ['ping', '-c1', '-t', '3', '192.168.1.107'])
        everett_is = 'home'
        break
    except subprocess.CalledProcessError:
        pass

print 'Everett is', everett_is
REDIS = redis.from_url(os.getenv('REDISTOGO_URL'))
REDIS.setex('everett_is', everett_is, 60*3)  # Expires in 3m

TZ = pytz.timezone('US/Pacific')
now = datetime.datetime.now(tz=pytz.utc).astimezone(TZ)
datestr = now.strftime('%A, %B %d %Y')
hourstr = now.strftime('%I:%M %p')
logging.basicConfig(
    filename='check_away.log',
    level=logging.DEBUG,
    format='%(asctime)s:%(levelname)s:%(message)s')
logging.info(everett_is)
