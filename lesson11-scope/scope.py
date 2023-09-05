# ======= GLOBAL SCOPE VS LOCAL SCOPE =======
# name = 'Dave'  # Global variable: Available to everything in this file.


# def greeting(name):
#     color = 'blue'  # Local variable
#     print(color)
#     print(name)


# greeting('John')
# # blue
# # John

# ======= SCOPE APPLIES TO FUNCTIONS, TOO =======
# def another():
#     color = 'blue'

#     def greeting(name):
#         print(color)
#         print(name)

#     greeting('Dave')


# # Call the another() function
# another()
# # blue
# # Dave

# ======= THE global KEYWORD =======
# count = 1
# print(count)  # 1


# def another():
#     # Modify a global variable
#     global count
#     count += 1
#     print(count)  # 2


# # Call the another() function
# another()

# # Display the value of "count" variable
# print(count)  # 2 (This globale varaible has been modified.)


# ======= THE nonlocal KEYWORD =======
def another():
    color = 'blue'

    def greeting():
        # Modify a variable of outside function
        nonlocal color
        color = 'red'
        print(color)  # red

    # Call the greeting() function
    greeting()

    # Display the value of the "color" variable
    print(color)  # red


# Call the another() function
another()
