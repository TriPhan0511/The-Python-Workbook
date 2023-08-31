##
# Compute the area of a room.
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
def compute_area_in_meters():
    # Read the dimensions from the user
    length = float(input('Enter the length of the room in meters: '))
    width = float(input('Enter the width of the room in meters: '))
    # Compute the area of the room and return the result
    return length * width


# Run the program
area = compute_area_in_meters()
print(f'The area of the room is {format_float(area)} square meter')
