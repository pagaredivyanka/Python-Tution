# Definition:
# Built-in functions are pre-defined functions in Python that perform common tasks. These functions are always available for use without requiring imports.

#1.
print() #it displays o/p on the console screen / terminal
# ex. 
print("Good morning! Robot")

#2.
len() #used to calculate the length of the string, list and any iterable.
# ex. 
text = "Hello, Rites"
length = len(text)
print(length)

type()
str()

int() # --> int(input("enter no"))

float() # --> float(input("enter no"))
input() # --> int(input("enter no"))
range() # --> create a sequence of num from 0 to 5 and print each item in the sequence.
x = range(10)
for n in x:
    print(n)
    
# Syntax
# range(start, stop, step)
x = range(2, 10)  # prints from 2 to 9
for n in x:
    print(n) 
    
x = range(2, 10, 3)
for n in x:
    print(n) #2 _ _ 5 _ _ 8
    
    
list() # creates a list object. it is a collection which is ordered and changable(we can change the elements of the list after it's creation).
x = list(('apple', 'banana', 'cherry')) # tuple to list
print(x)
sum()