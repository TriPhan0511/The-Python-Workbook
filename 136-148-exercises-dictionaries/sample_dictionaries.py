# # Dictionaries

# There are many parallels between lists and dictionaries. Like lists, dictionaries allow
# several, even many, values to be stored in one variable. Each element in a list has
# a unique integer index associated with it, and these indices must be integers that
# increase sequentially from zero. Similarly, each value in a dictionary has a unique
# key associated with it, but a dictionary’s keys are more flexible than a list’s indices. A
# dictionary’s keys can be integers. They can also be floating-point numbers or strings.
# When the keys are numeric they do not have to start from zero, nor do they have to
# be sequential. When the keys are strings they can be any combination of characters,
# including the empty string. All of the keys in a dictionary must be distinct just as all
# of the indices in a list are distinct.

# Every key in a dictionary must have a value associated with it. The value associated
# with a key can be an integer, a floating-point number, a string or a Boolean value. It
# can also be a list, or even another dictionary. A dictionary key and it’s corresponding
# value are often referred to as a key-value pair. While the keys in a dictionary must be
# distinct there is no parallel restriction on the values. Consequently, the same value
# can be associated with multiple keys.

# Starting in Python 3.7, the key-value pairs in a dictionary are always stored in the
# order in which they were added to the dictionary. Each time a new key-value pair
# is added to the dictionary it is added to the end of the existing collection. There is
# no mechanism for inserting a key-value pair in the middle of an existing dictionary.
# Removing a key-value pair from the dictionary does not change the order of the
# remaining key-value pairs in the dictionary.

# A variable that holds a dictionary is created using an assignment statement. The
# empty dictionary, which does not contain any key-value pairs, is denoted by {} (an
# open brace immediately followed by a close brace). A non-empty dictionary can
# be created by including a comma separated collection of key-value pairs inside the
# braces. A colon is used to separate the key from its value in each key-value pair.
# For example, the following program creates a dictionary with three key-value pairs
# where the keys are strings and the values are floating-point numbers. Each key-value
# pair associates the name of a common mathematical constant to its value. Then all
# of the key-value pairs are displayed by calling the print function.

# constants = {'pi': 3.14, 'e': 2.71, 'root 2': 1.41}
# print(constants)  # {'pi': 3.14, 'e': 2.71, 'root 2': 1.41}

# ======== 6.1 Accessing,Modifying and Adding Values ========

# Accessing a value in a dictionary is similar to accessing a value in a list. When the
# index of a value in a list is known, we can use the name of the list and the index
# enclosed in square brackets to access the value at that location. Similarly, when the
# key associated with a value in a dictionary is known, we can use the name of the
# dictionary and the key enclosed in square brackets to access the value associated
# with that key.

# Modifying an existing value in a dictionary and adding a new key-value pair
# to a dictionary are both performed using assignment statements. The name of the
# dictionary, along with the key enclosed in square brackets, is placed to the left of the
# assignment operator, and the value to associate with the key is placed to the right of the
# assignment operator. If the key is already present in the dictionary then the assignment
# statement will replace the key’s current value with the value to the right of the
# assignment operator. If the key is not already present in the dictionary then a newkeyvalue
# pair is added to it. These operations are demonstrated in the following program.

# # Create new dictionary with 2 key-value pairs
# results = {'pass': 0, 'fail': 0}

# # Add a new key-value pair to the dictionary
# results['withdrawal'] = 1

# # # Test
# # print(results)  #  {'pass': 0, 'fail': 0, 'withdrawal': 1}

# # Update two values in the dictionary
# results['pass'] = 3
# results['fail'] += 1

# # Test
# print(results)  # {'pass': 3, 'fail': 1, 'withdrawal': 1}

# # Display the values associated with fail, pass and withdrawal respectively
# print(results['fail'])  # 1
# print(results['pass'])  # 3
# print(results['withdrawal'])  # 1


# print('fail' in results.keys())
# print(3 in results.values())

# ======== 6.2 Removing a Key-Value Pair ========

# A key-value pair is removed from a dictionary using the pop method. One argument,
# which is the key to remove, must be supplied when the method is called. When the
# method executes it removes both the key and the value associated with it from the
# dictionary. Unlike a list, it is not possible to pop the last key-value pair out of a
# dictionary by calling pop without any arguments.

# The pop method returns the value associated with the key that is removed from the
# dictionary. This value can be stored into a variable using an assignment statement, or
# it can be used anywhere else that a value is needed, such as passing it as an argument
# to another function or method call, or as part of an arithmetic expression.

# # Create a dictionary with 2 key-value pairs
# results = {'pass': 10, 'fail': 5}

# # # Test
# # print(results) # {'pass': 10, 'fail': 5}

# # Remove one key-value pair in the dictionary
# val = results.pop('pass')

# # Test
# print(results)  # {'fail': 5}
# print(val)  # 10

# ======== 6.3 Additional Dictionary Operations ========

# Some programs add key-value pairs to dictionaries where the key or the value were
# read from the user. Once all of the key-value pairs have been stored in the dictionary
# it might be necessary to determine how many there are, whether a particular
# key is present in the dictionary, or whether a particular value is present in the
# dictionary. Python provides functions, methods and operators that allow us to perform
# these tasks.

# The len function, which we previously used to determine the number of elements
# in a list, can also be used to determine how many key-value pairs are in a dictionary.
# The dictionary is passed as the only argument to the function, and the number of
# key-value pairs is returned as the function’s result. The len function returns 0 if the
# dictionary passed as an argument is empty.

# The in operator can be used to determine whether or not a particular key or value
# is present in a dictionary. When searching for a key, the key appears to the left of the
# in operator and a dictionary appears to its right. The operator evaluates to True
# if the key is present in the dictionary. Otherwise it evaluates to False. The result
# returned by the in operator can be used anywhere that a Boolean value is needed,
# including in the condition of an if statement or while loop.

# The in operator is used together with the values method to determine whether
# or not a value is present in a dictionary. The value being searched for appears to
# the left of the in operator and a dictionary, with the values method applied to it,
# appears to its right. For example, the following code segment determines whether or
# not any of the values in dictionary d are equal to the value that is currently stored in
# variable x.

# results = {'pass': 10, 'fail': 5}

# # print(len(results))  # 2
# # print(len({}))  # 0

# # print('pass' in results)  # True
# # print('withdrawla' in results)  # False
# # print(10 in results)  # False

# x = 5
# if x in results.values():
#     print(f'At least one of the values in results is {x}')
# else:
#     print(f'None of the values in results are {x}')

# ======== 6.4 Loops and Dictionaries ========

# A for loop can be used to iterate over all of the keys in a dictionary, as shown below.
# A different key from the dictionary is stored into the for loop’s variable, k, each
# time the loop body executes.

# # Create a dictionary
# constants = {'pi': 3.14, 'e': 2.71, 'root 2': 1.41}

# # Print all of the keys and values with nice formatting
# for k in constants:
#     print(f'The value associated with {k} is {constants[k]}')

# # The value associated with pi is 3.14
# # The value associated with e is 2.71
# # The value associated with root 2 is 1.41

# A for loop can also be used to iterate over the values in a dictionary (instead of
# the keys). This is accomplished by applying the values method, which does not
# take an arguments, to a dictionary to create the collection of values used by the for
# loop. For example, the following program computes the sum of all of the values in
# a dictionary. When it executes, constants.values() will be a collection that
# includes 3.14, 2.71 and 1.41. Each of these values is stored in v as the for loop runs,
# and this allows the total to be computed without using any of the dictionary’s keys.

# # Create a dictionary
# constants = {'pi': 3.14, 'e': 2.71, 'root 2': 1.41}

# # Compute the sum of all the values in the dictionary
# total = 0
# for v in constants.values():
#     total += v

# # Display the total
# print(f'The total is {total}')  # The total is 7.26

# Some problems involving dictionaries are better solved with while loops than
# for loops. For example, the following program uses a while loop to read strings
# from the user until 5 unique values have been entered. Then all of the strings are
# displayed with their counts.

# # Create an empty dictionary
# counts = {}

# # Loop until 5 distinct strings have been entered
# while len(counts) < 5:
#     line = input('Enter a word: ')
#     if not line.strip():
#         continue
#     if line in counts:
#         counts[line] += 1
#     else:
#         counts[line] = 1

# # Display the result
# print('')
# for k, v in counts.items():
#     print(f'{k} occured {v} time(s).')

# ======== 6.5 Dictionaries as Arguments and Return Values ========

# Dictionaries can be passed as arguments to functions, just like values of other types.
# As with lists, a change made to a parameter variable that contains a dictionary
# can modify both the parameter variable and the argument passed to the function.
# For example, inserting or deleting a key-value pair will modify both the parameter
# variable and the argument, as will modifying the value associated with one key in
# the dictionary using an assignment statement. However an assignment to the entire
# dictionary (where only the name of the dictionary appears to the left of the assignment
# operator) only impacts the parameter variable. It does not modify the argument passed
# to the function. As with other types, dictionaries are returned from a function using
# the return keyword.

# def modify_results(d):
#     if not isinstance(d, dict):
#         return
#     if 'pass' in d:
#         d['pass'] = 10000


# results = {'pass': 10, 'fail': 5}

# # # Test
# # print(results) # {'pass': 10, 'fail': 5}

# modify_results(results)

# # Test
# print(results)  # {'pass': 10000, 'fail': 5}
