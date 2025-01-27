# 1. List (list) to Tuple (tuple):
# Function --> tuple() 

x = [1, 2, 3]

print(x) # [1, 2, 3]

print(type(x)) # <class 'list'>
y = tuple(x) 
print(y) # (1, 2, 3)
print(type(y)) # <class 'tuple'>


#2 tuple to list

x = (1, 2, 3)
print(x) # (1, 2, 3)

print(type(x)) # <class 'tuple'>
y = list(x)
print(y) # [1, 2, 3]
print(type(y)) # <class 'list'>








'''
Note ->

1. In Python, lists and tuples are both data structures that store collections of items. 
2. The main difference between the two is that lists can be changed, while tuples cannot. 


1. List ->
    - They are enclosed in square brackets [].
    - They can contain any type of objects.
    - They can be nested (i.e., containing other lists or tuples). [1,2,[3,5],8]
    - Lists are mutable (i.e., we can change their elements).
    - Lists are ordered (i.e., elements follow a specific order).
    - Lists are homogeneous (i.e., all elements must be of the same type).
    - Lists are used to store multiple items of different types.

Ex. We can change the number of items/ elements in after creation
Class of 40 Students
1. List: [1,2,3,4,5,6,7,8,9,...,39,40]
List of Present Students
2. List: [1,2,4,6,7,8,...,39] 

2. Tuple ->
    - They are enclosed in parentheses ().
    - They are immutable --> cannot be changed (i.e., once created, we cannot change their elements).
    - They can contain any type of objects.
    - They can be nested (i.e., containing other lists or tuples). (1,2,[3,5],8)
    - Tuples are ordered (i.e., elements follow a specific order).
    - Tuples are homogeneous (i.e., all elements must be of the same type).
    - Tuples are used to store multiple items of different types.
    
    
    Ex. We cannot change the number of items/elements in after creation.
    
    Employees in Office
    Tuple: (1,2,3,4,5,6,7,8,9,10) --> Employee ID
    Tuple: (1,2,3,4,5,6,7,8,9,10)
    
    Note: Python does not allow duplicate values in a tuple. If we try to add a duplicate value, it will raise a TypeError.

'''
