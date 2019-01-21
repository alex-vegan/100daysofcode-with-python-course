from collections import namedtuple
from datetime import datetime, timedelta

TimeOffset = namedtuple('TimeOffset', 'offset date_str divider')

NOW = datetime.now()
MINUTE, HOUR, DAY = 60, 60*60, 24*60*60
TIME_OFFSETS = (
    TimeOffset(10, 'just now', None),
    TimeOffset(MINUTE, '{} seconds ago', None),
    TimeOffset(2*MINUTE, 'a minute ago', None),
    TimeOffset(HOUR, '{} minutes ago', MINUTE),
    TimeOffset(2*HOUR, 'an hour ago', None),
    TimeOffset(DAY, '{} hours ago', HOUR),
    TimeOffset(2*DAY, 'yesterday', None),
)


def pretty_date(date):
    """Receives a datetime object and converts/returns a readable string
       using TIME_OFFSETS"""
    if not type(date) == datetime:
        raise ValueError('the mistake of time format :(')
    how_long_days = (NOW - date).days
    if how_long_days < 0:
        raise ValueError('back to the future :)')
    if how_long_days >= 2:
        return date.strftime('%m/%d/%y')
    how_long_seconds = (NOW - date).seconds + how_long_days * DAY
    for time_offset in TIME_OFFSETS:
        if how_long_seconds < time_offset.offset:
            if time_offset.divider:
                how_long_seconds = int(how_long_seconds // time_offset.divider)
            result = time_offset.date_str
            if '{}' in time_offset.date_str:
                result = result.format(how_long_seconds)
            break
    return result


if __name__ == "__main__":
    date = NOW - timedelta(days=1, hours=23, minutes=59, seconds=59)
    print(pretty_date(date))
