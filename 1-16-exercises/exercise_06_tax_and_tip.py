##
# Compute tax and tip
#

def format_amount(amt):
    return f'${amt:.2f}'


def get_cost_and_compute_amounts(cost):
    TAX_RATE = 0.05
    TIP_RATE = 0.18
    tax = cost * TAX_RATE
    tip = cost * TIP_RATE
    total = cost + tax + tip
    return (tax, tip, total)


def compute_and_display():
    cost = float(input('Enter the cost of the meal: $'))
    amounts = get_cost_and_compute_amounts(cost)
    print(
        f'The tax is {format_amount(amounts[0])} and the tip is {format_amount(amounts[1])}, making the total {format_amount(amounts[2])}.')


# Run the program
compute_and_display()
