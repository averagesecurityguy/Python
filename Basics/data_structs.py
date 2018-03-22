#!/usr/bin/env python

# Python has three common data structures built into the language, list, tuple
# and dictionary.
print("# Data Structures")
print("## List")
# Remember, everything in python is an object and a list is an ordered
# collection of objects, which means a list can contain objects of different
# types.
a = [1, "1", 1.0]

# An object in a list can be accessed by its index number like so.
print(a[0])

# Python also supports slice notation on lists.
print(a[1:3])

# Python also supports a number of operations on lists including.
a.append("one")  # Add an item to the end of a list.
print(a)

a.extend([2, "2", 2.0])  # Add a list to the end of a list.
print(a)

print(a.pop())  # Pop an item off the end of the list.
print(a)
print(a.pop(1))  #Pop the item at the given index off the list.
print(a)

print("\n## Tuple")
# Tuples are very similar to lists but are immutable, meaning you cannot change
# the value of an item in a tuple. Tuples are denoted with parenthesis and a
# a comma
b = (1,)  # A tuple with a single value in it.
b = b + ("1", 1.0)  # Add two tuples together
print(b)

# Tuples are indexed just like lists but you cannot modify them.
print(b[0])

# Uncomment the following code to get a TypeError.
# b[0] = 2

print("\n## Dictionary")
# A dictionary is often called a map in other languages, it is key/value store.
# Keys must be immutable objects such as strings or tuples. Dictionaries are
# declared using a syntax very similar JSON. Dictionaries are indexed on their
# keys.
name = {'first': 'Stephen', 'last': 'Haywood'}
print(name['first'])
print(name['last'])

# A single dictionary can map to many different objects
d = {'string': 'one', 'int': 1, 'float': 1.0}

# If you try to access a key that does not exist in the dictionary, you will
# get a KeyError. Uncomment the next line to see this in action.
# print(d['notexist'])
