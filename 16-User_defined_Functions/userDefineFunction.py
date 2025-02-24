# Definition:
# User-defined functions are functions created by the user to perform specific tasks. These functions help in code reusability and modular programming.

# Syntax
# Declaring a function
def fun():
    print("Inside function")

# Driver's code
# Calling function
fun()

# output -> Inside Function

# Example:
# A simple function to add two numbers:

# print(add(3,5))  # this gives error because add is user defined function and we have to define a function before it's use

def add(a, b):   # define a func
    return a + b   #--> process

result = add(3, 5)  # --> function call  , we can write any variable name at the place of ()result.
print(result)  # 8


# Multiply two numbers
def multiply(a, b):
    return a * b

result = multiply(5, 10)
print(result)  # 50

# practice q's
"""
    1. evenOdd 
    2. student_info --> first name, last name
"""