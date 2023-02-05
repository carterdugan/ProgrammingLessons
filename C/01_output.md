# Output

Most software takes input from the user and gives back some sort of output in response. When thinking of an example of input, think your mouse and keyboard. The output would be your cursor moving on the screen as a result of the mouse moving, or letters/numbers appearing as a result of typing on your keyboard. All of this is happening as a result of some software that is taking in some input and spitting out some output.

In this lesson we are going to focus on learning how to use some basic output functionality provided by the C standard library. To be more specific, we will be focusing on the `printf()` function. The word `function` is another topic for another day. For now just think of `printf()` as a tool that C provides you.

---

## Dissecting the First Program

Let's take a look at the program we wrote before and pick it apart line by line.

```c
#include <stdio.h>

int main(void)
{
    printf("Hello, World!\n");

    return 0;
}

```

### Setup

The first line of our program is `#include <stdio.h>`. All this does is tell the compiler what tools we want to include in our program. In this case we are including `stdio.h` which includes tools for standard input and output, hence the `std` for standard and `io` for input and output.

Next we have `int main(void)`. Without getting too deep into it, we can simple look at this line as telling the compiler where our code begins. The compiler will always look for `main` and know that is where to start.

We then see an opening curly brace `{`. You may notice that at the bottom of our program is a closing curly brace `}`. These tell the program where the code that belongs to `main` goes. In other words, it tells the program what code to execute when it finds `main` and that it begins after `{` and ends before `}`.

### The good stuff
Now we get into the meat of our program, `printf("Hello, World!\n");`. If you were able to successfully get this program to run, you may have noticed that the output of the program matched the text inside of the double quotes within the paranthesis of `printf()`, except the `\n`. That is the whole purpose of `printf()`: to ouput text on the screen.

The `()` tells `printf()` that we are going to be giving it information, in this case the information being `"Hello, World!\n"`. When you have text inside of double quotes, that is called a `string`, a `string` being a collection of [ASCII Characters](https://www.computerhope.com/jargon/a/ascii.htm) (TLDR; alphebatical, numberic and special characters).

So we see that everything we put inside of the double quotes in `printf()` appeared on the screen with the exception of `\n`. This is ebcause `\n` is a special set of characteres, in this case representing a new line. There a collection of these, but for now we will be using `\n` only whenever we need to separate two lines of text. See the next few examples to understand why we need `\n`.

Finally, we see a semicolon `;` at the end. This tells the compiler that the current instruction is finished (in this case, the `printf()` instruction). If you don't understand this, you will catch on as we write some examples.

### Cleaning up

For now, don't worry about `return 0`. There will be more information about that later on in the lesson about `functions/method`. Its purpose in this case is to tell the user that the program finished without any errors. You'll see that this line, too ends with a semicolon `;`.

Finally we have the `}` that we discussed before.

---

## Playing with `printf()`

### Multiple `printf()`s.

Let's see what we can do with `printf()`, starting with multiple `printf()` statements.

```c
#include <stdio.h>

int main(void)
{

    printf("Hello, ");
    printf(" World!\n");

    return 0;
}
```

Notice how both strings appear on the same line with the output. This is because the first `printf()` has no `\n` in the contained string.

Also note that there is a semicolon `;` after each line. If you did not understand its purpose before, you may now see that every instruction is followed by a `;`. If you're curious, try removing the `;` on one of the lines and see what the compiler does when you try and run the program.

### Printing numbers and doing some math

Now let's start playing with some numbers. We can print numbers as strings as you might expect.

```c
#include <stdio.h>

int main(void)
{

    printf("2\n");

    return 0;
}
```

But there is another way to print numbers:

```c
#include <stdio.h>

int main(void)
{

    printf("%d\n", 2);

    return 0;
}
```

As you can see, both programs produce the same output, so why use the second method? And what does that `%d` mean? Before we get into `%d`, let's see a more powerful way to use it.

```c
#include <stdio.h>

int main(void)
{

    printf("%d\n", 2 + 2);

    return 0;
}
```

Your output should be `4`. If this is not the output, ask your teacher for help.

If it did work, let's finally take a look at what the `%d` did and how the program new what to do with the `2 + 2`. The `%d` tells the compiler that we will be inserting a number in its place within the string. Easy! The 2 + 2 is simple enough for the compiler to calculate the answer before the program runs. When we do more complex calculations later on (with variables. Yay!) we will see then that the compiler will not be able to do the math for us, and rather the program itself will do the math.

If you got lost in that last part, don't worry. It will all make sense later on. For now, just play with the math and see what other exciting results you can get. See what works and what doesn't. We will cover math more in depth when we cover variables, but I encourage you to first experiment with what we have learned. Here is another example to get you started.

```c
#include <stdio.h>

int main(void)
{
    printf("%d\n", 5 * 2);

    return 0;
}
```
