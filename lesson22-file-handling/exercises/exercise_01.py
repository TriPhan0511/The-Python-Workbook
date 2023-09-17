##
# Exercise 1: Write a program to read through a file and print the contents
# of the file (line by line) all in upper case. Executing the program will
# look as follows:

# python shout.py
# Enter a file name: mbox-short.txt
# FROM STEPHEN.MARQUARD@UCT.AC.ZA SAT JAN 5 09:14:16 2008
# RETURN-PATH: <POSTMASTER@COLLAB.SAKAIPROJECT.ORG>
# RECEIVED: FROM MURDER (MAIL.UMICH.EDU [141.211.14.90])
# BY FRANKENSTEIN.MAIL.UMICH.EDU (CYRUS V2.3.8) WITH LMTPA;
# SAT, 05 JAN 2008 09:14:16 -0500
#

def upper_and_print():
    while True:
        file_name = input('\nEnter a file name:\n')
        try:
            fhand = open(file_name)
        except FileNotFoundError:
            print(f'\nThe file was not found.\nPlease enter another file name.')
            continue
        else:
            for line in fhand:
                print(line.strip().upper())
            break


def main():
    upper_and_print()


if __name__ == '__main__':
    main()
