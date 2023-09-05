# Closure is a function having to access to the scope of its parent
# function after the parent function has returned

# def parent_function(person):
#     coins = 3

#     def play_game():
#         nonlocal coins
#         coins -= 1

#         if coins > 1:
#             print(f'\n{person} has {coins} coins left.')
#         elif coins == 1:
#             print(f'\n{person} has {coins} coin left.')
#         else:
#             print(f'\n{person} is out of coins.')

#     return play_game


# tommy = parent_function('Tommy')
# jenny = parent_function('Jenny')

# tommy()  # Tommy has 2 coins left.
# tommy()  # Tommy has 1 coin left.

# jenny()  # Jenny has 2 coins left.

# tommy()  # Tommy is out of coins.
# -------------------------------------------------------------------------

def parent_function(person, coins):

    def play_game():
        nonlocal coins
        coins -= 1

        if coins > 1:
            print(f'\n{person} has {coins} coins left.')
        elif coins == 1:
            print(f'\n{person} has {coins} coin left.')
        else:
            print(f'\n{person} is out of coins.')

    return play_game


tommy = parent_function('Tommy', 3)
jenny = parent_function('Jenny', 5)

tommy()  # Tommy has 2 coins left.
tommy()  # Tommy has 1 coin left.

jenny()  # Jenny has 4 coins left.

tommy()  # Tommy is out of coins.
