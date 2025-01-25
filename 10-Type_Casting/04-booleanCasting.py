#1. Integer(int) to Boolean(bool)

"""
   
"""


x = 0    # 0 --> False
y = bool(x)
print(x) # 0
print(type(x))  # <class 'int'>

print(y) # False
print(type(y)) # <class 'bool'>

a = 99  # any other positive (integer) number than 0 then it will print True 
b = bool(a)
print(b)

a = -99  # any other positive (integer) number than 0 then it will print True 
b = bool(a)  
print(b) # True
print(type(b)) # <class 'bool'>

#2. Float(float) to Boolean(bool)

x = 0.0 
y = bool(x)
print(x) # 0.0
print(type(x))  # <class 'float'>
print(y) # False
print(type(y))  # <class 'bool'>

#3. String(str) to Boolean(bool)

x = "Ritesh"
y = bool(x)
print(x)
print(type(x))

print(y) # True
print(type(y)) # <class 'bool'>


a = None  # specia type which we used to specify unknown values
print(a) # None
print(type(a)) # <class 'NoneType'>

y = bool(x)
print(y) # False
print(type(y)) # <class 'bool'>


## VVIMP 

x = ""
print(x)
print(type(x))
z = bool(x)
print(z) # False
print(type(z)) # <class 'bool'>

r = "  "
print(r)
print(type(r))

y = bool(r) 
print(y) # True
print(type(y)) # <class 'bool'>


name = "RiteshGirase" # 12
name1 = "Ritesh Girase" # 13

print(name)
print(type(name))

print(name1)
print(type(name1))

v = len(name)  # len() is function 
print(v) # 12
print(type(v)) # <class 'int'>

w = len(name1)  # len() is function 
print(w) # 13  --> 12 characters + 1 empty space = 13
print(type(w)) # <class 'int'>


# Notes --> 

"""
    1. if we convert the value of integer to   boolean an the integer value is 0(zero) then it will give output as False 
   
    2. and if there is any other positive or negative integer other than 0 then it will give us output as True
    
    3. len() is function to count the no. of characters in a give string.
    
    4. space is also consider while calculating the number of characters in the string.
    
"""






