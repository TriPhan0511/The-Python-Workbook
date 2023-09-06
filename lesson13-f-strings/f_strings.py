# Helpful link: https://www.w3schools.com/python/ref_string_format.asp#:~:text=Definition%20and%20Usage,method%20returns%20the%20formatted%20string.

# person = 'Dave'
# coins = 3

# print('\n' + person + ' has ' + str(coins) + ' coins left.')

# message = '\n%s has %s coins left.' % (person, coins)
# print(message)

# message = '\n{} has {} coins left.'.format(person, coins)
# print(message)

# message = '\n{1} has {0} coins left.'.format(coins, person)
# print(message)

# message = '\n{person} has {coins} coins left.'.format(
#     coins=coins, person=person)
# print(message)

# player = {'person': 'Dave', 'coins': 3}
# message = '\n{person} has {coins} coins left.'.format(**player)
# print(message)

# ======= f-String! This is the way. =======
# person = ' Dave'
# coins = 3

# message = f'\n{person} has {coins} coins left.'
# print(message)

# message = f'\n{person} has {2 * 5} coins left.'
# print(message)

# message = f'\n{person.lower()} has {2 * 5} coins left.'
# print(message)

# player = {'person': 'Dave', 'coins': 3}
# message = f'\n{player["person"]} has {player["coins"]} coins left.'
# print(message)

# ======= You can pass formatting options. =======
# num = 10
# print(f'\n2.25 time {num} is {2.25 * num:.2f}')  # 2.25 time 10 is 22.50

# for num in range(1, 11):
#     print(f'2.25 times {num} is {2.25 * num:.2f}')

for num in range(1, 11):
    print(f'{num} divided by 4.52 is {num / 4.52:.2f}')
    print(f'{num} divided by 4.52 is {num / 4.52:.2%}')
# 1 divided by 4.52 is 0.22
# 1 divided by 4.52 is 22.12%
