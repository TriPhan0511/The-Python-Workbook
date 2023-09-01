users = ['Dave', 'John', 'Sara']
data = ['Dave', 42, True]
empty_list = []

print('')

# ======= CHECK FOR A VALUE IN A LIST =======
# print('Dave' in users)  # True
# print('dave' in users)  # False
# print('Beck' in users)  # False

# ======= RETRIEVE A LIST VALUE BY INDEX =======
# print(users[0])  # Dave
# print(users[-1])  # Sara
# print(users[-2])  # John

# print(users.index('Sara'))  # 2

# ======= RETRIEVE A RANGE OF LIST VALUES =======
# print(users[0:2])  # ['Dave', 'John']
# print(users[1:])  # ['John', 'Sara']
# print(users[:2])  # ['Dave', 'John']
# print(users[-3:-1])  # ['Dave', 'John']
# print(users[:])  # ['Dave', 'John', 'Sara']

# ======= GET THE LENGTH OF A LIST =======
# print(len(users))  # 3
# print(len(data))  # 3
# print(len(empty_list))  # 0

# ======= ADDING ITEMS TO A LIST =======
# users.append('Elsa')
# print(users)  # ['Dave', 'John', 'Sara', 'Elsa']
# print(len(users))  # 4

# users += ['Jason']
# print(users)  # ['Dave', 'John', 'Sara', 'Jason']

# users.extend(['Robert', 'Jimmy'])
# print(users)  # ['Dave', 'John', 'Sara', 'Robert', 'Jimmy']

# users.extend(data)
# print(users)  # ['Dave', 'John', 'Sara', 'Dave', 42, True]

# ======= INSERTING VALUES AT A SPECIFIC LIST INDEX =======
# users.insert(0, 'Bob')
# print(users)  # ['Bob', 'Dave', 'John', 'Sara']

# print(users)  # ['Dave', 'John', 'Sara']
# users[2:2] = ['Eddie', 'Alex']
# print(users)  # ['Dave', 'John', 'Eddie', 'Alex', 'Sara']

# ======= REPLACING LIST VALUES =======
# print(users)  # ['Dave', 'John', 'Sara']
# users[1:3] = ['Robert', 'JPJ']
# print(users)  # ['Dave', 'Robert', 'JPJ']

# ======= REMOVING, DELETING, CLEARING =======
# print(users)  # ['Dave', 'John', 'Sara']
# users.remove('Dave')
# print(users)  # ['John', 'Sara']

# print(users)  # ['Dave', 'John', 'Sara']
# print(users.pop())  # Sara
# print(users)  # ['Dave', 'John']

# print(users)  # ['Dave', 'John', 'Sara']
# users.pop(0)
# print(users)  # ['John', 'Sara']

# print(users)  # ['Dave', 'John', 'Sara']
# del users[0]
# print(users)  # ['John', 'Sara']

# print(data) # ['Dave', 42, True]
# del data
# print(data)  # NameError: name 'data' is not defined

# print(data)  # ['Dave', 42, True]
# data.clear()
# print(data)  # []
# print(len(data))  # 0

# ======= SORTING LISTS =======
# Re-define the users list
users = ['dave', 'John', 'Sara', 'JPJ', 'Alex', 'Elsa', 'Jason', 'Robert']

# print(users)
# # ['dave', 'John', 'Sara', 'JPJ', 'Alex', 'Elsa', 'Jason', 'Robert']
# users.sort()
# print(users)
# # ['Alex', 'Elsa', 'JPJ', 'Jason', 'John', 'Robert', 'Sara', 'dave']

# print(users)
# # ['dave', 'John', 'Sara', 'JPJ', 'Alex', 'Elsa', 'Jason', 'Robert']
# users.sort(reverse=True)
# print(users)
# # ['dave', 'Sara', 'Robert', 'John', 'Jason', 'JPJ', 'Elsa', 'Alex']

# print(users)
# # ['dave', 'John', 'Sara', 'JPJ', 'Alex', 'Elsa', 'Jason', 'Robert']
# users.sort(key=str.lower)
# print(users)
# # ['Alex', 'dave', 'Elsa', 'Jason', 'John', 'JPJ', 'Robert', 'Sara']

# nums = [4, 42, 78, 1, 5]
# nums.reverse()
# print(nums)  # [5, 1, 78, 42, 4]

# nums.sort(reverse=True)
# print(nums)  # [78, 42, 5, 4, 1]

# print(sorted(nums, reverse=True))  # [78, 42, 5, 4, 1]
# print(nums)  # [4, 42, 78, 1, 5]

# ======= COPYING LISTS =======
# nums = [4, 42, 78, 1, 5]

# numscopy = nums.copy()
# mynums = list(nums)
# mycopy = nums[:]

# print(numscopy)  # [4, 42, 78, 1, 5]
# print(mynums)  # [4, 42, 78, 1, 5]
# mycopy.sort()
# print(mycopy)  # [1, 4, 5, 42, 78]
# print(nums)  # [4, 42, 78, 1, 5]

# ======= LIST CONSTRUCTOR AND DATA TYPE =======
# nums = [4, 42, 78, 1, 5]
# print(type(nums))  # <class 'list'>

# my_list = list([1, 'Neil', True])
# print(type(my_list))  # <class 'list'>
# print(isinstance(my_list, list))  # True
# print(my_list)  # [1, 'Neil', True]

# ======= TUPLES =======
# my_tuple = tuple(('Dave', 42, True))
# another_tuple = (1, 4, 2, 8)

# print(my_tuple)  # ('Dave', 42, True)
# print(type(my_tuple))  # <class 'tuple'>
# print(type(another_tuple))  # <class 'tuple'>

# ======= IF YOU NEED TO CHANGE A TUPLE =======
# my_tuple = ('Dave', 42, True)
# new_list = list(my_tuple)
# new_list.append('Neil')
# new_tuple = tuple(new_list)
# print(new_tuple)  # ('Dave', 42, True, 'Neil')

# ======= UNPACKING TUPLES =======
# my_tuple = (1, 4, 2, 8)

# (one, two, *hey) = my_tuple
# print(one)  # 1
# print(two)  # 4
# print(hey)  # [2, 8]

# (one, *two, hey) = my_tuple
# print(one)  # 1
# print(two)  # [4, 2]
# print(hey)  # 8

# ======= USING DOT NOTATION TO FIND METHODS =======
my_tuple = (1, 4, 2, 1, 8)
print(my_tuple.count(1))  # 2
print(my_tuple.count(9000))  # 0
