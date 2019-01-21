from datetime import datetime

BITE_CREATED_DT = datetime.strptime('2018-02-26 23:24:04', '%Y-%m-%d %H:%M:%S')

PY2_RETIRE = datetime.strptime('2020-04-12 00:00:00', '%Y-%m-%d %H:%M:%S')


def py2_earth_hours_left():
    """Return how many hours, rounded to 2 decimals, Python 2 has
       left on Planet Earth"""
    return round((PY2_RETIRE - BITE_CREATED_DT).total_seconds() / (60*60), 2)


def py2_miller_min_left():
    """Return how many minutes, rounded to 2 decimals, Python 2 has
       left on Planet Miller"""
    return round((PY2_RETIRE - BITE_CREATED_DT).total_seconds() / (60*24*365*7), 2)
