# As the programs that we write grow, we need to take steps to make them easier to
# develop and debug. One way that we can do this is by breaking the program’s code
# into sections called functions.
# Functions serve several important purposes: They let us write code once and then
# call it from many locations, they allow us to test different parts of our solution
# individually, and they allow us to hide (or at least set aside) the details once we
# have completed part of our program. Functions achieve these goals by allowing the
# programmer to name and set aside a collection of Python statements for later use.
# Then our program can cause those statements to execute whenever they are needed.
# The statements are named by defining a function. The statements are executed by
# calling a function. When the statements in a function finish executing, control returns
# to the location where the function was called and the program continues to execute
# from that location.

# The programs that you have written previously called functions like print,
# input, int and float. All of these functions have already been defined by the
# people that created the Python programming language, and these functions can be
# called in any Python program. In this chapter you will learn how to define and call
# your own functions, in addition to calling those that have been defined previously.
# A function definition begins with a line that consists of def, followed by the
# name of the function that is being defined, followed by an open parenthesis, a close
# parenthesis and a colon. This line is followed by the body of the function, which is
# the collection of statements that will execute when the function is called. As with the
# bodies of if statements and loops, the bodies of functions are indented. A function’s
# body ends before the next line that is indented the same amount as (or less than) the
# line that begins with def. For example, the following lines of code define a function
# that draws a box constructed from asterisk characters.

# def drawBox():
# print("**********")
# print("* *")
# print("* *")
# print("**********")

# On their own, these lines of code do not produce any output because, while the
# drawBox function has been defined, it is never called. Defining the function sets
# these statements aside for future use and associates the name drawBox with them,
# but it does not execute them. A Python program that consists of only these lines is a
# valid program, but it will not generate any output when it is executed.
# The drawBox function is called by using its name, followed by an open parenthesis
# and a close parenthesis. Adding the following line to the end of the previous
# program (without indenting it) will call the function and cause the box to be drawn.
# drawBox()

# Adding a second copy of this line will cause a second box to be drawn and adding
# a third copy of it will cause a third box to be drawn. More generally, a function can
# be called as many times as needed when solving a problem, and those calls can be
# made from many different locations within the program. The statements in the body
# of the function execute every time the function is called. When the function returns
# execution continues with the statement immediately after the function call.

# 4.1 Functions with Parameters
# The drawBox function works correctly. It draws the particular box that it was
# intended to draw, but it is not flexible, and as a result, it is not as useful as it could be.
# In particular, our function would be more flexible and useful if it could draw boxes
# of many different sizes.
# Many functions take arguments which are values provided inside the parentheses
# when the function is called. The function receives these argument values in parameter
# variables that are included inside the parentheses when the function is defined. The
# number of parameter variables in a function’s definition indicates the number of
# arguments that must be supplied when the function is called.
# We can make the drawBox function more useful by adding two parameters to its
# definition. These parameters, which are separated by a comma, will hold the width
# of the box and the height of the box respectively. The body of the function uses the
# values in the parameter variables to draw the box, as shown below. An if statement
# and the quit function are used to end the program immediately if the arguments
# provided to the function are invalid.

# def drawBox():
#     print("**********")
#     print("*        *")
#     print("*        *")
#     print("**********")


# drawBox()

# def drawBox(width, height):
#     # A box that is smaller than 2x2 cannot be drawn by this function
#     if width < 2 or height < 2:
#         print("Error: The width or height is too small.")
#         quit()
#     # Draw the top of the box
#     print("*" * width)
#     # Draw the sides of the box
#     for i in range(height - 2):
#         print("*" + " " * (width - 2) + "*")
#     # Draw the bottom of the box
#     print("*" * width)


# drawBox(10, 4)

# Two arguments must be supplied when the drawBox function is called because
# its definition includes two parameter variables. When the function executes the value
# of the first argument will be placed in the first parameter variable, and similarly, the
# value of the second argument will be placed in the second parameter variable. For
# example, the following function call draws a box with a width of 15 characters and a
# height of 4 characters. Additional boxes can be drawn with different sizes by calling
# the function again with different arguments.

# drawBox(15, 4)

# In its current form the drawBox function always draws the outline of the box
# with asterisk characters and it always fills the box with spaces. While this may work
# well in many circumstances there could also be times when the programmer needs a
# box drawn or filled with different characters. To accommodate this, we are going to
# update drawBox so that it takes two additional parameters which specify the outline
# and fill characters respectively. The body of the function must also be updated to
# use these additional parameter variables, as shown below. A call to the drawBox
# function which outlines the box with at symbols and fills the box with periods is
# included at the end of the program.

# def draw_box(width, height, outline='*', fill=' '):
#     # A box that is smaller than 2x2 cannot be drawn by this function
#     if width < 2 or height < 2:
#         print('Error: The width or height is too small.')
#         quit()
#     # Draw the top of the box
#     print(outline * width)
#     # Draw the sides of the box
#     for i in range(height - 2):
#         print(f"{outline}{fill * (width - 2)}{outline}")
#     # Draw the bottom of the box
#     print(outline * width)


# draw_box(10, 1)
# draw_box(1, 10)
# draw_box(10, 4)
# draw_box(15, 7, ".", '@')

# The programmer will have to include the outline and fill values (in addition to the
# width and height) every time this version of drawBox is called. While needing to
# do so might be fine in some circumstances, it will be frustrating when asterisk and
# space are used much more frequently than other character combinations because these
# arguments will have to be repeated every time the function is called. To overcome
# this, we will add default values for the outline and fill parameters to the function’s
# definition. The default value for a parameter is separated from its name by an equal
# sign, as shown below.
# def drawBox(width, height, outline="*", fill=" "):

# Once this change is made drawBox can be called with two, three or four arguments.
# If drawBox is called with two arguments, the first argument will be placed
# in the width parameter variable and the second argument will be placed in the
# height parameter variable. The outline and fill parameter variables will
# hold their default values of asterisk and space respectively. These default values are
# used because no arguments were provided for these parameters when the function
# was called.
# Now consider the following call to drawBox:

# draw_box(10,4,'@')
# draw_box(10, 4, fill='@')


# 4.2 Variables in Functions
# When a variable is created inside a function the variable is local to that function. This
# means that the variable only exists when the function is executing and that it can only
# be accessed within the body of that function. The variable ceases to exist when the
# function returns, and as such, it cannot be accessed after that time. The drawBox
# function uses several variables to perform its task. These include parameter variables
# such as width and fill that are created when the function is called, as well as
# the for loop control variable, i, that is created when the loop begins to execute.
# All of these are local variables that can only be accessed within this function. Variables
# created with assignment statements in the body of a function are also local
# variables.

# 4.3 Return Values
# Our box-drawing function prints characters on the screen. While it takes arguments
# that specify how the box will be drawn, the function does not compute
# a result that needs to be stored in a variable and used later in the program. But
# many functions do compute such a value. For example, the sqrt function in the
# math module computes the square root of its argument and returns this value
# so that it can be used in subsequent calculations. Similarly, the input function
# reads a value typed by the user and then returns it so that it can be used later
# in the program. Some of the functions that you write will also need to return
# values.
# A function returns a value using the return keyword, followed by the value
# that will be returned. When the return executes the function ends immediately
# and control returns to the location where the function was called. For example, the
# following statement immediately ends the function’s execution and returns 5 to the
# location from which it was called.
# return 5

# Functions that return values are often called on the right side of an assignment
# statement, but they can also be called in other contexts where a value is needed. Examples
# of such include an if statement or while loop condition, or as an argument
# to another function, such as print or range.

# A function that does not return a result does not need to use the return keyword
# because the function will automatically return after the last statement in the function’s
# body executes. However, a programmer can use the return keyword, without a
# trailing value, to force the function to return at an earlier point in its body. Any
# function, whether it returns a value or not, can include multiple return statements.
# Such a function will return as soon as any of the return statements execute.
# Consider the following example.A geometric sequence is a sequence of terms that
# begins with some value, a, followed by an infinite number of additional terms. Each
# term in the sequence, beyond the first, is computed by multiplying its immediate
# predecessor by r , which is referred to as the common ratio. As a result, the terms
# in the sequence are a, ar, ar2, ar3, …. When r is 1, the sum of the first n terms of
# a geometric sequence is a × n. When r is not 1, the sum of the first n terms of a
# geometric sequence can be computed using the following formula.
# sum = a(1 − r n)
# 1 − r


# 4.4 Importing Functions into Other Programs
# One of the benefits of using functions is the ability to write a function once and
# then call it many times from different locations. This is easily accomplished when
# the function definition and call locations all reside in the same file. The function is
# defined and then it is called by using its name, followed by parentheses containing
# any arguments.

# At some point you will find yourself in the situation where you want to call a
# function that you wrote for a previous program while solving a new problem. New
# programmers (and even some experienced programmers) are often tempted to copy
# the function from the file containing the old program into the file containing the new
# one, but this is an undesirable approach. Copying the function results in the same
# code residing in two places. As a result, when a bug is identified it will need to be
# corrected twice.A better approach is to import the function from the old program into
# the new one, similar to the way that functions are imported from Python’s built-in
# modules.

# Functions from an old Python program can be imported into a new one using
# the import keyword, followed by the name of the Python file that contains the
# functions of interest (without the .py extension). This allows the new program to
# call all of the functions in the old file, but it also causes the program in the old file
# to execute. While this may be desirable in some situations, we often want access
# to the old program’s functions without actually running the program. This is normally
# accomplished by creating a function named main that contains the statements
# needed to solve the problem. Then one line of code at the end of the file calls the
# main function. Finally, an if statement is added to ensure that the main function
# does not execute when the file has been imported into another program, as shown
# below:

# if __name__ == "__main__":
#     main()
