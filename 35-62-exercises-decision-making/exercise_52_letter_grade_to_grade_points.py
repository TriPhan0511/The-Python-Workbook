##
# Convert from a letter grade to a number of grade points.
#
# ----------------------------
# Letter          Grade Points
# ----------------------------
# A+              4.0
# A               4.0
# A-              3.7
# B+              3.3
# B               3.0
# B-              2.7
# C+              2.3
# C               2.0
# C-              1.7
# D+              1.3
# D               1.0
# F               0
# ----------------------------
#


# Define a dictionary that contains grade letter and gade points (used by both functions)
GRADES = {'A+': 4.0, 'A': 4.0, 'A-': 3.7, 'B+': 3.3, 'B': 3.0,
          'B-': 2.7, 'C+': 2.3, 'C': 2.0, 'C-': 1.7, 'D+': 1.3, 'D': 1.0, 'F': 0}


# Define a function that converts from letter grade to grade points
def compute_grade_points():
    # Read letter grade from user
    while True:
        letter = input('\nEnter a letter grade: ')
        letter = letter.upper()
        if letter not in GRADES.keys():
            print("This wasn't a valid letter.\nYou should enter a valid letter grade.")
            continue
        else:
            points = GRADES[letter]
            break
    # Display the result
    print(
        f'A(n) {letter} is equal to {points} grade points.')


# Define a function that display the letter-points conversion table
def display_conversion_table():
    line = '-' * 28
    print(f'\n{line}')
    print(f"{'Letter':15} Grade Points")
    print(line)
    for k, v in GRADES.items():
        print(f"{k:15} {v}")
    print(line)


# Run the program
display_conversion_table()
compute_grade_points()
