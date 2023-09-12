# # Exercise 113:Avoiding Duplicates

# In this exercise, you will create a program that reads words from the user until the
# user enters a blank line. After the user enters a blank line your program should display
# each word entered by the user exactly once. The words should be displayed in
# the same order that they were first entered. For example, if the user enters:

# first
# second
# first
# third
# second

# then your program should display:

# first
# second
# third

def remove_duplicates():
    data = []
    while True:
        word = input('\nEnter a word (blank line to quit): ')
        if not word.strip():
            break
        if word.strip() not in data:
            data.append(word)
    return data


def display_data(data):
    if len(data) == 0:
        print('Empty')
    else:
        for item in data:
            print(item)


if __name__ == '__main__':
    data = remove_duplicates()
    display_data(data)
