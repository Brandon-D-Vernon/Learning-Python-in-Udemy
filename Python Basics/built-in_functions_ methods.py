#built in functions + methods

greet = 'holaaaaaa'
print(greet[0:len(greet)])


#*****************************************


# A "method" starts with a period.

quote = 'to be or not to be'

print(quote.upper()) #.upper - Capitalize all letters.

#*****************************************


quote1 = 'to be or not to be'

print(quote1.capitalize()) #.capitalize - Make the first letter upper case.

#*****************************************

quote2 = 'to be or not to be'

print(quote2.lower()) #.lower - Makes all the letters lowercase.

#*****************************************

quote3 = 'to be or not to be'

print(quote3.find('be')) #.finds - Finds a word in "quote" by giving it's indexs number.

#*****************************************

quote4 = 'to be or not to be'

print(quote4.replace('be', 'me')) #.replace - Replaces all 'be' with 'me'.

print(quote4)


#*****************************************


# Built-in Functions
# https://www.w3schools.com/python/python_ref_functions.asp
# https://docs.python.org/3/library/functions.html

# A
# abs()	-  Returns the absolute value of a number
# aiter()	-  
# all()	-  Returns True if all items in an iterable object are true
# any()	-  Returns True if any item in an iterable object is true
# anext()	-  Returns a readable version of an object. Replaces none-ascii characters with escape character
# ascii()	-  

# B
# bin()	-  Returns the binary version of a number
# bool()	-  Returns the boolean value of the specified object
# breakpoint()	-  
# bytearray()	-  Returns an array of bytes
# bytes()	-  

# C
# callable()	-  Returns True if the specified object is callable, otherwise False
# chr()	-  Returns a character from the specified Unicode code.
# classmethod()	-  Converts a method into a class method
# compile()	-  Returns the specified source as an object, ready to be executed
# complex()	-  Returns a complex number

# D
# delattr()	-  Deletes the specified attribute (property or method) from the specified object
# dict()	-  Returns a dictionary (Array)
# dir()	-  Returns a list of the specified object's properties and methods
# divmod()	-  Returns the quotient and the remainder when argument1 is divided by argument2

# E
# enumerate()	-  Takes a collection (e.g. a tuple) and returns it as an enumerate object
# eval()	-  Evaluates and executes an expression
# exec()	-  Executes the specified code (or object)

# F
# filter()	-  Use a filter function to exclude items in an iterable object
# float()	-  Returns a floating point number
# format()	-  Formats a specified value
# frozenset()	-  Returns a frozenset object

# G
# getattr()	-  Returns the value of the specified attribute (property or method)
# globals()	-  Returns the current global symbol table as a dictionary

# H
# hasattr()	-  Returns True if the specified object has the specified attribute (property/method)
# hash()	-  Returns the hash value of a specified object
# help()	-  Executes the built-in help system
# hex()	-  Converts a number into a hexadecimal value

# I
# id()	-  	Returns the id of an object
# input()	-  Allowing user input
# int()	-  Returns an integer number
# isinstance()	-  Returns True if a specified object is an instance of a specified object
# issubclass()	-  Returns True if a specified class is a subclass of a specified object
# iter()	-  Returns an iterator object

# L
# len()	-  Returns the length of an object
# list()	-  Returns a list
# locals()	-  Returns an updated dictionary of the current local symbol table

# M
# map()	-  Returns the specified iterator with the specified function applied to each item
# max()	-  Returns the largest item in an iterable
# memoryview()	-  Returns a memory view object
# min()	-  Returns the smallest item in an iterable

# N
# next()	-  Returns the next item in an iterable

# O
# object()	-  Returns a new object
# oct()	-  Converts a number into an octal
# open()	-  Opens a file and returns a file object
# ord()	-  Convert an integer representing the Unicode of the specified character

# P
# pow()	-  	Returns the value of x to the power of y
# print()	-  Prints to the standard output device
# property()	-  Gets, sets, deletes a property

# R
# range()	-  Returns a sequence of numbers, starting from 0 and increments by 1 (by default)
# repr()	-  Returns a readable version of an object
# reversed()	-  Returns a reversed iterator
# round()	-  Rounds a numbers

# S
# set()	-  Returns a new set object
# setattr()	-  Sets an attribute (property/method) of an object
# slice()	-  Returns a slice object
# sorted()	-  Returns a sorted list
# staticmethod()	-  Converts a method into a static method
# str()	-  Returns a string object
# sum()	-  Sums the items of an iterator
# super()	-  Returns an object that represents the parent class

# T
# tuple()	-  Returns a tuple
# type()	-  Returns the type of an object

# V
# vars()	-  Returns the __dict__ property of an object

# Z
# zip()	-  	Returns an iterator, from two or more iterators

# _
# __import__()	-  


#*****************************************


# Python String Methods
# https://www.w3schools.com/python/python_ref_string.asp

# C
# capitalize()	-  Converts the first character to upper case
# casefold()	-  Converts string into lower case
# center()	-  Returns a centered string
# count()	-  Returns the number of times a specified value occurs in a string

# E
# encode()	-  Returns an encoded version of the string
# endswith()	-  Returns true if the string ends with the specified value
# expandtabs()	-  Sets the tab size of the string

# F
# find()	-  Searches the string for a specified value and returns the position of where it was found
# format()	-  Formats specified values in a string
# format_map()	-  Formats specified values in a string

# I
# index()	-  Searches the string for a specified value and returns the position of where it was found
# isalnum()	-  Returns True if all characters in the string are alphanumeric
# isalpha()	-  Returns True if all characters in the string are in the alphabet
# isascii()	-  Returns True if all characters in the string are ascii characters
# isdecimal()	-  Returns True if all characters in the string are decimals
# isdigit()	-  Returns True if all characters in the string are digits
# isidentifier()	-  Returns True if the string is an identifier
# islower()	-  Returns True if all characters in the string are lower case
# isnumeric()	-  Returns True if all characters in the string are numeric
# isprintable()	-  Returns True if all characters in the string are printable
# isspace()	-  Returns True if all characters in the string are whitespaces
# istitle()	-  Returns True if the string follows the rules of a title
# isupper()	-  Returns True if all characters in the string are upper case

# J
# join()	-  Converts the elements of an iterable into a string

# L
# ljust()	-  Returns a left justified version of the string
# lower()	-  Converts a string into lower case
# lstrip()	-  Returns a left trim version of the string

# M
# maketrans()	-  Returns a translation table to be used in translations

# P
# partition()	-  Returns a tuple where the string is parted into three parts

# R
# replace()	-  Returns a string where a specified value is replaced with a specified value
# rfind()	-  Searches the string for a specified value and returns the last position of where it was found
# rindex()	-  Searches the string for a specified value and returns the last position of where it was found
# rjust()	-  Returns a right justified version of the string
# rpartition()	-  Returns a tuple where the string is parted into three parts
# rsplit()	-  Splits the string at the specified separator, and returns a list
# rstrip()	-  Returns a right trim version of the string

# S
# split()	-  Splits the string at the specified separator, and returns a list
# splitlines()	-  Splits the string at line breaks and returns a list
# startswith()	-  Returns true if the string starts with the specified value
# strip()	-  Returns a trimmed version of the string
# swapcase()	-  Swaps cases, lower case becomes upper case and vice versa

# T
# title()	-  Converts the first character of each word to upper case
# translate()	-  Returns a translated string

# U
# upper()	-  Converts a string into upper case

# Z
# zfill()	-  Fills the string with a specified number of 0 values at the beginning