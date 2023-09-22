fname = input('Where will the number will be stored? ')
fout = open(fname, 'w')
limit = int(input('What is the maximum value? '))
for i in range(1, limit + 1):
    fout.write(f'{i}\n')

fout.close()