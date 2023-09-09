import sys
import random


def guess_number(name='PlayerOne'):
    game_count = 0
    player_wins = 0

    def play_guess_number():
        player_choice = input(
            f"\n{name}, guess which number I'm thinking of... 1, 2, or 3.\n\n")
        if player_choice not in ['1', '2', '3']:
            print(f'\n{name}, please enter 1, 2, or 3.')
            return play_guess_number()
        player = int(player_choice)

        computer = int(random.choice('123'))

        print(f'\n{name}, you chose {player}.')
        print(f'I was thinking about the number {computer}.\n')

        def decide_winner(player, computer):
            nonlocal player_wins
            if player == computer:
                player_wins += 1
                return f'🎉 {name}, you win!'
            else:
                return f'Sorry, {name}. Better luck next time.'

        print(decide_winner(player, computer))

        nonlocal game_count
        game_count += 1

        print(f'\nGame count: {game_count}')
        print(f"\n{name}'s win: {player_wins}")
        print(f'\nYour winning percentage: {player_wins / game_count: .2%}')

        # Play again
        print(f'Play again, {name}?')
        while True:
            play_again = input('\nY for Yes or \nQ to Quit\n')
            play_again = play_again.lower()
            if play_again not in ['y', 'q']:
                continue
            else:
                break

        if play_again == 'y':
            return play_guess_number()
        else:
            print('\n🎉🎉🎉🎉')
            print('Thank you for playing!\n')
            if __name__ == '__main__':
                sys.exit(f'By {name}! 👋')
            else:
                return

    return play_guess_number


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description='Provides a personalized game experience.')
    parser.add_argument('-n', '--name', metavar='name',
                        help='The name of the person playing the game.')

    args = parser.parse_args()
    if not args.name:
        guess_my_number = guess_number()
    else:
        guess_my_number = guess_number(args.name)

    # Play the game
    guess_my_number()
