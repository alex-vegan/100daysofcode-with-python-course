#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pairs wines and cheeses by similarity of wine name and cheese name.
"""

from collections import Counter
import operator
from pprint import pprint as pp

CHEESES = [
    "Red Leicester",
    "Tilsit",
    "Caerphilly",
    "Bel Paese",
    "Red Windsor",
    "Stilton",
    "Emmental",
    "Gruyere",
    "Norwegian Jarlsberg",
    "Liptauer",
    "Lancashire",
    "White Stilton",
    "Danish Blue",
    "Double Gloucester",
    "Cheshire",
    "Dorset Blue Vinney",
    "Brie",
    "Roquefort",
    "Pont l'Eveque",
    "Port Salut",
    "Savoyard",
    "Saint-Paulin",
    "Carre de l'Est",
    "Bresse-Bleu",
    "Boursin",
    "Camembert",
    "Gouda",
    "Edam",
    "Caithness",
    "Smoked Austrian",
    "Japanese Sage Derby",
    "Wensleydale",
    "Greek Feta",
    "Gorgonzola",
    "Parmesan",
    "Mozzarella",
    "Pipo Creme",
    "Danish Fynbo",
    "Czech sheep's milk",
    "Venezuelan Beaver Cheese",
    "Cheddar",
    "Ilchester",
    "Limburger",
]

RED_WINES = [
    "Chateauneuf-du-Pape",  # 95% of production is red
    "Syrah",
    "Merlot",
    "Cabernet sauvignon",
    "Malbec",
    "Pinot noir",
    "Zinfandel",
    "Sangiovese",
    "Barbera",
    "Barolo",
    "Rioja",
    "Garnacha",
]

WHITE_WINES = [
    "Chardonnay",
    "Sauvignon blanc",
    "Semillon",
    "Moscato",
    "Pinot grigio",
    "Gewurztraminer",
    "Riesling",
]

SPARKLING_WINES = [
    "Cava",
    "Champagne",
    "Cremant d�Alsace",
    "Moscato d�Asti",
    "Prosecco",
    "Franciacorta",
    "Lambrusco",
]

def _similarity(str1, str2):
    c1 = Counter(list(str1))
    c2 = Counter(list(str2))
    intersection = 0
    for k,v in c1.items():
        if k in c2.keys():
            intersection += min(v, c2[k])
    return intersection / (1 + pow(len(str1) - len(str2), 2))


def best_match_per_wine(wine_type="all"):
    """ wine cheese pair with the highest match score
    returns a tuple which contains wine, cheese, score
    """
    best_match = ('', '', 0)
    wine_dict = {'all': RED_WINES + WHITE_WINES + SPARKLING_WINES,
                 'red': RED_WINES,
                 'white': WHITE_WINES,
                 'sparkling': SPARKLING_WINES}
    if wine_type in wine_dict:
        wines = wine_dict[wine_type]
    elif wine_type.capitalize() in wine_dict['all']:
        wines = [wine_type]
    else:
        raise ValueError(f'Sorry, but "{wine_type}" is unknown type of wine.')
    for wine in wines:
        for cheese in CHEESES:
            score = _similarity(wine.lower(), cheese.lower())
            if score > best_match[2]:
                best_match = (wine, cheese, score)
    return best_match


def match_wine_5cheeses():
    """  pairs all types of wines with cheeses ; returns a sorted list of tuples,
    where each tuple contains: wine, list of 5 best matching cheeses.
    List of cheeses is sorted by score descending then alphabetically ascending.
    e.g: [
    ('Barbera', ['Cheddar', 'Gruyere', 'Boursin', 'Parmesan', 'Liptauer']),
    ...
    ...
    ('Zinfandel', ['Caithness', 'Bel Paese', 'Ilchester', 'Limburger', 'Lancashire'])
    ]
    """
    result = []
    for wine in sorted(RED_WINES + WHITE_WINES + SPARKLING_WINES):
        c = Counter()
        for cheese in sorted(CHEESES):
            c[cheese] = _similarity(wine.lower(), cheese.lower())
        result.append((wine, [item[0] for item in c.most_common(5)]))
    return result


if __name__ == "__main__":
    #print(best_match_per_wine('pinot gRigio'))
    pp(match_wine_5cheeses())
