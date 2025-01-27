# 2. List (list) to Set (set):

x = [1, 2, 2, 3]
print(x)
print(type(x))
y = set(x)
print(y)  # Output: {1, 2, 3}
print(type(y))

# [1, 2, 2, 3]
# <class 'list'>
# {1, 2, 3}
# <class 'set'>

'''
Set ->
    - Unordered collection of unique elements
    - Elements are separated by commas and enclosed in curly braces {}
    - Sets are mutable, i.e., they can be modified after creation
    - Sets do not support indexing or slicing, but they can be used in loops.
    - Sets can be used to perform mathematical operations like union, intersection, difference, and symmetric difference
'''
