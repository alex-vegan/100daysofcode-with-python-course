def get_index_different_char(chars):
    alphanumeric_count, not_alphanumeric_count = 0, 0
    last_alphanumeric_idx, last_not_alphanumeric_idx = 0, 0
    alphanumeric = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    for idx, char in enumerate(chars):
        if str(char) in alphanumeric:
            alphanumeric_count += 1
            last_alphanumeric_idx = idx
        else:
            not_alphanumeric_count += 1
            last_not_alphanumeric_idx = idx
    if alphanumeric_count > not_alphanumeric_count:
        return last_not_alphanumeric_idx
    return last_alphanumeric_idx


if __name__ == '__main__':
    print(get_index_different_char(['A', 'f', '.', 'Q', 2]))
    print(get_index_different_char(['.', '{', ' ^', '%', 'a']))
    print(get_index_different_char([1, '=', 3, 4, 5, 'A', 'b', 'a', 'b', 'c']))
    print(get_index_different_char(['=', '=', '', '/', '/', 9, ':', ';', '?', '¡']))
    print(get_index_different_char(list(range(1,9)) + ['}'] + list('abcde')))
    #pytest --cov-report term-missing --cov='.'
            
