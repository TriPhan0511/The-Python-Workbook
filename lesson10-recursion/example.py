# value = True
value = 'y'  # same as value = True
count = 0
while value:
    count += 1
    print(count)
    if count == 5:
        break
    else:
        value = 0  # sames as value = False
        continue
