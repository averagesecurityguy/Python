#!/usr/bin/env python

# Python supports standard flow control such as conditionals and loops.
print("##If..Else")

# The if..else statement works exactly as you expect. If the conditional is True
# the statements after the if will be executed, otherwise the statements in the
# else block will be executed.
a = 1
if a == 1:
    print("It equals one.")
else:
    print("It does not equal one.")

# An else block is not necessary.
if a != 1:
    print("It does not equal one.")

# In some cases you may want to do nothing if the conditional is True.
if a == 1:
    pass
else:
    print("Do something here.")

# Python does not have a switch statement so you have to use the if..elif..else
# statement.
a = 2
if a == 1:
    print("One")
elif a == 2:
    print("Two")  # This will be executed.
else:
    print("None of the above.")

print("\n##For..in")
# Python has the concept of iterators. An iterator is any object that can be
# indexed such as a string, a list, a tuple, or a dictionary (keys). The for..in
# construct operates over an iterator.

# This will print each letter in word.
for w in 'word':
    print(w)

# The built-in xrange function generates a list of integers.
for i in xrange(10):
    print(i)

# This will print each item in the given list.
for i in [1, "1", 1.0]:
    print(i)

# This will print each item in the given tuple.
for i in (1, "1", 1.0):
    print(i)

# This will print each key and value in the given dictionary.
items = {'string': 'one', 'int': 1, 'float': 1.0}
for i in items:
    print(i, items[i])

# You can get a list of all of the dictionary keys using the keys() method.
# If you need to modify a dictionary, particularly if you are deleting items,
# you should get the list of keys and iterate over those instead of iterating
# over the dictionary directly.
for i in items.keys():
    del(items[i])

# Uncomment the code to see what happens if you try to delete items in a
# dictionary as you are iterating over it.
# for i in items:
#     del(items[i])


# While loops in python behave as you would expect.
print("\n##While")

# The following code will add 1 to i until i reaches 10.
print("\nAll")
i = 0
while i < 10:
    print(i)
    i += 1

# The following code will create an endless loop. Uncomment the code to see it
# in action.
# while True:
#    print('A')

# The break keyword can be used to exit a while or for loop early. The continue
# keyword can be used to immediately move to the next item in the list.
print("\nOdds")
i = 0
while True:
    i += 1

    if i % 2 == 0:  # Skip the even numbers.
        continue

    if i > 9:  # Stop looping if i is greater than 9
        break

    print(i)
