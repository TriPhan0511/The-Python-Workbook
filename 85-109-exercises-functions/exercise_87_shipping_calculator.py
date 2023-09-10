##
# An online retailer provides express shipping for many of its items at a rate of $10.95
# for the first item in an order, and $2.95 for each subsequent item in the same order.
# Write a function that takes the number of items in the order as its only parameter.
# Return the shipping charge for the order as the function’s result. Include a main
# program that reads the number of items purchased from the user and displays the
# shipping charge.
#

FIRST_ITEM_CHARGE = 10.95
SUBSEQUENT_ITEM_CHARGE = 2.95


def compute_shipping_charge(items):
    if items == 1:
        return FIRST_ITEM_CHARGE
    else:
        sum = 0
        for i in range(items - 1):
            sum += SUBSEQUENT_ITEM_CHARGE
        return 10.95 + sum


def main():
    items = int(input('\nEnter the number of items in the order: '))
    print(f'\nShipping charge: ${compute_shipping_charge(items)}')


if __name__ == '__main__':
    main()
