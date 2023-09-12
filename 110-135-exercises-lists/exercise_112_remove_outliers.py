# # Exercise 112:Remove Outliers

# Remove the outliers from a data set.

# When analysing data collected as part of a science experiment it may be desirable
# to remove the most extreme values before performing other calculations. Write a
# function that takes a list of values and an non-negative integer, n, as its parameters.
# The function should create a new copy of the list with the n largest elements and the
# n smallest elements removed. Then it should return the new copy of the list as the
# function’s only result. The order of the elements in the returned list does not have to
# match the order of the elements in the original list.

# Write a main program that demonstrates your function. It should read a list of
# numbers from the user and remove the two largest and two smallest values from it by
# calling the function described previously. Display the list with the outliers removed,
# followed by the original list. Your program should generate an appropriate error
# message if the user enters less than 4 values.

def remove_outliers(data, num_outliers=1):
    if not isinstance(data, list):
        print('Please enter values of a list.')
        return
    if len(data) < num_outliers * 2:
        print(f'Please enter at least {num_outliers * 2} values.')
        return

    # Create a copied list
    new_list = data[:]
    # Sort the new list in ascending order
    new_list.sort()
    # Trim n largest elements and n smallest elements and return the result
    return new_list[num_outliers:-num_outliers]


def main():
    # Get values for a list from user
    numbers = []
    while True:
        line = input('\nEnter a number (blank line to quit): ')
        if not line.strip():
            break
        numbers.append(int(line))

    # Get how many elements does user want to trim
    n = int(input('\nHow many elements do you want to trim? '))

    result = remove_outliers(numbers, n)
    if result == None:
        return main()
    print(f'\nList after trimmed: {result}')
    print(f'\nOriginal list: {numbers}')


if __name__ == '__main__':
    main()
