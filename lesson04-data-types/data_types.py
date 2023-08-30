import math

# String data type

# literal assigment

first = 'Tri'
last = 'Phan'

# print(type(first))  # <class 'str'>
# print(type(first) == str)  # True
# print(isinstance(first, str))  # True

# Constructor function
# pizza = str("Pepperoni")
# print(type(pizza))  # <class 'str'>
# print(type(pizza) == str)  # True
# print(isinstance(pizza, str))  # True

# Concatenation
# fullname = first + ' ' + last
# print(fullname)

# fullname += '!'
# print(fullname)

# Casting a number to a string
# decade = str(1980)
# print(isinstance(decade, str))  # True
# print(decade)

# statement = 'I like rock music from ' + decade + "s."
# print(statement)

# Multiple lines
multiline = '''
Hey, how are you?                                             

I was checking in.  
                      All good?


'''
# print(multiline)

# Escaping special characters
# sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located?'
# print(sentence)

# String Methods
# print(first)  # Tri
# print(first.lower())  # tri
# print(first.upper())  # TRI
# print(first)  # Tri

# print(multiline.title())
# print(multiline.replace('good', 'ok'))
# print(multiline)

# print(len(multiline))  # 120
# multiline += '                                   '
# multiline = '                  ' + multiline
# print(multiline)

# print(len(multiline))  # 173

# print(len(multiline.strip()))  # 116
# print(len(multiline.lstrip()))  # 154
# print(len(multiline.rstrip()))  # 135

# Build a menu
# title = 'menu'.upper()
# print(title.center(20, '='))
# print("Coffee".ljust(16, '.') + '$1'.rjust(4))
# print("Muffin".ljust(16, '.') + '$2'.rjust(4))
# print("Cheesecake".ljust(16, '.') + '$4'.rjust(4))

# String index values
# print(first[0])  # T
# print(first[1])  # r
# print(first[-1])  # i
# print(first[1:-1])  # r
# print(first[1:])  # ri
# print(first[:])  # Tri

# Some methods return boolean data
# print(first.startswith('T'))  # True
# print(first.startswith('t'))  # False
# print(first.lower().startswith('t'))  # True
# print(first.endswith('z'))  # False

# Boolean data type
# myvalue = True
# x = bool(False)
# print(type(myvalue))  # <class 'bool'>
# print(isinstance(x, bool))  # True

# Numeric data types

# integer type
# price = 100
# best_price = int(80)
# print(type(price))  # <class 'int'>
# print(isinstance(best_price, int))  # True

# float type
gpa = 3.28
y = float(1.14)
# print(type(gpa))  # <class 'float'>
# print(isinstance(y, float))  # True


# complex type
comp_value = 5+3j
# print(type(comp_value))  # <class 'complex'>
# print(isinstance(comp_value, complex))  # True
# print(comp_value.real)  # 5.0
# print(comp_value.imag)  # 3.0

# Built-in functions for numbers

# print(abs(gpa))  # 3.28
# print(abs(gpa * -1))  # 3.28
# print(round(gpa))  # 3.28
# print(round(gpa, 1))  # 3.3


# print(math.pi)  # 3.141592653589793
# print(math.sqrt(64))  # 8.0
# print(math.ceil(gpa))  # 4
# print(math.floor(gpa))  # 3

# Casting a string to a number
# zipcode = '10001'
# zip_value = int(zipcode)
# print(type(zip_value))  # <class 'int'>

# Error if you attempt to cast incorrect data
# zip_value = int('New York') # ValueError: invalid literal for int() with base 10: 'New York'
