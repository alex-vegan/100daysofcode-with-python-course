from collections import OrderedDict

roman_dict = OrderedDict([(1000, ('M', 1000)),
                          (900, ('C', -100)),
                          (500, ('D', 500)),
                          (400, ('C', -100)),
                          (100, ('C', 100)),
                          (90, ('X', -10)),
                          (50, ('L', 50)),
                          (40, ('X', -10)),
                          (10, ('X', 10)),
                          (9, ('I', -1)),
                          (5, ('V', 5)),
                          (4, ('I', -1)),
                          (1, ('I', 1))])


def romanize(decimal_number):
    """Takes a decimal number int and converts its Roman Numeral str"""
    if not (type(decimal_number) == int and 0 < decimal_number < 4000):
        raise ValueError
    roman_numeral = ''
    while decimal_number > 0:
        for number in roman_dict.keys():
            if decimal_number >= number:
                roman_numeral += roman_dict[number][0]
                decimal_number -= roman_dict[number][1]
                break
    return roman_numeral


if __name__ == "__main__":
    num = 101
    print('-'*101)
    while num != '':
        num = input('input decimal number between 0 and 4K: ')
        try:
            print(romanize(int(num)))
        except Exception as x:
            raise x
        print('-'*101)
