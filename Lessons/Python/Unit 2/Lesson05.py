### CLASSES ###
'''
While not difficult to program, many people find the
concept of classes and OOP difficult to understand and
leave a lot of people lost, so don't be worried if you
struggle with this concept.

A class is a body of code that can be used to classify
objects. Think of a class called Job. Objects that might
classify under job might be...
- Programmer
- Plumber
- Teacher
- Electrician

All of these are jobs and in programming could be created
underneath the classification of Job. In programming, to
create a class is to create that classification and to
give it attributes and features that belongs to objects
that fall within it. Let's try and make a small class.

The syntax is to use the keyword 'class' followed by the
name of the class. Unlike variables and functions,
class names should always have the first letter
capitalized.

A class can contain functions and variables that belong
to each member (an object that belongs to it) and can be
accessed by each member as well. Here is an example of a
class used for classifying family members.
'''

class FamilyMember:
	def setName(self, name):
		self.name = name
	def sayHello(self):
		print(self.name + " says 'Hello'")

'''
We now have a class called family member with two
functions and its own variable. The functions and
variables of a class are called 'attributes'. If you run
this code, nothing will happen because this class is
unused. Notice how all of these functions have the word
'self' within them? That means that to use those
functions, a member of that class must exist. Let's make
two.

Since this class is for family members, let's make a
family member called "Dad". First, we must assign a
variable to our dad object and make it clear to python
that our variable is a member of the FamilyMember class.

Let's do the same thing for a son family member as well.
'''

dad = FamilyMember()
son = FamilyMember()

'''
Now that they exist, let's give them names using their
'setName' function attribute. But we don't want them to
have the same name, so how do we call this function for
them individually? This is done by typing the variable,
then a period, and finally the name of the function we
want to call. Then, pass any neccessary parameters.
'''

dad.setName("Doug")
son.setName("Charlie")

'''
Now they have names. And we can see that by asking
python to print their name attribute. We can see that
the name attribute exists because within the class, they
are assinged a name to themselves with 'self.name'.
'''

print(dad.name)
print(son.name)

'''
It works! Now lets call that last function for each of
them and see what happens.
'''
dad.sayHello()
son.sayHello()

'''
Excellent! So why use classes? Unfortunately we do not
know enough about them now to make something useful with
them, however we can imagine how they might be useful in
the future. Imagine a game with a bunch of enemies moving
around. Rather than changing their position manually, one
by one, we could make them all part of a class, then tell
that class to move all together. That would cut our code
into a small fraction of the nightmare it would've been.
'''