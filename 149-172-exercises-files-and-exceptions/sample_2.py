
# s = input('Enter a string: ')
# s = s.upper()
# print(s)

# --------------------------------------------------------

# # s = '123456'
# s = input()
# if len(s) < 2:
#     print('')
# else:
#     print(f'{s[:2]}{s[-2:]}')

# --------------------------------------------------------

# # s1 = 'sun'
# # s2 = 'moon'

# # s1 = 'apple'
# # s2 = 'banana'

# s1 = input()
# s2 = input()

# first_two_1 = s1[:2]
# first_two_2 = s2[:2]

# s1 = first_two_2 + s1[2:]
# s2 = first_two_1 + s2[2:]

# print(f'{s1} {s2}')

# --------------------------------------------------------

# # s = 'Python Exercises'
# s = input()
# words = s.split(' ')
# words.reverse()
# result = ' '.join(words)
# print(result)

# --------------------------------------------------------


# f = open('text.txt', 'w+')
# # print(f.read(2))

# --------------------------------------------------------

# # print(list('funix'))
# # list1 = list()

# x = 'hello'
# # print([i for i in x if i not in "aeiouy"])

# # out = []
# # for letter in x:
# #     if letter not in 'aeiouy':
# #         out.append(letter)

# # print(out)

# print([i for i in x if i not in 'aeiouy'])

# --------------------------------------------------------

# import random
# from functools import reduce

# # n = 3
# n = int(input())

# numbers = []
# for i in range(n):
#     numbers.append(random.randrange(0, 100))
# # print(numbers)  # Test

# smallest = reduce(lambda x, y: x if x < y else y, numbers)

# # smallest = numbers.sort()
# # print(smallest)


# def find_smallest(n):
#     lst = []
#     for i in range(n):
#         lst.append(random.randrange(0, 100))
#     print(f'Test: {lst}')  # Test
#     # return reduce(lambda x, y: x if x < y else y, lst)
#     return min(lst)

# # def find_smallest(n):
# #     lst = []
# #     for i in range(n):
# #         lst.append(random.randrange(0, 100))
# #     print(f'Test: {lst}') # Test
# #     return reduce(lambda x, y: x if x < y else y, lst)


# print(find_smallest(3))


# n = int(input())
# lst = []
# for i in range(n):
#     lst.append(int(input()))

# lst.sort()
# print(lst[0])

# n = int(input())
# total = 0
# for i in range(n):
#     total += int(input())
# print(total)

# n = int(input())
# lst = []
# for i in range(n):
#     lst.append(int(input()))
# lst.sort()
# print(lst)

# n = int(input())
# lst = []
# for i in range(n):
#     lst.append(int(input()))
# lst = list(filter(lambda e: e % 2 != 0, lst))
# print(lst)

# n = int(input())
# lst = []
# for i in range(n):
#     lst.append(int(input()))
# lst = list(filter(lambda e: e % 5 == 0, lst))


# if len(lst) == 0:
#     print([0])
# else:
#     print(lst)

# --------------------------------------------------------

# s = {1, 2, 3}

# print(s)
# # print(type(s))

# s.add(100)
# print(s)


# # print(s[0])


# d = set()
# d = {40, 45}
# d = {}

# print(type(d))


# d = {'one': 2, 'two': 2}

# for k, v in d.items():
#     if v == 2:
#         print(k)


# d = {1: 2, 1: 3}
# print(type(d))
# print(d[1])

a = {1: 'a', 2: 'b', 'a': 'c'}
print(a)
# del a
# print(a)
