#Syntax

# def function_name(parameters):
#     """function body"""
#   return value

# function_name(value)    ----> function call



def greet():
    print("Hello")

greet()


# adding two numbers

def add(a, b):
    return a + b

result = add(5, 10)
print(result)  # 15

print(add(50, 45))   #95


# ________________________________________________

# traditional way to multiply numbers

a = 45
b = 367
multiplication = a * b 
print (multiplication)

a = 78
b = 456
multiplication = a * b
print (multiplication)

val1 = int(input("enter the value of a : " ))
val2 = int(input("enter the value of b : "))

multiplication = a * b

print("The multiplication of two numbers is : ", multiplication)

# we can just get the output of different numbers/ parameteres on runtime  

print(add(76, 90))


def is_even(num):
    return num % 2 == 0

print(is_even(10))  # True
print(is_even(45))  # False
print(is_even(65))  # False
print(is_even(54))  # True
print(is_even(97))  # False
print(is_even(90))  # True


"""
1. divide by zero
2. max of three numbers
3. find the area of square, circle
4. find the square of number

"""

def power(base, exp=2):
    return base ** exp

print(power(5))    # function call # 25

# base ^ 2
# 5 ^ 2 = 25

    