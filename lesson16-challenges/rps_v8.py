##
# Implement the game Rock Paper Scissors.
#

import sys
import random
from enum import Enum


def rps(name='PlayerOne'):
    # Declare some variables
    game_count = 0
    player_wins = 0
    python_wins = 0

    # Define a function that implement the game
    def play_rps():
        # nonlocal name
        # nonlocal player_wins
        # nonlocal python_wins

        # Define a class that extends the Enum class
        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        # Get input from the user
        player_choice = input(
            f'\n{name}, please enter... \n1 for Rock,\n2 for Paper,\n3 for Scissors:\n\n')
        if player_choice not in ['1', '2', '3']:
            print(f'{name}, please enter 1, 2, or 3.')
            return play_rps()
        player = int(player_choice)

        # Generate a random choice
        computer_choice = random.choice('123')
        computer = int(computer_choice)

        # Display the choices
        print(f"\n{name} chose {str(RPS(player)).replace('RPS.', '').title()}.")
        print(
            f"Python chose {str(RPS(computer)).replace('RPS.', '').title()}.\n")

        # Define a nested function that decides winner
        def decide_winner(player, computer):
            # nonlocal name
            nonlocal player_wins
            nonlocal python_wins

            if player == 1 and computer == 3:
                player_wins += 1
                return f'🎉 {name}, you win!'
            elif player == 2 and computer == 1:
                player_wins += 1
                return f'🎉 {name}, you win!'
            elif player == 3 and computer == 2:
                player_wins += 1
                return f'🎉 {name}, you win!'
            elif player == computer:
                return '😲 Tie game!'
            else:
                python_wins += 1
                return f'🐍 Python win!\nSorry! {name}..😢'

        # Display the result
        result = decide_winner(player, computer)
        print(result)

        nonlocal game_count
        game_count += 1

        print(f'\nGame count: {game_count}')
        print(f"{name}'s wins: {player_wins}")
        print(f'\nPython wins: {python_wins}')

        # Play again?
        print(f'\nPlay again, {name}?')
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

    return play_rps


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description='Provides a personalized game experience.'
    )

    parser.add_argument(
        '-n', '--name', metavar='name',
        help='The name of the person playing the game.'
        # required=True, help='The name of the person playing the game.'
    )

    args = parser.parse_args()

    if not args.name or len(args.name.strip()) == 0:
        rock_paper_scissors = rps()
    else:
        rock_paper_scissors = rps(args.name)

    rock_paper_scissors()
