import itertools
import os
import urllib.request

# PREWORK
#DICTIONARY = os.path.join('/tmp', 'dictionary.txt')
#urllib.request.urlretrieve('http://bit.ly/2iQ3dlZ', DICTIONARY)

DICTIONARY = 'dictionary.txt'

with open(DICTIONARY) as f:
    dictionary = set([word.strip().lower() for word in f.read().split()])
    


def get_possible_dict_words(draw):
    """Get all possible words from a draw (list of letters) which are
       valid dictionary words. Use _get_permutations_draw and provided
       dictionary"""
    perm = _get_permutations_draw(draw)
    set_of_words = set()
    while True:
        try:
            word = "".join(perm.__next__()).lower()
            if word in dictionary:
                set_of_words.add(word)
        except StopIteration:
            return tuple(set_of_words)


def _get_permutations_draw(draw):
    """Helper to get all permutations of a draw (list of letters), hint:
       use itertools.permutations (order of letters matters)"""
    for i in range(len(draw)):
        list_perm = itertools.permutations(draw, i+1)
        for perm in list_perm:
            yield perm


if __name__ == "__main__":
    #print(get_possible_dict_words('T, I, I, G, T, T, L'.split(", ")))
