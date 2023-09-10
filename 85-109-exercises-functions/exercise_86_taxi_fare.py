##
# In a particular jurisdiction, taxi fares consist of a base fare of $4.00, plus $0.25
# for every 140 meters travelled. Write a function that takes the distance travelled (in
# kilometers) as its only parameter and returns the total fare as its only result. Write a
# main program that demonstrates the function.
#
# Hint: Taxi fares change over time. Use constants to represent the base fare and
# the variable portion of the fare so that the program can be updated easily when
# the rates increase.
#

BASE_FARE = 4
MONEY = 0.25
METTERS = 140


def compute_fare(distance):
    return BASE_FARE + MONEY * (distance * 1000 / METTERS)


def main():
    distance = float(input('\nEnter the distance travelled (in kilometers): '))
    print(f'\nFare: ${compute_fare(distance):.2f}')


if __name__ == '__main__':
    main()
