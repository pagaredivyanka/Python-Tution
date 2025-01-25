#Integer(int) to Compelx(complex)

#type 1
a = 3
print(complex(a)) # (3+0j)
print(type(complex(a))) # <class 'complex'>

#type 2

# complex(x,y)
x = 7
y = 4
print(complex(x,y)) # (7 + 4j)
print(complex(y,x)) # (4 + 7j)


'''

Example 1. --> 3 + 0j
    when we have 2 integers and we want to write it in a format of complex number then we have to write it as 

    complex(real_part, imaginary_part) -> complex(x, y)

    in this case, 
    real_part = 3 
    imaginary_part = 0
    
    output --> (3+0j)
    Type --> <class 'complex'>

Example 2. where we have 2 values 
x = 7 
y = 4

complex(x, y) -> complex(7, 4)
real_part = 7,
imaginary_part = 4
output -> (7 + 4j)

complex(y, x) -> complex(4, 7)
real_part = 4,
imaginary_part = 7
output -> (4 + 7j)

So, the output will be (7 + 4j) and (4 + 7j) respectively

'''
