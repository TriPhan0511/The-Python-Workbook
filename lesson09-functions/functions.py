# def hello_world():
#     print('Hello world!')


# hello_world()


# ======= CHECK ARGUMENT TYPES =======

# def sum(num1, num2):
#     # Check argument types
#     if (type(num1) is not int) or (type(num2) is not int):
#         return
#     return num1 + num2


# total = sum('a', 3)
# print(total)  # None


# ======= DEFAULT PAREMETER VALUES =======
# def sum(num1=0, num2=0):
#     if (type(num1) is not int) or (type(num2) is not int):
#         return 0
#     return num1 + num2


# # total = sum()  # 0
# # total = sum(1)  # 1
# total = sum(1, 2)  # 3
# total = sum('a', 2)  # 3
# print(total)

# ======= RECEIVING AN UNKNOWN NUMBER OF ARGUMENTS (args) =======
# def multiple_items(*args):
#     print(args)
#     print(type(args))  # <class 'tuple'>


# multiple_items('Dave', 'John', 'Sara')
# # ('Dave', 'John', 'Sara')
# # <class 'tuple'>

# ======= RECEIVING AN UNKNOWN NUMBER OF KEY WORD ARGUMENTS (kwargs) =======
# def mult_named_items(**kwargs):
#     print(kwargs)
#     print(type(kwargs))  # <class 'dict'>


# mult_named_items(first='Dave', last='Gray', age=42)
# # {'first': 'Dave', 'last': 'Gray', 'age': 42}
# # <class 'dict'>


# ======= Example 1: How to access elements in args =======
# def my_function(*args):
#     if len(args) == 0:
#         print('Nothing')
#     else:
#         print(args[0])
#     # print(args)


# # my_function()
# my_function(1, 2)


# ======= Example 2: How to access elements in args =======
# def my_function(first, *args, next_to_last, last):
#     print(first)
#     print(args)
#     print(next_to_last)
#     print(last)


# my_function(1, 2, 3, 4, 5, last=100, next_to_last=99)
# # 1
# # (2, 3, 4, 5)
# # 99
# # 100


# ======= Example 3:  How to access elements in kwargs =======
# def my_func(**kwargs):
#     # print(kwargs.keys())
#     # print(kwargs.values())
#     # print(kwargs.items())
#     for key, value in kwargs.items():
#         print(f'{key} = {value}')


# my_func(name='Dave', age=42)
# # name = Dave
# # age = 42


# ======= Example 4:  How to access elements in kwargs =======

# def my_second_func(first, **kwargs):
#     print(first)
#     print(kwargs.items())


# # my_second_func(1, name='Gray', age=42)
# # my_second_func(first = 1, name='Gray', age=42)
# # # 1
# # # dict_items([('name', 'Gray'), ('age', 42)])
