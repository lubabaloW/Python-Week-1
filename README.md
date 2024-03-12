# Python-Week-1

#VARIABLES AND TYPES
The basic unit of a program is called a variable, which is assigned a value.
(=) is used as an assignment operator.
Variable name:
 - Should not begin with a number.
 - Can contain upper and lower case letters, as well as underscores.
 - Traditionally beigins with lower case letters.
There are several types of variables in Python:
 - Intergers (whole numbers)
 - Floats (decimal numbers)
 - Complex numbers (for complex mathematical calculations)
 - Strings (collection of characters)
 - Boolean (true or false)
(+) sign is used to link strings, but cannot be used to add strings and numbers.     
Error messeges can provide useful information.

#DATA STRUCTURES
Allow for storage of a list of values in a single variable

~List Data Type~
Contains any data type, including a list within a list.
Length of a list can be determined using a length function.

~Set Data Type~
Is similar to a list, except it only contains unique elements and is declared using curly braces.
The order of elements in a set is not improtant, unlike in a list.

~Tuples Data Type~
Are similar to lists, except they cannot be modified once declared.
They are useful when you need to store large amounts of data more efficiently in memory like X Y coordinate pairs.

~Dictionary Data Type~
Is a collection of key-value pairs, similar to a word and its definition in a book.
Dictionaries are declared using curly braces and accessed using keys.

#OPERATORS 
Are instructions that perform operations on values and variables in Python.
They are used to manipulate and perform actions on data.
The most familiar type of operater is the arithmetic operator, which is used for mathematical calculations.

~Arithmetic operator examples~
Addition (+), adding one and one gives you two.
Multiplication (*), multiples numbers together.
Division (/), returns are floating-point value, even if the result is a whole number.
Exponent operator, raises a number to a specified power.
Modulus, provides a remainder are devision.
Comparison operator (><==)
Logical operator (&&, ||)
Membership operator (in / not in)

#CONTROL FLOW
~If/else statements~
~For loop~
~While loop~

#FUNCTIONS
A function is like a machine that takes input and produces outputs.
It can be defined using the "def" keyword followed by the function name and arguments in parentheses.
The function body is indented and contains code that performes the desires operation on the input and the "return" keyword returns the output.
The keyword "none" represents the absence of a value. It is basically used when a function does not return any value.
  
#CLASSES AND OBJECTS
A class helps to label and organise related collections of classes and attributes.
Initialization (Init) function is called everytime an instance of a class is created.
The init function takes in a variable called "self" which refers to a specific instance in a class.
    
       class Dog:
       def _Init_(self, name)
       self.name = name
       self.legs = 4

       def speak (self):
       print (self.name+ 'says: bark')


















