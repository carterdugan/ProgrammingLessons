### CUSTOM FUNCTIONS ###
'''
So far, we have looked at the built in 'print()' function. Python has
many other built in functions, but a lot of them require more extensive
knowledge of the language, so for now we are instead finally going to
look into making our own functions.

Functions are similar to variables in that they can be named anything.
Most people use the same naming convention for functions as they do
with variables. The difference is, when you define (create) a function,
you must tell python what you are doing. To tell python you are making
a function, the syntax is as follows:
'''

def functionName():
    #do stuff
    pass

'''
Notice how just like if statements, we have a colon and white space
indicating a block of code will follow. That block of code will
replace the 'do stuff' comment. Below that comment, we see another
python keyword 'pass'. The 'pass' keyword means literally 'do nothing'
the only reason it is there is because a function cannot be empty in
python, it must contain some code.

So what is the point of a function? Remember how in the last lesson
we ended up typing the same code several times? A function's purpose
is to prevent you from needing to write the same code more than
neccessary. For example, say we wanted to print 'Hello, world!'
multiple times without typing 'print("Hello, world!")' over and over.
'''

def phw():
    print("Hello world!")

'''
We have created our function, now it is time to call it. Remember how
we called 'print()'? We must put a pair of parenthesis at the end of
the name of the function to call it.
'''

phw()

# We can do it as many times as we like!
phw()
phw()
phw()

# NOTE: A function must be defined (created) before it is
#		called, as python reads files from top to bottom
#		and won't know what to do if you call a function before
#		it is created.

'''
This is cool and all, but it does not actually do anything useful. The
true power of functions is when you have one that does some sort of
computing with data that you provide to it. Remember how we could pass
a string or a number to 'print()' to make it print something on the
terminal? You can make your custom functions take data in as well. The
information you are passing to your function are called 'parameters'.

Parameters are what go inside of your function's parenthesis. When you
create your function, you will put the parameters in the parenthesis as
variables. You can then use these parameters as if you declared them as
variables with an '=' sign. When you call the function, you can pass
anything you want as long it is the same amount of parameters and the
right order that you want, or else you might get an unwanted outcome.

Let's demonstrate this by creating a simple function that adds two
numbers.
'''

def add(x, y):
    print(x + y)

# We have created a function that takes two numbers and prints their stum
# Now, lets call it
add(2, 1)


### MORE BOOLEAN OPERATORS ###
'''
Before we continue having fun with functions, we should take some time
to learn more complex boolean operators. This will also serve as a
review, as later we will begin combining multiple aspects of what we
have learned.
'''

# Set some variables to perform boolean logic
x = 1
y = 2
z = 1

# Review what we have seen before
print(x == 1)
print(x != y)
print(x != z )

# New operators
print(y > x) # checks if y is greater than x
print(y < x) # checks if y is less than x
print(x >= z) # checks if x is greater than or equal to z
print(y <= 2) # checks if y is less than or equal to 2

'''
There are three other operators that are also very important but
will require a more complex explanation.

The first operator is the not operator. It is the most simple of
the three. The not operator comes before a boolean operation and
inverts/flips the result. For example, if we have an operation that
is 'True', placing a 'not' before it will flip it to 'False'
and vice versa.
'''
x = True
print(x)
print(not x)

y = 2
print(not(y != 2))

# A more complex example. Challenge: This can be written in
# a better way. Can you write it better?
x = 5
y = 6
if(not(x + y == 10)):
    print("The sum of 6 and 5 is not 10")

'''
The second operator is the boolean 'and'. An and can link two
booleans together to form their own boolean. In order for a boolean
'and' to be true, both sides of the operator must be true. For
example, if I asked you to bring me a keyboard and a mouse, and you
only brought me a keyboard, would you have done what I asked? No, you
must bring me a keyboard AND a mouse in order to have done what I
asked.
'''
x = True
y = True
print(x and y) # This should return True, as both x and y are true

z = False
print(x and z) # This should return False, as not both x and z are true

'''
The third and alst operator we are going over is the boolean 'or'.
Like 'and', 'or' links two boolean functions together. However, with
'or', as long as at least one side is true, then the 'or' will be
true. Using the same example as before, if I asked you to get me a
keyboard OR a mouse, I would be okay with you bringing just a keyboard,
just a mouse, or both. But I would not be okay with you bringing me
neither.
'''
x = True
y = False
z = True

print(x or y)
print(x or z)
print(y or False)
