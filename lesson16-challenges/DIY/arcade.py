import sys
import rps_v8
import guess_number


def arcade(name='Player'):
    print(f'\n{name}, welcome to the Arcade! 🤖')

    def choose_game():
        msg1 = '\n\nPlease choose a game:\n1 = Rock Paper Scissors\n2 = Guess My Number'
        msg2 = '\n\nOr press "x" to exit the Arcade.\n'
        player_choice = input(f'{msg1}{msg2}\n')
        player_choice = player_choice.lower()
        if player_choice not in ['1', '2', 'x']:
            print(f'\n{name}, please enter 1, 2, or x.')
            return choose_game()
        elif player_choice == 'x':
            sys.exit(f'\nSee you next time!\n\nBye Dave! 👋')
        elif player_choice == '1':
            rps = rps_v8.rps(name)
            rps()
        else:
            guess_number_game = guess_number.guess_number(name)
            guess_number_game()

        print(f'\n{name}, welcome back to the Arcade menu.')
        return choose_game()

    return choose_game


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description='Provides personalized game experience.')
    parser.add_argument('-n', '--name', metavar='name')
    args = parser.parse_args()

    if not args.name:
        game = arcade()
    else:
        game = arcade(args.name)

    game()
