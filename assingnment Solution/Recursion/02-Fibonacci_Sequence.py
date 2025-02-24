def fibonacci(n):
    if n <= 0:
        return "Invalid input"
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))  # Output: 5

# Steps to Solve:
# Base cases:
# If n == 1, return 0.
# If n == 2, return 1.

# Recursive case: Return fibonacci(n-1) + fibonacci(n-2).
# Breakdown for fibonacci(6):

# fibonacci(6) = fibonacci(5) + fibonacci(4)
# fibonacci(5) = fibonacci(4) + fibonacci(3)
# fibonacci(4) = fibonacci(3) + fibonacci(2)
# ...
# Continue until base cases are reached.

# Output:
# 5

# Time Complexity: O(2ⁿ) (Exponential due to repeated calls)
# Space Complexity: O(n) (Call stack depth)
