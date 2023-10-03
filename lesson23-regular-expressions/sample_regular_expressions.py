import os
import re


def get_full_path(file_name):
    return f'{os.path.dirname(__file__)}/{file_name}'


# # Search for lines that contain "From":
# file_name = 'mbox-short.txt'
# fhand = open(get_full_path(file_name))
# for line in fhand:
#     line = line.rstrip()
#     if re.search('From:', line):
#         print(line)

# -----------------------------------------------------------------

# The caret character (^) is used in regular expressions to match "the beginning" of a line.

# # Change our program to only match lines where "From:" was at beginning of the lines
# file_name = 'mbox-short.txt'
# fhand = open(get_full_path(file_name))
# for line in fhand:
#     line = line.rstrip()
#     if re.search('^From:', line):
#         print(line)


# ========== Character matching in regular expressions ==========

# The period or full stop (.) is used to match any character.

# # In the following example, the regular expression F..m: would match any of the
# # strings “From:”, “Fxxm:”, “F12m:”, or “F!@m:” since the period characters in the
# # regular expression match any character.

# file_name = 'mbox-short.txt'
# fhand = open(get_full_path(file_name))
# for line in fhand:
#     line = line.rstrip()
#     if re.match('^F..m:', line):
#         print(line)

# The period character (.) is particularly powerful when combined with the ability to indicate
#  that a character can be repeated any number of times using the * or + characters in your
# regular expression. These special characters mean that instead of matching a single
# character in the search string, they match zero-or-more characters (in the case of
# the asterisk) or one-or-more of the characters (in the case of the plus sign).

# We can further narrow down the lines that we match using a repeated wild card
# character in the following example:

# # Search for lines that start with From and have an at sign
# file_name = 'mbox-short.txt'
# fhand = open(get_full_path(file_name))
# for line in fhand:
#     line = line.rstrip()
#     if re.match('^From:.+@', line):
#         print(line)

# The search string ˆFrom:.+@ will successfully match lines that start with “From:”,
# followed by one or more characters (.+), followed by an at-sign. So this will match
# the following line:

# From: stephen.marquard@uct.ac.za

# You can think of the .+ wildcard as expanding to match all the characters between
# the colon character and the at-sign.

# From:.+@

# It is good to think of the plus and asterisk characters as “pushy”. For example,
# the following string would match the last at-sign in the string as the .+ pushes
# outwards, as shown below:

# From: stephen.marquard@uct.ac.za, csev@umich.edu, and cwen @iupui.edu

# ========== Extracting data using regular expressions ==========

# If we want to extract data from a string in Python we can use the findall()
# method to extract all of the substrings which match a regular expression.

# Sample: Pull the email addresses from each of the following line:

# The findall() method searches the string in the second argument and returns a
# list of all of the strings that look like email addresses.
#  We are using a two-character sequence that matches a non-whitespace character (\S).

# s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
# lst = re.findall('\S+@\S+', s)

# Output:
# ['csev@umich.edu', 'cwen@iupui.edu']

# Translating the regular expression, we are looking for substrings that have at least
# one non-whitespace character, followed by an at-sign, followed by at least one more
# non-whitespace character. The \S+ matches as many non-whitespace characters
# as possible.

# The regular expression would match twice (csev@umich.edu and cwen@iupui.edu),
# but it would not match the string “@2PM” because there are no non-blank characters
# before the at-sign.

# # We can use this regular expression in a program to read all the lines in a file
# # and print out anything that looks like an email address as follows:
# file_name = 'mbox-short.txt'
# fhand = open(get_full_path(file_name))
# for line in fhand:
#     line = line.rstrip()
#     lst = re.findall('\S+@\S+', line)
#     if len(lst) > 0:
#         print(lst)

# Ouput:
# ['stephen.marquard@uct.ac.za']
# ['<postmaster@collab.sakaiproject.org>']
# ['<200801051412.m05ECIaH010327@nakamura.uits.iupui.edu>']
# ['<source@collab.sakaiproject.org>;']
# ['<source@collab.sakaiproject.org>;']
# ['<source@collab.sakaiproject.org>;']
# ['apache@localhost)']
# ['source@collab.sakaiproject.org;']
# ...

# Some of our email addresses have incorrect characters like “<” or “;” at the beginning
# or end. Let’s declare that we are only interested in the portion of the string
# that starts and ends with a letter or a number.

# To do this, we use another feature of regular expressions. Square brackets are used
# to indicate a set of multiple acceptable characters we are willing to consider matching.
# In a sense, the \S is asking to match the set of “non-whitespace characters”.
# Now we will be a little more explicit in terms of the characters we will match.

# Here is our new regular expression:

# [a-zA-Z0-9]\S*@\S*[a-zA-Z]

# # Sample:
# # Search for lines that have an at sign between characters
# # The characters must be a letter of number
# file_name = 'mbox-short.txt'
# fhand = open(get_full_path(file_name))
# for line in fhand:
#     line = line.rstrip()
#     lst = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]', line)
#     if len(lst) > 0:
#         print(lst)

# Output:
# ['stephen.marquard@uct.ac.za']
# ['postmaster@collab.sakaiproject.org']
# ['200801051412.m05ECIaH010327@nakamura.uits.iupui.edu']
# ['source@collab.sakaiproject.org']
# ['source@collab.sakaiproject.org']
# ['source@collab.sakaiproject.org']
# ['apache@localhost']
# ['source@collab.sakaiproject.org']
# ...

# Translating this regular expression: [a-zA-Z0-9]\S*@\S*[a-zA-Z]
# We are looking for substrings that start with a single lowercase letter, uppercase
# letter, or number “[a-zA-Z0-9]”, followed by zero or more non-blank characters
# (\S*), followed by an at-sign, followed by zero or more non-blank characters (\S*),
# followed by an uppercase or lowercase letter.

# Note that we switched from + to * to indicate zero or more non-blank characters
# since [a-zA-Z0-9] is already one non-blank character.
# Remember that the * or + applies to the single character immediately to the left of the plus or asterisk.

# ========== Combining searching and extracting ==========

# pattern = 'X-\S+-\S+: [0-9.]+'
# lst = re.findall(pattern, s)
# for i in lst:
#     num = float(i[i.find(':')+2:])
#     print(num)

# Sample:
# Search for lines that starts with 'X' followed by any non-whitespace characters and ':'
# followed by a space and any number.
# The number can include a decimal

# file_name = 'mbox-short.txt'
# fhand = open(get_full_path(file_name))
# for line in fhand:
#     line = line.rstrip()
#     if re.search('^X\S*: [0-9.]+', line):
#         print(line)

# Output:
# X-DSPAM-Confidence: 0.8475
# X-DSPAM-Probability: 0.0000
# X-DSPAM-Confidence: 0.6178
# X-DSPAM-Probability: 0.0000
# ...

# But now we have to solve the problem of extracting the numbers. While it would
# be simple enough to use the split fucntion, we can use another feature of regular expressions
# to both search and parse the line at the same time.

# Parentheses are another special character in regular expressions. When you add
# parentheses to a regular expression, they are ignored when matching the string.
# But when you are using findall(), parentheses indicate that while you want the
# whole expression to match, you only are interested in extracting a portion of the
# substring that matches the regular expression.

# Sample:
# Search for lines that starts with 'X' followed by any non-whitespace characters and ':'
# followed by a space and any number.
# The number can include a decimal.
# The print the number if it is greater than zero.

# file_name = 'mbox-short.txt'
# fhand = open(get_full_path(file_name))
# for line in fhand:
#     line = line.rstrip()
#     lst = re.findall('^X\S*: ([0-9.]+)', line)
#     if len(lst) > 0:
#         # # print(lst)
#         # Output:
#         # ['0.8475']
#         # ['0.0000']
#         # ['0.6178']
#         # ['0.0000']
#         # ...
#         lst = [float(num) for num in lst]
#         for num in lst:
#             if num > 0:
#                 print(num)

# # Output:
# # 0.8475
# # 0.6178
# # 0.6961
# # 0.7565
# # ...

# Sample:
# In the file 'mbox-short.txt', there are a number of lines of the form:

# Details: http://source.sakaiproject.org/viewsvn/?view=rev&rev=39772

# Extract all of the revision numbers (the integer number at the end of these lines)
# using the same technique as above

# file_name = 'mbox-short.txt'
# fhand = open(get_full_path(file_name))
# for line in fhand:
#     line = line.rstrip()
#     nums = re.findall('^Details:.*rev=([0-9]+)', line)
#     if len(nums) > 0:
#         print(nums)

# Output:
# ['39772']
# ['39771']
# ['39770']
# ['39769']
# ...

# Translating our regular expression, we are looking for lines that start with
# Details:, followed by any number of characters (.*), followed by rev=, and then
# by one or more digits. We want to find lines that match the entire expression but
# we only want to extract the integer number at the end of the line, so we surround
# [0-9]+ with parentheses.

# Remember that the [0-9]+ is “greedy” and it tries to make as large a string of
# digits as possible before extracting those digits. This “greedy” behavior is why we
# get all five digits for each number. The regular expression library expands in both
# directions until it encounters a non-digit, or the beginning or the end of a line.

# Sample
# Search for lines that start with 'From' and any character
# followed by a two digit number between 00 and 99 and follwed by ':'
# Then print the number

# A sample line:

# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

# file_name = 'mbox-short.txt'
# fhand = open(get_full_path(file_name))
# for line in fhand:
#     line = line.rstrip()
#     lst = re.findall('^From .* ([0-9][0-9]):', line)
#     if len(lst) > 0:
#         print(lst)

# Output:
# ['09']
# ['18']
# ['16']
# ['15']
# ...

# The translation of this regular expression is that we are looking for lines that start
# with From (note the space), followed by any number of characters (.*), followed by
# a space, followed by two digits [0-9][0-9], followed by a colon character. This is
# the definition of the kinds of lines we are looking for.

# ========== Escape character ==========

# Since we use special characters in regular expressions to match the beginning or
# end of a line or specify wild cards, we need a way to indicate that these characters
# are “normal” and we want to match the actual character such as a dollar sign or caret.

# We can indicate that we want to simply match a character by prefixing that character
# with a backslash. For example, we can find money amounts with the following
# regular expression.

# s = 'We just received $10.00 for cookies.'
# lst = re.findall('\$([0-9.]+) .*', s)
# print(lst)

# Output:
# ['10.00']


# Since we prefix the dollar sign with a backslash, it actually matches the dollar
# sign in the input string instead of matching the “end of line”, and the rest of
# the regular expression matches one or more digits or the period character.

# Note:
# Inside square brackets, characters are not “special”. So when we say [0-9.], it
# really means digits or a period. Outside of square brackets, a period is the “wildcard”
# character and matches any character. Inside square brackets, the period is a period.

# ========== Summary ==========

# While this only scratched the surface of regular expressions, we have learned a bit
# about the language of regular expressions. They are search strings with special
# characters in them that communicate your wishes to the regular expression system
# as to what defines “matching” and what is extracted from the matched strings.

# Here are some of those special characters and character sequences:

# ^ Matches the beginning of the line.

# $ Matches the end of the line.

# . Matches any character (a wildcard).

# \s Matches a whitespace character.

# \S Matches a non-whitespace character (opposite as \s).

# * Applies to the immediately preceding character(s) and indicates to match zero
#   or more times.

# *? Applies to the immediately preceding character(s) and indicates to match zero
#   or more times in "non-greedy mode".

# + Applies to the immediately preceding character(s) and indicates to match one
#   or more times.

# +? Applies to the immediately preceding character(s) and indicates to match one
#   or more times in "non-greedy mode".

# ? Applies to the immediately preceding character(s) and indicates to match zero
#   or one times.

# ?? Applies to the immediately preceding character(s) and indicates to match zero
#   or one time in "non-greedy mode".

# [aeiou] Matches a single character as long as that character is in the specified set.
#   In this example, it would match "a", "e", "i", "o", "u", but no other characters.

# [a-z0-9] You can specify ranges of characters using the minus sign.
#   This example is a single character that must be a lowercase letter or a digit.

# [^A-Za-z] When the first character in the set notation is a caret, it inverts the logic.
#   This example matches a single character that
#   is anything other than an uppercase or lowercase letter.

# () When parentheses are added to a regular expression, they are ignored for the
#   purpose of matching, but allow you to extract a particular subset of the matched
#   string rather than the whole string when using findall().

# \b Matches the empty string, but only at the start or end of a word.

# \B Matches the empty string, but not only at the start or end of a word.

# \d Matches any decimal digit; equivalent to the set [0-9].

# \D Matches any non-digit character; equivalent to the set [^0-9].


# -----------------------------------------------------------------------

# Sample 1: ^ Matches the beginning of the line.

# s = "My name's David."
# # s = "And My name's David."
# lst = re.findall('^My .+ ([a-zA-Z]+)', s)
# print(lst)  # ['David']

# -----------------------------------------------------------------------

# Sample 2: $ Matches the end of the line

# s = 'I am 12'
# # s = 'I am 12 year old'
# lst = re.findall('.+ ([0-9]+$)', s)
# # lst = re.findall('.+ ([0-9]+)$', s)
# print(lst)  # ['12']
