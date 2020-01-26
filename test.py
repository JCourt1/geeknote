import os
import datetime
import pytz

for tz in pytz.all_timezones:
    os.environ['TZ'] = tz
    print datetime.datetime.fromtimestamp(1095292800)

