# Exercise 110: Sorted Order

# Write a program that reads integers from the user and stores them in a list. Your
# program should continue reading values until the user enters 0. Then it should display
# all of the values entered by the user (except for the 0) in ascending order, with one
# value appearing on each line. Use either the sort method or the sorted function
# to sort the list.

def sorted_order():
    numbers = []
    while True:
        line = input('Enter an integer (0 to quit): ')
        if line == '0':
            break
        numbers.append(int(line))
    return numbers


def display_sorted_order_list(numbers):
    for val in numbers:
        print(val)


# # Ascending order numbers (use the sort method)
# numbers = sorted_order()
# numbers.sort()  # use the sort method
# display_sorted_order_list(numbers)

# Ascending order numbers (use the sorted function)
numbers = sorted_order()
sorted_numbers = sorted(numbers)
display_sorted_order_list(sorted_numbers)
