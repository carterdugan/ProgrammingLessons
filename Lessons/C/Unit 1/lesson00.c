/*
We will look at a simple hello world program in C today.
Remember that C is a very complex language, so a program
that takes a short amount of code in python will take a
bit more code in C. I will write the program line by
line and give a detailed explanation for what each line
means and what it does.
*/

/*
We first tell the compiler to include a library. This
library is called 'stdio' and is contained in the header
file 'stdio.h'. It gives us some tools to interact with
the command line, such as printing a message to the
screen and getting user input. The 'std' means standard
library and the 'io' means 'input' and 'output'.
*/
#include <stdio.h>

/*
Unlike python, the program does not run the first code
it sees. Rather, it looks for the main function, which
is always called 'main' and has the return type of
'int'. Remember when we returned values from functions
in python? In C, if a function is going to return
something, you must tell the compiler what type of data
the function is going to return. In the case of 'main',
the function will return an integer. More on this later.

Unlike python, white space such as tabs and newlines are
not a requirement. The way you tell the compiler what
belongs to a function's scope is with curly braces. This
means everything within main's curly braces will execute
when main is called.
*/
int main()
{

	/*
	One of the functions we included from stdio was the
	'printf' function. It is used to print things to the
	screen and even format the print before hand. More
	on that later, but for now, we will use it to print
	to the screen only.

	Notice how there is a semicolon at the end of the
	line. This tells the compiler that this line of code
	is done executing. Remember how we said newlines
	don't matter? We could technically right every line
	of code on one line together. This is bad practice,
	so the things that pyhton forces, such as tabs at
	the beginning of certain lines and newlines before
	every line of code, are a standard that should be
	used.

	You WILL forget to use semicolons... but it is an
	easy fix.
	*/
	printf("Hello, world!");

	/*
	As said before, main needs to return an integer
	value as we described in its signature ("int main").
	This is the value we will be returning. The integer
	returned by main is the error code. The error code 
	is useful for helping us debug errors in our code.
	If our program exits with an error code of zero, we
	know that our program finished without and errors.
	Otherwise, we know there is something we need to
	fix.
	*/
	return 0;


}