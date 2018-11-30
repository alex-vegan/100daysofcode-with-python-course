INDENTS = 4


def print_hanging_indents(poem):
    indent = False
    for row in poem.strip().split("\n"):
        if row.strip() and indent:
            print(' '*INDENTS + row.strip())
        elif row.strip():
            print(row.strip())
            indent = True
        else:
            indent = False
