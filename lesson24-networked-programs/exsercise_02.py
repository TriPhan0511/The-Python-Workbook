import socket
import re

# #
# Exercise 2: Change your socket program so that it counts the number
# of characters it has received and stops displaying any text after it has
# shown 3000 characters. The program should retrieve the entire docu-
# ment and count the total number of characters and display the count
# of the number of characters at the end of the document.
#


def get_socket(url):
    url = url.strip()
    if not re.search('^http[s]?://.+', url):
        print('The entered link is not an improperly formatted url.')
        return
    words = url.split('/')
    if len(words) < 4:
        print('Wrong input')
        return
    host = words[2]
    port = 80
    try:
        my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        my_sock.connect((host, port))
        cmd = f'GET {url} HTTP/1.0\r\n\r\n'.encode()
        my_sock.send(cmd)
    except:
        print('Something went wrong when open connection.')
        return
    return my_sock


def get_and_count_text(url):
    try:
        my_sock = get_socket(url)
    except:
        print(f'Can not open connection to {url}')
        exit()
    count = 0
    info = b''
    while True:
        try:
            data = my_sock.recv(5120)
        except:
            print('Something went wrong when receiving data.')
            exit()
        if len(data) < 1:
            break
        info += data
        count += len(data)
    my_sock.close()
    return (info.decode(), count)


def display_text(url, limit):
    (info, count) = get_and_count_text(url)

    # # The first {limit} characters in the doument
    # print(f'\n***** The first {limit} characters in the doument: *****\n')
    # print(info[:limit])

    # The first {limit} characters after headers in the doument
    print(
        f'\n***** The first {limit} characters after headers in the doument: *****\n')
    pos = info.find('\r\n\r\n')
    info = info[pos+4:]
    print(info[:limit])

    print(f'\n***** Received {count} characters in total. *****')


def main():
    # url = input('Enter a link (sample: http://data.pr4e.org/romeo.txt):\n')
    # url = 'http:/data.pr4e.org/romeo.txt'
    # url = 'http://data.pr4e.org'
    # url = 'http://data.pr4e.org/romeo.txt'
    url = 'http://data.pr4e.org/romeo-full.txt'
    limit = 3000

    display_text(url, limit)


if __name__ == '__main__':
    main()
