import os
import re


def get_full_path(file_name):
    return f'{os.path.dirname(__file__)}/{file_name}'


# # Search for lines that contain "From":
# file_name = 'mbox-short.txt'
# fhand = open(get_full_path(file_name))
# for line in fhand:
#     line = line.rstrip()
#     if re.search('From:', line):
#         print(line)

# -----------------------------------------------------------------

# The caret character is used in regular expressions to match "the beginning" of a line.

# Change our program to only match lines where "From:" was at beginning of the lines
file_name = 'mbox-short.txt'
fhand = open(get_full_path(file_name))
for line in fhand:
    line = line.rstrip()
    if re.search('^From:', line):
        print(line)
