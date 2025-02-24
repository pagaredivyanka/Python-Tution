def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120

Steps to Solve:
Base case: If n == 0 or n == 1, return 1.
Recursive case: Multiply n with factorial(n-1).
Example breakdown for factorial(5):

factorial(5) = 5 * factorial(4)
factorial(4) = 4 * factorial(3)
factorial(3) = 3 * factorial(2)
factorial(2) = 2 * factorial(1)
factorial(1) = 1  (Base case)
                 
Compute back up the stack: 1 → 2 → 6 → 24 → 120.
Output:
120
                 
Time Complexity:
O(n) (Each recursive call decreases n by 1)
Space Complexity:
O(n) (Recursive stack depth is n)
