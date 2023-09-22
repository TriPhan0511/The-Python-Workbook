##
# Unix-based operating systems also typically include a tool named tail. It displays
# the last 10 lines of a file whose name is provided as a command line argument.
# Write a Python program that provides the same behaviour. Display an appropriate
# error message if the file requested by the user does not exist, or if the command line
# argument is omitted.

# There are several different approaches that can be taken to solve this problem.
# One option is to load the entire contents of the file into a list and then display its
# last 10 elements. Another option is to read the contents of the file twice, once to
# count the lines, and a second time to display its last 10 lines. However, both of these
# solutions are undesirable when working with large files. Another solution exists that
# only requires you to read the file once, and only requires you to store 10 lines from
# the file at one time. For an added challenge, develop such a solution.
#

import sys

MAX_LINES = 10


def tail(file_name, max_lines):
    try:
        fhand = open(file_name)
    except:
        print(f'File cannot be opened: {file_name}')
        exit()

    # # Option 1:
    # # Load the entire contents of the file into a list
    # # and then display its last 10 elements
    # lines = fhand.readlines()
    # lines = lines[-1 - max_lines: -1]
    # for line in lines:
    #     print(line.strip())

    # Option 2:
    # Read the file once,
    # and only requires you to store 10 lines from the file at one time
    lines = []
    for line in fhand:
        lines.append(line.strip())
        if len(lines) > max_lines:
            lines.pop(0)
    # Display the last lines of the file
    for line in lines:
        print(line)

    fhand.close()


def main():
    args = sys.argv
    # Verify that exactly one command line argument (in addition to the .py file) was provided
    if len(args) != 2:
        print('Please provide the file name as a command line argument.')
        exit()
    tail(args[1], MAX_LINES)

    # # Test
    # tail('ex149.txt', MAX_LINES)


if __name__ == '__main__':
    main()
