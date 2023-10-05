import os
from urllib.request import urlopen

# #
# Exercise 3: Use urllib to replicate the previous exercise of (1) retrieving
# the document from a URL, (2) displaying up to 3000 characters, and
# (3) counting the overall number of characters in the document. Don’t
# worry about the headers for this exercise, simply show the first 3000
# characters of the document contents.
#


def get_full_path(file_name):
    return f'{os.path.dirname(__file__)}/{file_name}'


def get_file_name(url):
    # Get the last "word"
    words = url.strip().split('/')
    return words[-1]


def save_text_file(url):
    try:
        fhand = urlopen(url)
    except:
        print(f'Something went wrong when connecting to {url}')
        exit()
    file_name = get_file_name(url)
    fout = open(get_full_path(file_name), 'w')
    while True:
        data = fhand.read(100000)
        if len(data) < 1:
            break
        fout.write(data.decode().strip())
    fout.close()
    print('A text file was saved.')
    # return (info.decode(), len(info))

# def get_and_count_text(url):
#     try:
#         f = urlopen(url)
#     except:
#         print(f'Something went wrong when connecting to {url}')
#         exit()
#     info = b''
#     while True:
#         data = f.read(100000)
#         if len(data) < 1:
#             break
#         info += data
#     return (info.decode(), len(info))


def display_text(url, limit):
    (info, count) = save_text_file(url)
    print(
        f'\n***** The first {limit} characters of the doument contents: *****\n')
    print(info[:limit])
    print(f'\n***** Received {count} characters in total. *****')


def main():
    # url = input('Enter a link (sample: http://data.pr4e.org/romeo.txt):\n')
    # url = 'http:/data.pr4e.org/romeo.txt'
    # url = 'http://data.pr4e.org'
    # url = 'http://data.pr4e.org/romeo.txt'
    url = 'http://data.pr4e.org/romeo-full.txt'
    limit = 3000

    # display_text(url, limit)

    save_text_file(url)


if __name__ == '__main__':
    main()
