import os
import re
import urllib.request

# #
# Parsing HTML using regular expressions

# One simple way to parse HTML is to use regular expressions to repeatedly search
# for and extract substrings that match a particular pattern.
#


a_page = '''
<h1>The First Page</h1>
<p>
If you like, you can switch to the
<a href="http://www.dr-chuck.com/page2.html">
Second Page</a>.
</p>
'''

pattern = '"(http[s]?://.+?)"'
lst = re.findall(pattern, a_page)  # ['http://www.dr-chuck.com/page2.html']
print(lst)

# Our regular expression looks for strings that start with “href="http://” or
# “href="https://”, followed by one or more characters (.+?), followed by another
# double quote. The question mark behind the [s]? indicates to search for the
# string “http” followed by zero or one “s”.

# The question mark added to the .+? indicates that the match is to be done in
# a “non-greedy” fashion instead of a “greedy” fashion. A non-greedy match tries
# to find the smallest possible matching string and a greedy match tries to find the
# largest possible matching string.

# We add parentheses to our regular expression to indicate which part of our matched
# string we would like to extract, and produce the following program:
