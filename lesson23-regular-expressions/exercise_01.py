import os
import sys
import re

# Exercise 1: Write a simple program to simulate the operation of the
# grep command on Unix. Ask the user to enter a regular expression and
# count the number of lines that matched the regular expression:

# $ python grep.py
# Enter a regular expression: ^Author
# mbox.txt had 1798 lines that matched ^Author

# $ python grep.py
# Enter a regular expression: ^X-
# mbox.txt had 14368 lines that matched ^X-

# $ python grep.py
# Enter a regular expression: java$
# mbox.txt had 4175 lines that matched java$


def get_full_path(file_name):
    return f'{os.path.dirname(__file__)}/{file_name}'


# def find(file_name, pattern):
def find(pattern, file_name='mbox.txt'):
    fhand = open(get_full_path(file_name))
    count = 0
    for line in fhand:
        # line = line.rstrip() # Wrong???
        lst = re.findall(pattern, line)
        if len(lst) > 0:
            count += 1
    return count


def main():
    file_name = 'mbox.txt'
    pattern = input('Enter a regular expression: ')
    print(f'{file_name} had {find(pattern, file_name)} lines that matched {pattern}')

# def main():
#     args = sys.argv
#     if len(args) == 1:
#         pattern = input('Enter a regular expression: ')
#         print(f'{file_name} had {find(pattern)} lines that matched {pattern}')
#     elif len(args) == 2:
#         file_name = args[1]
#         print(
#             f'{file_name} had {find(pattern, file_name)} lines that matched {pattern}')
#     else:
#         print('\nYou should enter one argument')
#         exit()

#     # pattern = input('Enter a regular expression: ')
#     # print(f'{file_name} had {find(file_name, pattern)} lines that matched {pattern}')


if __name__ == '__main__':
    main()
