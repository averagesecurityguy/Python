# Introduction to Python
This video is a brief introduction to the python programming language. It will not cover the installation of python. If you have a Linux or Mac machine then python is already installed. If you have a Windows machine then you will need to install python yourself. I recommend installing python3 on Windows. By default, python2 is installed on most Linux and Mac machines. This tutorial will work with either version.

With this video, we will discuss some basic concepts, data structures, flow control and functions. This will be enough to get you started but I highly recommend going through the tutorial as well. All of the code used in this video is available online.

## Overview
First, python is an interpreted language, which means you need an interpreter to execute the code. You can execute code either by calling python and providing a file name or by adding an interpreter directive to your file and making it executable.

Python, like all scripting languages supports file processing, regular expressions, and string manipulation. It also has built-in support for standard data structures such as lists, stacks, queues, and dictionaries.

Python is unique in modern languages in that it uses whitespace to indicate the beginning and end of code blocks. All code indented at the same level is in the same block. You can use either spaces or tabs for the indentions but you must be consistent throughout the script. The python style guide (PEP 8) recommends indenting with spaces and using 4 spaces for each indent.

Everything in python is an object including the script itself. Python does not require a main method like other languages, it evaluates statements in order starting at the top of the file. Any code that is not indented is considered part of the main method.

Because python is interpreted on a statement by statement basis, you will not see syntax errors until a particular statement is evaluated. This means part of your script may run before the syntax error is found.

## Basic Syntax
For this portion of the video we will be looking at the types.py file. To print something to the terminal use the print() method. The print method will write the given string to the terminal and then write a newline character.

### Numbers and Math
Python supports arbitrary large integers and floats. It also supports standard mathematics operators. Python is not strongly typed so you can use both integers and floats in the same mathematics operation. If one of the operands is a float then the answer will be a float. If they are both integers, the answer will be an integer.

Use the ** operator to do exponentiation. Python supports arbitrarily large integers by default.

### Strings and Things
In python a string is denoted with either single quotes or double quotes. Unlike other languages python does not make a distinction between single quoted strings and double quoted strings. If you need an unescaped string, define a raw string using the letter r before the quote.

Python also supports multiline strings using either a triple single quote or a triple double quote.

Earlier we said that everyting in python is an object. Mathematics operators are just methods on those objects and Python defines the + and * operators for strings.

### Variables
Variables in python are a bit different. Instead of assigning a value to a variable, an object is created and a variable references that object. This means multiple variables can reference the same object and the object can be modified by any of the variables that reference it. Once all references to an object are deleted or are out of scope, the object will be garbage collected.

Variable names can contain numbers but must start with either an alpha or underscore character.

## Data Structures
Python has three basic data structures, list, tuple, and dictionary. You can use these data structures to build other more complex data structures, but that is out of scope for this video.

### List
A list is a collection of objects that is ordered and indexed with a integer. A list can contain any object and not all of the objects in the list must be the same type. You can access or modify any item in the list using its index number. You can also append items to a list or extend a list with another list. The list object also has a pop method that removes an item from the end of the list. Using the append and pop methods you can create a stack with the list. Using pop(0) and append you can create a queue with a list.

### Tuple
A tuple is a collection of objects that is ordered and indexed with a number. Tuples however, are immutable. You cannot change the assigned values of a tuple after it is created. You can add two tuples together though. Tuples are denoted with a comma and are often surrounded by parenthesis. To create a single item tuple, you must use a comma after the first object.

### Dict
A dictionary, which is often called a map in other languages, is a key/value store. The keys in the dictionary must be immutable objects like strings or tuples. The values can be any object. Objects in the dictionary are indexed by their key. In python, dictionaries are declared using a syntax similar to JSON. If you try to access a key that does not exist you get a KeyError.

## Flow Control
Python uses common flow control constructs such as if..else, and while. Python does not have a traditional for loop but defines a for..in construct, which is very powerful.

### If..Else
The if..else statement works exactly as you would expect. If the condition evaluates to true, then the if block is executed, if not the else block is executed. It should be noted that an else block is not necessary. In addition, python has a pass keyword that does nothing, which allows you to not execute code when a condition is met.

Python does not have a switch statement. Instead, use the if..elif..else construct.

### For..In
Python has the concept of iterators, which is basically any object that can be indexed such as a string, a list, a tuple, or a dictionary. You can also create ranges of numbers using the xrange() method. The for..in construct operates over an iterator and allows you to execute code for each item in the iterator.

Although you can iterate over a dictionary using the for..in construct if you plan to modify the dictionary, deleting or adding items, iterate over a separate list of keys, which can be obtained using the keys() method of the dictionary object.

### While
While loops execute a block of code as long as the conditional remains true. You can use a counter with a while loop or you can use the while True: construct to create an infinite loop. If you create an infinite loop then you must break out of the loop at some point. You can also use the continue keyword to move to the next iteration of the loop. The continue and break keywords can be used in any of the loop constructs.

## Functions
Functions are created using the def kyeword. Functions allow us to use the same pieces of code more than once. All functions have a return value, which is denoted with the return keyword. If the return keyword is not used the function returns None.

Function parameters are passed by reference. A variable that is declared outside the scope of the function cannot be reassigned within a function. However, a function can make calls to the methods of the parameter and some of those methods may alter the underlying object.
