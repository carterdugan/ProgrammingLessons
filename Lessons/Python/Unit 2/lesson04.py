### TUPLES ###
'''
Before we continue, I strongly encourage you to take a
look at the Working with Errors document provided to
your instructor.

When programming, there is times where we might want to
contain our data in some way so that we can interact
with large bodies of data without typing a ludicrous
amount of code. The different ways of containing and
representing data are called "Data Structures". In the
python language, one data structure we can use is tuples.

Tuples are a group of data that can be accessed and read,
but after they are created they cannot be changed. They
are useful for containing groups of data that you do not
need to change and would like to reference as if it were
a single object. The pieces of data within a tuple are
called 'elements'. Let's take a look at how we create a
tuple.
'''

exampleTuple = (10, 12, 44, 2, 27)

# Let's print it and see what we get
print(exampleTuple)

'''
An example of how you could use a tuple can be
dimensions of a shape, such as a rectangle
'''
rectDim = (12, 4)

'''
Tuples can be indexed, meaning we can ask a tuple for an
individual element.
'''
example = (1, 2, 3, 4, 5)
print(example[1])

'''
That's weird. We asked for the element at index 1 and we
recieved the second element. Remember when we discussed
for loops and we learned that counting always starts at
zero? It applies here too. If you want the first element,
you asked for index 0. The second element is at index 1,
and so on so forth.
'''
example = (1, 2, 3, 4, 5)
print(example[0])
print(example[1])
print(example[2])
print(example[3])
print(example[4])

'''
This is where we can learn something interesting about
for loops. We can 'iterate' through every element in a
tuple using a for loop like such.
'''
example = (1, 2, 3, 4, 5)
for num in range(5): # remember, starts at zero, ends at 5 - 1 
	print(example[num])

'''
Excellent! This is a great way to have both the index of
the elements as well as the elements themselves. If we
just needed the elements themselves, there is an easier
way.
'''
example2 = (44, 22, 11)
for num in example2:
	print(num)

# It is important to know how to do this both ways


### LISTS ###
'''
Tuples are great, especially if you don't want anyone
changing with your data. But what if we want to change
our data later? Or what if we don't know how much data
will need to be stored? This is where lists come in.
Lists are just like tuples, except you can change any of
the data that is held inside of them. Let's take a look.
'''
exampleList = [5, 22, 78, 13, 19, 21, 22]

# You can still print lists!
print(exampleList)

# We can index it just as we could a tuple
print(exampleList[4]) # What number do you think this
					  # will show?

'''
Now lets try changing an element, this is done by
indexing the element we want to change and setting it to
what we want it to be. Here is the syntax
'''
exampleList = [5, 22, 78, 13, 19, 21, 22]
print(exampleList)
exampleList[2] = 14
print(exampleList)

'''
It worked! What else can we do with list? Quite a lot.
We can actuall add and remove elements to a list.
'''
exampleList = [5, 22, 78, 13, 19, 21, 22]
exampleList.append(23) # Adds to the end
print(exampleList)

# And we can remove from a list!

exampleList.remove(22)
print(exampleList)

'''
Notice how before we had two 22s in that list, and when
we removed one, only the first one was removed.

We can also remove a certain element by index using
'del' before name of a list and its index like so.
'''
ls = ['a', 'b', 'c', 'c', 'd']

# Let's fix this list by removing the second 'c'
del ls[3]
print(ls)

'''
You might have a list that has too many elements to add
manually, in which case it would be a good idea to make
and empty list and append to it with a for loop.
'''

# Let's make a list with numbers 0 - 99
ls = []
for i in range(100):
	ls.append(i)
print(ls)

'''
Lists, like many tools in our python toolbox, has too
many functionalities to go over in this lesson. There
are ways to insert new elements at a certain index,
remove an entire range of elements, and more. A lot of
these might be covered in future lessons, but if you
want to learn more sooner, I recommend looking into the
python documentation for lists. You should get used to
looking into python documentation if you are exploring
things on your own, because these tutorials cannot
possibly cover everything it has to offer.

As a side note, these lessons will no longer walk you
through avoiding errors. You must get used to finding
out for yourself what will work and what doesn't. Use
the debugging cheat sheet provided to your instructor to
help you solve these problems.
'''