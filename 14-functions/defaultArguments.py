# Defination -->
# Default arguments allow you to initialize parameters with default values if no argument is provided during the function call.

# def fun_name(parameteres, default_parameter = 45):
def pow(base, power = 2):
    return base ** power

print(pow(base = 4)) # function call
# Output : 16   --> 4 ** 2 


# Example 2 :
def greet(name="Friend"):
    print(f"Hello, {name}!")

greet()        # Uses default value
greet("Ritesh")  # Uses provided value
# Output : 
# Hello, Friend!
# Hello, Ritesh!

def power(base, exponent=2):
    return base ** exponent
print(power(3))     # Default exponent = 2
#Output : 3 ** 2 = 9 ---> used default exponent 

print(power(3, 3))  # Exponent provided
#Output : 3 ** 3 = 27  ---> exponent is provided at the time of function call



