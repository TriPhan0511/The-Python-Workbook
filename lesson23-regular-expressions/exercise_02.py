import os
import re

# #
# Exercise 2: Write a program to look for lines of the form:

# New Revision: 39772

# Extract the number from each of the lines using a regular expression
# and the findall() method. Compute the average of the numbers and
# print out the average as an integer.

# Enter file:mbox.txt
# 38549

# Enter file:mbox-short.txt
# 39756
#


def get_full_path(file_name):
    return f'{os.path.dirname(__file__)}/{file_name}'


def compute_avg(file_name):
    try:
        fhand = open(get_full_path(file_name))
    except FileNotFoundError:
        print(f'File can not be found: {file_name}')
        exit()
    total = 0
    count = 0
    for line in fhand:
        pattern = 'New Revision: ([0-9]+)$'
        lst = re.findall(pattern, line)
        if len(lst) > 0:
            total += int(lst[0])
            count += 1
    return int(total / count)


def main():
    # file_name = 'mbox-short.txt'
    # file_name = 'mbox.txt'
    file_name = input('Enter file: ')
    print(compute_avg(file_name))


if __name__ == '__main__':
    main()
