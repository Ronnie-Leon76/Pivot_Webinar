name = 'Pivot'
print(isinstance(name,str))

"""
Data Types in Python
Operators in Python
The Ternary Operator in Python
Strings in Python
Booleans in Python
Numbers in Python
Constants in Python
Enums in Python
User Input in Python
Control Statements in Python
Lists in Python
Tuples in Python
Dictionaries in Python
Sets in Python
Functions in Python
Objects in Python
Loops in Python
Classes in Python
Modules in Python
The Python Standard Library
The PEP8 Python Style Guide
Debugging in Python
Variable Scope in Python
How to Accept Arguments from the Command Line in Python
Lambda Functions in Python
Recursion in Python
Nested Functions in Python
Closures in Python
Decorators in Python
Docstrings in Python
Introspection in Python
Annotations in Python
Exceptions in Python
The with Statement in Python
How to Install 3rd Party Packages in Python Using pip
List Comprehensions in Python
Polymorphism in Python
Operator Overloading in Python
Virtual Environments in Python
"""


#Data types in Python
#age = 10
#name = 'Python'
#Operators in Python
"""
    a) Assignment operators
    b) Arithmetic operators
    c) Comparison operators
    d) Logical operators
    e) Bitwise operators
"""
#Assignment operators
#age = 8
#anotherVariable = age
#Arithmetic operators
"""
    Python has a number of arithmetic operators: +,-*,/,%,**(exponentiation) and //floor division

"""
#num1 = 10
#num2 = 5
#sum = num1 + num2
#difference = num1 - num2
#product = num1*num2
#division = num1/num2
#modulus = num1%num2
#exponents = num1**2
#floor = num1//num2
# + is also used to concatentate strings
#name = 'Pivot'
print('Welcome to ' + '' + name + ' Python Webinar series')
"""
    We can combine the assignment operator with arithmetic operators: +=, -=, *=, /=, %=
"""
#years = 10
#years += 1
#Comparison operators in Python: ==, !=, >, <, <=, >=
#num1 == num2
#num1 != num2
#Boolean operators in Python
"""
    Python gives us the following boolean operations:not, and & or
"""
#condition1 = True
#condition2 = False
#not condition1
#condition1 and condition2
#condition1 or condition2

#Bitwise operators in Python
"""
Some operators are used to work on bits and binary numbers.
    a) & performs binary ADD
    b) | performs binary OR
    c) ^ performs a binary XOR operation
    d) ~ performs a binary NOT operation
    e) << shifts left operation
    f) >> shifts right operation
"""
#is and in in Python
"""
    is is called the identity operator. It is used to compare two objects and returns true if both are the same object
    in is called the membership operator. It is used to tell if a value is contained in a list, or another sequence
"""
#Ternary operator in Python
"""
def is_adult(age):
    if age > 18:
        return True
    else:
        return False
"""

"""
def is_adult(age):
    return True if age > 18 else False
"""


#Strings in Python

#Introspection in Python with help(),type() and dir()


#member = 'John'
"""
    A string has a set of built-in methods, like:
    a) isalpha(): check if a string contains only characters and is not empty
    b) isalnum(): check if a string contains characters or digits and is not empty
    c) isdecimal(): check if a string contains digits and is not empty
    d) lower(): to get a lowercase version of a sring
    e) islower(): to check if a string is lowercase
    f) upper(): to get an uppercase version of a string
    g) isupper(): to check if a string is uppercase
    h) title(): to get a capitalized version of a string
    i) startswith(): to check if the string starts with a specific substring
    j) endswith(): to check if the string ends with a specific substring
    k) replace(): to replace a part of a string
    l) split(): to split a string on a specific character separator
    m) strip(): to trim the whitespace from a string
    n) join(): to append new letters to a string
    o) find(): to find the position of a substring
"""
#print(member.lower())
#print(len(member))
#print("Jo" in member)
#Slicing
#name = 'Pivot'
#name[1:3]
#Numbers in Python
"""
    1) Integer numbers
    2) Floating point numbers
    3) Complex Numbers
"""
#Complex numbers can be declared as follows:
#complexNumber = 2 + 3j
# Or declared as follows:
#complexNumber = complex(2 + 3)
#complexNumber.real
#complexNumber.imag
#Built-in Functions in Python
"""
    There are 2 built-in functions that help with numbers:
        a) abs(): retains the absolute value of a number
        b) round(): given a number, returns its value rounded to the nearest integer 
"""
#round(0.12)
#round(0.12,1)
#Python Standard Library modules include: math, cmath, decimal and fractions

#Constants in Python
"""
    Python has no way to enforce that a variable should be a constant. The nearest you can get is to use an enum or use tuples
"""
#from enum import Enum
"""
class State(Enum):
    INACTIVE = 0
    ACTIVE = 1
"""


#User Input in Python
#print("What is your favorite music genre?")
#favMusicGenre = input()
#print('Your favorite music genre is' + favMusicGenre)

#Control Statements in Python
#condition = True
"""
if condition == True:
    print('The condition')
    print('was true')
"""


#grade = ('A','B','C','D','E')
"""
if grade == 'A':
    print('Excellent')
elif grade == 'B':
    print('Very Good')
elif grade == 'C':
    print('Fair')
elif grade == 'D':
    print('Poor')
else:
    print('Very Poor')

"""

#Data structures in Python
# 1) Lists in Python
"""
    Lists are an essential Python data structure
"""
#musicGenre = ['Pop','RNBs','HipHop']
#musicGenre[0]
#musicGenre[1]
#You can also use the index() method
#musicGenre.index(0)
#You can extract a part of a list
#musicGenre[0:2]
#You can add items to the list using a list append() method
#musicGenre.append('CountryMusic')
#Or use the extend() method
#musicGenre.extend(['House'])
#Remove an item using the remove() method
#musicGenre.remove('CountryMusic')
#You can also add multiple elements using:
#musicGenre += ['Dancehall','Reggae']
#Alternatively
#musicGenre.extend(['Gengetone', 'Rhumba'])
#These append the item to the end of the list. To add an item in the middle of a list at a specific index use insert() method
#musicGenre.insert("Test",1)#adds Test at index 1
#Sort a list using the sort() method
#musicGenre.sort()

# 2) List Comprehensions
"""
    List comprehensions are a way to create lists in a very concise way.

"""
#numbers = [1, 2, 3, 4, 5]
#numbers_power_2 = [n**2 for n in numbers]

# 3) Tuples
"""
    Allow you to create immutable groups of objects.
    A tuple is ordered like a list, so you can get its values by referencing an index value
"""
#constants = (3.142,3*10**8)
#constants[0]
#len(constants)
#constants[0:2]

# 4) Dictionaries
"""
    Dictionaries are a very important Python data structure. While lists allow, you to create a collection of values,
    dictionaries allow you to create a collection of key/value pairs
    They key can be any immutable value like a string, a number or a tuple
"""
#bestTeams = {'EPL': 'Mancity', 'Bundesliga':'Bayern Munchen'}
#bestTeams['EPL']
#bestTeams['Bundesliga']
#Using the same notation you can change the value stored at a specific index
#bestTeams['EPL'] = 'Manchester United'
#Another way is using the get() method, which has an option to add a default value
#bestTeams.get('EPL')
#The pop() method retrieves the values of a key, and subsequently deletes the item from the dictionary
#bestTeams.pop('EPL')
#The popitem() method retrieves and removes the last key/value pair inserted into the dictionary
#bestTeams.popitem()
#bestTeams.append({'SuperLeague':'Mancity'})
#You can add a new key/value pair to the dictionary
#bestTeams['Europa'] = 'Juventus'
#Get a list with keys in a dictionary using the keys() method, passing its result to the list() constructor
#list(bestTeams.keys())
#Get the values using the values() method, and the key/value pairs tuples using the items() method
#print(list(bestTeams.values()))
#print(list(bestTeams.items()))
#You can remove a key/value pair from a dictionary using the del statement
#del bestTeams['Europa']
#To copy a dictionary, use the copy() method
#bestTeamsCopy = bestTeams.copy()

# 5) Sets in Python
"""
    Sets work like tuples, but they aren't ordered, and they are mutable. They also have an immutable version called frozenset
"""
#programmingLanguages = {'Python', 'C++', 'C','C#', 'JavaScript'}
#set1 = {'C++','C#','C'}
#set2 = {'Python','Perl','Matlab'}
#intersect
#set1 & programmingLanguages
#union
#set1 | programmingLanguages
#difference
#set1 - programmingLanguages
#You can check if a set is a superset of another
#isSuperset = set1 > programmingLanguages

# Functions in Python
"""
    Allow us to decompose a program into manageable parts, and they promote readability and code reuse
"""
"""
def hello():
    print('Hello!')

def hello1(name):
    print('Hello'+ name + '!')
"""


#hello1(Pythonistas)
"""
def individual(name,age):
    print('Hello' + name + 'you are' + str(age) + 'years old')
"""



# Objects in Python
"""
    Values of basic primitive types such as integer, string, float are objects. Lists, Tuples, dictionaries are objects.
    Objects have attributes and methods that can be accessed using the dot syntax
    Examples shown below:
"""
#total = 58
#print(total.real)
#print(total.imag)
#print(total.bit_length())
#the bit_length() returns the number of bits necessary to represent this number in binary notation

#The id() global function provided by Python lets you inspect the location in memory for a particular object
#id(total)

#total = 65
#id(total)

#The address of the variable total is changed 

#trophiesWon = [13,3]
#print(id(trophiesWon))

#trophiesWon.append(13)
#print(trophiesWon)
#print(id(trophiesWon))


#Loops in Python
"""
    In Python we have two kinds of loops: while and for loops
"""
#while loops in Python
#count = 0
"""
while count < 10:
    print('The condition is true')
    count += 1
print('After the loop')
"""

#for loops in Python
#items = [1,2,3,4]
"""
for item in items:
    print(item)
"""


#You can iterate a specific amount of time using the range() function
"""
for item in range(4):
    print(item)
"""

#range(4) creates a sequence that starts from 0 and contains 4 items: [0,1,2,3]

# If you want to get the index, you should wrap the sequence into the enumerate() function.
"""
for index,item in enumerate(items):
    print(index,item)
"""


#Break and Continue in Python
"""
    Both while and for loops can be interrupted inside the block, using two special keywords: break and continue
        1) Continue: stops the current iteration and tells Python to execute the next one
        2) Break: stops the loop altogether and goes on with the next instruction after the loop ends
"""
"""
for item in items:
    if item == 2:
        continue
    print(item)

for item in items:
    if item == 2:
        break
    print(item)
"""


#Classes in Python
"""
    An object is an instance of a class. A class is the type of an object.
    A class can define methods
"""

"""
class Pythonista:
    def level(self):
        print('Amateur')
"""


# self as the argument of the method points to the current object instance, and must be specified when defining a method

# Create an instance of a class, using the syntax:
#Guido_Von_Rossum = Pythonista()

#A special type of method __init__(), a constructor is used to initialize one or more properties when we create a new object from that class

"""
class Pythonista:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def level(self):
        print('Novice')

Person1 = Pythonista('John', 16)
print(Person1.name)
print(Person1.age)
Person1.level()

"""

# Inheritance
"""
class Animal:
    def walk(self):
        print('Walking...')

class Dog(Animal):
    def bark(self):
        print('WOF!')
"""


#Now creating a new object of class Dog will have the walks() method as that's inherited from Animal
#roger = Dog()
#roger.walk()
#roger.bark()

#Modules in Python
"""
    Every python file is a module. You can import a module from other files, and that's the base of any program of moderate complexity
"""
# Python Standard Library
"""
Python exposes a lot of built-in functionality through its standard library.

The standard library is a huge collection of all sort of utilities, 
ranging from math utilities to debugging to creating graphical user interfaces.

You can find the full list of standard library modules here: https://docs.python.org/3/library/index.html
Some of the important modules are:
    1) math for math utilities
    2) re for regular expressions
    3) json to work with JSON
    4) datetime to work with dates
    5) sqlite3 to use SQLite
    6) os for Operating System utilities
    7) random for random number generation
    8) statistics for statistics utilities
    9) requests to perform HTTP network requests
    10)http to create HTTP servers
    11)urllib to manage URLs
"""

# Debugging in Python
#You debug by adding a breakpoint into your code
#breakpoint()

#Variable scope in Python
#Global variables and Local Variables

#Recursion in Python
"""
    A function in Python can call itself. 
    That's what recursion is. 
    And it can be pretty useful in many scenarios.
"""
"""
def factorial(n):
    if n == 1: return 1
    return n * factorial(n-1)

print(factorial(3))
print(factorial(4)) 
print(factorial(5)) 
"""


#Decorators in Python
"""
    Decorators are a way to change, enhance, or alter in any way how a function works.

    Decorators are defined with the @ symbol followed by the decorator name, just before the function definition.

"""
"""
@logtime
def hello():
    print('hello!')

"""

"""
    A decorator is a function that takes a function as a parameter, 
    wraps the function in an inner function that performs the job it has to do,
    and returns that inner function. 

"""
"""
def logtime(func):
    def wrapper():
        # do something before
        val = func()
        # do something after
        return val
    return wrapper
"""


#How to Install 3rd Party Packages in Python Using pip
"""
    The Python standard library contains a huge number of utilities that simplify our Python development needs,
    but nothing can satisfy everything.
    Those modules are all collected in a single place,
    the Python Package Index available at https://pypi.org,
    and they can be installed on your system using pip.
"""

#Python virtual environments
"""
    When applications require the same module,
    at some point you will reach a tricky situation where an app needs a version of a module,
    and another app a different version of that same module.

    To solve this, you use virtual environments.
"""
















