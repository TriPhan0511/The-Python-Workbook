# # Exercise 114: Negatives,Zeros and Positives

# Create a program that reads integers from the user until a blank line is entered. Once
# all of the integers have been read your program should display all of the negative
# numbers, followed by all of the zeros, followed by all of the positive numbers.Within
# each group the numbers should be displayed in the same order that they were entered
# by the user. For example, if the user enters the values 3, -4, 1, 0, -1, 0, and -2 then
# your program should output the values -4, -1, -2, 0, 0, 3, and 1. Your program
# should display each value on its own line.

def categorize_numbers():
    negatives = []
    zeros = []
    positives = []
    while True:
        line = input('Enter a number (blank line to quit): ')
        if not line.strip():
            break
        number = int(line)
        if number < 0:
            negatives.append(number)
        elif number == 0:
            zeros.append(number)
        else:
            positives.append(number)
    return negatives + zeros + positives


def display_data(data):
    if len(data) == 0:
        print('Empty data')
    else:
        for item in data:
            print(item)


def main():
    data = categorize_numbers()
    display_data(data)


if __name__ == '__main__':
    main()
