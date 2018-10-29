from random import sample
from itertools import islice
from pprint import pprint as pp

NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


def convert_title_case_names(names=NAMES):
    return [name.title() for name in names]


def reverse_first_last_names(names=NAMES):
    return [" ".join(name.split()[::-1]) for name in names]


def gen_pairs(names=NAMES):
    while True:
        l, r = sample(names, 2)
        yield f"{(l.split()[0]).title()} teams up with {(r.split()[0]).title()}"

'''
if __name__ == "__main__":
    print(convert_title_case_names())
    print('-'*101)
    print(reverse_first_last_names())
    print('-'*101)
    pairs = gen_pairs()
    for _ in range(10):
        print(next(pairs))
    print('-'*101)
    pp(list(islice(pairs, 10)))
'''
