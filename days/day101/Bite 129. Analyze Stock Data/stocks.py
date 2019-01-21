import requests
from collections import Counter

STOCK_DATA = 'https://bit.ly/2MzKAQg'

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(STOCK_DATA).json()


# your turn:

def _cap_str_to_mln_float(cap):
    """If cap = 'n/a' return 0, else:
       - strip off leading '$',
       - if 'M' in cap value, strip it off and return value as float,
       - if 'B', strip it off and multiple by 1,000 and return
         value as float"""
    if cap == 'n/a':
        return 0
    mult = 1
    if cap[-1] == "B":
        mult = 1000
    return float(cap[1:-1]) * mult


def get_industry_cap(industry):
    """Return the sum of all cap values for given industry, use
       the _cap_str_to_mln_float to parse the cap values,
       return a float with 2 digit precision"""
    return round(sum([_cap_str_to_mln_float(_['cap']) for _ in data
                                if _['industry'] == industry]), 2)


def get_stock_symbol_with_highest_cap():
    """Return the stock symbol (e.g. PACD) with the highest cap, use
       the _cap_str_to_mln_float to parse the cap values"""
    return sorted(data, key=lambda x: _cap_str_to_mln_float(x['cap']))[-1]['symbol']


def get_sectors_with_max_and_min_stocks():
    """Return a tuple of the sectors with most and least stocks,
       discard n/a"""
    c = Counter(_['sector'] for _ in data if _['sector'] != "n/a").most_common()
    return (c[0][0], c[-1][0])


def get_sector_with_max_and_min_cap():
    """Return a tuple of the sectors with most and least stocks,
       discard n/a"""
    max_cap, min_cap = 0.0, _cap_str_to_mln_float(data[0]['cap'])
    max_sector, min_sector = '', ''
    for item in data:
        cap = _cap_str_to_mln_float(item['cap'])
        if cap and cap > max_cap:
            max_cap = cap
            max_sector = item['sector']
        elif cap and cap < min_cap:
            min_cap = cap
            min_sector = item['sector']
    print(min_cap, max_cap)
    return (max_sector, min_sector)






if __name__ == "__main__":
    #print(get_industry_cap('Finance: Consumer Services'))
    #print(get_stock_symbol_with_highest_cap())
    #print(get_sector_with_max_and_min_cap())
    print(get_sectors_with_max_and_min_stocks())
