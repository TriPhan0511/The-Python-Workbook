# ======= WHILE LOOPS =======
# while True:
#     num = int(input('Enter an integer (0 to quit): '))
#     if num < 0:
#         print("That's a negative number.")
#     elif num > 0:
#         print("That's a positive number.")
#     else:
#         break

# num = int(input('Enter an integer (0 to quit): '))
# while num != 0:
#     if num < 0:
#         print("That's a negative number.")
#     else:
#         print("That's a positive number.")
#     num = int(input('Enter an integer (0 to quit): '))


# ======= FOR LOOPS =======
# for num in range(0, -4, -1):
#     print(num)
# # -> 0 -1 -2 -3

# limit = int(input('Enter an integer: '))
# print(f'The multiples of 3 up to and including {limit} are:')
# for num in range(3, limit + 1, 3):
#     print(num)

# ======= NESTED LOOPS =======
while True:
    message = input('Enter a message (blank to quit): ')
    if message == '':
        break
    n = int(input('How many times should it be repeated? '))
    for i in range(n):
        print(message)

# message = input('Enter a message (blank to quit): ')
# while message != '':
#     n = int(input('How many times should it be repeated? '))
#     for i in range(n):
#         print(message)
#     message = input('Enter a message (blank to quit): ')
