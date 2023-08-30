import sys
import random


def choice(inp):
    if inp == 1:
        return 'Rock'
    if inp == 2:
        return 'Paper'
    if inp == 3:
        return 'Scissors'


def who_win(player_one_name, player_one_choice, player_two_name, player_two_choice):
    if player_one_choice == player_two_choice:
        return 'Draw!'
    else:
        if (player_one_choice == 1 and player_two_choice == 2) or (player_one_choice == 2 and player_two_choice == 3) or (player_one_choice == 3 and player_two_choice == 1):
            return f'{player_two_name} won!'
        else:
            return f'{player_one_name} won!'


def play_game_with_computer():
    player_one_name = 'You'
    player_two_name = 'Python'
    print('\n')
    print('GAME START')
    print('\n\n')
    player_one_choice_str = input(
        'Enter...\n1 for Rock, \n2 for Paper, or \n3 for Scissors:\n\n')
    player_one_choice = int(player_one_choice_str)
    if player_one_choice < 1 or player_one_choice > 3:
        sys.exit('You must enter 1, 2, or 3')
    player_two_choice_str = random.choice('123')
    player_two_choice = int(player_two_choice_str)
    print(f'{player_one_name} chose {choice(player_one_choice)}({player_one_choice}).')
    print(f'{player_two_name} chose {choice(player_two_choice)}({player_two_choice}).')
    return who_win('You', player_one_choice, 'Python', player_two_choice)


# Play game
print('\n')
print(play_game_with_computer())
