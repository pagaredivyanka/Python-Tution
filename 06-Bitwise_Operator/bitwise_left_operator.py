# bitwise left operator 
print(5 << 1) 

#5 -> 0101
# b = 1 -> we will shift 1 by single digit in the above bunary number

# 0101 -> 1010 
# (binary) 1010 -> (decimal) 10

# 1 -> 1
# 2 -> 10
# 4 -> 100
# 8 -> 1000
# 16 -> 10000

print(3 << 2) # shift 1 by 2 digits 

# 11 -> shift by 2 digits left
# 1100 -> 1000 (8) + 100 (4) 
# 1000
# + 
# 0100
#--------
# 1100 -> 8 + 4 = 12

a = int(input("enter the value of a : "))
b = int(input("enter the value of b : "))
print("Left Shift : ", a << b)

# 5 -> 101 -> 10 (decimal form)
# 5 -> 101 {shift by 3} -> 101000 | 40 (decimal)


 