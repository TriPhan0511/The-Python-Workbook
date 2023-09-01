# ======= IF STATEMENTS =======
# num = float(input('Enter a number: '))
# if num == 0:
#     result = 'The number was zero.'
# if num != 0:
#     result = 'The number was not zero'
# print(result)

# ======= IF-ELSE STATEMENTS =======
# num = float(input('Enter a number: '))
# if num == 0:
#     result = 'The number was zero.'
# else:
#     result = 'The number was not zero.'
# print(result)

# ======= IF-ELIF-ELSE STATEMENTS =======
# num = float(input('Enter a number: '))
# if num == 0:
#     result = 'The number was zero'
# elif num > 0:
#     result = 'The number was a positive number'
# else:
#     result = 'The number was a negative number'
# print(result)

# ======= NESTED IF STATEMENTS =======
# num = float(input('Enter a number: '))

# if num > 0:
#     adjective = ' '
#     if num >= 1000000:
#         adjective = ' really big '
#     elif num >= 1000:
#         adjective = ' big '
#     result = f'That\'s a{adjective}postive number'
# elif num < 0:
#     result = 'That\'s a negative number'
# elif num == 0:
#     result = 'That\'s zero'

# print(result)

# ======= BOOLEAN LOGIC =======
x = int(input('Enter a number: '))
if x == 2 or x == 3 or x == 5 or x == 7 or x == 11:
    print('That\'s one of the first primes.')
else:
    print('That is not one of the first primes.')
