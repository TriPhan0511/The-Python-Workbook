##
#   One of the first known examples of encryption was used by Julius Caesar. Caesar
# needed to provide written instructions to his generals, but he didn’t want his enemies
# to learn his plans if the message slipped into their hands. As a result, he developed
# what later became known as the Caesar cipher.
#   The idea behind this cipher is simple (and as such, it provides no protection against
# modern code breaking techniques). Each letter in the original message is shifted by
# 3 places. As a result, A becomes D, B becomes E, C becomes F, D becomes G, etc.
#   The last three letters in the alphabet are wrapped around to the beginning: X becomes
# A, Y becomes B and Z becomes C. Non-letter characters are not modified by the
# cipher.
#   Write a program that implements a Caesar cipher. Allow the user to supply the
# message and the shift amount, and then display the shifted message. Ensure that
# your program encodes both uppercase and lowercase letters. Your program should
# also support negative shift values so that it can be used both to encode messages and
# decode messages.
#

# A1BC -> D1EF
# X = 88 -> X + 3 = 88 + 3 = 91 -> 91 - 26 = 65 <- A
# X -> A : 88 - 23 = 65

# Y = 89 -> Y + 3 = 89 + 3 = 92 -> 92 - 26 = 66 <- B
# Y -> B: 89 - 23 =

# Z = 90 -> Z + 3 = 90 + 3 = 93 -> 93 - 26 = 67 <- C

# ------------------------------------------------------------

# print(f"A = {ord('A')}")  # A = 65

# print(f"A + 3 = {ord('A') + 3}")  # A + 3 = 68
# print(f"A + 3 = {chr(ord('A') + 3)}")  # A + 3 = D

# print(f"X + 3 = {ord('X') + 3}")  # X + 3 = 91
# print(f"X + 3 = {chr(ord('X') + 3)}")  # X + 3 = D

# print(f"a = {ord('a')}")  # a = 97

# print(f'A is alphabet: {"A".isalpha()}')  # A is alphabet: True
# print(f'0 is alphabet: {"0".isalpha()}')  # A is alphabet: False

# print(f'A is a digit: {"A".isdigit()}')  # A is a digit: False
# print(f'0 is a digit: {"0".isdigit()}')  # A is a digit: True

# for letter in message:
#     print(letter)

# letters = list(message)
# print(letters)
# print(type(letters))

# message2 = ''
# for let in letters:
#     message2 += let
# print(f'message2 = {message2}')

# # print(f"{'['.isalpha}")
# print('['.isalpha())  # False
# for num in range(65, 91):
#     letter = chr(num)
#     print(f"Letter: {letter}")
#     print(f"Is alphabet: {letter.isalpha()}")


def caesar_cipher(message, shift_amount):

    letters = []
    for letter in message:
        current = ''
        if not letter.isalpha():
            current = letter
        else:
            num = ord(letter)
            if (65 <= num <= 87) or (97 <= num <= 119):
                current = chr(num + shift_amount)
            else:
                current = chr(num + shift_amount - 26)
        letters.append(current)

    # Convert from a list of letters to a string
    result = ''
    for letter in letters:
        result += letter

    return result


# message = 'ABC 0123456789 [] DEF'  # 'DEF 0123456789 [] GHI'
# message = 'ABC 0123456789 [] XYZ'  # 'DEF 0123456789 [] GHI'
# message = 'abc 0123456789 [] XYZ'  # 'DEF 0123456789 [] GHI'
message = 'abc 0123456789 [], yza'  # 'DEF 0123456789 [] GHI'
# shift_amout = 24
# shift_amout = 26
# shift_amout = 25
shift_amout = 3
encryted_message = caesar_cipher(message, shift_amout)
print(f'Encrypted message: {encryted_message}')
