##
# Compute the area of a field.
#

# Define a function to format a floating-point number
def format_float(number):
    rounded_number = round(number, 1)
    rounded_number_str = str(rounded_number)
    period_index = rounded_number_str.index('.')
    rounded_number = round(
        number) if rounded_number_str[period_index+1:] == '0' else rounded_number
    return rounded_number


# Define a function to compute the area of a room
def compute_area_in_feet():
    # Read the dimensions from the user
    length = float(input('Enter the length of the field in feet: '))
    width = float(input('Enter the width of the field in feet: '))
    # Compute the area and return the result
    return length * width


# Define a function to convert from square feet to acre
def convert_from_square_feet_to_acre(number_in_square_feet):
    SQFT_PER_ARCE = 43560
    return number_in_square_feet / SQFT_PER_ARCE


# Run the program
area_in_square_feet = compute_area_in_feet()
area_in_arce = convert_from_square_feet_to_acre(area_in_square_feet)
print(f'The area of the field is {format_float(area_in_arce)} arce.')
