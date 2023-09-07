##
# Exercise 63:
# In this exercise you will create a program that computes the average
# of a collection of values entered by the user.
# The user will enter 0 as a sentinel value to
# indicate that no further values will be provided.
# Your program should display an appropriate error message if
# the first value entered by the user is 0.

# Hint: Because the 0 marks the end of the input it should not be included
# in the average.
#


def compute_average():
    count = 0
    total = 0
    # Make sure the user don not enter zero for the first value.
    first = 1
    while True:
        first = float(input('Enter a number: '))
        if first == 0:
            print('You should not enter zero for the first time!')
            continue
        else:
            count = 1
            total += first
            break
    # Get input from the user and compute the average
    while True:
        num = float(input('Enter a number (0 to quit): '))
        if num == 0:
            break
        else:
            count += 1
            total += num
    return round(total / count, 2)


# Run the program
print(f'Average: {compute_average()}')
