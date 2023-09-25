##
# Exercise 158:Remove Comments
# Python uses the # character to mark the beginning of a comment. The comment
# continues from the # character to the end of the line containing it. Python does not
# provide any mechanism for ending a comment before the end of a line.

# In this exercise, you will create a program that removes all of the comments from a
# Python source file. Check each line in the file to determine if a # character is present.
# If it is then your program should remove all of the characters from the # character to
# the end of the line (we will ignore the situation where the comment character occurs
# inside of a string). Save the modified file using a new name. Both the name of the
# input file and the name of the output file should be read from the user. Ensure that an
# appropriate error message is displayed if a problem is encountered while accessing
# either of the files.
#

import os


def get_full_path(file_name):
    # This function returns the path of the file
    absolute_path = os.path.dirname(__file__)
    relative_path = ''
    # relative_path = 'src/lib'
    full_path = os.path.join(absolute_path, relative_path)
    return f'{full_path}/{file_name}'


def remove_comment(inp, out):
    # Open the input file
    try:
        fhand = open(get_full_path(inp))
    except:
        print(f'File cannot be opened: {inp}')
        print('Quitting...')
        exit()

    # Open the output file
    try:
        fout = open(get_full_path(out), 'w')
    except:
        fhand.close()
        print(f'File cannot be written: {out}')
        print('Quitting...')
        exit()

    # Read all of the lines from the input file, remove the comments from them,
    # and save the modified lines to a new file
    try:
        for line in fhand:
            # Find the position of the comment character (-1 if there isn't one)
            pos = line.find('#')

            # If there is a commnent then create a slice of the string that excludes it
            # and store it back into line
            if pos > -1:
                line = line[:pos]
                line = f'{line}\n'

            # Write the (potential modified) line to the file
            fout.write(line)
            print(line.rstrip())

        # Close the files
        fhand.close()
        fout.close()
    except Exception as err:
        print('A problem was encountered while processing the file.')
        print(err)
        print('Quitting...')
        exit()


# def remove_comment(inp, out):
#     try:
#         fhand = open(get_full_path(inp))
#     except:
#         print(f'File cannot be opened: {inp}')
#         exit()
#     s = ''
#     for line in fhand:
#         if '#' in line:
#             i1 = line.find('#')
#             i2 = line.find("'")
#             i3 = line.find('"')

#             if i2 != -1 and i2 < i1:
#                 s += line
#                 continue
#             if i3 != -1 and i3 < i1:
#                 s += line
#                 continue
#             i = line.find('#')
#             line = line[:i]
#             s += f'{line}\n'
#     print(s)


def main():
    # inp = 'sample_input.py'
    # out = 'sample_ouput.py'
    inp = input('Enter a name of a Python file: ')
    out = input('Enter the output file name: ')
    remove_comment(inp, out)


if __name__ == '__main__':
    main()
