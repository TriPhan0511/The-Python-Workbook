import sys
import random
from enum import Enum


def play_game():

    # Define a class that extends the Enum class
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    # Get input from user (use a while loop)
    while True:
        player_choice = input(
            '\nEnter... \n1 for Rock, \n2 for Paper, \n3 for Scissors.\n\n')
        if player_choice not in ['1', '2', '3']:
            print('\nYou must enter 1, 2, or 3.')
            continue
        else:
            break
    player = int(player_choice)

    # # Get input from user (use recursion)
    # player_choice = input(
    #     '\nEnter... \n1 for Rock, \n2 for Paper, \n3 for Scissors.\n\n')
    # if player_choice not in ['1', '2', '3']:
    #     print('\nYou must enter 1, 2, or 3.')
    #     return play_game()
    # player = int(player_choice)

    # Generate 1 random choice
    computer = int(random.choice('123'))

    # Display the two choices
    print(f"\nYou chose {str(RPS(player)).replace('RPS.', '').title()}")
    print(f"Python chose {str(RPS(computer)).replace('RPS.', '').title()}\n")

    # Game logic
    if player == computer:
        print('😲 Tie game!')
    elif (player == 1 and computer == 3) or (player == 2 and computer == 1) or (player == 3 and computer == 2):
        print('🎉 You won!')
    else:
        print('🐍 Python won!')

    # Play again? (use recursion)
    print('\nPlay again?')
    while True:
        play_again = input('\nY for Yes or \nQ for Quit\n\n').lower()
        if play_again not in ['y', 'q']:
            continue
        else:
            break
    if play_again == 'y':
        return play_game()
    else:
        print('\n🎉🎉🎉🎉🎉 ')
        print('Thank you for playing!\n')

        sys.exit('Bye! 👋')


# Run the program
play_game()
