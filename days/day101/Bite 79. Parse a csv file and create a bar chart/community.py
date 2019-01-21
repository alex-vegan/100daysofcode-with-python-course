import csv

import requests
from collections import Counter
from pprint import pprint as pp

CSV_URL = 'https://bit.ly/2HiD2i8'


def get_csv():
    """Use requests to download the csv and return the
       decoded content"""
    resp = requests.get(CSV_URL)
    resp.raise_for_status()
    return resp.text


def create_user_bar_chart(content):
    """Receives csv file (decoded) content and returns a table of timezones
       and their corresponding member counts in pluses (see Bite/tests)"""
    c = Counter()
    result = ''
    for row in content.split()[1:]:
        c[row.split(',')[-1]] += 1
    for k in sorted(c):
        result += '{:20} | {}\n'.format(k, '+' * c[k])
    print(result.strip())


if __name__ == "__main__":
    create_user_bar_chart(get_csv())
