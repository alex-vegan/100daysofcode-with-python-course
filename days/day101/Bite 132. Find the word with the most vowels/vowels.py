from collections import Counter


VOWELS = list('aeiou')


text = ("The Python interpreter is easily extended with new functions "
        "and data types implemented in C or C++ (or other languages "
        "callable from C). Python is also suitable as an extension "
        "language for customizable applications.")


def get_word_max_vowels(text):
    """Get the case insensitive word in text that has most vowels.
       Return a tuple of the matching word and the vowel count, e.g.
       ('object-oriented', 6)"""
    c = Counter()
    for word in set(text.lower().split()):
        for char in list(word):
            if char in VOWELS:
                c[word] += 1
    return c.most_common(1)[0]


if __name__ == "__main__":
    print(get_word_max_vowels(text))
