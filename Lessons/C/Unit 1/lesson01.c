/*
In this lesson we will be learning about variables in C,
a new operator that isn't in python, and little bit on
arrays. This is a lot of content, but it is important
knowledge for the road ahead. Let's begin.
*/

// First we must include our io library
#include <stdio.h>

// Lets start by making our main function
int main()
{

	/*
	We will now declare two variables in two different
	ways. The first way is to do it all in one line. We
	must tell the compiler what kind of data will be
	assigned to the variable first. In our case, we will
	have an integer. Then, we can name the variable. The
	naming conventions are the same as in python. Let's
	assign the value of 5 to our variable.
	*/
	int num = 5;

	/*
	The second way to name your variable is to
	initialize it (give it a data type and name) first
	and then assign it a value later. This may not seem
	very useful, but this will become a very useful tool
	later on.
	*/
	int num2;
	// We can now assign it a value.
	num2 = 5;


	/*
	Now we can print these values. Printing in C is very
	different in C compared to python. All 'printf' does
	is print a string, not numbers. However, it can take
	numbers as an argument when formatting the string.
	That is where the 'f' in 'printf' comes in, it means
	'format'.

	The first argument is the string to be formatted.
	Notice that where our values would go, there are two
	'%d'. The % tells printf that we are inserting a
	value in that position. The following letter tells
	printf what kind of value will be going there. In
	this case, the 'i' means 'signed integer'. After we
	give it our string, we give it the two values to
	insert as seperate arguments.
	*/
	printf("num is %i and num2 is %i", num, num2);

	/*
	Now for some math. C has all of the same math
	operators as pyhton, however it has one that python
	does not have. Like python, you could add one to the
	num variables like this:
	*/
	num += 1;

	// Or you could do it like this
	num2++;
	/*
	This is the standard way of adding one to a numeric
	value in c. You could also subtract one from it with
	num2--. Let's print out what we have so far.
	*/

	// Let's print a newline first to separate this line
	// from the last.
	printf("\n");

	printf("num is %i and num2 is %i", num, num2);


	/*
	Now lets get into the concept of arrays. If you
	remember lists from python, arrays are similar in
	that they hold data. Where they differ is that
	arrays are of fixed size, they cannot change size
	without being very familiar with how C works and
	knowing some work arounds.

	Let's look at two ways to make an array. The first
	is to make the array all together on one line. This
	is done by initializing the array by telling the
	compiler we are making an array with square brackets
	and then writing out the elements of the array with
	curly brackets.
	*/
	int numbers[] = {5, 6, 3, 2};

	/*
	The other way to make an array is to tell the
	compiler that the array will be a certain size. Then
	you can assign variables to the array at their
	specific index.
	*/
	int numbers2[3];
	numbers2[0] = 3;
	numbers2[1] = 4;
	numbers2[2] = 5;

	/*
	Now lets check and make sure it is working. There is
	not an easy way to print arrays of numbers, so for
	now lets print just the first element of the arrays.
	Remember, counting starts at 0.
	*/
	printf("\n");
	printf("The first element of numbers is %i and the first element of numbers2 is %i", numbers[0], numbers2[0]);

	/*
	The reason I am showing you arrays now is because
	string do not exist in basic C. A string in C is
	actually an array of 'char' data. A 'char' is a
	character, meaning a single symbol. Let's set a char
	variable and print it to the screen.
	*/

	char letter = 'a';
	char symbol = '~';

	printf("\n");

	// Notice how we now use %c for chars
	printf("letter is %c and symbol is %c", letter, symbol);

	/*
	Now we can make a character array for us to print.
	Lets make one that says 'Hello, world!'. Notice how
	I can use quotes to list the elements of the array.
	I am only able to do this for character arrays.
	*/
	char message[] = "Hello, world!";
	printf("\n");
	printf(message);

	// Return our error message
	return 0;
}