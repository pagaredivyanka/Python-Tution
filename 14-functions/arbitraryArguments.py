# Definition:
# Arbitrary arguments allow a function to accept an unlimited number of positional arguments.

# Example 1 :


def sum_numbers(*args):
    return sum(args)

print(sum_numbers(1, 2, 3)) 
"""
sum = 0 
sum = 1 + 2 = 3
sum = 3
sum + 3 = 6 
""" 
print(sum_numbers(10, 20, 30, 40))

# Output: 
# 6
# 100

