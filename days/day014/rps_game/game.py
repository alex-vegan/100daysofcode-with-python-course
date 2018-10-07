import random
from collections import namedtuple
from classes import Roll, Player 


def print_header():
    print('------------------------------------------') 
    print('         R@CK-PAP#R-SCISSOR8< GAME        ')
    print('------------------------------------------') 


def build_the_three_rolls():
    rock = Roll('rock',('scissors',))
    paper = Roll('paper',('rock',))
    scissors = Roll('scissors',('paper',))
    rolls = namedtuple('rolls', 'rock paper scissors')
    rolls.rock = rock
    rolls.paper = paper
    rolls.scissors = scissors
    return rolls


def get_player_name():
    name = ''
    while not name:
        name = input("Input your name: ")
    return name


def get_computer_roll(rolls):
    return random.choice((rolls.rock, rolls.paper, rolls.scissors))


def get_player_roll(rolls):
    choise = ''
    print("-"*42)
    while len(choise) == 0 or not choise.lower() in 'rps': 
        choise = input("Choose your roll: [R]ock, [P]aper or [S]cissors? ")
    if choise.lower() == "r":
        return rolls.rock
    elif choise.lower() == 'p':
        return rolls.paper
    else:
        return rolls.scissors


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
        print(f'{player1.name}({p1_roll.roll}) vs. '
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
    rolls = build_the_three_rolls()     # namedtuple of rolls(objects)
    name = get_player_name()
    player1 = Player(name)
    player2 = Player("computer")
    geme_loop(player1, player2, rolls)


if __name__ == "__main__":
    main()
