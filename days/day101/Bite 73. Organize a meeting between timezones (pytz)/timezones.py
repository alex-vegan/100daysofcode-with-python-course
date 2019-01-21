import pytz
from datetime import datetime, timedelta

MEETING_HOURS = range(6, 23)  # meet from 6 - 22 max
TIMEZONES = set(pytz.all_timezones)


def within_schedule(utc, *timezones):
    """Receive a utc datetime and one or more timezones and check if
       they are all within schedule (MEETING_HOURS)"""
    utc = pytz.timezone('UTC').localize(utc)
    #utc = pytz.utc.localize(utc)
    #utc = utc.replace(tzinfo=pytz.timezone('UTC'))
    #utc = utc.replace(tzinfo=pytz.utc)
    try:
        return all([utc.astimezone(pytz.timezone(tz)).hour in MEETING_HOURS for tz in timezones])
    except:
        raise ValueError


if __name__ == "__main__":
    timezones = ['Europe/Madrid', 'Australia/Sydney', 'America/Chicago']
    utc_times = [datetime(2018, 4, 18, 13, 28),
                 datetime(2018, 4, 18, 12, 28),
                 datetime(2018, 10, 18, 12, 28)]
    for dt in utc_times:
        print(within_schedule(dt, *timezones))
    print(within_schedule(datetime(2018, 4, 18, 13, 28), 'Europe/Madrid', 'bogus'))
