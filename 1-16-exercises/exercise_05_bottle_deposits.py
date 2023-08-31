##
# Compute the refund amount for a collection of bottles.
#

def compute_refund():
    LESS_DEPOSIT = 0.1
    MORE_DEPOSIT = 0.25
    less = int(input('How many containers 1 litre or less? '))
    more = int(input('How many containers more than 1 litre? '))
    return less * LESS_DEPOSIT + more * MORE_DEPOSIT


# Run the program
refund_amount = compute_refund()
print(f'Your total refund will be ${refund_amount:.2f} refund.')
