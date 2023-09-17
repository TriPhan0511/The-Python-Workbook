##
# Unix-based operating systems usually include a tool named head. It displays the
# first 10 lines of a file whose name is provided as a command line argument. Write
# a Python program that provides the same behaviour. Display an appropriate error
# message if the file requested by the user does not exist, or if the command line
# argument is omitted.
#

import sys

NUM_LINES = 5


def display_the_head_of_a_file(file_name):
    try:
        fhand = open(file_name)
        result = ''
        for i in range(NUM_LINES):
            result += fhand.readline()
        return result
    except FileNotFoundError:
        print('\nFile cannot be found.')


def main():
    args = sys.argv
    if len(args) != 2:
        print('\nA file name must be provided!')
    else:
        result = display_the_head_of_a_file(args[1])
        if result != None:
            if len(result) == 0:
                print(f'\nThe file "{args[1]}" is empty')
            else:
                print(result)


if __name__ == '__main__':
    main()


# Test:

# Case 1:
# $ py exercise_149_display_the_head_of_a_file.py
# -> A file name must be provided!

# Case 2:
# $ py exercise_149_display_the_head_of_a_file.py abnc
# -> File cannot be found.

# Case 3
# $ py exercise_149_display_the_head_of_a_file.py empty_file.txt
# ->The file "empty_file.txt" is empty

# Case 4:
# $ py exercise_149_display_the_head_of_a_file.py ex149.txt
# ->
# Line one
# Line two
# Line three
# Line four
# Line five
# Line six
# Line seven
# Line eight
# Line nine
# Line ten
