##
# Implement the game Rock Paper Scissors.
#

import sys
import random
from enum import Enum

game_count = 0  # Declare a global variable that used to count how many times the game was played


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

    # Define a nested function that decides winner
    def decide_winner(player, computer):
        # Game logic
        if player == 1 and computer == 3:
            return '🎉 You win!'
        elif player == 2 and computer == 1:
            return '🎉 You win!'
        elif player == 3 and computer == 2:
            return '🎉 You win!'
        elif player == computer:
            return '😲 Tie game!'
        else:
            return '🐍 Python win!'

    # Display the result
    print(decide_winner(player, computer))

    # Count how many times the game was played and display it.
    global game_count  # This line makes the global variable named "game_count" can be modified
    game_count += 1
    print(f'\nGame count: {game_count}')

    # Play again?
    print('\nPlay again?')
    while True:
        play_again = input('\nY for Yes or \nQ to Quit\n')
        play_again = play_again.lower()
        if play_again not in ['y', 'q']:
            continue
        else:
            break
    if play_again == 'y':
        return play_rps()
    else:
        print('\n🎉🎉🎉🎉🎉 ')
        print('Thank you for playing!\n')
        sys.exit('Bye! 👋')


# Call the play_rps() function
play_rps()
