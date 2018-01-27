# Lesson 2.1
## while loop

---
Hello! Today you will learn about the while loop.
The while loop is a device that will allow you to
repeat the same statements any number of times ---
including infinite. It's the perfect way to automate
away mundane tasks. Let's get going.
*************************************************
# Section 1
## Introduction

---

*************************************************
## While Loop

A *while loop* is a statement that repeatedly evaluates
a condition and executes a series of consequent
statements if that condition is true. If the condition
is or becomes false, the repeating stops. You may
think of a while loop as a repeating if statement.

---
*************************************************
## While Loop

```python
while answer != "when":
  print("Parm")
  print("Cheese")
```

---
This is an example of a while loop.
*************************************************
## While Loop

```python
[[while]][[keyword]] answer != "when":
  print("Parm")
  print("Cheese")
```

---
A while loop starts with the `while` keyword,
*************************************************
## While Loop

```python
while [[answer != "when"]][[conditional clause]]:
  print("Parm")
  print("Cheese")
```

---
followed by a conditional clause, similarly to an if statement.

In this case we are using the `!=` operator, which is called the
*not equal* operator. This conditional will only be true if
the value inside the `answer` variable is not equal to `"when"`.
*************************************************
## While Loop

```python
while answer != "when"[[:]][[colon]]
  print("Parm")
  print("Cheese")
```

---
*and* the mandatory colon, let's not forget about that!
*************************************************
## While Loop

```python
while answer != "when":
[[  print("Parm")
  print("Cheese")]][[loop body]]
```

---
The next lines are indented to the right. These indented lines
form the `loop body`.
*************************************************
## While Loop

```python
while answer != "when":
  print("Parm")
  print("Cheese")
```

---
If the condition in the conditional clause
is evaluated to true, the statements in the loop body are executed.

After the statements are executed, we go back to the top of the
while loop and evaluate the condition again, if it is true again,
the loop body is executed again. This repeats over and over again,
until the condition is false. If the condition never becomes false,
the program will run **forever**.
*************************************************
## While Loop

```python
answer = "That's enough."
while answer != "when":
  print("Parm")
  print("Cheese")
```

---
Try running this program using the `python` command in your terminal.

Oh, if it runs forever, you'll want to use press `control-c`
(hold down the `control` or `ctrl` key while pressing `c` on your
  keyboard) to kill your program. If it worked, you should see
  `KeyboardInterrupt`.
*************************************************
## While Loop

```
Parm
Cheese
Parm
Cheese
.
.
.
```

---
So, this program runs and prints this...

over and over and over again.
*************************************************
## While Loop

```python
answer = "That's enough."
while answer != "when":
  print("Parm")
  print("Cheese")
```

---
Why? Because the value of the `answer` variable was set
to `"That's enough."`, and it was never changed. It will
never contain the value "when", if we don't change it.
*************************************************
## While Loop

```python
answer = "That's enough."
while answer != "when":
  print("Parm")
  print("Cheese")
```

---
For this reason, whenever you write a while loop, you'll
need to think about how to make it stop.
*************************************************
## While Loop

Python Tutor and Infinite Loops

---
Unfortunately, Python Tutor does not deal well with infinitely
loops. If you [run the previous program in Python Tutor](http://pythontutor.com/visualize.html#code=answer%20%3D%20%22That's%20enough.%22%0Awhile%20answer%20!%3D%20%22when%22%3A%0A%20%20print%28%22Parm%22%29%0A%20%20print%28%22Cheese%22%29&cumulative=false&curInstr=0&heapPrimitives=false&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false),

you should get the error: "Stopped after running 1000 steps. Please shorten your code, since Python Tutor is not designed to handle long-running code."

This error is misleading. It's not that your program is too long, it
just ran for too long. *Forever*, for that matter. If you see this
error in Python Tutor, you probably have an infinite loop in your
program and you need to figure out how to make it stop.
*************************************************
## While Loop

```python
answer = "That's enough."
while answer != "when":
  print("Parm")
  print("Cheese")
```

---
So how to make this while loop stop?
*************************************************
## While Loop

```python
answer = "That's enough."
while answer != "when":
  print("Parm")
  print("Cheese")
  [[answer = input("Say when: ")]][[Ask the user]]
```

---
One way is to prompt the user for the answer --- within the
loop body.
*************************************************
## While Loop

```python
[[answer = input("Say when: ")]][[Ask the user too]]
while answer != "when":
  print("Parm")
  print("Cheese")
  answer = input("Say when: ")
```

---
While we are at it, we'll change the first line to ask
the user for the answer too.
*************************************************
## While Loop

```python
answer = input("Say when: ")
while answer != "when":
  print("Parm")
  print("Cheese")
  answer = input("Say when: ")
```

---
Okay, now, this program stands a chance of completing before
the end of time.

Run this in Python Tutor. (You may copy-n-paste the code
in there.)

When prompted for an input, type:

* "ok"
* then "enough"
* then "stop it"
* finally "when"

to make it stop.
*************************************************
## Statements After the Loop

```python
answer = input("Say when: ")
while answer != "when":
  print("Parm")
  print("Cheese")
  answer = input("Say when: ")
→
```

---
If you write additional statements after the while
loop, they will execute after the while loop has
stopped looping.
*************************************************
## Statements After the Loop

```python
answer = input("Say when: ")
while answer != "when":
  print("Parm")
  print("Cheese")
  answer = input("Say when: ")
[[print("You said when! You did! You did!")]][[additional statement]]
```

---
For example, given the additional print statement
at the end.
*************************************************
## Statements After the Loop

```python
answer = input("Say when: ")
while [[answer != "when"]][[answer is "when"]]:
  print("Parm")
  print("Cheese")
  answer = input("Say when: ")
print("You said when! You did! You did!")
```

---
when the while loop condition is true --- this would
happen if the user typed in "when".
*************************************************
## Statements After the Loop

```python
answer = input("Say when: ")
while answer != "when":
  print("Parm")
  print("Cheese")
  answer = input("Say when: ")
[[print("You said when! You did! You did!")]][[1st line outside of loop body]]
```

---
then the control of the program will jump to the next line
outside of the body of the while loop.
*************************************************
## The Break Statement

The *break statement* is a standalone statement
that can be used within a loop (while or for loop).
When it is executed, the program immediately jumps
out of the loop and continues on the next statement
after the body of the loop.

---
Now let's take about the break statement, a useful
statement to use inside a loop.
*************************************************
## The Break Statement

```python
pancakes = int(input("How many pancakes do you want to make? "))
eggs = pancakes / 5 * 2
print("You need", eggs, "eggs")
```

---
Take the egg calculator for making pancakes you did
as an exercise in the first lesson. We will make this
program repeat over and over again, as the user wants
to.

*************************************************
## The Break Statement

```python
→ pancakes = int(input("How many pancakes do you want to make? "))
→ eggs = pancakes / 5 * 2
→ print("You need", eggs, "eggs")
```

---
How? First, indent the statements to the right.
*************************************************
## The Break Statement

```python
while True:
  pancakes = int(input("How many pancakes do you want to make? "))
  eggs = pancakes / 5 * 2
  print("You need", eggs, "eggs")
```

---
Then add `while True:` at the top.
*************************************************
## The Break Statement

```python
while [[True]][[always true]]:
  pancakes = int(input("How many pancakes do you want to make? "))
  eggs = pancakes / 5 * 2
  print("You need", eggs, "eggs")
```

---
`True` is a special value in Python. When you put `True`
in a conditional (while loop or if statement), it will
always be true, just like if you put `2 > 1`, that will
always return true.

Does that mean this loop will repeat forever? Yes,
unless there's a break statement in the body to change
that.
*************************************************
## The Break Statement

```python
while True:
  pancakes = int(input("How many pancakes do you want to make? "))
  eggs = pancakes / 5 * 2
  print("You need", eggs, "eggs")
[[  answer = input("Do another? (y or n) ")
  if answer != "y":
    break]][[make it stop]]
```

---
Now, we'll add some code to make this loop stop.
*************************************************
## The Break Statement

```python
while True:
  pancakes = int(input("How many pancakes do you want to make? "))
  eggs = pancakes / 5 * 2
  print("You need", eggs, "eggs")
  answer = input("Do another? (y or n) ")
  if answer != "y":
    break
[[print("Good bye!")]][[say bye]]
```

---
And we'll say good bye to the user when they are done,
to be polite.
*************************************************
## The Break Statement

```python
while True:
  pancakes = int(input("How many pancakes do you want to make? "))
  eggs = pancakes / 5 * 2
  print("You need", eggs, "eggs")
  [[answer = input("Do another? (y or n) ")]][[ask for y or n]]
  if answer != "y":
    break
print("Good bye!")
```

---
First, we ask the user to type in either the character "y" or "n"
*************************************************
## The Break Statement

```python
while True:
  pancakes = int(input("How many pancakes do you want to make? "))
  eggs = pancakes / 5 * 2
  print("You need", eggs, "eggs")
  answer = input("Do another? (y or n) ")
  [[if answer != "y":]][[if they typed anything but "y"]]
    break
print("Good bye!")
```

---
If they typed "y", we want the while loop to repeat.

If they typed "n" or anything that's not "y",
that's when we want to stop this loop from repeating.

So the conditional for this if statement is `answer != "y"`,
which would return true if the value in `answer` is "n" or
anything other than "y".
*************************************************
## The Break Statement

```python
while True:
  pancakes = int(input("How many pancakes do you want to make? "))
  eggs = pancakes / 5 * 2
  print("You need", eggs, "eggs")
  answer = input("Do another? (y or n) ")
  if answer != "y":
    [[break]][[stops the loop]]
print("Good bye!")
```

---
So, if that is the case, the break statement jumps us
out of the loop
*************************************************
## The Break Statement

```python
while True:
  pancakes = int(input("How many pancakes do you want to make? "))
  eggs = pancakes / 5 * 2
  print("You need", eggs, "eggs")
  answer = input("Do another? (y or n) ")
  if answer != "y":
    break
[[print("Good bye!")]][[1st statement outside of loop]]
```

---
To this print statement.
*************************************************
## The Break Statement

```python
while True:
  pancakes = int(input("How many pancakes do you want to make? "))
  eggs = pancakes / 5 * 2
  print("You need", eggs, "eggs")
  answer = input("Do another? (y or n) ")
  if answer != "y":
    break
print("Good bye!")
```

---
Run this code in Python Tutor to understand how it works. Repeat
the egg calculator a couple of times, and then make it stop.
*************************************************
## The Break Statement

```python
while True:
  pancakes = int(input("How many pancakes do you want to make? "))
  eggs = pancakes / 5 * 2
  print("You need", eggs, "eggs")
  answer = input("Do another? (y or n) ")
  if answer != "y":
    break
print("Good bye!")
```

---
This is the end of section 1. You may choose to do
section 1 of the [homework](https://gist.github.com/airportyh/5812d22ea97d36d47b22152334234fef) before moving on.
*************************************************
# Section 2
## Loop Counter Pattern

---
In this section, you'll learn your first pattern.
This is exciting stuff! If you are not excited yet,
that's okay, I am excited enough for the both of us!!!

Now, what *is* a pattern?
*************************************************
## Pattern

A *pattern* is a structure commonly found in code
solutions to various problems.

---
This is the definition. It is admittedly vague,
so let's see a real example...
*************************************************
## Loop Counter Pattern

The *loop counter pattern* is used to repeat a set
of statements a fixed number of times. It consists
of a counter variable, a while loop, a repeating
condition and an incrementor statement within the
loop to increment the value of the counter variable.

---
This is the definition for the loop counter pattern...
*************************************************
## Loop Counter Pattern

```python
counter = 1
while counter <= 10:
  print(counter)
  counter = counter + 1
```

---
This is an example of the loop counter pattern.
*************************************************
## Loop Counter Pattern

```python
[[counter = 1]][[counter initialization]]
while counter <= 10:
  print(counter)
  counter = counter + 1
```

---
It begins with the declaration of a counter variable,
which we simply call `counter` --- although we could
have given it any name. We initialize its
value to 1. This is called the *counter initialization*.
*************************************************
## Loop Counter Pattern

```python
counter = 1
[[while counter <= 10:]][[while loop]]
  print(counter)
  counter = counter + 1
```

---
Then we begin the while loop.
*************************************************
## Loop Counter Pattern

```python
counter = 1
while [[counter <= 10]][[repeating condition]]:
  print(counter)
  counter = counter + 1
```

---
this is the *repeating condition*. This loop will keep running
until this condition evaluates to false. In this case,
It will go until the value in the `counter` variable
is less or equal to 10.
*************************************************
## Loop Counter Pattern

```python
counter = 1
while counter <= 10:
  [[print(counter)]][[print the counter]]
  counter = counter + 1
```

---
Next we'll print the counter variable. This is the
meat of the loop, where you can write any number
of statements here, and those statements will
get repeated the desired number of times.
*************************************************
## Loop Counter Pattern

```python
counter = 1
while counter <= 10:
  print(counter)
  [[counter = counter + 1]][[incrementor statement]]
```

---
Finally, we have the incrementor statement. The incrementor
statement causes the value in the `counter` variable
to increase by 1.
*************************************************
## Incrementor Statement

```python
counter = counter + 1
```

---
I want to dig into this statement a little bit. What is
going on here?

A weird thing to notice is that the variable `counter`
is present on both sides of the `=` sign. If you are a
math person, you are understandably offended. A number
that is equal to itself plus one? Impossible!!
*************************************************
## Incrementor Statement

```python
counter [[=]][[assignment operator]] counter + 1
```

---
But that's not what this statement stands for, because the
`=` sign is not the equality operator, but rather
the **assignment operator**. (`==` is the equality operator)
*************************************************
## Incrementor Statement

```python
counter = [[counter + 1]][[evaluate rhs]]
```

---
What happens with an assignment operator is that it
first evaluates the right-hand side of the `=` operator
to figure out what value to assign. In this case,
it is the current value of `counter` plus 1.
*************************************************
## Incrementor Statement

```python
counter = [[counter]][[5]] + 1
```

---
As an example, let's say the current `counter` value is 5,
*************************************************
## Incrementor Statement

```python
counter = [[counter + 1]][[6]]
```

---
so the right-hand side gives us 6.
*************************************************
## Incrementor Statement

```python
[[counter]][[assigns 6 back to counter]] = counter + 1
```

---
Now that is has evaluated the right-hand side to 6, it
assigns the 6 back to the `counter` variable.
*************************************************
## Loop Counter Pattern

```python
counter = 1
while counter <= 10:
  print(counter)
  counter = counter + 1
```

---
Okay, now back to the loop counter pattern.

Run this code in Python Tutor. Make sure you pay attention
to the value of the counter variable:

* when does it change?
* when does it cause the while loop to repeat?
*************************************************
## Mechanics of Loop Counter Pattern

* counter initialization
* repeating condition
* incrementor statement

---
These 3 things govern the mechanics of a loop that uses
the loop counter pattern. When you set out to write a
loop in this pattern, you should think about what each
of these are.
*************************************************
## Challenge 1

```python
counter = 1
while counter <= 10:
  print(counter)
  counter = counter + 1
```

---
Change this program to go from 5 to 10.
Should you change the *counter initialization*, or
the *repeating condition*, or the *incrementor statement*?

Give it a try and then see the solution next.
*************************************************
## Challenge 1: Solution

```python
counter = 5
while counter <= 10:
  print(counter)
  counter = counter + 1
```

---
This is the solution.
*************************************************
## Challenge 1: Solution

Solution:
```python
[[counter = 5]][[change counter initialization]]
while counter <= 10:
  print(counter)
  counter = counter + 1
```

---
The solution is to change the counter initialization
to set it to 5.
*************************************************
## Challenge 2

```python
counter = 1
while counter <= 10:
  print(counter)
  counter = counter + 1
```

---
Now, make this print the numbers from 1 to 10, but skipping by 2s.
So, 1, 3, 5, 7, 9. Try it then flip for the solution.
*************************************************
## Challenge 2: Solution

```python
counter = 1
while counter <= 10:
  print(counter)
  [[counter = counter + 2]][[change incrementor statement]]
```

---
This time we change the incrementor statement to make it
add 2 instead of 1.
*************************************************
## Challenge 3

```python
counter = 1
while counter <= 10:
  print(counter)
  counter = counter + 1
```

---
Change this to make it print "Hello" 10 times. Which part
would you change? Next slide for the solution.
*************************************************
## Challenge 3: Solution

```python
counter = 1
while counter <= 10:
  [[print("Hello")]][[change print statement]]
  counter = counter + 1
```

---
This time you need to change the print statement
in the body.

If you missed any of the solutions, don't worry.
The homework will give you more practice.
*************************************************
## Summary

* While loop
* Statements after the loop
* Break statement
* Repeating a program
* Loop Counter Pattern

---
You made it to the end! This is what you've learned.
*************************************************
## Homework

[homework](https://gist.github.com/airportyh/5812d22ea97d36d47b22152334234fef)

---
Enjoy your homework!
