# Python: Lesson 1
---
Welcome to Lesson 1 of this Python Curriculum!!
********************************************
## Printing

```python
print('Hello, world!')
```
---
We'll start with printing. This is a Python program
that prints the words Hello, world! to the screen.

Try typing this program in Python Tutor and running it
yourself.
********************************************
## Printing

```python
[[print]][[The print function]]('Hello, world!')
```

---
The word "print" on the left is the print function.
We call this function whenever we want to print something
to the screen.
********************************************
## Definition: Function

A function is a bundle of code that performs a specific
task and/or answers a specific question. Sometimes it takes
one or more input arguments, and sometimes it produces
and returns an output value. The function is executed when
it is called.

---
You will encounter many functions on your journey, and
eventually you'll learn to create your own functions.

For now, you'll learn to use a set of built-in functions
provided by Python out of the box, including:

* `print`
* `input`
********************************************
## Function Example 1

```python
print('Hello, world!')
```
---
print is the first function you will encounter, and its
purpose is to print something to the screen.
********************************************
## Function Example 1

```python
[[print('Hello, world!')]][[A function call]]
```
---
This entire statement - including the name of the function
on the left, the open parenthesis, the text inside the
parenthesis, and the closing parenthesis - is a
*function call*.
********************************************
## Function Example 1

```python
print[[('Hello, world!')]][[The argument list]]
```
---
The parenthesis to the right of the function name is called
the *argument list*. With it, you can pass a number of values
to the function. These are also called the *inputs* of a
function.
********************************************
## Function Example 2

```python
print[[('Hello', 'Sam', 'you', 'are', 4, 'years', 'old.')]][[An argument list with 7 arguments]]
```
---
You can pass more than 1 argument to a function if you separate them
with a comma.

How many arguments you can give to a function depends on the
function. Some functions take no arguments, some take exactly 1, some take
exactly 2, some can take any number of arguments. In the case of the
`print` function, it can take any number of arguments - it will simply
print them all out.

Try running this code in Python Tutor, and changing it around to print
different numbers of arguments.
********************************************
## Variables

```python
thing = 'Thingamabobber'
```
---
Now, let's talk about variables. This is a variable assignment.
********************************************
## Definition: Variable

A variable is a named placeholder that can store a value. The variable's
name can be used anywhere in a program in place of an actual value.
A variable's value may change as the result of a variable assignment
using the `=` operator.

---
The ability of variables to act as placeholders is what gives programs
their dynamic ability. It allows a single program to solve a variety of
problems.
********************************************
## Variables

```python
thing = 'Thingamabobber'
```
---
Coming back to this variable assignment now.
********************************************
## Variable Assignment

```python
thing [[=]][[The assignment operator]] 'Thingamabobber'
```
---
The single equals sign is called the *assignment operator*.
********************************************
## Variable Assignment

```python
[[thing]][[Variable name / identifier]] = 'Thingamabobber'
```
---
The thing on the left of the assignment operator is
the *variable name*. It is the name that you'll
use later in the program to refer back to this variable.

You can name a variable anything you'd like, as long as:

1. It contains only alphabet letters and/or the underscore character: `_`.
2. It can contain digits but not as the first character of the variable name.
********************************************
## Variable Assignment

```python
thing = [['Thingamabobber']][[Value]]
```
---
The thing on the right of the assignment operator is the value you are
assigning to the variable.

When this variable assignment statement is executed,

1. if the variable by that name (in this case `thing`) doesn't already exist,
        it will be created and the value on the right will be assigned to it.
2. if the variable already exists, it will simply assign the value on the
        right to that existing variable, overwriting its previous value.
********************************************
## Variable Usage

```python
thing = 'Thingamabobber'
print('I like this', thing)
```
---
Once a variable exists through an initial variable assignment statement
that creates it, it can be used by simply referring to its name where
an actual value might have previously been used.
********************************************
## Variable Usage

```python
thing = 'Thingamabobber'
print('I like this', [[thing]][[Uses the value in the thing variable]])
```
prints:
```
I like this Thingamabobber
```
---
This example prints `'I like this'`, and then the variable `thing`. When
it uses the variable `thing`, what it actually gets is the value stored inside
`thing`, which at the time was `'Thingamabobber'`.
********************************************
## Python Tutor

![Variable slot](./lessons/python/lesson-1/images/variable-pt.png)

---
If you [run the program through Python Tutor](http://pythontutor.com/visualize.html#code=thing%20%3D%20'Thingamabobber'%0Aprint%28'I%20like%20this',%20thing%29&cumulative=false&curInstr=2&heapPrimitives=false&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false), you'll see
this.
********************************************
## Python Tutor: Variable Slots

![Global frame](./lessons/python/lesson-1/images/global-frame.png)

---
The thing I want you to focus on is the *global frame*. This is where
the values of your variables are stored - inside these variable slots.
********************************************
## Changing Variables

```python
thing = 'Thingamabobber'
print('thing is', thing)
thing = 'Thingamajig'
print('thing is', thing)
```
---
You can change the value of a variable in the middle of a program, just like
this. [Run it in Python Tutor](http://pythontutor.com/visualize.html#code=thing%20%3D%20'Thingamabobber'%0Aprint%28'thing%20is',%20thing%29%0Athing%20%3D%20'Thingamajig'%0Aprint%28'thing%20is',%20thing%29&cumulative=false&curInstr=0&heapPrimitives=false&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false) to see it for yourself.
********************************************
## Madlibs Game

A Madlibs game:

```
Tennis is a _____________ sport.
             adjective 1
I ______ it because it is _____________.
   verb                    adjective 2
Compared to _______________ it is more _____________.
             another sport              adjective 3
```
___
Madlibs is a fun game that kids and adults play alike.
You are given a paragraph of text with some blanks for you to fill in
yourself.
********************************************
## Madlibs Game in Python

```python
adjective1 = 'popular'
verb = 'play'
adjective2 = 'fun'
another_sport = 'golf'
adjective3 = 'active'
print('Tennis is a', adjective1, 'sport.')
print('I', verb, 'it because it is', adjective2, '.')
print('Compared to', another_sport, 'it is more', adjective3, '.')
```
---
This is how you would write the program using variables as placeholders.

Copy (type it out) this program and run it in Python Tutor. Then, change
the values of the placeholders (variables) and run the program again to get your new
paragraph.
********************************************
## Prompting the user

```python
answer = input('What is your name? ')
```
---
In Python, you can ask the user of the program a question.
Since you are still learning, you'll be the one running the program most
of the time, therefore, you'll be the one answering the questions.

This statement uses the `input` function to ask the user a question
and get the user's response.
********************************************
## The input function

The `input` function is used to ask the user of program a question.
It will print a question to the terminal, wait for the user to type
a response and then hit ENTER, and then return the user's response.

---
********************************************
## input example

```python
answer = input([['What is your name? ']][[Prompt text argument]])
```
---
When you use the `input` function, you supply a text argument - this is
going to be the the prompt text the user sees.
********************************************
## input example

```python
answer = [[input('What is your name? ')]][[The user response]]
```
---
When the user finishes entering their response and hits ENTER, the function
call will return the user's response. For example, let's say if the user
entered 'Sally', it would be as if 'Sally' replace this function call.
********************************************
## input example

```python
[[answer]][[Response is stored in here]] = input('What is your name? ')
```
---
Then with this variable assignment statement, the user's response is stored
in the `answer` variable.
********************************************
## Hello, You!

```python
answer = input('What is your name? ')
print('Hello,', answer, '!')
```
---
Now we can write an interactive program!!!
********************************************
## input in Python Tutor

![Input in Python Tutor](./lessons/python/lesson-1/images/input-pt.png)

---
When the input function is called in Python Tutor, it presents the
questions to you in a red box.

To submit an answer, simply type in the text you desire, and hit Submit.
********************************************
## input in terminal

![Hello you](./lessons/python/lesson-1/images/hello-you.png)

---
When the input function is called in the terminal - if you run Python using
the `python3` command, it prints the prompt text in the terminal, and just
waits. Now it's your turn to type.
********************************************
## input in terminal

![Hello you](./lessons/python/lesson-1/images/hello-you-2.png)

---
You type your name: here I am typing mine...
********************************************
## input in terminal

![Hello you](./lessons/python/lesson-1/images/hello-you-3.png)

---
Then hit ENTER, and the program prints `Hello, <YOUR NAME> !`.

Now, you might have noticed that there's an unwanted space before the
exclamation point(!). There's a way to fix that, but we'll gloss over that
detail for now.

Run this program, in both Python Tutor and in the terminal so that you
can get used to how this works.
********************************************
## Numbers and Arithmetic

```python
1
2 + 2
2 * 5
4 - 8
```
---
As you might have imagined, Python supports working with numbers.

Although it doesn't do anything useful, the above code is actually a valid
Python program. It merely generates some numbers, in some cases even
performing some calculations, but without printing them out or storing
them in variables, no visible effect is shown.

In general you'll want to store numbers in variables before working
with them...
********************************************
## Numbers and Arithmetic

```python
age = 37
this_year = 2017
year_born = this_year - 37
print('I was born in the year', year_born)
```
---
This program uses simple arithmetic - subtraction to be precise - to calculate
the birth year of a person give his current age and the current year.
********************************************
## Arithmetic Operators

| Operator | Use                                        |
|----------|--------------------------------------------|
|    +     | Add two numbers                            |
|    -     | Subtract two numbers                       |
|    *     | Multiply two numbers                       |
|    /     | Divide two numbers                         |
|    %     | Modulus - reminder of dividing two numbers |

---
These are the basic arithmetic operators in Python. Armed with these weapons,
you can go forth and calculate!

But wait! Not before you can ask the user to enter in numbers...
********************************************
## Converting answers to numbers

```python
answer_as_string = input('What is your age? ')
```
---
I've glossed over this detail previously, but when you asks the user to enter
a question, you get an answer which is a string value - we will dive into
what strings are in the next lesson. For now, suffice to say, a string is not
a number, and in order to do arithmetic with it, you need to convert it to a
number.
********************************************
## int function

```python
answer_as_string = input('What is your age? ')
answer_as_integer = int(answer_as_string)
```
---
The way you convert a string to a number is by using the `int` function.
********************************************
## int function

```python
answer_as_string = input('What is your age? ')
answer_as_integer = [[int(answer_as_string)]][[Converts a string to an integer]]
```
---
`int` is short for integer - which means a number without any trailing decimal
points.

If you answered 8, answer_as_string would contain the string '8', and then
answer_as_integer would contain the number 8.

If you answered a non number, like abc, answer_as_string would contain
the string 'abc', and then the int function would fail and give you an error:
`ValueError: invalid literal for int() with base 10: 'abc'` - what this means
is that it was taking the string 'abc' as a literal number and it was
simply not valid, and it had to give up.

If you answered a decimal number, like 8.5, answer_as_string would contain
the string '8.5', and then the int function would also fail and give you an
error along the same lines, because integers do not allow decimal points.

Run this code in Python Tutor, and try entering different numeric as well as
non-numeric values and see how Python Tutor behaves.
********************************************
## float function

```python
answer_as_string = input('How many liters of water? ')
answer_as_float = float(answer_as_string)
```
---
If you do want a number with a decimal point, then you want the `float`
function.
********************************************
## float function

```python
answer_as_string = input('How many liters of water? ')
answer_as_float = [[float(answer_as_string)]][[Converts a string to a float]]
```
---
It will convert a string to a float, which is short for
*floating point number*. Floating point numbers which is
common way in which computers represent decimal numbers.
********************************************
## 2 in 1 shortcut

```python
age_as_integer = int(input('What is your age? '))
weight_as_float = float(input('What is your weight? '))
```
---
As a shortcut, you can call the `input` function and then immediately pass its
result to `int` or `float` right on the same line. It is a more succinct way
to write this code, and is a pattern we'll use going forward.
********************************************
## Let's calculate!!! Example 1

```python
your_name = input('What is your name? ')
this_year = int(input('What year is it now? '))
born_year = int(input('What year were you born? '))
your_age = this_year - born_year
print('Hello', your_name, '! I predict your age is', your_age, '!!!')
```
---
This program asks 3 questions and then predicts your age. Please read through
it, and understand how it works. Review the slides if you need to.
You may [run it through Python Tutor](http://pythontutor.com/visualize.html#code=your_name%20%3D%20input%28'What%20is%20your%20name%3F%20'%29%0Athis_year%20%3D%20int%28input%28'What%20year%20is%20it%20now%3F%20'%29%29%0Aborn_year%20%3D%20int%28input%28'What%20year%20were%20you%20born%3F%20'%29%29%0Ayour_age%20%3D%20this_year%20-%20born_year%0Aprint%28'Hello,',%20your_name,%20'I%20predict%20your%20age%20is',%20your_age,%20'!!!'%29&cumulative=false&curInstr=0&heapPrimitives=false&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%22Toby%22,%222017%22,%221980%22%5D&textReferences=false).

Once you are done with that, try changing it slightly to do something else.
Such as: instead of asking for this year and the year their were born,
ask them their age, and this year, and predict the year they were born.
********************************************
## Let's calculate!!! Example 2

```python
your_name = input('What is your name? ')
feet = float(input('How tall are you in feet? '))
inches = feet * 12
print('Hello', your_name, 'you are', inches, 'inches tall!!!')
```
---
This program asks for your height in feet and converts it to inches.
Again, read through it and understand how it works.

Can you think of another common unit conversion that would be helpful?
Write a program that does that.
