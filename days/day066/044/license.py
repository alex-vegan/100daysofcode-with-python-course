from random import choice
from string import ascii_uppercase, digits

def gen_key(parts=4, chars_per_part=8):
    key = ''
    for part in range(parts):
        for char in range(chars_per_part):
            key += choice(ascii_uppercase + digits)
        key += '-'
    return key[:-1]


if __name__ == "__main__":
    print(gen_key(10,1))
    