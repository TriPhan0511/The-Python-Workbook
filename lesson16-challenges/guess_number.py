import random
import sys


def guess_number(name='Player'):
    # Declare some variables
    game_count = 0
    player_wins = 0
    computer_wins = 0
    player_winning_percentage = 0
    formatted_percentage = ''

    def play_game():

        # Get a choice from player
        player_choice = input(
            f'\n{name}, guess which number I\'m thinking of... 1, 2, or 3.\n\n')
        if player_choice not in ['1', '2', '3']:
            print(f'\n{name}, please enter 1, 2, or 3.')
            return play_game()
        player = int(player_choice)

        # Generate a random choice
        computer = int(random.choice('123'))

        # Display both of choices
        print(f'\n{name}, you chose {player}.')
        print(f'I was thinking about the number {computer}.')

        # Make the variables be able to be modified
        nonlocal game_count
        nonlocal player_wins
        nonlocal computer_wins
        nonlocal player_winning_percentage
        nonlocal formatted_percentage

        # Game logic
        if player == computer:
            player_wins += 1
            print(f'\n🎉 {name}, you win!')

        else:
            computer_wins += 1
            print(f'\nSorry, {name}. Better luck next time. 😢')

        # Statistics
        game_count += 1
        formatted_percentage = f'{(player_wins / game_count):.2%}'
        if formatted_percentage[-3] == '0':
            formatted_percentage = f'{formatted_percentage[:-4]}%'
        print(f'\nGame count: {game_count}')
        print(f"\n{name}'s wins: {player_wins}")
        print(f'\nYour winning percentage: {formatted_percentage}')

        # Play again
        while True:
            print(f'\nPlay again, {name}?')
            play_again = input('\nY for Yes or\nQ to Quit\n')
            play_again = play_again.lower()
            if play_again not in ['y', 'q']:
                print(f'\n{name}, please enter Y or Q.')
                continue
            elif play_again == 'y':
                return play_game()
            else:
                sys.exit(f'\n🎉🎉🎉🎉\nThank you for playing!\n\nBye {name}! 👋')

    return play_game


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description='Provides a personalized game experience.')
    parser.add_argument('-n', '--name', metavar='name',
                        help='The name of the person playing the game.')
    args = parser.parse_args()

    if not args.name:
        game = guess_number()
    else:
        game = guess_number(args.name)

    # Play game
    game()
