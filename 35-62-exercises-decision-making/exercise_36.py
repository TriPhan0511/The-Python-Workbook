##
# Indicate dog years.
#

def format_number(num):
    num_str = str(num)
    i = num_str.find('.')
    if i != -1 and num_str[i + 1] == '0':
        num_str = num_str[:i]
        return int(num_str)
    return num


def dog_year():
    num = int(input('Enter a human year(s): '))
    if num < 0:
        result = 'Please enter a postive number.'
    elif num <= 2:
        result = f'{format_number(num * 10.5)} dog year(s).'
    else:
        result = f'{format_number(2 * 10.5 + (num - 2) * 4)} dog years.'
    print(result)


# Run the program
dog_year()


# Test
# num = -1 # Please enter a postive number.
# num = 0 # 0 dog year(s).
# num = 1 # 10.5 dog year(s)
# num = 2 # 21 dog year(s)
# num = 3 # 25 dog year(s)
# num = 4 # 29 dog year(s)
# num = 10 # 53 dog year(s)
