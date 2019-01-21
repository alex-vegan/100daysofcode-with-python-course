from datetime import datetime
import heapq
import copy

numbers = [0, -1, 1, -2, 2, -3, 3, -4, 4, -5, 5, -6, 6]
dates = [datetime(2018, 1, 23, 0, 0),
         datetime(2017, 12, 19, 0, 0),
         datetime(2017, 10, 15, 0, 0),
         datetime(2019, 2, 27, 0, 0),
         datetime(2017, 3, 29, 0, 0),
         datetime(2018, 8, 11, 0, 0),
         datetime(2018, 5, 3, 0, 0),
         datetime(2018, 12, 19, 0, 0),
         datetime(2018, 11, 19, 0, 0),
         datetime(2017, 7, 7, 0, 0)]
# https://www.forbes.com/celebrities/list
earnings_mln = [
    {'name': 'Kevin Durant', 'earnings': 60.6},
    {'name': 'Adele', 'earnings': 69},
    {'name': 'Lionel Messi', 'earnings': 80},
    {'name': 'J.K. Rowling', 'earnings': 95},
    {'name': 'Elton John', 'earnings': 60},
    {'name': 'Chris Rock', 'earnings': 57},
    {'name': 'Justin Bieber', 'earnings': 83.5},
    {'name': 'Cristiano Ronaldo', 'earnings': 93},
    {'name': 'Beyonce Knowles', 'earnings': 105},
    {'name': 'Jackie Chan', 'earnings': 49},
]


def get_largest_number(numbers, n=3):
    min_numbers = []
    invert_numbers = [-num for num in numbers]
    heapq.heapify(invert_numbers)
    for _ in range(n):
        min_numbers.append(heapq.heappop(invert_numbers))
    return [-num for num in min_numbers]


def get_latest_dates(dates, n=3):
    latest_dates = []
    dates_copy = dates.copy()
    for _ in range(n):
        heapq._heapify_max(dates_copy)
        latest_dates.append(heapq.heappop(dates_copy))
    return latest_dates


def get_highest_earnings(earnings_mln, n=3):
    highest_earnings = []
    earnings_mln_copy = copy.deepcopy(earnings_mln)
    earnings_mln_list = [_['earnings'] for _ in earnings_mln_copy]
    for _ in range(n):
        heapq._heapify_max(earnings_mln_list)
        max_mln = heapq.heappop(earnings_mln_list)
        highest_earnings.append([_ for _ in earnings_mln_copy if _['earnings']==max_mln][0])
    return highest_earnings

'''
def get_highest_earnings(earnings_mln, n=3):
    highest_earnings = []
    earnings_mln_copy = copy.deepcopy(earnings_mln)
    sorted_emc = sorted(earnings_mln_copy, key = lambda x: x['earnings'])
    for _ in range(n):
        highest_earnings.append(sorted_emc.pop())
    return highest_earnings
'''