VALID_COLORS = ['blue', 'yellow', 'red']


def print_colors():
    """Ask for color, lowercase it, check if 'quit' is entered, if so print
       'bye' and break, next check if given color is in VALID_COLORS, if not,
       continue, finally if that check passes, print the color"""
    while True:
        quest = input('enter a color: ').lower()
        if quest == 'quit':
            print('bye')
            break
        elif not quest in VALID_COLORS:
            print('Not a valid color') 
            continue
        print(quest)
    return None
