# # Exercise 137: Two Dice Simulation

# In this exercise you will simulate 1,000 rolls of two dice. Begin by writing a function
# that simulates rolling a pair of six-sided dice. Your function will not take any
# parameters. It will return the total that was rolled on two dice as its only result.
# Write a main program that uses your function to simulate rolling two six-sided
# dice 1,000 times. As your program runs, it should count the number of times that
# each total occurs. Then it should display a table that summarizes this data. Express
# the frequency for each total as a percentage of the number of rolls performed. Your
# program should also display the percentage expected by probability theory for each
# total. Sample output is shown below.

# Total   Simulated Percent   Expected Percent
#     2                3.20               2.78
#     3                6.50               5.56
#     4                9.40               8.33
#     5               10.20              11.11
#     6               13.00              13.89
#     7               15.80              16.67
#     8               13.40              13.89
#     9                9.90              11.11
#    10                8.80               8.33
#    11                7.00               5.56
#    12                2.80               2.78

from random import randrange

DICE_MAX = 6
NUM_RUNS = 1000
EXPECTED = {2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36, 6: 5/36,
            7: 6/36, 8: 5/36, 9: 4/36, 10: 3/36, 11: 2/36, 12: 1/36, }


def simulate_two_dice(d_max):
    dice_one = randrange(1, d_max + 1)
    dice_two = randrange(1, d_max + 1)
    return dice_one + dice_two


def count(times):
    data = {}
    for i in range(times):
        k = simulate_two_dice(DICE_MAX)
        if k in data:
            data[k] += 1
        else:
            data[k] = 1
    return data


def display_data(data, times):
    print(f"{'Total':8s}{'Simulated Percent':20s}{'Expected Percent'}")
    for k in sorted(data.keys()):
        print(
            f'{k:5d}{(data[k]/times * 100):20.2f}{(EXPECTED[k] * 100):19.2f}')


def main():
    display_data(count(NUM_RUNS), NUM_RUNS)


if __name__ == '__main__':
    main()
