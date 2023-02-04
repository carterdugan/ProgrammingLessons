# Introduction

C is a lower-level language that gives the programmer control over their computer hardware and very fast performance due to how close it is to [assembly language](https://en.wikipedia.org/wiki/Assembly_language). For these very reasons it is often used for systems programming such as operating system development and embedded systems. While C is very powerful, it is not without it's drawbacks. With great power comes great responsibility, and the raw power that C provides to the programmer often leads to bugs that can be very difficult to fix. Don't let this fact intimidate you, as C can be very useful to learn for the knowledge it provides about how software interfaces with hardware at a fundamental level.

In these lessons we will cover a multitude of topics from basic C programming to advanced C programming. These tutorials are meant for beginners with little to no programming experience up to intermediates who are already familiar with C and have a solid foundation in programming. I hope that no matter what level of experience you have, you will be able to learn something from these lessons.

---

## Resources

* [The C Programming Language](http://cslabcms.nju.edu.cn/problem_solving/images/c/cc/The_C_Programming_Language_%282nd_Edition_Ritchie_Kernighan%29.pdf)
* [Online C Compiler](https://www.onlinegdb.com/online_c_compiler)
* [The C programming langauge wikipedia](https://en.wikipedia.org/wiki/C_(programming_language))
* [GCC compiler (Ubuntu, used for these lessons) download and install tutorial](https://www.youtube.com/watch?v=oLjN6jAg-sY&ab_channel=ProgrammingKnowledge2)
* [MINGW compiler (Windows, very close to gcc) download and install tutorial](https://www.youtube.com/watch?v=WWTocqPrzMk&ab_channel=GeekyScript)
* [CodeBlocks IDE (Windows) download and install tutorial](https://www.youtube.com/watch?v=GWJqsmitR2I&ab_channel=LearningLad)
* [CodeBlocks IDE (Ubuntu) download and install tutorial](https://www.youtube.com/watch?v=fixgxDb6wK0&ab_channel=KrishnaOjha)
* [Supplementary C Tutorials by TheNewBoston](https://www.youtube.com/watch?v=2NWeucMKrLI&list=PL6gx4Cwl9DGAKIXv8Yr6nhGJ9Vlcjyymq&ab_channel=thenewboston)

### Note on Resources

I encourage beginners to start with the CodeBlocks IDE. However if you are trying to move to a text editor, please look into GCC for linux based operating systems (the link above is for Ubuntu) or mingw for Windows.

### Important Notes for Non-Beginners

All of this code will be written and tested using the GCC compiler unless otherwise stated I will also be using the compiler flags `-Wall`, `-Wextra` and `-ansi`. When we get to more advanced topics I encourage you to use the GCC compiler and the ANSI standard as well. I will state this again when we get to that point.

---

## First program

Plug this code into your compiler and run the resulting executable. If your output is not `Hello, World!`, please ask your teacher for assistance.

```c
#include <stdio.h>

int main(void)
{
    printf("Hello, World!\n");

    return 0;
}

```