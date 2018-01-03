# Lesson 9
## Functions - Part 1
---
Welcome to lesson 9!!! This time we will cover functions.
Oooooh, yes! The long awaited functions.
**********************************************
## Definition: Function

A function is a bundle of code that performs a specific
task and/or answers a specific question. Sometimes it takes
one or more input arguments, and sometimes it produces
and returns an output value.

---
This is the definition of a function from lesson one. The
difference is this time, we'll start to write our own
functions.
**********************************************
![Input/Output](./lessons/python/lesson-9/images/input-output.png)

---
An important aspect of a function is its inputs and its
output.

A function's job is to turn its input into its output.
**********************************************
## Input

![Order](./lessons/python/lesson-9/images/order.png)

---
The inputs of a function are like an order sent in to a pizza shop.
It contains the description of the pizza(s) to be delivered.
**********************************************
## Output

![Order](./lessons/python/lesson-9/images/pizza.png)

---
The output of a function is the product of the work --- the pizza that gets
delivered.

This analogy breaks down for functions that do not have an input, or
those that do not have an output, but we'll roll with it for now.
**********************************************
## len Example

```python
result_length = len("abc")
```

---
Let's use the `len` function as an example. `len` gives you the length of a
list or a string.
**********************************************
## len Example: Input

```python
result_length = len[[("abc")]][[Input: Argument list]]
```

---
When we call `len`, we give it a list of arguments,
consisting of one argument: the string `"abc"`.

This argument list is the *input* of the function.
**********************************************
## len Example: Output

```python
result_length = [[len("abc")]][[Output: Return value 3]]
```

---
The resulting value that come from calling the len function
is the output.

This function call expression --- `len("abc")`
--- equates to its return value: 3.

In this case we have saved the output value to the `result_length`
variable. So `result_length` would contain the value of 3.
**********************************************
## input Example

```python
answer = input("What is your name? ")
```

---
Here is another example using the `input` function --- not
to be confused with the notion of function inputs.
**********************************************
## input Example: input

```python
answer = input([["What is your name? "]][[Input: text prompt]])
```

---
Incidentally, the input function has inputs too. It has one
input argument: a string to be used as the text prompt to show to
the user.
**********************************************
## input Example: output

```python
answer = [[input("What is your name? ")]][[Output: the user ]]
```

---
The output of the input function is the text that is entered
by the user.

In this case, we save the return value in to the
`answer` variable.
**********************************************
## print Example

```python
print("Hello", "world")
```

---
One more example, the `print` function.

I want to show this example because:

* it is an example of a function that can have more than one
input, and
* it is an example of a function that has no output
**********************************************
## print Example: input

```python
print[[("Hello", "world")]][[Input: things to print]]
```

---
`print`'s input arguments are any number of values to be
printed to the terminal. `print` is a special function that
can take any number of arguments in its argument list, and
will go through and print them all.
**********************************************
## print Example: Output

```python
[[print("Hello", "world")]][[Output: None]]
```

---
Print doesn't have an output value, this is why when we call
the print function, we never receive its value and save it
into a variable like we did with the `len` or `input` functions.

Rather than supplying its work product as a return value, print does
its work by displaying characters in the terminal.

Technically, print *does* have a return value, it's just
not useful. print always returns the `None` value,
which is the value that is used to represent nothing in Python.
**********************************************
## convert_c2f Example

```python
fahrenheit = convert_c2f(celsius)
```

---
Here is a handy function: `convert_c2f`. It converts a temperature
from degrees Celsius to degrees Fahrenheit.
**********************************************
## convert_c2f Example

```python
fahrenheit = convert_c2f([[celsius]][[Input: degrees in °C]])
```

---
It takes a number representing a temperature in Celsius as
its input argument,
**********************************************
## convert_c2f Example

```python
fahrenheit = [[convert_c2f(celsius)]][[Output: degrees in °F]]
```

---

and returns a number representing a temperature in Fahrenheit
as its output.
**********************************************
## convert_c2f Example

```python
celsius = float(input("How cold is it (°C)? "))
fahrenheit = convert_c2f(celsius)
print("It is %.2f °F." % fahrenheit)
```

---
This program asks the user to enter a temperature in °C,
and uses the `convert_c2f` function
to convert it to degrees °F and then prints it out.

Try running this program in Python Tutor now. When you are
done, or if you hit a snag, go to the next slide.
**********************************************
## convert_c2f Example

```
NameError: name 'convert_c2f' is not defined
```

---
What happened? Did you get this error?

Yeah, that's because the convent_c2f function doesn't exist...yet!
Yes, I tricked you!

If we want this program to work, we'll need to create our own `convert_c2f`
function. Let's do that.
**********************************************
## Defining a Function

```python
def convert_c2f(c):
    f = c * 9 / 5 + 32
    return f
```

---
This is the code you would write to make our very own `convert_c2f`
function.
**********************************************
## Defining a Function

```python
[[def]][[The def keyword]] convert_c2f(c):
    f = c * 9 / 5 + 32
    return f
```

---
To define a new function, you use the def statement, which
starts with the "def" keyword. This is also called a *function definition*.
**********************************************
## Defining a Function

```python
def [[convert_c2f]][[Function name]](c):
    f = c * 9 / 5 + 32
    return f
```

---
The def keyword is followed by the name of the function, which
you are free to choose. The rules governing what function names
are permitted are the same as those for variable names.
**********************************************
## Defining a Function

```python
def convert_c2f[[(c)]][[Parameter list]]:
    f = c * 9 / 5 + 32
    return f
```

---
Following the name of the function is a *parameter list* that
is surrounded by parenthesis.
**********************************************
## Arguments vs Parameters

```python
fahrenheit = convert_c2f[[(celsius)]][[Argument list]]
```

```python
def convert_c2f[[(c)]][[Parameter list]]:
    f = c * 9 / 5 + 32
    return f
```

---
The parameter list of a function definition is the mirror image of
the argument list of a function call. When you call a function,
each argument you pass to the function is given to the corresponding
parameter of the function where that function is defined, in the order
that is given.

In this example, the argument list only has one argument --- the value
in the variable `celcius` --- and that is given to the parameter
`c` in the parameter list.
**********************************************
## Arguments vs Parameters

```python
result = equation[[(5, 299792458)]][[Argument list]]
```

```python
def equation[[(m, c)]][[Parameter list]]:
    c_squared = c * c
    e = m * c_squared
    return e
```

---
Here is another example.

This example function "equation" has more than one
parameter: namely m and c. When equation is called, the arguments 5 and
299792458 are supplied. The mapping of an argument to a parameter is
based on their respective order. So,
**********************************************
## Arguments vs Parameters

```python
result = equation([[5]][[First argument]], 299792458)
```

```python
def equation([[m]][[First parameter]], c):
    c_squared = c * c
    e = m * c_squared
    return e
```

---
the first argument 5 goes to the first parameter m,
**********************************************
## Arguments vs Parameters

```python
result = equation(5, [[299792458]][[Second argument]])
```

```python
def equation(m, [[c]][[Second parameter]]):
    c_squared = c * c
    e = m * c_squared
    return e
```

---
and the second argument 299792458 goes to the second parameter c.

**********************************************
## Defining a Function

```python
def convert_c2f(c):
    f = c * 9 / 5 + 32
    return f
```

---
Back to the `convert_c2f` function. Let's continue going through the syntax
for defining a function.
**********************************************
## Defining a Function

```python
def convert_c2f(c)[[:]][[A colon]]
    f = c * 9 / 5 + 32
    return f
```

---
Similarly to an if statement, a while loop, or a for loop, a function
definition also has a colon, to denote the start of a block.
**********************************************
## Defining a Function

```python
def convert_c2f(c):
[[    f = c * 9 / 5 + 32
    return f]][[Function body]]
```

---
After the def line that ends with the colon comes the indented block that
is the function body, which contains code instructions that will execute
each time this function is called.

The indentation rules for this block is the same as those for the if statement,
while loop, and for loop.
**********************************************
## Defining a Function

```python
def convert_c2f(c):
    [[f = c * 9 / 5 + 32]][[The work]]
    return f
```

---

This statement contains the actual work that's done by this function.
It creates a variable `f`, and assigns to it the result of taking `c` --- the
temperature in degrees Celsius -- and performing then conversion formula to
calculate the degrees in Fahrenheit: `c x 9 / 5 + 32`.

[More info about this formula here.](https://www.rapidtables.com/convert/temperature/how-celsius-to-fahrenheit.html)
**********************************************
## Defining a Function

```python
def convert_c2f(c):
    f = c * 9 / 5 + 32
    [[return f]][[Return statement]]
```

---
The last line in the body of this function is the return statement.

A return statement:

1. Starts with the "return" keyword
2. Can only exist within the body of a function
3. Returns a *return value* back to the caller of the function
**********************************************
## Defining a Function

```python
def convert_c2f(c):
    f = c * 9 / 5 + 32
    return [[f]][[Return value]]
```

---
The return value is an expression that comes after the return keyword.
In this case, it is `f`, which was calculated on the previous line.
**********************************************
## Defining a Function

```python
def print_hello(person):
    print("Hello, %s!" % person)
```

---
In Python, return statements are optional. Which means that
not all functions have return statements. This `print_hello`
function is an example of that. This function has one parameter: `person`,
and prints a sentence which says hello to that person.

If a function does not have a return statement in it, it will
always return the `None` value.
**********************************************
## Defining a Function

```python
def convert_c2f(c):
    f = c * 9 / 5 + 32
    return f

celsius = float(input("How cold is it (°C)? "))
fahrenheit = convert_c2f(celsius)
print("It is %.2f °F." % fahrenheit)
```

---

Now, given that we have the function definition for `convert_c2f`. Try running
this code in Python Tutor. When you are done, go to the next slide.
**********************************************
## Defining a Function

```python
def convert_c2f(c):
    f = c * 9 / 5 + 32
    return f

celsius = float(input("How cold is it (°C)? "))
fahrenheit = convert_c2f(celsius)
print("It is %.2f °F." % fahrenheit)
```

---
When making your own functions, make sure you put the function definition
before the function call.
**********************************************
## Defining a Function

```python
celsius = float(input("How cold is it (°C)? "))
fahrenheit = convert_c2f(celsius)
print("It is %.2f °F." % fahrenheit)

def convert_c2f(c):
    f = c * 9 / 5 + 32
    return f
```
---
If you do it in the wrong order, like this, the function wouldn't have
existed yet at the time it was called,
**********************************************
## Defining a Function

```
NameError: name 'convert_c2f' is not defined
```

---
and you would get this error.
**********************************************
## The Frame

```python
def convert_c2f(c):
    f = c * 9 / 5 + 32
    return f

celsius = float(input("How cold is it (°C)? "))
fahrenheit = convert_c2f(celsius)
print("It is %.2f °F." % fahrenheit)
```

---
Now, we are going to step through this program in Python Tutor.
We are going to focus on the *frame* of a function when it is executed
in Python Tutor.
**********************************************
## Executing a Function

![Step 1](./lessons/python/lesson-9/images/pt-step1.png)

---
As we step through this code, watch closely to see what happens to the
"Frames" section.

So far, the only frame we have seen is the global frame,
which stores the names and the values of our variables. When
you call a function, a new frame gets created that will be used to store
the variables that are local to (belongs to) that function.
**********************************************
## Executing a Function

![Step 1](./lessons/python/lesson-9/images/pt-step1.png)

---
Okay, let's get started!!

At the beginning of the program, there isn't anything there
in the frames section.

The first line of this program defines a function. Let's see
what happens when we step.
**********************************************
## Executing a Function

![Step 2](./lessons/python/lesson-9/images/pt-step2.png)

---
Once you execute the `def` statement, the function is defined
in the global frame. As you can see, a function is stored in the same
way as a variable is stored.

The function's name convert_c2f is the slot name in the global frame.
The function itself is stored in the objects section, and is pointed
to by the slot.

Now, we are on line 5, which will prompt the user to enter a number.
**********************************************
## Executing a Function

![Step 3](./lessons/python/lesson-9/images/pt-step3.png)

---
I entered 12 when I was prompted "How cold is it °C?", and so now the
`celcius` variable has been created and contains the value 12.

Next, we will actually call the `convert_c2f` function we've defined. Let's
see what happens.
**********************************************
## Executing a Function

![Step 3](./lessons/python/lesson-9/images/pt-step4.png)

---
When the function is called, a new frame called "convert_c2f" has been
added to the frames section, and it already contains one variable:
`c`, which contains the value 12.

The value of 12 was passed in from the
argument list in the function call on line 6: `convert_c2f(celsius)`
, and `c` is the name of the parameter on the inside of the function.

So the value of `celsius` on the outside of the function is passed to `c`
on the inside of the function.

And now the program counter is on line 1 --- the beginning of the
`convert_c2f` function.

Step...
**********************************************
## Executing a Function

![Step 4](./lessons/python/lesson-9/images/pt-step5.png)

---
Now we are on line 2, the *real* first line of the function.
It creates a new variable
`f` and assigns to it the result of performing the calculations for the
unit conversion equation.

Step over that, and...
**********************************************
## Executing a Function

![Step 5](./lessons/python/lesson-9/images/pt-step6.png)

---
the `f` variable has been created with the value of
53.6 --- the calculated result.
**********************************************
## Executing a Function

![Step 5](./lessons/python/lesson-9/images/pt-step6.png)

---

Next, we will return the value of `f` as the return value of this function.
**********************************************
## Executing a Function

![Step 7](./lessons/python/lesson-9/images/pt-step7.png)

---
When the return statement is executed, Python Tutor shows us that the
return value of this function (in red), which in this case is 53.6.

When we step again, what do you think happens to the convert_c2f frame?
Make your prediction, and then go to the next slide to find out.
**********************************************
## Executing a Function

![Step 8](./lessons/python/lesson-9/images/pt-step8.png)

---
If you guessed the frame disappears, you were correct!

When a function finishes
executing, the frame that was created to store its variables disappears,
because they are no longer needed. A frame is like scratch paper for you
to work out the solution of a math problem, but once you have the answer,
you don't need it anymore.

Due to line 6, we have save the return value of the function call into
a new `fahrenheit` variable. And so now we are ready to print it out.
**********************************************
## Executing a Function

![Step 8](./lessons/python/lesson-9/images/pt-end.png)

---
There is the print out that says "It is 53.60 °F".

Now, you may [Walk through it in Python Tutor on your own](http://pythontutor.com/visualize.html#code=def%20convert_c2f%28c%29%3A%0A%20%20%20%20f%20%3D%20c%20*%209%20/%205%20%2B%2032%0A%20%20%20%20return%20f%0A%0Acelsius%20%3D%20float%28input%28%22How%20cold%20is%20it%20%28%C2%B0C%29%3F%20%22%29%29%0Afahrenheit%20%3D%20convert_c2f%28celsius%29%0Aprint%28%22It%20is%20%25.2f%20%C2%B0F.%22%20%25%20fahrenheit%29&cumulative=false&curInstr=0&heapPrimitives=false&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false).
**********************************************
## Executing a Function

![Step 8](./lessons/python/lesson-9/images/pt-end.png)

---
Now that you know how calling a function works. Let's see one more
complex example of function usage.
**********************************************
## Problem: Reverse the Words

Given a phrase entered by the user, reverse its words and print it back out.

---
Let's do a problem that's come up before in one of your previous exercises:
reversing the words of a phrase. Only this time, we'll be doing it with
functions.
**********************************************
## Reverse the Words: Reverse a word

```python
def reverse_word(word):
    result = ""
    for letter in word:
        result = letter + result
    return result
```

---
We know that --- obviously --- one of the problems we'll need to solve
to tackle the larger problem is: how do we reverse a word? So let's write
a function to do just that. This is it: `reverse_word`.

`reverse_word` takes a string `word` as its only parameter, and returns the
reversed word as its return value.
**********************************************
## Reverse the Words: Reverse a word

```python
def reverse_word(word):
    [[result = ""
    for letter in word:
        result = letter + result]][[Accumulator pattern]]
    return result
```

---
It uses the accumulator pattern to do this, accumulating a letter at a time
to the `result` variable to arrive at the final result.
**********************************************
## Reverse the Words: Reverse a word

```python
def reverse_word(word):
    result = ""
    for letter in word:
        result = letter + result
    [[return result]][[Return statement]]
```

---
Then finally, it returns the contents of the `result` variable --- which should
contain the reversed word --- as the return value back to the caller.
**********************************************
## Testing Functions in Isolation

```python
print(reverse_word("bananas"))
```

---
The nice thing about breaking a program up into small pieces is that you can
test each piece in isolation, and thus get feedback faster about whether or
not you are getting it right.

In our case, we can apply the `reverse_word` function to just any old word,
like bananas, to see that it's doing what it's supposed to do. If it works,
that means we can move on to the next step.
**********************************************
## Testing Functions in Isolation

```python
print(reverse_word("bananas"))
print(reverse_word("a"))
print(reverse_word(""))
```

---
In general, you want to remember to test the special cases --- like if there's
just one character, or even an empty string --- in addition to the the
usual suspects, because things that seem obvious often break on the special
cases.
**********************************************
## Reverse the Words: Reverse All The Words

```python
def reverse_all_words(phrase):
    words = phrase.split(" ")
    result_words = []
    for word in words:
        result_word = reverse_word(word)
        result_words.append(result_word)
    result_phrase = " ".join(result_words)
    return result_phrase
```

---
Given that we have a function to help us reverse a single word, now let's write
a function to take phrase, and reverse all its words. This function:
`reverse_all_words` does that.

It takes a single `phrase` string parameter, and outputs a version of the phrase
with its words reversed.
**********************************************
## Reverse the Words: Reverse All The Words

```python
def reverse_all_words(phrase):
    [[words = phrase.split(" ")]][[Split into words]]
    result_words = []
    for word in words:
        result_word = reverse_word(word)
        result_words.append(result_word)
    result_phrase = " ".join(result_words)
    return result_phrase
```

---
This function first splits the phrase into a list of words.
**********************************************
## Reverse the Words: Reverse All The Words

```python
def reverse_all_words(phrase):
    words = phrase.split(" ")
    [[result_words = []
    for word in words:
        result_word = reverse_word(word)
        result_words.append(result_word)]][[Accumulator pattern]]
    result_phrase = " ".join(result_words)
    return result_phrase
```

---
Then it uses the accumulator pattern, accumulating to the
`result_words` variable for each word through the for loop.
**********************************************
## Reverse the Words: Reverse All The Words

```python
def reverse_all_words(phrase):
    words = phrase.split(" ")
    result_words = []
    for word in words:
        result_word = [[reverse_word(word)]][[Use reverse_word]]
        result_words.append(result_word)
    result_phrase = " ".join(result_words)
    return result_phrase
```

---
Within the loop, it uses the `reverse_word` function to convert each word,
**********************************************
## Reverse the Words: Reverse All The Words

```python
def reverse_all_words(phrase):
    words = phrase.split(" ")
    result_words = []
    for word in words:
        result_word = reverse_word(word)
        [[result_words.append(result_word)]][[Added reversed word to list]]
    result_phrase = " ".join(result_words)
    return result_phrase
```

---
and then it adds it to the list.
**********************************************
## Reverse the Words: Reverse All The Words

```python
def reverse_all_words(phrase):
    words = phrase.split(" ")
    result_words = []
    for word in words:
        result_word = reverse_word(word)
        result_words.append(result_word)
    [[result_phrase = " ".join(result_words)]][[Combine the reversed words]]
    return result_phrase
```

---
When it's done with the accumulator pattern, it combines the list back to a
string using the join method.
**********************************************
## Reverse the Words: Reverse All The Words

```python
def reverse_all_words(phrase):
    words = phrase.split(" ")
    result_words = []
    for word in words:
        result_word = reverse_word(word)
        result_words.append(result_word)
    result_phrase = " ".join(result_words)
    [[return result_phrase]][[Return statement]]
```

---
Finally, it returns the converted `result_phrase` using the return statement.
**********************************************
## Reverse the Words: Main Program

```python
phrase = input("Type a phrase: ")
result = reverse_all_words(phrase)
print(result)
```

---
Now, with the aid of the `reverse_all_words` function, we can write the main
program in 3 lines, like so.
**********************************************
## Reverse the Words: Full Source

```python
def process_word(word):
    result = ""
    for letter in word:
        result = letter + result
    return result

def reverse_all_words(phrase):
    words = phrase.split(" ")
    result_words = []
    for word in words:
        result_word = process_word(word)
        result_words.append(result_word)
    result_phrase = " ".join(result_words)
    return result_phrase

phrase = input("Type a phrase: ")
result = reverse_all_words(phrase)
print(result)
```

---
This is the full source code of this example. Run this code in Python Tutor.
Pay close attention to the frames section. When does:

1. a new frame get created?
2. a frame get destroyed?
**********************************************
## Reverse the Words: Full Source

![3 Frames](./lessons/python/lesson-9/images/3-frames.png)

---
Notice that at one point, you will have 3 frames like this. This is because
we have a function that calls another function.

First, at the top we have the global frame.

Then, we have a `reverse_all_words` frame, which was created when
the `reverse_all_words` was called.

Finally, we have a `reverse_word` frame, which was called within the
`reverse_all_words` function to reverse a single word.
**********************************************
## Reverse the Words: Full Source

![3 Frames](./lessons/python/lesson-9/images/3-frames.png)

---

Theoretically, you can have a stack of frames that grows to any size, but
Python puts a limit on the stack to avoid letting your program take over
all the system memory of the computer. If your program tries to
go over limit, Python will give a *stack overflow error* and immediately
stop the program.
**********************************************
## Summary

* Functions
* Inputs / Outputs
* Defining a function
* Frames
* Testing functions in isolation
* Breaking up problems

---
Okay, That's all for this lesson.
This is a summary of what you learned.
**********************************************
## Homework

[Click here for your homework!!!](https://gist.github.com/airportyh/77f796d07721e4c74884f33910ca385b)

---
Here is your homework. Enjoy!
