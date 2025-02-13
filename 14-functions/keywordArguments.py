# Definition:
# Keyword arguments allow you to pass arguments to a function using parameter names, providing flexibility in the order of arguments.


# ex. 

def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")
greet(age = 21, name = "Ritesh")

# area of rectangle

def area_rectangle(length, width):
    return length * width
print(area_rectangle(width = 6, length= 45))