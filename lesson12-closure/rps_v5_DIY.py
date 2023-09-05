from enum import Enum
import random
import sys


def rps():
    # Define a class that extends the "Enum" class.
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    # Define some variables
    game_count = 0
    player_wins = 0
    python_wins = 0

    # Define a function that implement game

    def play_rps():
        # Define a function that decide winner
        def decide_winner(player, computer):
            nonlocal player_wins
            nonlocal python_wins
            if player == computer:
                return '😲 Tie game!'
            elif (player == 1 and computer == 3) or (player == 2 and computer == 1) or (player == 3 and computer == 1):
                player_wins += 1
                return '🎉 You win!'
            else:
                python_wins += 1
                return '🐍 Python wins!'

        # Get user's choice
        while True:
            player_choice = input(
                '\nEnter... \n1 for Rock \n2 for Paper \n3 for Scissors.\n\n')
            if player_choice not in ['1', '2', '3']:
                print('\nYou should enter 1, 2, or 3.')
                continue
            else:
                break
        player = int(player_choice)

        # Generate a random choice
        computer = int(random.choice('123'))

        # Display both of choices
        print(f"\nYou chose: {str(RPS(player)).replace('RPS.', '').title()}")
        print(
            f"\nPython chose: {str(RPS(computer)).replace('RPS.', '').title()}")

        # Display result
        print(f'\n{decide_winner(player, computer)}')

        nonlocal game_count
        game_count += 1
        print(f'\nGame count: {game_count}')
        print(f'\nPlayer wins: {player_wins}')
        print(f'\nPython wins: {python_wins}')

        # Play again
        while True:
            play_again = input(
                '\nDo you want to play again? (Y for Yes, Q for Quit):\n\n')
            play_again = play_again.lower()
            if play_again not in ['y', 'q']:
                continue
            else:
                break
        if play_again == 'y':
            return play_rps()
        else:
            print('')
            sys.exit('👋 Bye!')

    return play_rps


game = rps()
game()

# -----------------------------------------------------------------------------
# from enum import Enum
# import random
# import sys


# def rps():
#     # Define a class that extends the "Enum" class.
#     class RPS(Enum):
#         ROCK = 1
#         PAPER = 2
#         SCISSORS = 3

#     # Define some variables
#     game_count = 0
#     player_wins = 0
#     python_wins = 0

#     # Define a function that decide winner
#     def decide_winner(player, computer):
#         nonlocal player_wins
#         nonlocal python_wins
#         if player == computer:
#             return '😲 Tie game!'
#         elif (player == 1 and computer == 3) or (player == 2 and computer == 1) or (player == 3 and computer == 1):
#             player_wins += 1
#             return '🎉 You win!'
#         else:
#             python_wins += 1
#             return '🐍 Python wins!'

#     # Define a function that implement game
#     def play_rps():
#         # Get user's choice
#         while True:
#             player_choice = input(
#                 '\nEnter... \n1 for Rock \n2 for Paper \n3 for Scissors.\n\n')
#             if player_choice not in ['1', '2', '3']:
#                 print('\nYou should enter 1, 2, or 3.')
#                 continue
#             else:
#                 break
#         player = int(player_choice)

#         # Generate a random choice
#         computer = int(random.choice('123'))

#         # Display both of choices
#         print(f"\nYou chose: {str(RPS(player)).replace('RPS.', '').title()}")
#         print(
#             f"\nPython chose: {str(RPS(computer)).replace('RPS.', '').title()}")

#         # Display result
#         print(f'\n{decide_winner(player, computer)}')

#         nonlocal game_count
#         game_count += 1
#         print(f'\nGame count: {game_count}')
#         print(f'\nPlayer wins: {player_wins}')
#         print(f'\nPython wins: {python_wins}')

#         # Play again
#         while True:
#             play_again = input(
#                 '\nDo you want to play again? (Y for Yes, Q for Quit):\n\n')
#             play_again = play_again.lower()
#             if play_again not in ['y', 'q']:
#                 continue
#             else:
#                 break
#         if play_again == 'y':
#             return play_rps()
#         else:
#             print('')
#             sys.exit('👋 Bye!')

#     return play_rps


# game = rps()
# game()
