Sum of Digits

def sum_of_digits(n):
    if n == 0:
        return 0
    return (n % 10) + sum_of_digits(n // 10)

print(sum_of_digits(1234))  # Output: 10

# Steps to Solve:
# Base case: If n == 0, return 0.
# Recursive case: Extract last digit (n % 10) and add it to the sum of the remaining digits (n // 10).
# Breakdown for sum_of_digits(1234):

# sum_of_digits(1234) = 4 + sum_of_digits(123)
# sum_of_digits(123)  = 3 + sum_of_digits(12)
# sum_of_digits(12)   = 2 + sum_of_digits(1)
# sum_of_digits(1)    = 1 + sum_of_digits(0)
# sum_of_digits(0)    = 0 (Base case)
# Add up values to get 10.

# Output:
# 10

# Time Complexity: O(log n) (Each step reduces n by a factor of 10)
# Space Complexity: O(log n) (Recursive depth depends on the number of digits)

# 4️⃣ Power Function (a^b)

def power(a, b):
    if b == 0:
        return 1
    return a * power(a, b - 1)

print(power(2, 3))  # Output: 8

# Steps to Solve:
# Base case: If b == 0, return 1.
# Recursive case: Multiply a with power(a, b - 1).
# Breakdown for power(2, 3):

# power(2,3) = 2 * power(2,2)
# power(2,2) = 2 * power(2,1)
# power(2,1) = 2 * power(2,0)
# power(2,0) = 1 (Base case)
# Compute back: 1 → 2 → 4 → 8.

# Output:
# 8

# Time Complexity: O(b) (Recursive depth is b)
# Space Complexity: O(b) (Recursive stack)

# 5️⃣ Reverse a String

def reverse_string(s):
    if len(s) == 0:
        return s
    return s[-1] + reverse_string(s[:-1])

print(reverse_string("hello"))  # Output: "olleh"

# Steps to Solve:
# Base case: If s is empty, return s.
# Recursive case: Return the last character (s[-1]) + reverse of the remaining string (s[:-1]).
# Breakdown for "hello":

# reverse("hello") = "o" + reverse("hell")
# reverse("hell")  = "l" + reverse("hel")
# reverse("hel")   = "l" + reverse("he")
# reverse("he")    = "e" + reverse("h")
# reverse("h")     = "h" (Base case)
# Join reversed parts.

# Output:
# "olleh"

# Time Complexity: O(n) (One call per character)
# Space Complexity: O(n) (Stack depth)

# 6️⃣ Check Palindrome

def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])
print(is_palindrome("madam"))  # Output: True
print(is_palindrome("hello"))  # Output: False

# Steps to Solve:
# Base case: If s has 0 or 1 characters, return True.
# Recursive case: If first and last characters don’t match, return False. Otherwise, check the substring without first and last characters.
# Breakdown for "madam":

# is_palindrome("madam") = is_palindrome("ada")
# is_palindrome("ada")   = is_palindrome("d")
# is_palindrome("d")     = True (Base case)

# Output:
# True
# False

# Time Complexity:
# O(n) (Checks half the string)
# Space Complexity:
# O(n) (Recursive calls)
