# Types of Scope
"""
there are 2 types of scope
1.Local Variables --> 
    a. Difine ---> Defined inside the function.
    b. Use --> Used in the perticular function only.
    c. Existence --> It's Exists inside the scope of the function only.
    
2.Global Variables --> 
    a. Difine --> defined outside the function.
    b. Used --> Used in the whole program.
    c. Existence --> It's accessible from anywhere in the program.

"""

x = 10  # Global variables
def test():
    x = 20 # Local variables
    print("Inside the function:", x)

test()   # function call
print("Outside the function:", x) # 10

# first it will print the inside function then the outside function

# printing of the print statement on the basis of in which sequence we are calling the functions.

