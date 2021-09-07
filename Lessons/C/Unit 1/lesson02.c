/*
In this lesson, we will be learning how to use
functions. At this point, you will begin to see that
most programming languages are very similar in a
lot of ways.

Functions are very similar to how we learned them in
python aside from a few key differences. Just like in
python, functions allow the programmer to execute the
same code multiple times and with different data without
having to write the same code over and over.

In C, we saw that we have to tell the compiler what kind
of data we are returning, if any. If we make a function
that does not return any data, we tell the compiler that
the function is 'void'.

*NOTE* The main function is still needed to run the
program, thus needed to call these functions. We will
add it to the end of the program because we cannot call
functions before they exist.
*/

// Include our library
#include <stdio.h>

void printHello()
{
	// print a newline to separate this text
	printf("\n");

	// print the message
	printf("Hello!");
	printf("\n");
}

/*
Our next function will take parameters, just like we
learned in python. The rules are mostly the same, except
when we add a parameter, remember that it is a variable
and a variable must have a data type.

Let's make a function that takes two integer parameters
and returns their sum.
*/

// Tell the compiler we are returning an int
int addFunc(int a, int b)
{
	// Return the sum
	return a+b;
}

/*
Note that scopes exist just like in python. Refer to the
python lesson about functions and scopes if you do not
remember the rules of scopes.
*/

// Our main function
int main()
{
	printHello();
	printf("%i", addFunc(2, 4));
	return 0;
}