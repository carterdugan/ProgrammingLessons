### WHILE LOOPS ###
'''
As a programmer, there will be times where you want your
program to do the same thing over and over again. Before,
when we made our game, we did that by letting our 'main()'
function call itself whenever we wanted to repeat a task.
This worked well for our purposes at the time, but for most
cases there is a better way for repeating tasks.

NOTE: The concept of repreating a task by calling a function
from within itself is called 'recursion'

The concept we are discussing is loops. There are two main
types of loops. The first one is called the 'while' loop.
A 'while' loop executes a block of code as long as a boolean
condition is True. That code will execute forever until that
condition is False. Say we wanted to count from 0 to 10.
Let's see how we can do this with a while loop.
'''
num = 0
while(num < 11):
	print(num)
	num += 1

# A second way to show some different ideas on how to
# solve the problem. Compare!
num2 = 0
while num2 <= 10:
	print(num2)
	num2+=1

'''
The while loop can do a lot more than just count. Let's
use the 'input()' function we learned before to control a
while loop.
'''
while(input("Say hi: ") != "hi"):
	print("That isn't 'hi' :(")

'''
We see that the loop doesn't always need a pre-existing
condition to work, and that the condition inside is always
tested. That means that in this case the 'input()' function
is called every time the while loop iterates, including
the first time. As soon as the condition is no longer true,
it exits.
'''

### FOR LOOPS ###
'''
A while loop can do a lot more than count, and even then
we don't always want to create a variable for a number to
be counted. For those reasons alone, a different kind of
loop exists called a 'for loop'. A for loop creates a
variable that exists only within the loop and removes
itself from the program after the loop ends. Let's try
counting to 10 again.
'''
for i in range(11):
	print(i)

# NOTE: the variable name 'i' can be anything, but it is
#		generally accepted that 'i' be used in the case
#		that the variable doesn't need any other name.
#		Feel free to name the variable anything you want!

'''
Let's disect this code. Notice the new keyword 'range()'.
'range()' is only used in for loops and just tells the
loop how we count. In this case we gave it one number, 11.
Just like before it started at 0 and went to only 10. That
is because counting always starts at 0 when programming.
The reason it never reaches 11 is because there are only
11 total numbers, and if the loop starts at 0, then it will
only reach 10. This may not make sense, but if you learn other
languages in the future you will see why this is the way it is.

So why create a whole new keyword such as 'range()' for this?
'range()' actually has room for one to three parameters. If you
use one parameter, by defualt that is the "stop" value. It will
count to this value and then stop. If you use two parameters, the
second one becomes the "stop" and the first one becomes the "start".
The for loop will start at the "start" and stop at the "stop" minus
one.
'''
for i in range(5, 11):
	print(i)

'''
There is one more parameter you can use. If you include a third
parameter, it will be the "step" parameter. By default, it is one
which is why the for loop always counts by one. If you needed
your loop to count by a different number, such as 5, you would
include that as your third parameter.
'''
for i in range(0, 11, 5):
	print(i)

# NOTE: Zero is still included

# Second NOTE: Code that comes after a loop will not be executed
#			   until that loop is complete

'''
Let's take what we have learned here and make a small program.
The program is to help people who do not know how to count. It
let's them enter a positive number, and will count to that number.
It will also let them quit the program.
'''

# Set an initial value
num = -1

# Exit only if they enter a 0
while num != 0:

	# Tell them to enter their number
	num = int(input("Enter a positive number, or 0 to quit: "))

	''' Since we are counting to the number they enter, tell
		it to stop at the number plus one'''
	for i in range(0, num+1):
		print(i)

# A pleasant message when they are done playing
print("Thank you! Goodbye!")


# No challenges for this one, I encourage you to think of
# and add your own features!

'''
Later on, we will discuss for loops further as they have other
uses than just counting.
'''
