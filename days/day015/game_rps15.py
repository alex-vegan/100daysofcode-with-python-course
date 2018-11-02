import random
from classes import Roll, Player
import csv
import sys
sys.path.append('../day014/rps_game')
from game import get_player_name


CSV_FILE = 'battle-table.csv'

def print_header():
    print('------------------------------------------')
    print('  ROCK-PAPER-SCISSORS (extended version)  ')
    print('------------------------------------------')

# dict of rolls(objects)
def build_the_fifteen_rolls():
    with open(CSV_FILE) as f:
        reader = csv.DictReader(f)
        rolls = {}
        for row in reader:
            defeat_list = []
            for key, value in row.items():
                if key == 'Attacker':
                    name = value
                elif value == 'win':
                    defeat_list.append(key)
            rolls[name] = Roll(name, tuple(defeat_list))
    return rolls


def get_computer_roll(rolls):
    return rolls[random.choice(list(rolls.keys()))]


def get_player_roll(rolls):
    choise = ''
    print("-"*42)
    while not len(choise) == 1 or not choise.lower() in 'adefghklnoprstw':
        choise = input("Choose your roll:\n"
                       "[R]ock, [P]aper, [S]cissors, d[E]vil, [G]un,\n"
                       "[L]ightning, [D]ragon, spo[N]ge, [T]ree, [A]ir,\n"
                       "[W]ater, [H]uman, w[O]lf, sna[K]e, [F]ire ? ")
    if choise.lower() == "r": return rolls["Rock"]
    if choise.lower() == "p": return rolls["Paper"]
    if choise.lower() == "s": return rolls["Scissors"]
    if choise.lower() == "g": return rolls["Gun"]
    if choise.lower() == "l": return rolls["Lightning"]
    if choise.lower() == "e": return rolls["Devil"]
    if choise.lower() == "d": return rolls["Dragon"]
    if choise.lower() == "w": return rolls["Water"]
    if choise.lower() == "a": return rolls["Air"]
    if choise.lower() == "n": return rolls["Sponge"]
    if choise.lower() == "o": return rolls["Wolf"]
    if choise.lower() == "t": return rolls["Tree"]
    if choise.lower() == "h": return rolls["Human"]
    if choise.lower() == "k": return rolls["Snake"]
    if choise.lower() == "f": return rolls["Fire"]


def geme_loop(player1, player2, rolls):
    count = 0
    while count < 3:
        p2_roll = get_computer_roll(rolls)
        p1_roll = get_player_roll(rolls)
        p1_outcome = p1_roll.candefeat(p2_roll)
        p2_outcome = p2_roll.candefeat(p1_roll)
        if p1_outcome:
            player1.count += 1
            winner = player1
        elif p2_outcome:
            player2.count += 1
            winner = player2
        else:
            winner = None
        print(f'\n{player1.name}({p1_roll.roll}) vs. '
              f'{player2.name}({p2_roll.roll})')
        if winner:
            print(f'In this round {winner.name} is won!')
        else:
            print(f'In this round both players have same result.')
        count += 1
    print('-'*42 + f'\nresult of game ({player1.count} : {player2.count})')
    if player1.count > player2.count:
        print(f'Congratulation {player1.name}, you won!')
    elif player1.count < player2.count:
        print(f"I'm sory for you {player1.name}, but {player2.name} won.")
    else:
        print(f'Score of both players is equal. Draw game!')


def main():
    print_header()
    rolls = build_the_fifteen_rolls()     # dict of rolls(objects)
    name = get_player_name()
    player1 = Player(name)
    player2 = Player("computer")
    geme_loop(player1, player2, rolls)


if __name__ == "__main__":
    main()
