from collections import ChainMap

NOT_FOUND = "Not found"

gr1 = {'tim': 30, 'bob': 17, 'ana': 24}
gr2 = {'ana': 26, 'thomas': 64, 'helen': 26}
gr3 = {'brenda': 17, 'otto': 44, 'thomas': 46}


def get_person_age(name):
    """Look up name (case insensitive search) and return age.
       If name in > 1 dict, return the match of the group with
       greatest N (so group3 > group2 > group1)
    """
    #gr2.update(group3)
    #gr1.update(group2)
    #return gr1.get(str(name).lower(), NOT_FOUND)
    return dict(ChainMap(gr3, gr2, gr1)).get(str(name).lower(), NOT_FOUND)