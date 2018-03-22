#!/usr/bin/env python

# To create functions in python use the def keyword.
def add(x, y):
    return x + y

# All functions have a return value. If the return keyword is not used then the
# function returns None.
def log(a):
    print("Log: {0}".format(a))

# Variables cannot be reassigned within a method.
def modify(a):
    a = [4, 5]

# Methods that modify the parameter in place will cause a change to the
# underlying object. If you are not careful, this will bite you hard especially
# in a situation like this. When you call the modify2 method it has the side
# effect of modifying the underlying list object.
def log2(a):
    print(a.append('1'))  # Prints None, which is the return value of append.


#---------
# Main
#---------
print("\nAdd two numbers")
a = add(1, 2)
print(a)

print("\nLog returns None")
b = log(a)  # b will be None.
print(b)

print("\nModify our list")
i = [1, 2]
print("Before", i)
modify(i)
print("After", i)

print("\nPrint our list with side-effect.")
print("Before", i)
b = log2(i)
print("After", i)  # i will not remain unchanged here.
