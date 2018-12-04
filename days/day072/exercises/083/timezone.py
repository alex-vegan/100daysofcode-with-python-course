from pytz import timezone, utc

AUSTRALIA = timezone('Australia/Sydney')
SPAIN = timezone('Europe/Madrid')


def what_time_lives_pybites(naive_utc_dt):
    """Receives a naive UTC datetime object and returns a two element
       tuple of Australian and Spanish (timezone aware) datetimes"""
    aus_dt = utc.localize(naive_utc_dt).astimezone(AUSTRALIA)
    spa_dt = utc.localize(naive_utc_dt).astimezone(SPAIN)
    return (aus_dt, spa_dt)