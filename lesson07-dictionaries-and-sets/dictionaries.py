# ======= DICTIONARIES =======
band = {
    'vocal': 'Plant',
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
# print(band['vocal'])  # Plant
# print(band.get('guitar'))  # Page

# ======= LIST ALL KEYS =======
# print(band.keys())  # dict_keys(['vocal', 'guitar'])

# ======= LIST ALL VALUES =======
# print(band.values())  # dict_values(['Plant', 'Page'])

# ======= LIST OF KEY/VALUE PAIRS AS TUPLES =======
# print(band.items())  # dict_items([('vocal', 'Plant'), ('guitar', 'Page')])

# ======= VERIFY A KEY EXISTS =======
print('guitar' in band)  # True
print('triangle' in band)  # False
print('Page' in band)  # False
