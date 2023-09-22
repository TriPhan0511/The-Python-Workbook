##
# Exercise 152: Number the Lines in a File
# Create a program that reads lines from a file, adds line numbers to them, and then
# stores the numbered lines into a new file. The name of the input file will be read from
# the user, as will the name of the new file that your program will create. Each line in
# the output file should begin with the line number, followed by a colon and a space,
# followed by the line from the input file.
#

# # The new file has a NEW NAME:
# def number_the_lines(file_name):
#     try:
#         fhand = open(file_name)
#     except:
#         print(f'File cannot be opened: {file_name}')
#         exit()

#     new_file_name = f"{file_name.lower().replace('.txt', '')}_NUMBERED_LINES.txt"
#     fout = open(new_file_name, 'w')
#     line_number = 1
#     for line in fhand:
#         fout.write(f'{line_number}: {line}')
#         line_number += 1
#     fhand.close()
#     fout.close()
#     print('Done!')
# -------------------------------------------

# # The new file has the SAME NAME with the input file:
def read_file(file_name):
    try:
        fhand = open(file_name)
    except:
        print(f'File cannot be opened: {file_name}')
        exit()
    s = ''
    line_number = 1
    for line in fhand:
        s += f'{line_number}: {line}'
        line_number += 1
    fhand.close()
    return s


def write_file(file_name, s):
    try:
        fout = open(file_name, 'w')
    except:
        print(f'File cannot be opened: {file_name}')
        exit()
    fout.write(s)
    fout.close()


def number_the_lines(file_name):
    s = read_file(file_name)
    write_file(file_name, s)
    print('Done!')


def main():
    file_name = 'text.txt'
    # file_name = 'MBOX-SHORT.TXT'
    # file_name = 'notfound.txt'

    # file_name = input('Enter a file name: ')
    number_the_lines(file_name)


if __name__ == '__main__':
    main()
