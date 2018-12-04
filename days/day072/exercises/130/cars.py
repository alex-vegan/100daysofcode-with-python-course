from collections import Counter

import requests

CAR_DATA = 'https://bit.ly/2Ov65SJ'

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(CAR_DATA).json()


# your turn:
def most_prolific_automaker(year):
    """Given year 'year' return the automaker that released
       the highest number of new car models"""
    xxx = Counter()
    for car in data:
        if car['year'] == year:
            xxx[car['automaker']] += 1
    return xxx.most_common(1)[0][0]
            


def get_models(automaker, year):
    """Filter cars 'data' by 'automaker' and 'year',
       return a set of models (a 'set' to avoid duplicate models)"""
    models = []
    for car in data:
        if car['automaker'] == automaker and car['year'] == year:
            models.append(car['model'])
    return set(models)
            