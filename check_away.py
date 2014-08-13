#!/usr/bin/python
import datetime
import logging
import os
import redis
import subprocess

import pytz

tries=3
while tries:
    tries -= 1
    try:
        x = subprocess.check_output(
            ['ping', '-c1', '-t', '3', '192.168.1.107'])
        return False
    except subprocess.CalledProcessError:
        pass
return True

away = check_away()
away_str = 'away' if away else 'home'
REDIS = redis.from_url(os.getenv('REDISTOGO_URL'))
REDIS.setex('everett_is', away_str, 60*3)  # Expires in 3m

TZ = pytz.timezone('US/Pacific')
now = datetime.datetime.now(tz=pytz.utc).astimezone(TZ)
datestr = now.strftime('%A, %B %d %Y')
hourstr = now.strftime('%I:%M %p')
logging.basicConfig(
    filename='check_away.log',
    level=logging.DEBUG,
    format='%(asctime)s:%(levelname)s:%(message)s')
logging.info(away_str)
