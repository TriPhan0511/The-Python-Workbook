# # Exercise 136: Reverse Lookup

# Write a function named reverseLookup that finds all of the keys in a dictionary
# that map to a specific value. The function will take the dictionary and the value to
# search for as its only parameters. It will return a (possibly empty) list of keys from
# the dictionary that map to the provided value.
# Include a main program that demonstrates the reverseLookup function as part
# of your solution to this exercise. Your program should create a dictionary and then
# show that the reverseLookup function works correctly when it returns multiple
# keys, a single key, and no keys. Ensure that your main program only runs when
# the file containing your solution to this exercise has not been imported into another
# program.

def reverseLookup(data, value):
    results = []
    if not isinstance(data, dict):
        return
    for k, v in data.items():
        if v == value:
            results.append(k)
    return results


def main():
    # Create a dictionary
    frEn = {'le': 'the', 'la': 'the', 'livre': 'book', 'prome': 'apple'}

    # Call the reverseLookup function
    results = reverseLookup(frEn, 'the')  # ['le', 'la']
    results = reverseLookup(frEn, 'book')  # ['livre']
    results = reverseLookup(frEn, 'song')  # []

    # Display the results
    print(results)


if __name__ == '__main__':
    main()
