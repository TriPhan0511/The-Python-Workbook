# Exercise 88: Median of Three Values

# Write a function that takes three numbers as parameters, and returns the median value
# of those parameters as its result. Include a main program that reads three values from
# the user and displays their median.

# Hint: The median value is the middle of the three values when they are sorted
# into ascending order. It can be found using if statements, or with a little bit of
# mathematical creativity.

def median(a, b, c):
    if (b < a and a < c) or (b > a and a > c):
        return a
    if (a < b and b < c) or (a > b and b > c):
        return b
    return c


def main():
    while True:
        v1 = float(input('\nEnter value one:\n'))
        v2 = float(input('\nEnter value two:\n'))
        v3 = float(input('\nEnter value three:\n'))
        if v1 == v2 or v1 == v3 or v2 == v3:
            print('\nPlease enter different values.')
            continue
        else:
            break
    print(
        f'\nMedian of three values ({v1}, {v2}, {v3}): {median(v1,v2,v3)}')


if __name__ == '__main__':
    main()
