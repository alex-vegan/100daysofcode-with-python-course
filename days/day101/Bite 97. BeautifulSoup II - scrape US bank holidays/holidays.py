from collections import defaultdict
import os
from urllib.request import urlretrieve
from pprint import pprint as pp
from bs4 import BeautifulSoup


# prep data
#holidays_page = os.path.join('/tmp', 'us_holidays.php')
#urlretrieve('https://bit.ly/2LG098I', holidays_page)

holidays_page = 'us_holidays.php'

with open(holidays_page) as f:
    content = f.read()

holidays = defaultdict(list)


def get_us_bank_holidays(content=content):
    """Receive scraped html output, make a BS object, parse the bank
       holiday table (css class = list-table), and return a dict of
       keys -> months and values -> list of bank holidays"""
    soup = BeautifulSoup(content, 'html.parser')
    holidays_table = soup.find('table', {'class': 'list-table'})
    holidays_list = holidays_table.tbody.find_all('tr')
    for item in holidays_list:
        holiday_list = item.find_all('td')
        month = holiday_list[1].time.text.strip().split('-')[1]
        holiday = holiday_list[3].a.text
        holidays[month].append(holiday)
    return holidays


if __name__ == "__main__":
    pp(get_us_bank_holidays(content=content))
