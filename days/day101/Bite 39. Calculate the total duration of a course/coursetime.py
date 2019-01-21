from datetime import datetime, timedelta
import os
import re
import urllib.request

# getting the data
#COURSE_TIMES = os.path.join('/tmp', 'course_timings')
#urllib.request.urlretrieve('http://bit.ly/2Eb0iQF', COURSE_TIMES)

COURSE_TIMES = 'course_timings'

def get_all_timestamps():
    """Read in the COURSE_TIMES and extract all MM:SS timestamps.
       Here is a snippet of the input file:

       Start  What is Practical JavaScript? (3:47)
       Start  The voice in your ear (4:41)
       Start  Is this course right for you? (1:21)
       ...

        Return a list of MM:SS timestamps
    """
    with open(COURSE_TIMES) as f:
        return re.findall(r'\((\d+:\d+)\)', f.read())


def calc_total_course_duration(timestamps):
    """Takes timestamps list as returned by get_all_timestamps
       and calculates the total duration as HH:MM:SS"""
    now = datetime.now()
    future = now
    for t in timestamps:
        minutes, seconds = [int(i) for i in t.split(':')]
        future += timedelta(minutes=minutes, seconds=seconds)
    diff = future - now
    hours = diff.seconds // 3600
    minutes = (diff.seconds % 3600) // 60
    seconds = (diff.seconds % 3600) % 60
    return f'{hours}:{minutes}:{seconds}'
        
        