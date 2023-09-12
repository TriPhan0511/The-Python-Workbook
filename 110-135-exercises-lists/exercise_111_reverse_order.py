def get_numbers():
    numbers = []
    while True:
        line = input('Enter an integer (0 to quit): ')
        if line.strip() == '0':
            break
        numbers.append(int(line))
    return numbers


def display_numbers(numbers):
    if not isinstance(numbers, list):
        print(numbers)
    else:
        for val in numbers:
            print(val)


numbers = get_numbers()
numbers.reverse()
print('\nNumbers in reverse order:')
display_numbers(numbers)
