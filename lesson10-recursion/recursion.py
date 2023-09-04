def add_one(num):
    if num >= 9:
        return num + 1
    total = num + 1
    print(total)
    return add_one(total)


new_total = add_one(0)
print(f'new_total = {new_total}')

# Recursion vs Loops


def add_one_2(num):
    if num >= 9:
        return num + 1
    else:
        for _ in range(10):
            num += 1
            print(num)
    return num


new_total_2 = add_one_2(0)
print(f'new_total_2 = {new_total_2}')
