##
# Implement the game Rock Paper Scissors.
#

import sys
import random
from enum import Enum


def play_rps():

    # Define a class that extends the Enum class
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    # Get input from the user
    player_choice = input(
        '\nEnter... \n1 for Rock,\n2 for Paper,\n3 for Scissors:\n\n')
    if player_choice not in ['1', '2', '3']:
        print('You must enter 1, 2, or 3.')
        return play_rps()
    player = int(player_choice)

    # Generate a random choice
    computer_choice = random.choice('123')
    computer = int(computer_choice)

    # Display the choices
    print(f"\nYou chose {str(RPS(player)).replace('RPS.', '').title()}.")
    print(f"Python chose {str(RPS(computer)).replace('RPS.', '').title()}.\n")

    # Game logic
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

    # Play again?
    print('\nPlay again?')
    while True:
        play_again = input('\nY for Yes or \nQ to Quit\n')
        if play_again.lower() not in ['y', 'q']:
            continue
        else:
            break
    if play_again.lower() == 'y':
        return play_rps()
        # play_rps()
    else:
        print('\n🎉🎉🎉🎉🎉 ')
        print('Thank you for playing!\n')
        sys.exit('Bye! 👋')


# Call the play_rps() function
play_rps()
