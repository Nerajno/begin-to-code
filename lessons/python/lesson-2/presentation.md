# Lesson 2: If Statements
---
In this lesson, we'll cover the if-statement.
***************************************************
## if statement

```python
if age >= 21:
  print("You are old enough")
  print("Please come in")
```

---
Let's jump right into it. This is the if statement. It performs a set
of statements if a specified condition is met, and does not perform them
if it is not met.
***************************************************
## if statement

```python
[[if]][[The if keyword]] age >= 21:
  print("You are old enough")
  print("Please come in")
```

---
An if statement starts with the if keyword.
***************************************************
## if statement

```python
if [[age >= 21]][[The conditional clause]]:
  print("You are old enough")
  print("Please come in")
```

---
It is followed by a conditional clause, which contains a *predicate*.
***************************************************
## Predicate

A statement that evaluates to either true or false.

---
What is a predicate? You say.
***************************************************
## if statement

```python
if [[age >= 21]][[The conditional clause / a predicate]]:
  print("You are old enough")
  print("Please come in")
```

---
So `age >= 21` is a predict. When Python executes this predicate, it gets
either a True or False value. More on that later.
***************************************************
## if statement

```python
if age [[>=]][[Greater-than-or-equal-to operator]] 21:
  print("You are old enough")
  print("Please come in")
```

---

Within a predicate, we can use comparison operators such as
`>`, `>=`, `==`, `<`, `<=`, and more. In this case, `>=` is
the greater-than-or-equal-to operator, and it will return
true if the value on the left-hand side --- in this case the `age` variable
--- is greater or equal to the value on the right-hand side --- in this case
21, and return false otherwise.
***************************************************
## if statement

```python
if age >= 21[[:]][[The colon]]
  print("You are old enough")
  print("Please come in")
```

---
A colon comes after the predicate / conditional clause. This colon is mandatory.
***************************************************
## if statement

```python
if age >= 21:
[[  print("You are old enough")
  print("Please come in")]][[Consequent block]]
```

---
Next we have the *consequent block* of the if statement. The *consequent
block* of an if statement is a set of statements which would be executed
as a consequence of the conditional clause being true.
***************************************************
## if statement: indentation

```python
if age >= 21:
 →print("You are old enough")
 →print("Please come in")
```

---

Each line within the consequent block must be indented to the right of the
if statement on the first line. More over, each line in this block must
line up, meaning that they must indent by the same amount.

The rule for code blocks is:

1. A colon (`:`) signals a block is going to begin on the next line
2. Starting on the next line, all of the instructions that go within the
block are indented one level to the right relative to the line ending in the
colon.
***************************************************
## if statement: else clause

```python
if age >= 21:
  print("You are old enough")
  print("Please come in")
else:
  print("Come back in a few years")
```

---
An optional part of the if statement is the else clause.
***************************************************
## if statement: else clause

```python
if age >= 21:
  print("You are old enough")
  print("Please come in")
[[else:
  print("Come back in a few years")]][[Else clause]]
```

---
The else clause also has an indented block.
***************************************************
## if statement: else clause

```python
if age >= 21:
  print("You are old enough")
  print("Please come in")
else[[:]][[The colon]]
  print("Come back in a few years")
```

---
See again: the mandatory colon.
***************************************************
## if statement: else clause

```python
if age >= 21:
  print("You are old enough")
  print("Please come in")
else:
 →print("Come back in a few years")
```

---
And again the mandatory indentation.
***************************************************
## if statement: else clause

```python
if age >= 21:
  print("You are old enough")
  print("Please come in")
else:
[[  print("Come back in a few years")]][[Alternate block]]
```

---
The block within the else
statement is called the *alternate block*, and it will
execute when the if statement's conditional clause --- in this case
`age >= 21` evaluates to false.
***************************************************
## if statement: elif clause

```python
if age >= 21:
  print("You are old enough")
  print("Please come in")
elif age >= 18:
  print("You are technically an adult, but still not old enough")
elif age >= 13:
  print("You are a teenager")
else:
  print("You are a baby")
```

---
In additional to the `else` clause, there is also an optional `elif` clause,
which is short for "else if".
***************************************************
## if statement: elif clause

```python
if age >= 21:
  print("You are old enough")
  print("Please come in")
[[elif age >= 18:
  print("You are technically an adult, but still not old enough")]][[elif statement]]
elif age >= 13:
  print("You are a teenager")
else:
  print("You are a baby")
```

---
This is an elif clause. But there can be multiple elif clauses.
***************************************************
## if statement: elif clause

```python
if age >= 21:
  print("You are old enough")
  print("Please come in")
elif age >= 18:
  print("You are technically an adult, but still not old enough")
[[elif age >= 13:
  print("You are a teenager")]][[another elif statement]]
else:
  print("You are a baby")
```

---
This is another.
***************************************************
## if statement: elif clause

```python
if age >= 21:
  print("You are old enough")
  print("Please come in")
[[elif]][[elif keyword]] age >= 18:
  print("You are technically an adult, but still not old enough")
elif age >= 13:
  print("You are a teenager")
else:
  print("You are a baby")
```

---
The elif clause starts with the `elif` keyword.
***************************************************
## if statement: elif clause

```python
if age >= 21:
  print("You are old enough")
  print("Please come in")
elif [[age >= 18]][[conditional clause]]:
  print("You are technically an adult, but still not old enough")
elif age >= 13:
  print("You are a teenager")
else:
  print("You are a baby")
```

---
It mirrors the if statement in that it also has a conditional clause,
***************************************************
## if statement: elif clause

```python
if age >= 21:
  print("You are old enough")
  print("Please come in")
elif age >= 18:
  [[print("You are technically an adult, but still not old enough")]][[consequent clause]]
elif age >= 13:
  print("You are a teenager")
else:
  print("You are a baby")
```

---
as well as a consequent clause.
***************************************************
## if statement: elif clause

```python
[[if age >= 21:
  print("You are old enough")
  print("Please come in")]][[starting if clause]]
elif age >= 18:
  print("You are technically an adult, but still not old enough")
elif age >= 13:
  print("You are a teenager")
else:
  print("You are a baby")
```

---
An elif clause must come after a starting if clause.

An elif clause's conditional will only be evaluated (considered) in the event
that the conditional clause of the if statement --- or that of another
elif statement ahead of it --- evaluated to false.
***************************************************
## if statement: elif clause

```python
if [[age >= 21]][[Is 25 greater than 21?]]:
  print("You are old enough")
  print("Please come in")
elif age >= 18:
  print("You are technically an adult, but still not old enough")
elif age >= 13:
  print("You are a teenager")
else:
  print("You are a baby")
```

---
Let's suppose that `age` was 25, and therefore greater than 21, making
the conditional clause a true statement,
***************************************************
## if statement: elif clause

```python
if age >= 21:
[[  print("You are old enough")
  print("Please come in")]][[Program executes these]]
elif age >= 18:
  print("You are technically an adult, but still not old enough")
elif age >= 13:
  print("You are a teenager")
else:
  print("You are a baby")
```

---
The program therefore executes these statements.
***************************************************
## if statement: elif clause

```python
if age >= 21:
  print("You are old enough")
  print("Please come in")
elif age >= 18:
  print("You are technically an adult, but still not old enough")
elif age >= 13:
  print("You are a teenager")
else:
  print("You are a baby")
[[  →]][[Skips to here]]
```

---
And then the program skips to the end of of all the clauses of the if
statement.
***************************************************
## if statement: elif clause

```python
if [[age >= 21]][[Is 19 greater than 21?]]:
  print("You are old enough")
  print("Please come in")
elif age >= 18:
  print("You are technically an adult, but still not old enough")
elif age >= 13:
  print("You are a teenager")
else:
  print("You are a baby")
```

---
If age was 19, and therefore not greater than or equal to 21, this conditional
would be false,
***************************************************
## if statement: elif clause

```python
if age >= 21:
  print("You are old enough")
  print("Please come in")
elif [[age >= 18]][[Is 19 greather than or equal to 18?]]:
  print("You are technically an adult, but still not old enough")
elif age >= 13:
  print("You are a teenager")
else:
  print("You are a baby")
```

---
Which allows the next conditional to the evaluated. In the case of this
elif statement, the conditional returns true.
***************************************************
## if statement: elif clause

```python
if age >= 21:
  print("You are old enough")
  print("Please come in")
elif age >= 18:
  [[print("You are technically an adult, but still not old enough")]][[Execute this]]
elif age >= 13:
  print("You are a teenager")
else:
  print("You are a baby")
```

---
Which means the code will reach its consequent block.
***************************************************
## if statement: elif clause

```python
if age >= 21:
  print("You are old enough")
  print("Please come in")
elif age >= 18:
  print("You are technically an adult, but still not old enough")
elif age >= 13:
  print("You are a teenager")
else:
  print("You are a baby")
[[  →]][[Skips to here]]
```

---
And then skip to the end.
***************************************************
## if statement: else clause

```python
if age >= 21:
  print("You are old enough")
  print("Please come in")
elif age >= 18:
  print("You are technically an adult, but still not old enough")
elif age >= 13:
  print("You are a teenager")
[[else:
  print("You are a baby")]][[else clause]]
```

---
An else clause --- if one exists --- must come after any if and elif clauses.
And the statements in its alternate block will only execute if all of the
conditional clauses in the preceding statements have evaluated to false.
***************************************************
## if statement: order of clauses

1. if clause
2. any number of elif clauses
3. an else clause

---
Thus, this is the order of the clauses in an if statement.
***************************************************
## Full Age Example

```python
age = int(input("How old are you? "))
if age >= 21:
  print("You are old enough")
  print("Please come in")
elif age >= 18:
  print("You are technically an adult, but still not old enough")
elif age >= 13:
  print("You are a teenager")
else:
  print("You are a baby")
```

---
Now, to make this code a full example, we'll add an instruction to
prompt the user to enter their age, and then convert that to an integer.

Run this in Python Tutor. Execute this code at least 4 times. Each time going
through a different consequent block. When prompted for the age,
use the ages: 22, 20, 15, and 5.
***************************************************
## Full Age Example

```python
age = int(input("How old are you? "))
if age >= 21:
  print("You are old enough")
  print("Please come in")
elif age >= 18:
  print("You are technically an adult, but still not old enough")
elif age >= 13:
  print("You are a teenager")
else:
  print("You are a baby")
```

---
Try to modify this code now. Make it do this: in the case that they are
between 14 and 18 years old, tell them how many years they should wait
until coming back.

Go to the next slide to see my solution.
***************************************************
## Solution

```python
age = int(input("How old are you? "))
if age >= 21:
  print("You are old enough")
  print("Please come in")
elif age >= 18:
  print("You are technically an adult, but still not old enough")
  difference = 21 - age
  print("Come back in", difference, "years")
elif age >= 13:
  print("You are a teenager")
else:
  print("You are a baby")
```

---
This is the solution.
***************************************************
## How's the Weather

```python
answer = input("How's the weather? (sunny or rainy) ")
if answer == "rainy":
  print("Let's stay home and watch TV.")
elif answer == "sunny":
  print("Let's go outside and play!")
```

---
Here's another example. This program asks the user about the weather. If
the user types "sunny", it says one thing, if they type "rainy" it says
another.
***************************************************
## How's the Weather

```python
answer = input("How's the weather? (sunny or rainy) ")
if answer [[==]][[Equality operator]] "rainy":
  print("Let's stay home and watch TV.")
elif answer == "sunny":
  print("Let's go outside and play!")
```

---
This program uses the equality operator, which will evaluate to true if
...
***************************************************
## How's the Weather

```python
answer = input("How's the weather? (sunny or rainy) ")
if [[answer]][[left-hand side]] == "rainy":
  print("Let's stay home and watch TV.")
elif answer == "sunny":
  print("Let's go outside and play!")
```

---
both the left-hand side...
***************************************************
## How's the Weather

```python
answer = input("How's the weather? (sunny or rainy) ")
if answer == [["rainy"]][[right-hand side]]:
  print("Let's stay home and watch TV.")
elif answer == "sunny":
  print("Let's go outside and play!")
```

---
and the right-hand side have the same value.
***************************************************
## How's the Weather

```python
answer = input("How's the weather? (sunny or rainy) ")
if [[answer == "rainy"]][[is the answer rainy?]]:
  print("Let's stay home and watch TV.")
elif answer == "sunny":
  print("Let's go outside and play!")
```

---
In our case, it evaluates whether the answer typed in by the user, is exacty
"rainy".
***************************************************
## How's the Weather

```python
answer = input("How's the weather? (sunny or rainy) ")
if answer == "rainy":
  print("Let's stay home and watch TV.")
elif [[answer == "sunny"]][[is the answer sunny]]:
  print("Let's go outside and play!")
```

---
Then, the next elif tests if they typed in the word "sunny".
***************************************************
## How's the Weather

```python
answer = input("How's the weather? (sunny or rainy) ")
if answer == "rainy":
  print("Let's stay home and watch TV.")
elif answer == "sunny":
  print("Let's go outside and play!")
```

---
What would happen if the user typed in something other than the words "rainy" or
"sunny"?

Please make your prediction, and then run this code in Python Tutor to find
out the answer.
***************************************************
## How's the Weather

```python
answer = input("How's the weather? (sunny or rainy) ")
if answer == "rainy":
  print("Let's stay home and watch TV.")
elif answer == "sunny":
  print("Let's go outside and play!")
```

---
You should have found out that if you wrote an answer that the program didn't
test for, then the program did not print anything. What can you do to fix it?
***************************************************
## How's the Weather

```python
answer = input("How's the weather? (sunny or rainy) ")
if answer == "rainy":
  print("Let's stay home and watch TV.")
elif answer == "sunny":
  print("Let's go outside and play!")
```

---
There are two cases:

1. If they type in something you want to respond to - what should you do?
2. If they type in something you don't want to respond to - what should you do?
***************************************************
## How's the Weather

```python
answer = input("How's the weather? (sunny or rainy) ")
if answer == "rainy":
  print("Let's stay home and watch TV.")
elif answer == "sunny":
  print("Let's go outside and play!")
```

---
We'd like to respond to the answer "cloudy". Please modify this code to do
that. You can choose what you'd like to say when it is cloudy.

Go to the next slide to see my solution.
***************************************************
## How's the Weather

```python
answer = input("How's the weather? (sunny, rainy, or cloudy) ")
if answer == "rainy":
  print("Let's stay home and watch TV.")
elif answer == "sunny":
  print("Let's go outside and play!")
elif answer == "cloudy":
  print("Let's go outside and play anyway!")
```

---
This is the solution --- a new elif clause was added to the if statement to
test for the answer of "cloudy", and print a corresponding sentence.
***************************************************
## Full Age Example

```python
answer = input("How's the weather? (sunny, rainy, or cloudy) ")
if answer == "rainy":
  print("Let's stay home and watch TV.")
elif answer == "sunny":
  print("Let's go outside and play!")
elif answer == "cloudy":
  print("Let's go outside and play anyway!")
```

---
Now, what if they type in something we don't understand?

Modify this program to say "Sorry, I don't understand what you said." if
they typed a different response to the above 3.

See solution in the next slide.
***************************************************
## Full Age Example

Solution:
```python
answer = input("How's the weather? (sunny, rainy, or cloudy) ")
if answer == "rainy":
  print("Let's stay home and watch TV.")
elif answer == "sunny":
  print("Let's go outside and play!")
elif answer == "cloudy":
  print("Let's go outside and play anyway!")
else:
  print("Sorry, I don't understand what you said.")
```

---
This is the solution --- to add an else clause.
***************************************************
## Nested If Statements

```python
if age < 10:
  if weather == "sunny":
    print("Let's go outside and play!")
  else:
    print("Let's stay home.")
```

---
It is possible to nest one if statement within another. In this example,
the inner if statement will only execute if the outter if statement's
conditional: `age < 10` evaluates to true.
***************************************************
## Nested If Statements: Coffee

```python
coffee = input("What coffee would you like? (coffee, latte) ")
size = input("What size? (small, big)")
```

---
Let's use buying coffee as an example. If you asked the user these two
questions, thus getting two variables with their separate values:

* coffee could be either "coffee" or "latte"
* size could be either "small" or "large"

You want to tell them the price of the drink you've ordered.
***************************************************
## Coffee Prices

* Small coffee: $2.5
* Large coffee: $3
* Small latte: $3.5
* Large latte: $4.5

---
These are the coffee prices. How would you go about writing the code?

Hint: you can use nested if statements.

Give this a try. And then turn the slide for the solution.
***************************************************
## Coffee Solution

```python
coffee = input("What coffee would you like? (coffee, latte) ")
size = input("What size? (small, big) ")
if coffee == "coffee":
    if size == "small":
        print("A small coffee is $2.50")
    elif size == "big":
        print("A big coffee is $3.00")
elif coffee == "latte":
    if size == "small":
        print("A small latte is $3.50")
    elif size == "big":
        print("A big latte is $4.50")
```

---
This is the solution.
***************************************************
## Coffee Solution

```python
[[coffee]][[coffee selection]] = input("What coffee would you like? (coffee, latte) ")
size = input("What size? (small, big) ")
if coffee == "coffee":
    if size == "small":
        print("A small coffee is $2.50")
    elif size == "big":
        print("A big coffee is $3.00")
elif coffee == "latte":
    if size == "small":
        print("A small latte is $3.50")
    elif size == "big":
        print("A big latte is $4.50")
```

---
If the coffee selection was coffee...
***************************************************
## Coffee Solution

```python
coffee = input("What coffee would you like? (coffee, latte) ")
size = input("What size? (small, big) ")
if [[coffee == "coffee"]][[conditional for coffee]]:
    if size == "small":
        print("A small coffee is $2.50")
    elif size == "big":
        print("A big coffee is $3.00")
elif coffee == "latte":
    if size == "small":
        print("A small latte is $3.50")
    elif size == "big":
        print("A big latte is $4.50")
```

---
This conditional evaluates to true.
***************************************************
## Coffee Solution

```python
coffee = input("What coffee would you like? (coffee, latte) ")
size = input("What size? (small, big) ")
if coffee == "coffee":
    [[if size == "small":
        print("A small coffee is $2.50")
    elif size == "big":
        print("A big coffee is $3.00")]][[Consequent clause for coffee]]
elif coffee == "latte":
    if size == "small":
        print("A small latte is $3.50")
    elif size == "big":
        print("A big latte is $4.50")
```

---
and the program takes the consequent clause for coffee.
***************************************************
## Coffee Solution

```python
coffee = input("What coffee would you like? (coffee, latte) ")
size = input("What size? (small, big) ")
if coffee == "coffee":
    if [[size == "small"]][[size is small conditional]]:
        print("A small coffee is $2.50")
    elif size == "big":
        print("A big coffee is $3.00")
elif coffee == "latte":
    if size == "small":
        print("A small latte is $3.50")
    elif size == "big":
        print("A big latte is $4.50")
```

---
Then it has to decide what price to charge based on the size. This is the
conditional to test for small.

Let's say the size the user entered was "big". It would skip this consequent
clause,
***************************************************
## Coffee Solution

```python
coffee = input("What coffee would you like? (coffee, latte) ")
size = input("What size? (small, big) ")
if coffee == "coffee":
    if size == "small":
        print("A small coffee is $2.50")
    elif [[size == "big"]][[size is big conditional]]:
        print("A big coffee is $3.00")
elif coffee == "latte":
    if size == "small":
        print("A small latte is $3.50")
    elif size == "big":
        print("A big latte is $4.50")
```

---
and try the second conditional which tests if the size is big. Since it is,
***************************************************
## Coffee Solution

```python
coffee = input("What coffee would you like? (coffee, latte) ")
size = input("What size? (small, big) ")
if coffee == "coffee":
    if size == "small":
        print("A small coffee is $2.50")
    elif size == "big":
        [[print("A big coffee is $3.00")]][[consequent clause for size is big]]
elif coffee == "latte":
    if size == "small":
        print("A small latte is $3.50")
    elif size == "big":
        print("A big latte is $4.50")
```

---
the program executes the consequent clause for if the size is big, and prints
the price of a big coffee.
***************************************************
## Coffee Solution

```python
coffee = input("What coffee would you like? (coffee, latte) ")
size = input("What size? (small, big) ")
if coffee == "coffee":
    if size == "small":
        print("A small coffee is $2.50")
    elif size == "big":
        print("A big coffee is $3.00")
elif coffee == "latte":
    if size == "small":
        print("A small latte is $3.50")
    elif size == "big":
        print("A big latte is $4.50")
```

---
Execute this program in Python Tutor. Make sure you re-run it with all 4
combinations of possible values: coffee small, coffee big, latte small, and
latte big and see it go through each branch of the nested if statements.


***************************************************
## Summary

* if statement
* else statement
* elif statement
* nested if statements

---
You made it to the end. Wow!!!

In this lesson, you learned about the if statement.
***************************************************
## Homework

[Homework](https://gist.github.com/airportyh/8e2a5b8349ed43a09c4fd1fd14ee5c6d)

---
Here is your homework. Enjoy!
