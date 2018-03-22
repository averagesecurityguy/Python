#!/usr/bin/env python

# Everything below is part of the main method.
print("# The Basics")

# Python supports arbitrary precision integers, floats and all the standard
# mathematical operators.
print("\n## Numbers and Math")
print(1 + 1)
print(1 - 1)
print(1 * 2)
print(2 ** 128)  # Use the ** operator for exponentiation.

# Python supports two types of division. Floor division and standard division.
# With floor division only the quotient is returned and with standard division,
# the quotient and the remainder are returned as a floating point.
print(1 / 2)     # If both operands are integers: floor division.
print(1.0 / 2)   # If one of the operands is a float: standard division.
print(1 // 2)    # Floor division with integer return type.
print(1.0 // 2)  # Floor division with float return type.


# Python supports string manipulation as well.
print("\n## Strings and Things")
# Unlike other languages, where double quoted strings means escape characters
# are interepreted, Python makes no distinction between single quoted and double
# quoted strings.
print('Single\tQuotes')
print("Double\tQuotes")

# Unescaped strings are called raw strings in python and are denoted with a r
# before the quotes.
print(r'Raw\tString')

# Python also supports multiline strings using triple quotes, using either the
# single or double quote character.
print('''This is a
multi-line string.''')

# Remember everything is python is an object and operators are methods on the
# object. Python defines some mathematic operators for strings as well.
print('A' + 'B')
print('A' * 10)

# Python supports string formatting as well using the format method on a string.
print("Formatted string: {0}, {1}, {2}".format(1, 'a' * 5, 2**128))


print("\n## Variables")
# Variables in Python are a bit different. You don't assign values to variables,
# instead you assign variable names to values, which are objects. Both a and b
# point to the same list object
a = [1, 2]
b = a

# Notice that changes to b affect a as well.
print('a = {0}'.format(a))
b[0] = 3
print('New a = {0}'.format(a))

# The list object referenced by a and b will not be garbage collected until
# both references to it are out of scope or deleted.
del(a)  # Delete the variable a
del(b)  # Delete the variable b
