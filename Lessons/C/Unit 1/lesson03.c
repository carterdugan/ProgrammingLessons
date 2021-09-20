/*
In this lesson, we will take a look at how to implement
boolean logic and the functionalities that use it within
the C language. C handles boolean logic in many ways
that are similar to python. In basic C, the only real
difference is the fact that there is not "true" or
"false" keywords in basic C. There are libraries that do
allow the use of these keywords just like in python, but
since C is a lower level language, it deals with the
core concept of binary for boolean logic.

First, lets include our input/output library
*/
#include <stdio.h>

// Now, lets begin our main function

int main()
{

	/*
	Binary represents bool statements in C in the way that 1
	represents true, and 0 represents false.

	An if-statement does the same thing in C that it does in
	python. If the statement following the keyword 'if' is
	true, meaning its boolean value is 1, then the code
	within its brackets will be executed. Otherwise,
	if the statement is false, meaning it has a boolean
	value of 0, it will not execute the code within its
	brackets.

	Let's run a few tests of if statements.
	*/
	if(1)
	{
		// We are printing a string, so %s
		printf("%s", "This statement is true");
	}

	// Print a new line to separate things
	printf("%s", "\n");

	if(0)
	{
		printf("%s", "This statement is false");
	}

	if(5==5)
	{
		printf("%s", "5 is equal to 5");
	}

	printf("%s", "\n");

	if(5==6)
	{
		printf("%s", "5 is equal to 6");
	}

	if(5>10)
	{
		printf("%s", "5 greater than 10");
	}

	if(5<10)
	{
		printf("%s", "5 less than 10");
	}

	printf("%s", "\n");


	// We can see an else statment works as expected
	int x = 0;
	if(x == 1)
	{
		printf("%s", "x is one");
	}else
	{
		printf("%s", "x is not one");
	}
	printf("%s", "\n");

	// Else if statments are a little different, but work the
	// same
	int y = 5;
	if(y == 4)
	{
		printf("%s", "y is 4");
	}else if(y == 5)
	{
		printf("%s", "y is 5");
	}else
	{
		printf("%s", "y is not 4 or 5");
	}

	printf("%s", "\n");

	int z = 6;
	if(z == 5)
	{
		printf("%s", "z is 5");
	}else if(z == 6)
	{
		printf("%s", "z is 6");
	}


	// Return an error code of 0 from the main function
	return 0;
}