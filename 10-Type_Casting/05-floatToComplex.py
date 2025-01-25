x = 9.9
y = complex(x)  

print(y)
print(type(y)) # <class 'complex'>

# Output: (9.9+0j)
x = 0
y = 8.7
output = complex(x,y)

print(output) # 8.7j
print(type(output)) # <class 'complex'>

'''
Note -> 

*** if we give only single variable as a parameter it will by default,
consider it as real value and it will consider the imaginary value as 0.

*** but if we give single value and want to consider it as imaginary part of the complex number then it will not happen by default, 
for that we have to give first variable/ prameter as 0(manually).

1. we cant take value as -> None
2. when first number is zero then the out will be only imaginary number ex. 8.7j
3.
'''