# ======= WHILE LOOPS =======

# ======= WHILE LOOP WITH A BREAK STATEMENT =======
# value = 1
# while value <= 10:
#     print(value)
#     if value == 5:
#         break
#     value += 1

# ======= WHILE LOOP WITH A CONTINUE STATEMENT =======
# value = 0
# while value < 10:
#     value += 1
#     if value == 5:
#         continue
#     print(value)

# ======= WHILE LOOP WITH A ELSE STATEMENT =======
# value = 0
# while value < 10:
#     value += 1
#     if value == 5:
#         continue
#     print(value)
# else:
#     print(f'Value is now equal to {value}')

# ======= FOR LOOPS =======

# ======= LOOP THROUGH A COLLECTION =======
# names = ['Dave', 'Sara', 'John']
# for name in names:
#     print(name)

# ======= LOOP THROUGH A STRING =======
# for letter in 'Mississippi':
#     print(letter)

# ======= FOR LOOP WITH A BREAK STATEMENT =======
# names = ['Dave', 'Sara', 'John']
# for name in names:
#     if name == 'Sara':
#         break
#     print(name)

# ======= FOR LOOP WITH A CONTINUE STATEMENT =======
# names = ['Dave', 'Sara', 'John']
# for name in names:
#     if name == 'Sara':
#         continue
#     print(name)

# ======= FOR LOOP WITH A ELSE STATEMENT =======
# names = ['Dave', 'Sara', 'John']
# for name in names:
#     print(name)
# else:
#     print("Inside Else")

# ======= LOOPING THROUGH A RANGE OF NUMBERS =======
# for num in range(4):
#     print(num)

# for num in range(2, 4):
#     print(num)

# for num in range(0, 100, 5):
#     print(num)

# ======= NESTED LOOPS =======
names = ['Dave', 'Sara', 'John']
actions = ['codes', 'eats', 'sleeps']

# for name in names:
#     for action in actions:
#         print(f'{name} {action}.')

for action in actions:
    for name in names:
        print(f'{name} {action}.')