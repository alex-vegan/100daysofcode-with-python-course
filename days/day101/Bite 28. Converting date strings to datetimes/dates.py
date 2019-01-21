import collections
from datetime import datetime
import os
import re
from urllib.request import urlretrieve

BASE_URL = 'http://projects.bobbelderbos.com/pcc/dates/'
RSS_FEED = 'all.rss.xml'
PUB_DATE = re.compile(r'<pubDate>(.*?)</pubDate>')
TMP = '/tmp'


def _get_dates():
    """Downloads PyBites feed and parses out all pub dates returning
       a list of date strings, e.g.: ['Sun, 07 Jan 2018 12:00:00 +0100',
       'Sun, 07 Jan 2018 11:00:00 +0100', ... ]"""
    remote = os.path.join(BASE_URL, RSS_FEED)
    local = os.path.join(TMP, RSS_FEED)
    urlretrieve(remote, local)

    with open(local) as f:
        return PUB_DATE.findall(f.read())


dates = _get_dates()

months = {
    1: 'Jan',
    2: 'Feb',
    3: 'Mar',
    4: 'Apr',
    5: 'May',
    6: 'Jun',
    7: 'Jul',
    8: 'Aug',
    9: 'Sep',
    10: 'Oct',
    11: 'Nov',
    12: 'Dec'         
}


def convert_to_datetime(date_str):
    """Receives a date str and convert it into a datetime object"""
    regex = (r'\S+, (\d+) (\S+) (\d+) (\d+):(\d+):.*')
    match = re.search(regex, date_str)
    year = int(match.groups()[2])
    month = [k for k,v in months.items() if v == match.groups()[1]][0] 
    day = int(match.groups()[0])
    hour = int(match.groups()[3])
    minute = int(match.groups()[4])
    dt = datetime(year=year, month=month, day=day, hour=hour, minute=minute)
    return dt


def get_month_most_posts(dates):
    """Receives a list of datetimes and returns the month (format YYYY-MM)
       that occurs most"""
    c = collections.Counter()
    for d in dates:
        c[str(d.year) + '-' + str(d.month).zfill(2)] += 1
    return c.most_common(1)[0][0]
        