##
# Write a function that takes the lengths of the two shorter sides of a right triangle as
# its parameters. Return the hypotenuse of the triangle, computed using Pythagorean
# theorem, as the function’s result. Include a main program that reads the lengths of
# the shorter sides of a right triangle from the user, uses your function to compute the
# length of the hypotenuse, and displays the result.
#
import math


def compute_hypotenuse(length_one, length_two):
    return math.sqrt(length_one * length_one + length_two * length_two)


def main():
    length_one = float(input('\nEnter length one: '))
    length_two = float(input('\nEnter length two: '))
    print(f'Hypotenuse: {compute_hypotenuse(length_one, length_two):.2f}')


if __name__ == '__main__':
    main()
