from itertools import cycle, islice
from string import ascii_uppercase

def sequence_generator():
    '''
    <<< Alpha-Digital Cycle Generator >>>
    1, 'A', 2, 'B', 3, 'C', ... 'X', 25, 'Y', 26, 'Z', 1, 'A', 2, 'B', ...
    '''
    alphas = list(ascii_uppercase)
    digits = list(range(1,27))
    alpha_digit_list = []
    for i in range(26):
        alpha_digit_list.append(digits[i])
        alpha_digit_list.append(alphas[i])
    return cycle(alpha_digit_list)
