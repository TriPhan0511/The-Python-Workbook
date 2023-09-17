from functools import reduce
import sys

# ======= Opening a file =======

# inf = open('input.txt', 'r')


# ======= Reading input from a file =======

# # Read the file name from the user and open the file
# # fname = input('\nEnter the file name:\n')
# fname = 'numbers.txt'
# inf = open(fname, 'r')

# # Initialize the total
# total = 0

# # Total the values in the file
# line = inf.readline()
# while line != '':
#     total += float(line)
#     line = inf.readline()

# # Close the file
# inf.close()

# # Display the result
# print(f'The total of the values in {fname} is {total}')

# --------------------------------------

# The following program uses readlines to compute the sum of all
# of the numbers in a file. It reads all of the data from the file at once
# instead of adding each number to the total as it is read.

# fname = 'numbers.txt'
# fhand = open(fname)
# numbers = fhand.readlines()
# total = reduce(lambda acc, cur: float(acc) + float(cur), numbers)
# print(f'The total of the values in {fname} is {total}')

# ======= End of line characters =======

# The following example uses the readline method to read and display all of the
# lines in a file. Each line is preceded by its line number and a colon when it is printed.

# fname = 'numbers.txt'
# inf = open(fname)
# line = inf.readline()
# num = 1
# while line != '':
#     print(f'{num}: {line.rstrip()}')
#     num += 1
#     line = inf.readline()
# inf.close

# ======= Writing output to a file =======

# The following program writes the numbers from 1 up to (and including) a number
# entered by the user to a file. String concatenation and the \n escape sequence are
# used so that each number is written on its own line.

# # Read the file name from the user and open the file
# fname = input('\nWhere will the numbers be stored?\n')
# inf = open(fname, 'w')

# # Read the maximum value that be written
# number = int(input('\nWhat is the maximum value?\n'))

# # Write the numbers to the file
# s = ''
# for i in range(1, number + 1):
#     s += f'{i}\n'
# inf.write(s)
# inf = open('output.txt', 'w')

# # Close the file
# inf.close()
# print('\nDone!')

# ======= Command line arguments =======

# Any command line arguments provided when the programwas executed are stored
# into a variable named argv (argument vector) that resides in the sys (system)
# module. This variable is a list, and each element in the list is a string. Elements in
# the list can be converted to other types by calling the appropriate type conversion
# functions like int and float. The first element in the argument vector is the name
# of the Python source file that is being executed. The subsequent elements in the list
# are the values provided on the command line after the name of the Python file (if
# any).

# The following program demonstrates accessing the argument vector. It begins
# by reporting the number of command line arguments provided to the program and
# the name of the source file that is being executed. Then it goes on and displays the
# arguments that appear after the name of the source file if such values were provided.
# Otherwise a message is displayed that indicates that there were no command line
# arguments beyond the .py file being executed.

# args = sys.argv
# number_of_args = len(args)
# if number_of_args == 1:
#     print(
#         f'\nThere were no command line arguments beyond the "{args[0]}" file being executed.')
# else:
#     if number_of_args == 2:
#         singular_or_plural = 'argument'
#         intro = 'The argument is'
#     else:
#         singular_or_plural = 'arguments'
#         intro = 'The arguments are'

#     print(
#         f'\nThere were {number_of_args - 1} command line {singular_or_plural} provided to the program.')
#     print(f'The source file name is {args[0]}.')
#     print(f'{intro} {reduce(lambda acc, cur: f"{acc}, {cur}", args[1:])}.')

# ---------------------------------------------------------

# Command line arguments can be used to supply any input values to the program
# that can be typed on the command line, such as integers, floating-point numbers and
# strings. These values can then be used just like any other values in the program. For
# example, the following lines of code are a revised version of our program that sums
# all of the numbers in a file. In this version of the program the name of the file is
# provided as a command line argument instead of being read from the keyboard.

# def sum_numbers_from_a_file(file_name):
#     try:
#         fhand = open(file_name)  # Open the file
#         total = 0
#         count = 0
#         for line in fhand:
#             try:
#                 total += float(line)
#                 count += 1
#             except ValueError:
#                 pass
#         if count == 0:
#             print('There is no any number in the file.')
#             total = None
#         fhand.close()  # Close the file
#         return total
#     except FileNotFoundError:
#         print('File not found!')
#         return


# def main():
#     args = sys.argv
#     if len(args) != 2:
#         print('A file name must be provided as a command line argument.')
#         return
#     result = sum_numbers_from_a_file(args[1])
#     if result != None:
#         print(result)


# if __name__ == '__main__':
#     main()

# ======= Exceptions =======


# while True:
#     file_name = input('\nEnter the file name:\n')
#     try:
#         fhand = open(file_name)
#         for line in fhand:
#             print(line.rstrip())
#         break
#     except FileNotFoundError:
#         print(f'\n{file_name} could not be opened. Please try again!')
#         continue


