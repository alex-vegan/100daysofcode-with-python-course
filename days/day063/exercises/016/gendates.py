from datetime import datetime, timedelta
from itertools import islice
from pprint import pprint as pp

PYBITES_BORN = datetime(year=2016, month=12, day=19)


def gen_special_pybites_dates():
    special_date = PYBITES_BORN
    special_day = special_date.day
    special_month = special_date.month
    date = special_date
    while True:
        date += timedelta(days=1)
        if date.day == special_day and date.month == special_month or \
            (date - special_date).days % 100 == 0:
            yield date


if __name__ == "__main__":
    gen = gen_special_pybites_dates()
    pp(list(islice(gen, 10)))
