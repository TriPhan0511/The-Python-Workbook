##
# Determine and display whether an integer entered by the user is even or odd.
#

def even_or_odd():
    num = int(input('Enter a number: '))
    if num % 2 == 0:
        print(f'{num} is even.')
    else:
        print(f'{num} is odd.')


# Run the program
even_or_odd()
