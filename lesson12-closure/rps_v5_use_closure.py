##
# Implement the game Rock Paper Scissors.
#

import sys
import random
from enum import Enum


def rps():
    # Declare some variables
    game_count = 0
    player_wins = 0
    python_wins = 0

    # Define a function that implement the game
    def play_rps():
        nonlocal player_wins
        nonlocal python_wins

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
        print(
            f"Python chose {str(RPS(computer)).replace('RPS.', '').title()}.\n")

        # Define a nested function that decides winner
        def decide_winner(player, computer):
            nonlocal player_wins
            nonlocal python_wins
            if player == 1 and computer == 3:
                player_wins += 1
                return '🎉 You win!'
            elif player == 2 and computer == 1:
                player_wins += 1
                return '🎉 You win!'
            elif player == 3 and computer == 2:
                player_wins += 1
                return '🎉 You win!'
            elif player == computer:
                return '😲 Tie game!'
            else:
                python_wins += 1
                return '🐍 Python win!'

        # Display the result
        result = decide_winner(player, computer)
        print(result)

        nonlocal game_count
        game_count += 1
        print(f'\nGame count: {game_count}')
        print(f'\nPlayer wins: {player_wins}')
        print(f'\nPython wins: {python_wins}')

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

    return play_rps


# Call the play_rps() function
play = rps()
play()
