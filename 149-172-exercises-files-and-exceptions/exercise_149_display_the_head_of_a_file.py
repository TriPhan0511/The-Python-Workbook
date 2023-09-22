##
# Unix-based operating systems usually include a tool named head. It displays the
# first 10 lines of a file whose name is provided as a command line argument. Write
# a Python program that provides the same behaviour. Display an appropriate error
# message if the file requested by the user does not exist, or if the command line
# argument is omitted.
#

import sys

MAX_LINES = 10


def head(file_name, max_lines):
    try:
        fhand = open(file_name)
    except:
        print(f'File cannot be opened: {file_name}')
        exit()

    count = 0
    for line in fhand:
        if count == max_lines:
            break
        print(line.strip())
        count += 1
    fhand.close()


def main():
    args = sys.argv
    # Verify that exactly one command line argument (in addition to the .py file) was provided
    if len(args) != 2:
        print('Please provide the file name as a command line argument.')
        exit()
    head(args[1], MAX_LINES)


if __name__ == '__main__':
    main()
