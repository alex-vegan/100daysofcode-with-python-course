from datetime import datetime, timedelta
import os
import urllib.request
import re

SHUTDOWN_EVENT = 'Shutdown initiated'

logfile = os.path.join('/tmp', 'log')
urllib.request.urlretrieve('http://bit.ly/2AKSIbf', logfile)


with open(logfile) as f:
    loglines = f.readlines()


def convert_to_datetime(line):
    '''TODO 1:
       Given a log line extract its timestamp and convert it to a datetime obj.
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)'''
    regex = ('\w+ +(?P<year>\d+)-(?P<month>\d+)-(?P<day>\d+)T'
             '(?P<hour>\d+):(?P<minute>\d+):(?P<second>\d+) +\S+')
    match = re.search(regex, line)
    year = int(match.group('year'))
    month = int(match.group('month'))
    day = int(match.group('day'))
    hour = int(match.group('hour'))
    minute = int(match.group('minute'))
    second = int(match.group('second'))
    return datetime(year, month, day, hour, minute, second)


def time_between_shutdowns(loglines):
    '''TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and
       calculate the timedelta between the first and last one.
       Return this datetime.timedelta object.'''
    for line in loglines:
       if  SHUTDOWN_EVENT in line:
           firstTime = convert_to_datetime(line)
           break
    for line in loglines[::-1]:
        if SHUTDOWN_EVENT in line:
            lastTime = convert_to_datetime(line)
            break
    return lastTime - firstTime