##
# Exercise 151: Concatenate Multiple Files
# Unix-based operating systems typically include a tool named cat, which is short for
# concatenate. Its purpose is to display the concatenation of one or more files whose
# names are provided as command line arguments. The files are displayed in the same
# order that they appear on the command line.
# Create a Python program that performs this task. It should generate an appropriate
# error message for any file that cannot be displayed, and then proceed to the next file.
# Display an appropriate error message if your program is started without any command
# line arguments.
#

import sys


def cat(files):
    for file in files:
        try:
            fhand = open(file)
            for line in fhand:
                print(line.strip())
            fhand.close()
        except:
            print(f'\n*** File cannot be opened: {file} ***\n')


def main():
    args = sys.argv
    if len(args) == 1:
        print('You must provide at least one file name.')
        exit()
    cat(args[1:])


if __name__ == '__main__':
    main()
