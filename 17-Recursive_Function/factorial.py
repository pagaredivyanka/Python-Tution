# Definition:
# A recursive function is a function that calls itself within its definition to solve a problem by breaking it down into smaller subproblems.

def function():
    print("Hello, World!")
    function()
    
# Recursion example:

# 5! = 5 * 4 * 3 * 2 * 1 = 120

# 3! = 3 * 2 * 1 = 6
# 1! = 1
# 0! = 1

def factorial(n):
    # Base case: factorial of 0 and 1 is 1
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1) # Recursive case: multiply the number by the factorial of (n-1)
n = 5
print("number", n) 
print("factorial : ",factorial(n))

# factorial(5) = 5 * factorial(4) = 120
# factorial(4) = 4 * factorial(3) = 24
# factorial(3) = 3 * factorial(2) = 6
# factorial(2) = 2 * factorial(1) = 2
# factorial(1) = 1 (Base case)

# Now, returning back:

# factorial(2) = 2 × 1 = 2
# factorial(3) = 3 × 2 = 6
# factorial(4) = 4 × 6 = 24
# factorial(5) = 5 × 24 = 120
# So, 5! = 120.


# time complexity = O(n)
# space complexity = O(n) 
"""
input  = 1
it will take time = 1

if input is 5 then it will take time = 5
if input is 10 = time is 10 

if input is n then time is n


sum = 0
num(1,5) # 1, 2, 3, 4, 5  # loop = 5
num = num + 1
starts from 1 to 5
sum = sum + num

sum = 0 + 1 = 1  # time = 1
sum = 1 + 2 = 3
sum = 3 + 3 = 6
sum = 6 + 4 = 10
sum = 10 + 5 = 15 # time = 5

if we increament end point as 10 then time also increament to 10 

final output is --> sum = 15
"""


