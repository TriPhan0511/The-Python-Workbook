import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


def play_game():
    while True:
        player_choice = input(
            '\nEnter... \n1 for Rock,\n2 for Paper,\n3 for Scissors:\n\n')
        player = int(player_choice)

        if player < 1 or player > 3:
            sys.exit('You must enter 1, 2, or 3.')

        computer_choice = random.choice('123')
        computer = int(computer_choice)

        print(f"\nYou chose {str(RPS(player)).replace('RPS.', '')}.")
        print(f"Python chose {str(RPS(computer)).replace('RPS.', '')}.\n")

        if player == 1 and computer == 3:
            print('🎉 You win!')
        elif player == 2 and computer == 1:
            print('🎉 You win!')
        elif player == 3 and computer == 2:
            print('🎉 You win!')
        elif player == computer:
            print('😲 Tie game!')
        else:
            print('🐍 Python win!')

        play_again = input('\nPlay again? \nY for Yes or \nQ to Quit  \n\n')
        if play_again.lower() == 'y':
            continue
        else:
            print('\n🎉🎉🎉🎉🎉 ')
            print('Thank you for playing!\n')
            break
    print('Bye! 👋')


# Run the program
play_game()
