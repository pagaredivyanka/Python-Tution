# 1. Sum of Digits

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


# 7️⃣ Greatest Common Divisor (GCD)

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
print(gcd(48, 18))  # Output: 6

# Steps to Solve:
# Base case: If b == 0, return a.
# Recursive case: Call gcd(b, a % b).

# Breakdown for gcd(48, 18):
# gcd(48, 18) = gcd(18, 48 % 18) = gcd(18, 12)
# gcd(18, 12) = gcd(12, 18 % 12) = gcd(12, 6)
# gcd(12, 6)  = gcd(6, 12 % 6)  = gcd(6, 0)
# gcd(6, 0)   = 6 (Base case)

# Output: 6
# Time Complexity: O(log(min(a, b))) (Euclidean algorithm)
# Space Complexity: O(log(min(a, b))) (Recursive depth)

# 8️⃣ Tower of Hanoi

def tower_of_hanoi(n, source, auxiliary, target):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    tower_of_hanoi(n - 1, source, target, auxiliary)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n - 1, auxiliary, source, target)

tower_of_hanoi(3, 'A', 'B', 'C')

# Steps to Solve:
# Move n-1 disks from source to auxiliary using target.
# Move disk n from source to target.
# Move n-1 disks from auxiliary to target using source.

# Breakdown for n = 3:
# Move disk 1 from A to C
# Move disk 2 from A to B
# Move disk 1 from C to B
# Move disk 3 from A to C
# Move disk 1 from B to A
# Move disk 2 from B to C
# Move disk 1 from A to C

# Output:
# Move disk 1 from A to C
# Move disk 2 from A to B
# Move disk 1 from C to B
# Move disk 3 from A to C
# Move disk 1 from B to A
# Move disk 2 from B to C
# Move disk 1 from A to C

# Time Complexity: O(2ⁿ - 1) ≈ O(2ⁿ) (Exponential growth)
# Space Complexity: O(n) (Recursive depth)

# 9️⃣ Count Ways to Climb Stairs

def count_ways(n):
    if n == 0:
        return 1
    if n < 0:
        return 0
    return count_ways(n - 1) + count_ways(n - 2)

print(count_ways(4))  # Output: 5

# Steps to Solve:
# Base case: If n == 0, return 1. If n < 0, return 0.
# Recursive case: Sum of count_ways(n-1) + count_ways(n-2).

# Breakdown for count_ways(4):
# count_ways(4) = count_ways(3) + count_ways(2)
# count_ways(3) = count_ways(2) + count_ways(1)
# count_ways(2) = count_ways(1) + count_ways(0)
# count_ways(1) = 1
# count_ways(0) = 1

# Output: 5
# Time Complexity: O(2ⁿ) (Exponential)
# Space Complexity: O(n) (Recursive depth)

# 🔟 Generate All Subsets of a String

def generate_subsets(s, current="", index=0):
    if index == len(s):
        print(current)
        return
    generate_subsets(s, current + s[index], index + 1)  # Include current character
    generate_subsets(s, current, index + 1)  # Exclude current character

generate_subsets("ABC")

# Steps to Solve:
# Base case: If index == len(s), print the subset.
    
# Recursive case:
# Include s[index] in subset.
# Exclude s[index] and move to next character.

# Breakdown for "abc":
# generate_subsets("abc") → "abc"
# generate_subsets("ab")
# generate_subsets("ac")
# generate_subsets("a")
# generate_subsets("bc")
# generate_subsets("b")
# generate_subsets("c")
# generate_subsets("")
    
# Output:
# abc
# ab
# ac
# a
# bc
# b
# c
    
# Time Complexity: O(2ⁿ) (Each character can be included or excluded)
# Space Complexity: O(n) (Recursive depth)
