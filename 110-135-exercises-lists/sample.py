# data = [2.71, 3.14, 1.41, 1.62]
# print(data)

# An individual list element can be updated using an assignment statement. The
# name of the list, followed by the element’s index enclosed in square brackets, appears
# to the left of the assignment operator. The new value that will be stored at that index
# appears to the assignment operator’s right. When the assignment statement executes,
# the element previously stored at the indicated index is overwritten with the newvalue.
# The other elements in the list are not impacted by this change.
# Consider the following example. It creates a list that contains four elements,
# and then it replaces the element at index 2 with 2.30. When the print statement
# executes it will display all of the values in the list. Those values are 2.71, 3.14, 2.30
# and 1.62.

# ======= 5.2 Loops and Lists =======

# A for loop executes once for each item in a collection. The collection can be a
# range of integers constructed by calling the range function. It can also be a list.
# The following example uses a for loop to total the values in data.

# data = [2.71, 3.14, 1.41, 1.62]
# total = 0
# for num in data:
#     total += num
#     print(f'Total: {total}')

# # print(f'Finally, Total: {total}')
# print(7.26 + 1.62)

# val1 = 1.61
# val2 = 3.49
# print(val1 + val2)

# val1 = 7.26
# val2 = 1.62
# print(float(val1) + float(val2))
# print(val1 + val2)


# ======= 5.3 Additional List Operations =======
# Lists can grow and shrink as a program runs. A new element can be inserted at
# any location in the list, and an element can be deleted based on its value or its
# index. Python also provides mechanisms for determining whether or not an element
# is present in a list, finding the index of the first occurrence of an element in a list,
# rearranging the elements in a list, and many other useful tasks.

# Tasks like inserting a new element into a list and removing an element from a
# list are performed by applying a method to a list. Much like a function, a method is
# a collection of statements that can be called upon to perform a task. However, the
# syntax used to apply a method to a list is slightly different from the syntax used to
# call a function.

# A method is applied to a list by using a statement that consists of a variable
# containing a list, followed by a period, followed by the method’s name. Like a
# function call, the name of the method is followed by parentheses that surround a
# comma separated collection of arguments. Some methods return a result. This result
# can be stored in a variable using an assignment statement, passed as an argument to
# another method or function call, or used as part of a calculation, just like the result
# returned by a function.

# ======= 5.3.1 Adding Elements to a List (methods: append, insert) =======

# Elements can be added to the end of an existing list by calling the append method. It
# takes one argument, which is the element that will be added to the list. For example,
# consider the following program:

# data = [2.71, 3.14, 1.41, 1.62]
# data.append(2.3)
# print(data)  # [2.71, 3.14, 1.41, 1.62, 2.3]

# The first line creates a new list of 4 elements and stores it in data. Then the
# append method is applied to data which increases its length from 4 to 5 by
# adding 2.30 to the end of the list. Finally, the list, which now contains 2.71, 3.14,
# 1.41, 1.62, and 2.30, is printed.

# Elements can be inserted at any location in a list using the insert method. It
# requires two arguments, which are the index at which the element will be inserted
# and its value. When an element is inserted any elements to the right of the insertion
# point have their index increased by 1 so that there is an index available for the new
# element. For example, the following code segment inserts 2.30 in the middle of data
# instead of appending it to the end of the list.

# data = [2.71, 3.14, 1.41, 1.62]
# data.insert(2, 2.3)
# print(data)  # [2.71, 3.14, 2.3, 1.41, 1.62]

# ======= 5.3.2 Removing Elements froma List (methods: pop, remove) =======

# The pop method is used to remove an element at a particular index from a list.
# The index of the element to remove is provided as an optional argument to pop. If
# the argument is omitted then pop removes the last element from the list. The pop
# method returns the value that was removed from the list as its only result. When this
# value is needed for a subsequent calculation it can be stored into a variable by calling
# pop on the right side of an assignment statement. Applying pop to an empty list is
# an error, as is attempting to remove an element from an index that is beyond the end
# of the list.

# A value can also be removed from a list by calling the remove method. It’s only
# argument is the value to remove (rather than the index of the value to remove). When
# the remove method executes it removes the first occurrence of its argument from
# the list. An error will be reported if the value passed to remove is not present in the
# list.

# Consider the following example. It creates a list, and then removes two elements
# from it. When the first print statement executes it displays [2.71, 3.14] because
# 1.62 and 1.41 were removed from the list. The second print statement displays 1.41
# because 1.41 was the last element in the list when the pop method was applied to it.

# data = [2.71, 3.14, 1.41, 1.62]

# data.remove(1.62)
# print(data)  # [2.71, 3.14, 1.41]

# last = data.pop()
# print(last)  # 1.41
# print(data)  # [2.71, 3.14]

# ======= 5.3.3 Rearranging the Elements in a List (methods: reverse, sort) =======

# Sometimes a list has all of the correct elements in it, but they aren’t in the order
# needed to solve a particular problem. Two elements in a list can be swapped using
# a series of assignment statements that read from and write to individual elements in
# the list, as shown in the following code segment.

# data = [2.71, 3.14, 1.41, 1.62]

# # Swap the element at index 1 with the element at index 3
# temp = data[1]
# data[1] = data[3]
# data[3] = temp

# print(data)  # [2.71, 1.62, 1.41, 3.14]

# There are twomethods that rearrange the elements in a list. The reverse method
# reverses the order of the elements in the list, and the sort method sorts the elements
# into ascending order. Both reverse and sort can be applied to a list without
# providing any arguments.

# data = [2.71, 3.14, 1.41, 1.62]
# data.reverse()
# print(data)  # [1.62, 1.41, 3.14, 2.71]

# data = [2.71, 3.14, 1.41, 1.62]
# data.sort()
# print(data)  # [1.41, 1.62, 2.71, 3.14]

# The following example reads a collection of numbers from the user and stores
# them in a list. Then it displays all of the values in sorted order.

# def get_numbers_and_sort():
#     numbers = []
#     while True:
#         num = input('Enter a number (blank line to quit):\n')
#         if not num or len(num.strip()) == 0:
#             break
#         num = float(num)
#         numbers.append(num)
#     if len(numbers) > 0:
#         # Ascending order
#         # numbers.sort()

#         # Descending order
#         numbers.sort()
#         numbers.reverse()
#         print(numbers)
#     else:
#         print('Empty list!')


# get_numbers_and_sort()

# ======= 5.3.4 Searching a List  (Python's in operator and index medthod) =======

# Sometimes we need to determine whether or not a particular value is present in a list.
# In other situations, we might want to determine the index of a value that is already
# known to be present in a list. Python’s in operator and index method allow us to
# perform these tasks.

# The in operator is used to determine whether or not a value is present in a list.
# The value that is being searched for is placed to the left of the operator. The list that
# is being searched is placed to the operator’s right. Such an expression evaluates to
# True if the value is present in the list. Otherwise it evaluates to False.

# The index method is used to identify the position of a particular value within
# a list. This value is passed to index as its only argument. The index of the first
# occurrence of the value in the list is returned as the method’s result. It is an error to
# call the index method with an argument that is not present in the list. As a result,
# programmers sometimes use the in operator to determine whether or not a value is
# present in a list and then use the index method to determine it’s location.

# The following example demonstrates several of the methods and operators introduced
# in this section. It begins by reading integers from the user and storing them
# in a list. Then one additional integer is read from the user. The position of the first
# occurrence of this additional integer in the list of values is reported (if it is present).
# An appropriate message is displayed if the additional integer is not present in the list
# of values entered by the user.


# def get_numbers_and_search():
#     numbers = []
#     while True:
#         num = input('Enter a number (blank line to finish):\n')
#         if not num or len(num.strip()) == 0:
#             break
#         num = int(num)
#         numbers.append(num)
#     print(f'Test - numbers: {numbers}')  # Test

#     searched_number = int(input('\n\nEnter a number for searching:\n'))

#     if not searched_number in numbers:
#         print(f'{searched_number} does not exists in {numbers}.')
#     else:
#         print(
#             f'The position of the first occurence of {searched_number} in list is: {numbers.index(searched_number)}')


# get_numbers_and_search()

# ======= 5.4 Lists as Return Values and Arguments =======

# Lists can be returned from functions. Like values of other types, a list is returned
# from a function using the return keyword. When the return statement executes,
# the function terminates and the list is returned to the location where the function was
# called. Then the list can be stored in a variable or used in a calculation.

# Lists can also be passed as arguments to functions. Like values of other types, any
# lists being passed to a function are included inside the parentheses that follow the
# function’s name when it is called. Each argument, whether it is a list or a value of
# another type, appears in the corresponding parameter variable inside the function.

# Parameter variables that contain lists can be used in the body of a function just like
# parameter variables that contain values of other types. However, unlike an integer,
# floating-point number, string or Boolean value, changes made to a list parameter
# variable can impact the argument passed to the function, in addition to the value
# stored in the parameter variable. In particular, a change made to a list using a method
# (such as append, pop or sort) will change the value of both the parameter variable
# and the argument that was provided when the function was called.

# def insert_at_the_end(t):
#     t.append(1000)


# numbers = [1, 2, 3]

# insert_at_the_end(numbers)

# print(numbers)  # [1, 2, 3, 1000]

# Updates performed on individual list elements (where the name of the list, followed
# by an index enclosed in square brackets, appears on the left side of an assignment
# operator) also modify both the parameter variable and the argument that was
# provided when the functionwas called. However, assignments to the entire list (where
# only the name of the list appears to the left of the assignment operator) only impact
# the parameter variable. Such assignments do not impact the argument provided when
# the function was called.

# def update_the_first_element(t):
#     t[0] = 1000


# numbers = [1, 2, 3]

# update_the_first_element(numbers)

# print(numbers)  # [1000, 2, 3]

# -----------------------------------

# def another_update(t):
#     t = [400, 500, 600]
#     t[0] = 1000


# numbers = [1, 2, 3]

# another_update(numbers)
# print(numbers)  # [1, 2, 3]

# The differences in behavior between list parameters and parameters of other
# types may seem arbitrary, as might the choice to have some changes apply to both
# the parameter variable and the argument while others only change the parameter
# variable. However, this is not the case. There are important technical reasons for
# these differences, but those details are beyond the scope of a brief introduction to
# Python.
