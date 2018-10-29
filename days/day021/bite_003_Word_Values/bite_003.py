import os
import urllib.request


# PREWORK
#DICTIONARY = os.path.join('/tmp', 'dictionary.txt')
#urllib.request.urlretrieve('http://bit.ly/2iQ3dlZ', DICTIONARY)

DICTIONARY = '../../day020/bite_065_Get_all_valid_dictionary_words_for_a_draw_of_letters/dictionary.txt'

scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                   (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]
LETTER_SCORES = {letter: score for score, letters in scrabble_scores
                 for letter in letters.split()}


# start coding

def load_words():
    """load the words dictionary (DICTIONARY constant) into a list and return it"""
    with open(DICTIONARY) as f:
        return [word.strip() for word in f.read().split()]


def calc_word_value(word):
    """given a word calculate its value using LETTER_SCORES"""
    word_value = 0
    for letter in word:
        word_value += LETTER_SCORES[letter.upper()]
    return word_value


def max_word_value(words=None):
    """given a list of words return the word with the maximum word value"""
    max_word_value = 0
    max_word = ''
    for word in words:
        word_value = calc_word_value(word)
        if word_value > max_word_value:
            max_word_value = word_value
            max_word = word
    return max_word
