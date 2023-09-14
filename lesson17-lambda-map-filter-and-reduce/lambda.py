# ======= Lambda function expression examples =======

# def squared(num): return num * num
# # lambda num: num * num
# # print(squared(2))


# def add_two(num): return num + 2
# # lambda num: num + 2
# # print(add_two(12))


# def sum(a, b): return a + b
# # lambda a, b: a + b
# # print(sum(2, 2))

# ======= When to use lambda expressions =======

# def func_builder(x):
#     return lambda num: num + x


# add_ten = func_builder(10)
# add_twenty = func_builder(20)

# print(add_ten(7))  # 17
# print(add_twenty(7))  # 27

# ======= Higher order functions =======

# numbers = [3, 7, 12, 18, 20, 21]
# squared_nums = map(lambda num: num * num, numbers)
# print(list(squared_nums))  # [9, 49, 144, 324, 400, 441]

# ======= filter() function =======

# numbers = [3, 7, 12, 18, 20, 21]
# odd_nums = list(filter(lambda num: num % 2 != 0, numbers))
# print(odd_nums)  # [3, 7, 21]

# ======= reduce() function =======

from functools import reduce

numbers = [3, 7, 12, 18, 20, 21, 1, 10]

# total = reduce(lambda accumulator, current: accumulator + current, numbers)
# print(total)  # 92

# total_2 = reduce(lambda accumulator, current: accumulator +
#                  current, numbers, 100)

# print(total_2)  # 192

# max = reduce(lambda x, y: x if x > y else y, numbers)
# print(max)  # 21

# print(sum(numbers, 100))

# ======= More complex reduce examples =======

names = ['Dave', 'Sarah Ito', 'John Jacob Jingleheimerschmidt']
char_count = reduce(lambda acc, curr: acc + len(curr), names, 0)
print(char_count)  # 43

# all_characters = ''
# for name in names:
#     all_characters += name
# print(all_characters)  # DaveSarah ItoJohn Jacob Jingleheimerschmidt
# print(len(all_characters))  # 43
