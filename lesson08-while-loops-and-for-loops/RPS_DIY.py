import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSOR = 3


def convert_to_rps(num):
    return str(RPS(num)).replace('RPS.', '')


def get_choice(msg, error_msg):
    while True:
        choice = int(input(msg))
        if choice < 0 or choice > 3:
            print(error_msg)
            continue
        else:
            break
    return choice


def who_win(player, computer):
    if player == computer:
        result = 'Tie game!'
    elif (player == 1 and computer == 3) or (player == 2 and computer == 1) or (player == 3 and computer == 2):
        result = 'You won!'
    else:
        result = 'Python won!'
    return result


def play_again(msg):
    while True:
        inp = input(msg)
        if int(inp) == 0:
            break


def play_game():
    # Display introduction message
    intro_msg = '\n1 for Rock, 2 for Paper, 3 for Scissor.\nPress 0 to quit the game.\nGAME START\n'
    print(intro_msg)
    player = 5
    while player != 0:
        # Get choice from the player
        player = get_choice('Enter your choice: ',
                            'Please enter 1 or 2 or 3 or press 0 to quit the game.')
        if player == 0:
            print('Quiting...')
            break
        # Generate a random choice
        computer = int(random.choice('123'))
        # Display the result
        print(
            f'You chose {convert_to_rps(player)} and Python chose {convert_to_rps(computer)}.')
        print(who_win(player, computer))
        print('Press any number to play again. Press 0 to quit the game.')


# Run the program
play_game()
