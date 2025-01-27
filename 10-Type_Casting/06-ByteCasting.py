# String to Byte
#bytes()

x = "Divyanka"
y = bytes(x,"utf-8")
print(y)


# string = " "
# char = ''


#Integer List to Bytes

x = [65, 66, 67]
print(x)
print(type(x))

y = bytes(x)
print(y)
print(type(y))

# [65, 66, 67]
# <class 'list'>
# b'ABC'
# <class 'bytes'>

x = ['a','b','c','d','e','f']

# print(x)
# print(type(x))
# y = bytes(x)
# print(y)
# print(type(y))


# We can't do this this will gives us an error
# TypeError: 'str' object cannot be interpreted as an integer

