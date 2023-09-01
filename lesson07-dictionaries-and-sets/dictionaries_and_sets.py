# ======= DICTIONARIES =======
band = {
    'vocals': 'Plant',
    'guitar': 'Page',
}

band2 = dict(vocals='Plant', guitar='Page')

# print(band)  # {'vocal': 'Plant', 'guitar': 'Page'}
# print(band2)  # {'vocal': 'Plant', 'guitar': 'Page'}
# print(type(band))  # <class 'dict'>
# print(type(band2))  # <class 'dict'>
# print(len(band))  # 2
# print(len(band2))  # 2

# ======= ACCESS ITEMS =======
# print(band['vocals'])  # Plant
# print(band.get('guitar'))  # Page

# ======= LIST ALL KEYS =======
# print(band.keys())  # dict_keys(['vocals', 'guitar'])

# ======= LIST ALL VALUES =======
# print(band.values())  # dict_values(['Plant', 'Page'])

# ======= LIST OF KEY/VALUE PAIRS AS TUPLES =======
# print(band.items())  # dict_items([('vocals', 'Plant'), ('guitar', 'Page')])

# ======= VERIFY A KEY EXISTS =======
# print('guitar' in band)  # True
# print('triangle' in band)  # False
# print('Page' in band)  # False

# ======= CHANGE VALUES =======
# band['vocals'] = 'Coverdale'
# band.update({'bass': 'JPJ'})
# print(band)  # {'vocals': 'Coverdale', 'guitar': 'Page', 'bass': 'JPJ'}

# ======= REMOVE ITEMS =======
# print(band)  # {'vocals': 'Plant', 'guitar': 'Page'}
# print(band.pop('guitar'))  # Page
# print(band)  # {'vocals': 'Plant'}

# band['drum'] = 'Bonham'
# print(band)  # {'vocals': 'Plant', 'guitar': 'Page', 'drum': 'Bonham'}
# print(band.popitem())  # ('drum', 'Bonham') <- tuple
# print(band)  # {'vocals': 'Plant', 'guitar': 'Page'}

# ======= DELETE AND CLEAR =======
# band['drum'] = 'Bonham'
# print(band)  # {'vocals': 'Plant', 'guitar': 'Page', 'drum': 'Bonham'}

# del band['drum']
# print(band)  # {'vocals': 'Plant', 'guitar': 'Page'}

# print(band2)  # {'vocals': 'Plant', 'guitar': 'Page'}
# band2.clear()
# print(band2)  # {}

# del band2
# # print(band2)  # NameError: name 'band2' is not defined. Did you mean: 'band'?

# ======= COPY DICTIONARIES =======
band = {
    'vocals': 'Plant',
    'guitar': 'Page'
}

# band2 = band  # Create a reference
# band2['drum'] = 'Dave'
# print('Bad copy!')
# print(band)  # {'vocals': 'Plant', 'guitar': 'Page', 'drum': 'Dave'}
# print(band2)  # {'vocals': 'Plant', 'guitar': 'Page', 'drum': 'Dave'}

# band2 = band.copy()
# band2['drum'] = 'Dave'
# print('Good copy!')
# print(band)  # {'vocals': 'Plant', 'guitar': 'Page'}
# print(band2)  # {'vocals': 'Plant', 'guitar': 'Page', 'drum': 'Dave'}

# or use the dict() constructor function
# band3 = dict(band)
# band3['drum'] = 'Bonham'
# print('Good copy!')
# print(band)  # {'vocals': 'Plant', 'guitar': 'Page'}
# print(band3)  # {'vocals': 'Plant', 'guitar': 'Page', 'drum': 'Bonham'}

# ======= NESTED DICTIONARIES =======
# member1 = {
#     'name': 'Plant',
#     'instrument': 'vocals'
# }
# member2 = {
#     'name': 'Page',
#     'instrument': 'guitar'
# }
# band = {
#     'member1': member1,
#     'member2': member2,
# }

# print(band['member1']['name'])  # Plant

# ======= SETS =======
# nums = {1, 2, 3, 4}
# nums2 = set((1, 2, 3, 4))

# print(nums)  # {1, 2, 3, 4}
# print(nums2)  # {1, 2, 3, 4}
# print(type(nums))  # <class 'set'>
# print(type(nums2))  # <class 'set'>
# print(len(nums))  # 4

# ======= NO DUPLICATE ALLOWED =======
# nums = {1, 2, 2, 3}
# print(nums)  # {1, 2, 3}
# print(len(nums))  # 3

# ======= TRUE IS A DUPE OF 1, FALSE IS A DUPE OF ZERO =======
# nums = {1, True, 2, False, 3, 4, 0}
# print(nums)  # {False, 1, 2, 3, 4}

# ======= CHECK IF A VALUE IS IN A SET =======
# nums = {1, True, 2, False, 3, 4, 0}
# print(nums)  # {False, 1, 2, 3, 4}

# print(2 in nums)  # True
# print(1 in nums)  # True
# print(True in nums)  # True
# print(False in nums)  # True
# print(0 in nums)  # True
# print(1000 in nums)  # False

# BUT YOU CANNOT REFER TO AN ELEMENT IN THE SET
# WITH AN INDEX POSITION OR A KEY

# ======= ADD A NEW ELEMENT TO A SET =======
# nums = {1, 2, 3, 4}
# nums.add(8)
# print(nums)  # {1, 2, 3, 4, 8}

# ======= ADD ELEMENTS FROM ONE SET TO ANOTHER =======
# nums = {1, 2, 3, 4}
# more_nums = {1, 5, 6, 7}
# nums.update(more_nums)
# print(nums)  # {1, 2, 3, 4, 5, 6, 7}

# YOU CAN USE UPDATE WITH LISTS, TUPLES, AND DICTIONARIES, TOO.

# ======= MERGE TWO SETS TO CREATE A NEW SET =======
# one = {1, 2, 3}
# two = {5, 6, 7, 1}
# my_new_set = one.union(two)
# print(my_new_set)  # {1, 2, 3, 5, 6, 7}
# print(one)  # {1, 2, 3}
# print(two)  # {1, 5, 6, 7}


# ======= KEEP ONLY THE DUPLICATES =======
# one = {1, 2, 3}
# two = {4, 2, 5, 3}

# one.intersection_update(two)
# print(one)  # {2, 3}
# print(two)  # {2, 3, 4, 5}

# new_set = one.intersection(two)
# print(new_set)  # {2, 3}
# print(one)  # {1, 2, 3}
# print(two)  # {2, 3, 4, 5}

# ======= KEEP EVERYTHING EXCEPT THE DUPLICATES =======
one = {1, 2, 3}
two = {4, 2, 5, 3}

one.symmetric_difference_update(two)
print(one)  # {1, 4, 5}

one.di
