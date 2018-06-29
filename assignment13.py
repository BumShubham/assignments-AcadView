#Q1 Name and handle the exception occurred in the following program:
try:
    a = 3
    if a < 4:
        a = a / (a - 3)
except (ZeroDivisionError, IndentationError):
    print("The answer is 0.")
else:
    print(a)

"""answer 1: The error that has occurred is IndentationError : unexpected indent and 
 also ZeroDivisionError : division by zero"""


#Q2 Name and handle the exception occurred in the following program:
try:
    l = [1, 2, 3]
    print(l[3])
except IndexError:
    print("Cannot access this Element.")

"""answer 2:IndexError: list index out of range"""


#Q3 What will be the output of the following code:
    #Program to depict Raising Exception
"""try:
    raise NameError("Hi there")  # Raise Error
except NameError:
    print
    "An exception"
    raise  # To determine whether the exception was raised or not"""

"""NameError:If Python encounters a name that it doesn't recognize,you'll get this error."""

"""
answer 3: raise NameError("Hi there")  # Raise Error
          NameError: Hi there
"""



#Q4  What will be the output of the following code:
    # Function which returns a/b
def AbyB(a, b):
    try:
        c = ((a + b) / (a - b))
    except ZeroDivisionError:
        print("a/b result in 0")
    else:
        print(c)


# Driver program to test above function
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)

"""answer 4: -5.0
             a/b result in 0
"""

#Q5 Write a program to show and handle following exceptions:
    # 1. Import Error
    # 2. Value Error
    # 3. Index Error

"""Import error: It basically comes when we try to import any module that is not present.If python cannot find the module."""
try:
    import mountain
    import shubham
except ImportError:
    print("This module is not present.")

"""Value error:It is raised when a built-in operation or function receives an argument that has the right type but an appropriate value"""
while True:
    try:
        n = int(input("please,Enter a number:"))
        break
    except ValueError:
        print("You are supposed to enter a number!please try again...")
print("great,you successfully entered a number.")

"""Index error:It is raised whenever attempting to access an index that is outside the bounds of a list"""
try:
    list = [1, 2]
    print(list[4])
except IndexError:
    print("This element can not be accessed.")


#Q6: Create a user-defined exception AgeTooSmallError() that warns the user when they have entered age less than 18.
    # The code must keep taking input till the user enters the appropriate age number(less than 18).

class AgeTooSmallError(Exception):
    pass


def input_age():
    no = int(input("Enter the age:"))
    return no


age = 18
while True:
    try:
        no = input_age()
        if no < age:
            raise AgeTooSmallError
        else:
            print("Age correct...")
            break
    except AgeTooSmallError:
        print("error,Age is too small,enter again...")