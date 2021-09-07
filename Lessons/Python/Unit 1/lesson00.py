### BUILT-IN FUNCTIONS ###
'''
Python, like many other languages, has a number of built-in functions.
In programming, a function or method is a block of code that can be
"called" or plugged in by typing its name and giving it the information
it needs. Later, we will create our own function, but for now we will
only be using the 'print()' function
'''

print("Hello, World!")

'''
Let's disect the above code. 'print()' is a built-in function that
prints out information to the console in the form of characters.
The name of the function is 'print' and, since it is a callable
function, requires a pair of parenthesis to follow it. Within the
parenthesis, we see that in this case we are using a string, that is,
a string of characters that will be printed out exactly as typed.
Strings are one of many data types, which are ways of representing
data. It is one of the main ones you will use as a beginner in
python. Another kind of data types you will see is numerical data 
types.
'''


### Numerical Data Types ###
'''
Numerical data can be represented with a lot of data types. The ones you
might see most often are integers, doubles and floats. The only difference
you need to worry about now is that integers are used when a number does
not need to be represented as a decimal. A double/float just means a number
represented as a decimal. Numerical data can also be printed to the terminal
using the 'print()' statement.

NOTE: Numerical data is a bit more complex than it was just described, but
	  at the beginner stage the difference is so small that it does not matter.
'''

print(5) # prints an integer
print(5.0) # prints a double

'''
We can also see that we can perform a number of math operations on
numerical data.
'''

print(2+2) # Addition operator, adds 2 and 2
print(4-2) # Subtraction operator, subtracts 2 from 4
print(2*2) # Multiplication operator, multiplies 2 by 2
print(6/2) # Double Division operator, divides 6 by 2 as a decimal
print(6//2) # Integer Division operator, divides 6 by 2 as an integer.
print(2**3) # Exponential operator, raises 2 to the power of 3
print(5%2) # Modulus operator, returns the remainder of 5 divided by 2.

print((2+2)*4//4) # Python follows the order of operations


### VARIABLES ###
'''
Like in math class, a variable is a representation of data that makes
things easier to work with and read. If you have a very large number and
complex number like 1903348, but don't want to type it every time you want
to use it, you can assign it to a variable and use the variable in its
place.
'''

x = 1903348
print(x)

# Math can also be performed on these variables
print(x+2)

y = 2
print(x + y)

z = x + y
print(z)

# Any data type can be represented as a variable
a = "Hello, world!"
print(a)

'''
You can name a variable anything as long as it is NOT a keyword such as
'print' or 'if' and does not have a number or symbol at the beginning
'''
stupidName = "This variable has a stupid name"
print(stupidName)

'''
There are naming conventions for writing variable names. Most commonly,
you will see that is the norm to make the entire name lowercase, only 
capitilizing all of the first letters of words after the first word
'''
goodVariable = 1
goodVariable1 = 1
badvariable = 0
BADVARIABLE = "blah"
KindaBadVariable = "blah2"

'''
Variables, when using numerical data, also have their own numerical
operators.
'''
x = 1

x += 1 # Adds one to x and then assigns sum to x
print(x)

x -= 1 # Subtracts one from x and then assigns difference to x
print(x)

x *= 5 # Multiplies x by 5 then assigns product to x
print(x)

x //= 5 # Divides x by 5 then assigns quotient to x (also works with /)
print(x)


### BOOLEAN LOGIC ###
'''
Boolean logic deals with data that can be represented as 'True' or 'False'
The boolean values 'True' and 'False' can be assigned to variables, but
more powerfully are returned from comparison statements such as '==' and
'!='. The '==' statement checks if two things are equal to each other, if
they are, it returns 'True'. Otherwise, it returns 'False'. The '!="
statement does the exact opposite.
'''
print(5==5)
print(5==6)

print(5!=5)
print(5!=6)

'''
What makes boolean values so powerful is that they can be used with if,
else, and else-if statements. These statements are what drive computer
programming forward, and are a large part of almost any programs code. An
'if' statement is used to check if a boolean logic statement is 'True', if
it is, it will then execute a specific block of code. An 'else' statement
can follow the 'if' statement, and if the 'if' statement is 'False' the
'else' is then executed.
'''

x = 5 # Run the following code first, then again after changing the
      # value of x
if(x == 5):
    print("x is 5!")
else:
    print("x is not 5...")

# NOTE: An 'if' statement does not always need an 'else' in order to work
#       but an 'else' always needs an 'if' before it

y = True
if(y):
    print("y is True!")

'''
If you have code for other values, you can put else-if statements, or
'elif' after your if statement to check other values.
'''

x = 10
if(x==11):
    print("x is 11!")
elif(x==10):
    print("x is 10!")

# You can also include an else statement after all of the 'elif'
# statements
y = 10
if(y == 8):
    print("y is 8!")
elif(y == 11):
    print("y is 11!")
else:
    print("y is not 8 or 11")


### Indentation and comments ###
'''
Now all the fun stuff is done, but before going on to explore the
different things you can do, make sure you make yourself knowledgable of
indentation and comments.

Indentation is the white space (spaces, tabs, empty lines) before, after
and in-between code. In most other languages, whitespace matters almost
not at all. In python, this is not always true. When doing an 'if'
statement or anything like that, the code that executes as a result of
the statement must be indented farther than the code that is not. This is
called the 'scope' of the statement. There is more to be discussed on
scopes later.

Furthermore, if you use one form of indentation, such as a tab-character,
1 space, 2 spaces, or any amount of tabs or spaces, you must use that
same indentation throughout you entire python file, or else you will get
a very annoying indentation error that is very tedious to fix.

Lastly, comments are the blocks of text used throughout this code to
write in plain english. A single line comment can be written using #
while a multi line comment can be enclosed in three single-quotes.
'''