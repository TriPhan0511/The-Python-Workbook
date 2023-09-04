##
# Calculate grade point average(gpa) from the grade letters entered by a user.
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

# Define a dictionary variable that contains grade letter and grade points
GRADES = {'A+': 4.0, 'A': 4.0, 'A-': 3.7, 'B+': 3.3, 'B': 3.0,
          'B-': 2.7, 'C+': 2.3, 'C': 2.0, 'C-': 1.7, 'D+': 1.3, 'D': 1.0, 'F': 0}


def compute_grade_point_average(grades):
    # Declare some variables
    total = 0
    count = 0
    letters = []
    # Read letter grade from user
    while True:
        letter = input('Enter a letter grade (blank to quit): ')
        if not letter or len(letter.strip()) == 0:
            break
        letter = letter.upper()
        if letter not in grades.keys():
            print("This wasn't a valid letter.\nYou should enter a valid letter grade.")
            continue
        else:
            points = grades[letter]
            total += points
            count += 1
            letters.append(letter)
            singular_or_plural = 'letter' if len(letters) == 1 else 'letters'
            print(
                f"You have entered {len(letters)} grade {singular_or_plural}.")
    # Display the result
    if count == 0:
        print("You didn't enter anything!")
    else:
        print('\nTable of grade letters and converted grade points you have entered:')
        display_result_table(letters, grades)
        print(f'Grade point average: {(total / count):.1f}')


# Define a function that display the letter-points table based on the grade letters
def display_result_table(letters, grades):
    line = '-' * 28
    print(f'\n{line}')
    print(f"{'Letter':15} Grade Points")
    print(line)
    for item in letters:
        print(f"{item:15} {grades[item]}")
    print(f'{line}\n')


# Define a function that display the letter-points conversion table
def display_conversion_table(grades):
    line = '-' * 28
    print(f'\n{line}')
    print(f"{'Letter':15} Grade Points")
    print(line)
    for k, v in grades.items():
        print(f"{k:15} {v}")
    print(f'{line}\n')


# Run the program
display_conversion_table(GRADES)
compute_grade_point_average(GRADES)
