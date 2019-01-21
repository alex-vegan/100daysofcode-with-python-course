def generate_xmas_tree(rows=10):
    """Generate a xmas tree of stars (*) for given rows (default 10).
       Each row has row_number*2-1 stars, simple example: for rows=3 the
       output would be like this (ignore docstring's indentation):
         *
        ***
       *****"""
    xmas_tree = ''
    for row in range(1, rows+1):
        xmas_tree += ' '*(rows-row) + '*'*(row*2-1) + '\n'
    return xmas_tree.rstrip()


if __name__ == "__main__":
    print(generate_xmas_tree())
