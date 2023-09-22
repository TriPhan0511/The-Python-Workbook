##
# Exercise 153: Find the Longest Word in a File
# In this exercise you will create a Python program that identifies the longest word(s)
# in a file. Your program should output an appropriate message that includes the length
# of the longest word, along with all of the words of that length that occurred in the file.
# Treat any group of non-white space characters as a word, even if it includes digits or
# punctuation marks.
#

import string


def find_the_longest_word(file_name):
    try:
        fhand = open(file_name)
    except:
        print(f'File cannot be opened: {file_name}')
        exit()

    counts = {}
    for line in fhand:
        line = line.strip()
        line = line.lower()
        words = line.split()
        for word in words:
            # Remove punctuation marks
            word = word.translate(word.maketrans('', '', string.punctuation))
            counts[word] = counts.get(word, 0) + 1

    result = [(value, key) for key, value in counts.items()]
    result.sort(reverse=True)
    # print(result)
    print('\nTen words have longest length are:')
    for w in result[:10]:
        print(f'{w[0]} {w[1]}')


def main():
    file_name = 'romeo-full.txt'
    # file_name = 'romeo.txt'
    find_the_longest_word(file_name)


if __name__ == '__main__':
    main()
