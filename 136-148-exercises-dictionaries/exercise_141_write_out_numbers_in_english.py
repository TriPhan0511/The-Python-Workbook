# # Exercise 141: Write out Numbers in English

# While the popularity of cheques as a payment method has diminished in recent years,
# some companies still issue them to pay employees or vendors. The amount being
# paid normally appears on a cheque twice, with one occurrence written using digits,
# and the other occurrence written using English words. Repeating the amount in two
# different formsmakes it much more difficult for an unscrupulous employee or vendor
# to modify the amount on the cheque before depositing it.

# In this exercise, your task is to create a function that takes an integer between 0 and
# 999 as its only parameter, and returns a string containing the English words for that
# number. For example, if the parameter to the function is 142 then your function should
# return “one hundred forty two”. Use one or more dictionaries to implement
# your solution rather than large if/elif/else constructs. Include a main program that
# reads an integer from the user and displays its value in English words.

# 1-9: one-nine
# 10: ten
# 11: eleven

NUMBERS_IN_ENGLISH = {
    '1':'','2':'','3':'','4':'','5':'',
    '6':'','7':'','8':'','9':'','10':'',
    '11':'','12':'','13':'','14':'','15':'',
    '16':'','17':'','18':'','19':'','20':'',
    '':'','':'','':'','':'','':'',
    '':'','':'','':'','':'','':'',
    '':'','':'','':'','':'','':'',
    '':'','':'','':'','':'','':'',
    '':'','':'','':'','':'','':'',
    '':'','':'','':'','':'','':'',
    '':'','':'','':'','':'','':'',
    '':'','':'','':'','':'','':'',
}