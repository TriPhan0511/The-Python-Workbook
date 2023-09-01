##
# Determine and display whether an letter entered by the user is a vowel or a consonant.
#

def vowel_or_consonant():
    letter = input('Enter a consonant: ')
    if letter in ['a', 'i', 'u', 'e', 'o']:
        result = f'{letter} is a vowel.'
    elif letter == 'y':
        result = f'Sometimes {letter} is a vowel, sometimes {letter} is a consonant.'
    else:
        result = f'{letter} is a consonant.'
    print(result)

# def vowel_or_consonant():
#     letter = input('Enter a consonant: ')
#     if letter == 'a' or letter == 'i' or letter == 'u' or letter == 'e' or letter == 'o':
#         result = f'{letter} is a vowel.'
#     elif letter == 'y':
#         result = f'{letter} is sometimes a vowel, sometimes a consonant.'
#     else:
#         result = f'{letter} is a consonant.'
#     print(result)


# Run the program
vowel_or_consonant()
