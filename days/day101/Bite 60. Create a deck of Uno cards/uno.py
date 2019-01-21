from collections import namedtuple

SUITS = 'Red Green Yellow Blue'.split()
NAMES = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
         'Draw Two', 'Skip', 'Reverse', 'Wild', 'Wild Draw Four']

UnoCard = namedtuple('UnoCard', 'suit name')


def create_uno_deck():
    """Create a deck of 108 Uno cards.
       Return a list of UnoCard namedtuples
       (for cards w/o suit use None in the namedtuple)"""
    uno_deck = []
    names_with_suit = NAMES[:-2]
    names_without_suit = NAMES[-2:]
    for suit in SUITS:
        uno_deck.append(UnoCard(suit=suit, name=names_with_suit[0]))
        for name in names_with_suit[1:]:
            uno_deck.append(UnoCard(suit=suit, name=name))
            uno_deck.append(UnoCard(suit=suit, name=name))
    for name in names_without_suit:
        for _ in range(4):
            uno_deck.append(UnoCard(suit=None, name=name))
    return uno_deck


if __name__ == "__main__":
    print(create_uno_deck())
