### Digging into Functions: Scope and Return ###
'''
Before, we looked at functions and found that they can do
some pretty cool and useful things. However, functions are
a much more vast concept than what we have discussed thus
far. In this lesson, we are going to focus entirely on
functions, and spend some time implementing them into a
program in such a way that you might see in the real world.

The first thing we will be looking at is scope. In the terms
of programming, the word "scope" means the place in which
certain data can be accessed. In more simpler terms, data
such as a variable is not always accessible from every part
of the program. For example, lets say we have a function as
such...
'''
def exampleFunction():
	x = 5

'''
This example function has a variable within it called x that
contains an integer 5. Lets try to print that variable
outside of the function in the main body of our file.
'''
#print(x)

'''
We get a NameError saying 'x' is not defined. That is because
x exists only within the scope of our funciton
'exampleFunction'. Let's try doing things the other way around.
'''
x = 5
def exampleFunction():
	print(x)
#Now that it is set up, lets call it
exampleFunction()

'''
It worked! Now, you would not be alone if this doesn't make
sense. Why can a function access the outside scope but not the
other way around? This is because the outside scope is called
the 'global scope'. It means that any data within the outside
scope is available to read without needing specification.

So what happens if we try something else, like changing the
value of a global variable from within a function. What do
you think will happen?
'''
x = 5
def exampleFunction():
	x = 2
#Now call the function
exampleFunction()
print(x)

'''
Well, we didn't get an error, but our program didn't work the
way we wanted it to. Even though the function has access to
variables within the global scope, the variable didn't change!
Remember when I said that the global scope allowed functions
to read global data without specification? Well, if you want to
WRITE global data, such as assigning a different value to a
global variable, you must specify that the variable you are
writing to is global. This is done by placing the keyword
'global' followed by the name of the global variable at the
beginning of the function.
'''
x = 5
def exampleFunction():
	global x # specify that we are messing with global data
	x = 2
exampleFunction()
print(x)

'''
It works! However, let it be known that it is bad practice to
write global data from within a function. It is still important
to know and use the global keyword, but changing global data from
within a function is typically something programmers look down on.
But sometimes we might still rely on functions to efficiently 
work with our data, global or not!

That is where the 'return' keyword comes in. The 'return' keyword
is used to return a value from the functions scope to the scope of
wherever the function is called (NOTE: functions can be called by
other functions). This means that data from within the function can
be accessed, and can also be used to change global data using a
functino without needing to do so within the function. Let's try it!

NOTE: When a value is returned from a function, it takes the place of
	  the function call wherever it was called.
'''
x = 2
def addTwo(variable):
	variable += 2
	return variable

x = addTwo(x) # When a value is returned from a function,
			  # it takes the place of the function call.
print(x)

'''
This was an example of how you might see a function changing
global data more realistically. However, return has a quirk
that some might see as a limitation. As soon as return is called,
the function ends. That means that the seond print call within the
function in the following example will never be called.
'''
def exampleFunction():
	print("Hello...")
	return
	print("...world!")
exampleFunction()

'''
However, you will never want to place code that *needs* to be done
after the 'return' keyword. If there is a possiblity you might need
to return before the other code is executed, you should use an 'if'
statement. Let's see how we can do such a thing.
'''
def isFour(variable):
	if(variable == 4): # Checks if the variable passed in
					   # is 4

		return True # if it is, return true

	return False # Return false. If the variable is 4, it will
				 # never get here

x = 4
y = 7
print(isFour(x)) # True
print(isFour(y)) # False
print(isFour(18))# False

### Type Casting and User Input ###
'''
Lastly, we are going to introduce two new tools, as we try to
make a game with what we know so far. The first tool we will
learn is called casting. Say we have a string that contains just
a number as follows...
'''
x = "5"

# If we try to do math with it, watch what happens
#print(x + 2)

'''
We get an error. This is because "5" is a string, not a number,
therefore it won't work. We can change "5" into a number by casting
it using 'int()'
'''
print(int("5") + 2)
print(int(x) + 2) # Still works with variables!

# It works! You can do this the other way around to add numbers
# to strings using the 'str()' cast keyword

print("I am " + str(20) + " years old!")

'''
The last thing we are going to learn is the concept of user input.
If we have a program, and we need the user to input something for us
to use, one way we can do this is by getting them to type something
into the terminal using the 'input()' keyword.

When 'input()' is called, the program halts until the user enters
something on the terminal. Whatever they enter is then returned.
Let's assign it to a variable and print it out!
'''
iWillRepeat = input()
print(iWillRepeat)
# Lets do it again but with a string as a parameter, and then tack
# it onto another string
simonSays = input("Type something: ")
print("Simon says '" + simonSays + "'")

#Notice how the string parameter is not repeated with the result

'''
NOTE: 'input()' by default returns a string. If the user gives you a
	   number, and you want to use it in a calculation, you must cast
	   the result as an 'int()'.
'''

### MAKING A GAME ###
'''
Let's challenge ourselves to use all we know to make a game. The game
is simple, there is a random number between 1 and 1000 that the user
must guess. If the user guesses too low, the game will tell them
"higher". If the user guesses too high, the game will tell them
"lower". If the user guesses correctly, they win! Let's begin.
'''

# First we assign our hidden number
winningNum = 273

# Then we can make a function for handling the player's
# guess
def playerGuess():
	# We cast the guess to a number to avoid an error later
	num = int(input("Your guess: "))
	return num

# Let's make a main function to handle all of the game functionality
def main():
	# This is the beginning of the game
	print("I am thinking of a number between 1 and 1000...")

	# Now lets let get their guess
	guess = playerGuess()

	# Let's see if they got it right
	if(guess == winningNum): # Global so we can read it
		print("You win!")
		return
	# Now if they undershoot
	elif(guess < winningNum):
		print("Higher")
		main() # Call the function again so they can keep trying
	# ...or overshoot
	elif(guess > winningNum):
		print("Lower")
		main()

# Don't forget to call the function to play the game!!!

'''
We have made our game! But it is a little boring. See if you can add
some stuff on your own to spice it up. Here is a list of things to add:

-Tell the player how many attempts it took them
-A limit on the attempts they have
-Tell them how many attempts they have left
-A score based on attempts
-Add spacing between the game's responses

At the bottom of this document I will include a version of the game
that has all of those features. Be sure to look it over and compare
it to your own code and see what you could have done differently!
'''





# First we assign our hidden number
winningNum = 273

# The player's attempts start at 0
attempts = 0

# Then we can make a function for handling the player's
# guess
def playerGuess():
	# We cast the guess to a number to avoid an error later
	num = int(input("Your guess: "))
	return num

# Let's make a main function to handle all of the game functionality
def main():
	# Clarify attempts is global so we can add to it
	global attempts

	# Add some space between text
	print()
	print()

	# Do not let the players surpass 10 attempts
	if(attempts > 10):
		print("You Lose...")
		return

	# This is the beginning of the game
	print("I am thinking of a number between 1 and 1000...")

	# Tell the player how many attempts they have left
	print("Attempts remaining: " + str(10 - attempts))

	# Now lets let get their guess
	guess = playerGuess()

	# Add to their attempts after every guess
	attempts += 1

	# Let's see if they got it right
	if(guess == winningNum): # Global so we can read it

		# Give them their attempts and calculate a score
		print("You won in " + str(attempts) + " attempts with a score of " + str(10000 - 1000 * attempts) + "!")
		return
	# Now if they undershoot
	elif(guess < winningNum):
		print("Higher")
		main() # Call the function again so they can keep trying
	# ...or overshoot
	elif(guess > winningNum):
		print("Lower")
		main()

main()