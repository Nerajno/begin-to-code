## Lesson 13
# Refactoring

---
Welcome back! This lesson will cover refactoring.

Refactoring is something developers do as part of
their job to make their job easier. It is analogous
to a carpenter making improvements to their workshop.

What *is* refactoring?
*************************************************
## Refactoring

Refactoring is the process of changing code
to improve the quality of the code while not
changing the functionality of the code.

---
When we are refactoring a program, we aim to
improve the quality of the program. But in
the process, we need to take care to not
change to the functionality of the program, which
we can assume to be exactly as desired.
(*Don't break the program!!!*)

This may seem strange at first. You might be wondering:
*If the program already works, why change it?*

The reason is that code quality is important.
But before we understand why it is important,
let's talk about what quality means in the first
place.
*************************************************
# What is Good Code?

---
If we are going to aim for better code quality,
we need to know what to aim at. What does good
quality even mean for code?

I would like you to think about this question, and
write down as many answers you can think of on a
piece of paper. Then turn the slide to see
my answers.
*************************************************
## What is Good Code?

* Clear
* Concise
* Simple
* Well Documented
* Easy to Understand

---
These are the characteristics of good code.

Good code is clear and unambiguous about its intentions.

Good code is concise. It doesn't waste words(variables,
  loops, functions) where they aren't needed.

Good code is simple. If there are two ways to do something,
good code chooses the simpler of the two.

Good code is well documented. If there is something in
it that is not self-explanatory, comments are there
to help you understand. If the code is to be used by
others, there is documentation to teach them how to use it.

Good code is easy to understand.

If we were to boil all of these down to *one word* that
is the essence of what good code means, it is...
*************************************************
# Readability

## Good Code ⇔ Readable Code
---

Good code is readable code.

Readable code is good code.

*Readability* is the *most important* attribute of
quality code. Why?

***********************************************

![Reading code](lessons/python/lesson-13/images/reading-code.png)

---

As a working software developer, you will
likely spend more time reading code than writing
code on a day to day basis. This is because in
order to contribute to a software product --- unless
you wrote that all of the code for that product
yourself --- you'll need to work with other people,
and other people's code.
***********************************************

![Welcome aboard](lessons/python/lesson-13/images/welcome.png)

---

When you become a new hire. The first day at the job
you'll have a large piece of code dropped on your
lap, and you'll have to read it and poke around in it
for a while to get a basic understanding how it works
before you can start writing code.
***********************************************

![New hire](lessons/python/lesson-13/images/new-hire.png)

---

Some companies have codebases that are so big
and complex that it's not uncommon for their new
hires to take months before they can even contribute
code of their own.
*************************************************
# Readability Matters

---
This is why *readability matters*. Those companies
with their large and complex code could *really*
use some refactoring!!!

The productiveness and the happiness of a software
team is largely dependent on the readability on
their code. The problem is that as code grows,
it is bound to get more complex, and that's
where refactoring comes in. Refactoring is an
ongoing process that is needed as a codebase grows.
It is needed to keep a software team functioning
the same way that changing oil is needed to keep
your car engine working.

You, as a kind and considerate software developer,
for the welfare of your future teammates, as well
as your future self (for you'll have to read your
own code as well), shall do your best to write
readable code. To write code that is clear,
concise, simple, well documented, and easy to understand.

This lesson will give you the first sampling of
the many tools you'll use to achieve this goal.
*************************************************

![Refactoring Book](lessons/python/lesson-13/images/refactoring-book.png)

---
The term *refactoring* was coined by Martin Fowler
with his book of the same name.

In this book, he provided the motivation behind
refactoring as well as a catalog of code
transformations --- what he calls *refactorings*.

*************************************************
## Refactorings

* Extract variable
* Inline temp (variable)
* Extract function
* Inline function

---
We will go through some of these refactorings.

Let's just jump into these...
*************************************************
## Section 1
### Extract Variable and Inline Temp (Variable)

---
*************************************************
## Extract Variable

When you have a complex and/or repeated expression.
Take that expression and store its result in a
temporary variable, and then use that variable
in place of the expression.

---
The first pattern is *extract variable*.
*************************************************
## Extract Variable: When to Use

1. Expression is complex and/or difficult to comprehend
2. Expression is repeated multiple times

---
You'd use this to improve a piece of code in one
of these situations: when you spot an expression
that's complex or difficult to understand, or
when you spot an expression that is repeated a number
of times.
*************************************************
## Extract Variable: Example

```python
def shelf_books(books):
    shelf = {}
    for title in books:
        if title[0] not in shelf:
            shelf[title[0]] = []
        shelf[title[0]].append(title)

    return shelf
```

---
Take a look at this example. If you don't fully
understand the code at first glance, that's okay.
Nevertheless, you may be able to spot patterns.

Do you see an opportunity to use *extract variable*?
*************************************************
## Extract Variable: Example

```python
def shelf_books(books):
    shelf = {}
    for title in books:
        if title[0] not in shelf:
            shelf[title[0]] = []
        shelf[title[0]].append(title)

    return shelf
```

---
Here, the expression `title[0]` is used in 3 different
places. Even though the expression itself is not
complex, we may benefit from extracting it into
a temporary variable. We have to name this variable.
Since `title[0]` is what we are using as the key into
this dictionary, let's call it `key`.

Ready? The next slide reveals the result of this
refactoring...
*************************************************
## Extract Variable: Example

```python
def shelf_books(books):
    shelf = {}
    for title in books:
        key = title[0]
        if key not in shelf:
            shelf[key] = []
        shelf[key].append(title)

    return shelf
```

---
Voila!

*************************************************
## Extract Variable: Example

```python
def shelf_books(books):
    shelf = {}
    for title in books:
        [[key = title[0]]][[Defined variable]]
        if key not in shelf:
            shelf[key] = []
        shelf[key].append(title)

    return shelf
```

---
On this line, we defined the variable key, and set its
value to the result of the original expression: `title[0]`.
*************************************************
## Extract Variable: Example

```python
def shelf_books(books):
    shelf = {}
    for title in books:
        key = title[0]
        if [[key]][[here]] not in shelf:
            shelf[key] = []
        shelf[key].append(title)

    return shelf
```

---
Then we use that variable in place of the original
expression, here,
*************************************************
## Extract Variable: Example

```python
def shelf_books(books):
    shelf = {}
    for title in books:
        key = title[0]
        if key not in shelf:
            shelf[[[key]][[here]]] = []
        shelf[key].append(title)

    return shelf
```

---
here,
*************************************************
## Extract Variable: Example

```python
def shelf_books(books):
    shelf = {}
    for title in books:
        key = title[0]
        if key not in shelf:
            shelf[key] = []
        shelf[[[key]][[and here]]].append(title)

    return shelf
```

---
and here.
*************************************************
## Extract Variable: Example

```python
def mask_credit_card(cc):
    return "#" * (len(cc) - 4) + cc[-4:]
```

---
Example number 2.

Here is a function `mask_credit_card`. Based on the
name of the function, you may infer that it masks
(hides) the credit card number in some way.

However,
*************************************************
## Extract Variable: Example

```python
def mask_credit_card(cc):
    return [["#" * (len(cc) - 4) + cc[-4:]]][[complex expression]]
```

---
This expression in the return statement is dense and
difficult to parse.
*************************************************
## Extract Variable: Example

```python
def mask_credit_card(cc):
    masked = "#" * (len(cc) - 4) + cc[-4:]
    return masked
```

---
We could introduce a temporary variable to store
that whole expression like so. Since we know this
function returns a masked credit card number,
we can reasonably called the variable `masked`.

Does this make it easier to read?
*************************************************
## Extract Variable: Example

```python
def mask_credit_card(cc):
    masked = "#" * (len(cc) - 4) + cc[-4:]
    return masked
```

---
*Not really.*

That expression is still complex. We've merely
moved the complexity to a different line.
*************************************************
## Extract Variable: Example

```python
def mask_credit_card(cc):
    return "#" * (len(cc) - 4) + cc[-4:]
```

---
In fact, having that expression in the return statement
doesn't really hurt --- the return statement is actually
more concise compared to a variable assignment statement.

What would be more beneficial is to break that statement
into smaller chunks. The goal being to make the most
dense line less dense.

We shall take the left-hand side of the `+` operator,
and do an extract variable on it. And then take the
right-hand side of it, ad do an extract variable on it
as well.
*************************************************
## Extract Variable: Example

```python
def mask_credit_card(cc):
    masked_digits = "#" * (len(cc) - 4)
    visible_digits = cc[-4:]
    return masked_digits + visible_digits
```

---
Like so.

With the aid of meaningful and descriptive
variable names: masked_digits and visible_digits,
a future reader can now more easily make sense of this
code.
*************************************************
## Inline Temp (Variable)

When you have a temporary variable assigned to an
expression that is only used once, and is not helping
to clarify the code.

Inline the expression in place of the variable, and
remove the variable altogether.

---
The next refactoring is *inline temp*. Where *temp* is
Fowler's shorthand for temporary variable. It is the
opposite of *extract variable*. Instead of introducing
a new variable, this refactoring removes an existing
variable.
*************************************************
## Inline Temp: Example

```python
def mask_credit_card(cc):
    masked = "#" * (len(cc) - 4) + cc[-4:]
    return masked
```

---
In fact, we've already done *inline temp* once!

When we had the mask credit card code in this form.
We decided that extracting the variable isn't really
helping the cause of making the code easier to read.

And we decided to go back to the...
*************************************************
## Inline Temp: Example

```python
def mask_credit_card(cc):
    return "#" * (len(cc) - 4) + cc[-4:]
```

---
original, by undoing the introduction of that
variable. Often, *inline temp* is used in preparation
of another refactoring move, which was the case
here as we decided to...
*************************************************
## Inline Temp: Example

```python
def mask_credit_card(cc):
    masked_digits = "#" * (len(cc) - 4)
    visible_digits = cc[-4:]
    return masked_digits + visible_digits
```

---
pick the sub-expressions to extract as variables.
*************************************************
## Extract Function

When you have a code fragment that can be
grouped together into a logical unit.

Define a new function and move that code fragment
into the body of that function. Introduce function
parameters if necessary and make adjustments to
the code fragment to utilize those parameters.

Replace the original code fragment with a call
to the newly introduced function, passing to it
the arguments to match its parameters, if necessary.

---
The next refactoring is extract function. This is one
of the *most powerful* ways to improve your code.

Although this maneuver is more difficult than *extract
variable* to perform, it is also much more versatile,
and its end result more profound.

I recommend that you take the time to master this
refactoring, because its mastery will take your
programming ability to the next level.
*************************************************
## Extract Function

When you have a code fragment that can be
grouped together into a logical unit.

Define a new function and move that code fragment
into the body of that function. Introduce function
parameters if necessary and make adjustments to
the code fragment to utilize those parameters.

Replace the original code fragment with a call
to the newly introduced function, passing to it
the arguments to match its parameters, if necessary.

---

*Note: this refactoring is called extract method
in Fowler's book because the book is based on the
Java language, which is entirely an object-oriented
programming language, and as such, has no functions.*
*************************************************
## Extract Function: Example

```python
phrase = input("Write a phrase: ")

words = phrase.split(" ")
result_words = []
for word in words:
    reversed_word = ""
    for letter in word:
        reversed_word = letter + reversed_word
    result_words.append(reversed_word)

result = " ".join(result_words)
print(result)
```

---
This code takes a phrase from the user and
reverses the words within the phrase. It uses
an accumulator pattern nested within another
accumulator pattern.

Take a moment to read this code. What opportunities
are there to use extract function? Write your ideas
down on paper, and then go to the next slide.
*************************************************
## Extract Function: Example

```python
phrase = input("Write a phrase: ")

[[words = phrase.split(" ")
result_words = []
for word in words:
    reversed_word = ""
    for letter in word:
        reversed_word = letter + reversed_word
    result_words.append(reversed_word)

result = " ".join(result_words)]][[Code fragment]]
print(result)
```

---
Step 0 of extracting a function: identify code
fragment to extract.

This is one logical *code fragment*. The code basically
performs the string manipulation required to solve
the problem. The only 2 lines that are not included
are used to interact with the user.

Let's go ahead and perform this *function extraction*.
*************************************************
## Extract Function: Example

```python
def reverse_the_words():
```

---
Step 1 of the extraction is to start the definition of a
new function, let's call it `reverse_the_words`.
*************************************************
## Extract Function: Example

```python
def reverse_the_words():
    words = phrase.split(" ")
    result_words = []
    for word in words:
        reversed_word = ""
        for letter in word:
            reversed_word = letter + reversed_word
        result_words.append(reversed_word)

    result = " ".join(result_words)
```

---
Step 2 is to copy the code fragment and paste it into
the body of that function, like so.
*************************************************
## Extract Function: Example

```python
def reverse_the_words():
    words = phrase.split(" ")
    result_words = []
    for word in words:
        reversed_word = ""
        for letter in word:
            reversed_word = letter + reversed_word
        result_words.append(reversed_word)

    result = " ".join(result_words)
```

---
Step 3: introduce necessary input parameters.
What is the input to this code here? The `phrase`.
*************************************************
## Extract Function: Example

```python
def reverse_the_words([[phrase]][[input parameter]]):
    words = phrase.split(" ")
    result_words = []
    for word in words:
        reversed_word = ""
        for letter in word:
            reversed_word = letter + reversed_word
        result_words.append(reversed_word)

    result = " ".join(result_words)
```

---
So, we'll make `phrase` an input parameter, whereas
before, it was a variable defined in the main
code.
*************************************************
## Extract Function: Example

```python
def reverse_the_words(phrase):
    words = phrase.split(" ")
    result_words = []
    for word in words:
        reversed_word = ""
        for letter in word:
            reversed_word = letter + reversed_word
        result_words.append(reversed_word)

    result = " ".join(result_words)
```

---
Step 4: introduce return value. If the situation calls
for it, you'll need to make your function return a value.

In this situation, the purpose of this code is to generate
a new version of the string. So a return value is needed.
And the thing we need to return is the `result`.
*************************************************
## Extract Function: Example

```python
def reverse_the_words(phrase):
    words = phrase.split(" ")
    result_words = []
    for word in words:
        reversed_word = ""
        for letter in word:
            reversed_word = letter + reversed_word
        result_words.append(reversed_word)

    result = " ".join(result_words)
    [[return result]][[return statement]]
```

---
Let's return it.
*************************************************
## Extract Function: Example

```python
def reverse_the_words(phrase):
    words = phrase.split(" ")
    result_words = []
    for word in words:
        reversed_word = ""
        for letter in word:
            reversed_word = letter + reversed_word
        result_words.append(reversed_word)

    result = " ".join(result_words)
    return result
```

---
Now, you might notice that the result variable is defined,
and then only used once. Maybe that variable is not
pulling its weight. Maybe we should get rid of it.
What refactoring do we use to get it rid of it?

It's the......
*************************************************
## Inline Temp (Variable): Example

```python
def reverse_the_words(phrase):
    words = phrase.split(" ")
    result_words = []
    for word in words:
        reversed_word = ""
        for letter in word:
            reversed_word = letter + reversed_word
        result_words.append(reversed_word)

    return " ".join(result_words)
```

---
*inline temp (variable)*! Poof! `result` is now gone.

This is the end of section 1. You may do the [homework](https://gist.github.com/airportyh/71fe63952b724289a57065e6e162c756)
for this section first before moving on.
*************************************************
## Section 2
### Extract Function and Inline Function

---
*************************************************
## Extract Function: Example

```python
def reverse_the_words(phrase):
    words = phrase.split(" ")
    result_words = []
    for word in words:
        reversed_word = ""
        for letter in word:
            reversed_word = letter + reversed_word
        result_words.append(reversed_word)

    return " ".join(result_words)
```

---
Okay, back to *extract function*. Now, that we have the
extracted function,

*************************************************
## Extract Function: Example

```python
phrase = input("Write a phrase: ")

words = phrase.split(" ")
result_words = []
for word in words:
    reversed_word = ""
    for letter in word:
        reversed_word = letter + reversed_word
    result_words.append(reversed_word)

result = " ".join(result_words)
print(result)
```

---
Step 5: go back to the main code,
*************************************************
## Extract Function: Example

```python
phrase = input("Write a phrase: ")

[[words = phrase.split(" ")
result_words = []
for word in words:
    reversed_word = ""
    for letter in word:
        reversed_word = letter + reversed_word
    result_words.append(reversed_word)

result = " ".join(result_words)]][[code fragment]]
print(result)
```

---
and replace the original code fragment with...
*************************************************
## Extract Function: Example

```python
phrase = input("Write a phrase: ")

result = reverse_the_words(phrase)
print(result)
```

---
a call to the function we just made.

Wow! Refreshing, huh?

*************************************************
## Extract Function: Example

```python
def reverse_the_words(phrase):
    words = phrase.split(" ")
    result_words = []
    for word in words:
        reversed_word = ""
        for letter in word:
            reversed_word = letter + reversed_word
        result_words.append(reversed_word)

    return " ".join(result_words)

phrase = input("Write a phrase: ")

result = reverse_the_words(phrase)
print(result)
```

---
This is the full version of the code after the
*extract function* refactoring.
*************************************************
## Extract Function: Example

```python
def reverse_the_words(phrase):
    words = phrase.split(" ")
    result_words = []
    for word in words:
        reversed_word = ""
        for letter in word:
            reversed_word = letter + reversed_word
        result_words.append(reversed_word)

    return " ".join(result_words)

phrase = input("Write a phrase: ")

result = reverse_the_words(phrase)
print(result)
```

---
But wait! We are not done! Let's do another one!

I bet we could extract out another function
whose job is to reverse an individual word!

If you want to play along at home, please attempt
this now on your own. Make sure the final result
still works though --- don't break anything.
*************************************************
## Extract Function: Example

```python
def reverse_the_words(phrase):
    words = phrase.split(" ")
    result_words = []
    for word in words:
        [[reversed_word = ""
        for letter in word:
            reversed_word = letter + reversed_word]][[code fragment]]
        result_words.append(reversed_word)

    return " ".join(result_words)

phrase = input("Write a phrase: ")

result = reverse_the_words(phrase)
print(result)
```

---
Ok, let's begin!

Step 0: Identify the code fragment you are going to
extract. This code within the for loop is responsible
for reversing an individual word within the phrase.

Let's extract this out.
*************************************************
## Extract Function: Example

```python
def reverse_word():

```

---
Step 1: define a function.
*************************************************
## Extract Function: Example

```python
def reverse_word():
    reversed_word = ""
    for letter in word:
        reversed_word = letter + reversed_word
```

---
Step 2: drop in the code fragment.
*************************************************
## Extract Function: Example

```python
def reverse_word([[word]][[input]]):
    reversed_word = ""
    for letter in word:
        reversed_word = letter + reversed_word
```

---
Step 3: introduce input parameter. In this case the input
is the original word which we are going to iterate
through.
*************************************************
## Extract Function: Example

```python
def reverse_word(word):
    reversed_word = ""
    for letter in word:
        reversed_word = letter + reversed_word
    return reversed_word
```

---
Step 4: introduce return value. In the case, the job
of the function is to reverse a word, so the value
to return is the `reversed_word`.
*************************************************
## Extract Function: Example

```python
def reverse_the_words(phrase):
    words = phrase.split(" ")
    result_words = []
    for word in words:
        [[reversed_word = ""
        for letter in word:
            reversed_word = letter + reversed_word]][[original code fragment]]
        result_words.append(reversed_word)

    return " ".join(result_words)

phrase = input("Write a phrase: ")

result = reverse_the_words(phrase)
print(result)
```

---
And the final step --- step 5 is to: replace the
original code fragment with...
*************************************************
## Extract Function: Example

```python
def reverse_the_words(phrase):
    words = phrase.split(" ")
    result_words = []
    for word in words:
        [[reversed_word = reverse_word(word)]][[function call]]
        result_words.append(reversed_word)

    return " ".join(result_words)

phrase = input("Write a phrase: ")

result = reverse_the_words(phrase)
print(result)
```

---
a call to the new function.
*************************************************
## Extract Function: Example

```python
def reverse_word(word):
    reversed_word = ""
    for letter in word:
        reversed_word = letter + reversed_word
    return reversed_word

def reverse_the_words(phrase):
    words = phrase.split(" ")
    result_words = []
    for word in words:
        reversed_word = reverse_word(word)
        result_words.append(reversed_word)

    return " ".join(result_words)

phrase = input("Write a phrase: ")

result = reverse_the_words(phrase)
print(result)
```

---
And this is the full version of the code after
the second *extract function* refactoring.

What do you think? Was it worth it? Does this
improve the quality of the code? Why or why not?

Write your answers on paper. Then turn the slide.
*************************************************
## Extract Function: Example

```python
def reverse_word(word):
    reversed_word = ""
    for letter in word:
        reversed_word = letter + reversed_word
    return reversed_word

def reverse_the_words(phrase):
    words = phrase.split(" ")
    result_words = []
    for word in words:
        reversed_word = reverse_word(word)
        result_words.append(reversed_word)

    return " ".join(result_words)

phrase = input("Write a phrase: ")

result = reverse_the_words(phrase)
print(result)
```

---
In my opinion, the quality of this code has been
substantially improved. The biggest reason is
that the code has been broken down into smaller
pieces which can be individually understood in
isolation.

*************************************************
## Extract Function: Example

```python
[[def reverse_word(word):
    reversed_word = ""
    for letter in word:
        reversed_word = letter + reversed_word
    return reversed_word]][[used to reverse a word]]

def reverse_the_words(phrase):
    words = phrase.split(" ")
    result_words = []
    for word in words:
        reversed_word = reverse_word(word)
        result_words.append(reversed_word)

    return " ".join(result_words)

phrase = input("Write a phrase: ")

result = reverse_the_words(phrase)
print(result)
```

---
The `reverse_word` function has a well defined
purpose, which its name perfectly reflects.

The code within the function is simple, follows
a well-known pattern, and can easily be understood.
*************************************************
## Extract Function: Example

```python
def reverse_word(word):
    reversed_word = ""
    for letter in word:
        reversed_word = letter + reversed_word
    return reversed_word

[[def reverse_the_words(phrase):
    words = phrase.split(" ")
    result_words = []
    for word in words:
        reversed_word = reverse_word(word)
        result_words.append(reversed_word)

    return " ".join(result_words)]][[used to reverse all the words]]

phrase = input("Write a phrase: ")

result = reverse_the_words(phrase)
print(result)
```

---
Likewise, the `reverse_the_words` function has
a clear purpose, a name that reflects that purpose,
can be understood on its own, and although not
as concise as the `reverse_word` function, is
still easy enough to understand.
*************************************************
## Extract Function: Example

```python
def reverse_word(word):
    reversed_word = ""
    for letter in word:
        reversed_word = letter + reversed_word
    return reversed_word

def reverse_the_words(phrase):
    words = phrase.split(" ")
    result_words = []
    for word in words:
        [[reversed_word = reverse_word(word)]][[uses reverse_word]]
        result_words.append(reversed_word)

    return " ".join(result_words)

phrase = input("Write a phrase: ")

result = reverse_the_words(phrase)
print(result)
```

---
The line that calls the `reverse_word` function is
easy to understand, because the purpose of that
function is so well defined.

Phew!!! Now, we are done. And this is *extract
function*. Get to know this one, get to know
this one well.
*************************************************
## Inline Function

When you have a function that is not pulling its
weight because

1. It is only called 1 or 2 times.
2. It is just as easy to read the code in the body of
the function as it is to read the name of the function.

---
Just as *extract variable*, has an inverse: *inline temp
(variable)*, so too does *extract function* have
*inline function*.
*************************************************
## Inline Function: Example

```python
import math

def square(n):
    return n * n

def distance(x1, y1, x2, y2):
    return math.sqrt(square(x2 - x1) + square(y2 - y1))
```

---
Take this code, which defines a `distance` function
that calculates the distance between 2 points.
*************************************************
## Inline Function: Example

```python
import math

[[def square(n):
    return n * n]][[squares a number]]

def distance(x1, y1, x2, y2):
    return math.sqrt(square(x2 - x1) + square(y2 - y1))
```

---
The use of the `square` function seems slightly odd.
It calculates the square of a number by multiplying
it by itself --- which is rather simple to necessitate
a function.
*************************************************
## Inline Function: Example

```python
import math

def square(n):
    return [[n * n]][[return expression]]

def distance(x1, y1, x2, y2):
    return math.sqrt(square(x2 - x1) + square(y2 - y1))
```

---
We could *inline* the `square` function.

To do this, take the return expression of the function,
*************************************************
## Inline Function: Example

```python
import math

def square(n):
    return n * n

def distance(x1, y1, x2, y2):
    return math.sqrt([[n * n]][[overwrote square(x2 - x1)]] + square(y2 - y1))
```

---
Use it to overwrite the existing function call
*************************************************
## Inline Function: Example

```python
import math

def square(n):
    return n * n

def distance(x1, y1, x2, y2):
    return math.sqrt([[(x2 - x1) * (x2 - x1)]][[substitute calling argument]] + square(y2 - y1))
```

---
and then substitute the argument of the function call: `x2 - x1`
in for the input parameter of the function: `n`.

Here, since n was used twice in the expression, we actually
end up with (x2 - x1) appearing twice!!
*************************************************
## Inline Function: Example

```python
import math

def square(n):
    return n * n

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) * (x2 - x1) + [[(y2 - y1) * (y2 - y1)]][[inlined]])
```

---
We'll now do the same with the second call to `square`.
*************************************************
## Inline Function: Example

```python
import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))
```

---
Now it's safe to remove the `square` function.

How's this? Was it worth it?
*************************************************
## Inline Function: Example

```python
import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))
```

---
Wait a minute! Actually, this is worse than before!!!

UNDOOOOOOO!!!
*************************************************
## Inline Function: Example

```python
import math

def square(n):
    return n * n

def distance(x1, y1, x2, y2):
    return math.sqrt(square(x2 - x1) + square(y2 - y1))
```

---
Phew! Okay, better!

The thing about refactoring is: sometimes you don't know
if a refactoring move makes the code better or not
until you try it. This is perfectly normal. Sometimes,
you just have to learn by trial and error.
*************************************************
## Inline Function: Example

```python
import math

def square(n):
    return n * n

def distance(x1, y1, x2, y2):
    return math.sqrt(square(x2 - x1) + square(y2 - y1))
```

---
Let's try something different. So, you could also
square a number using the raise-to-the-power
operator: `**`,
*************************************************
## Inline Function: Example

```python
import math

def square(n):
    return [[n ** 2]][[n raised to the 2nd power]]

def distance(x1, y1, x2, y2):
    return math.sqrt(square(x2 - x1) + square(y2 - y1))
```

---
like so.
*************************************************
## Inline Function: Example

```python
import math

def square(n):
    return n ** 2

def distance(x1, y1, x2, y2):
    return math.sqrt(square(x2 - x1) + square(y2 - y1))
```

---
Now, inline this code and what do we get??
*************************************************
## Inline Function: Example

```python
import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
```

---
This. Nice!

To call this a thing of beauty might be a stretch,
but this code is slightly easier to read. Why?

Because

1. There is less code overall --- conciseness.
2. Less redirection: the reader does not have to look
up the definition of one more function to understand
the entire program.
*************************************************
## Summary

* What good code means: readable code
* Refactoring
* Extract variable
* Inline temp (variable)
* Extract function
* Inline function

---
Phew! You made it to the end!

This is what you've learned.
************************************************
## Homework

[Homework](https://gist.github.com/airportyh/71fe63952b724289a57065e6e162c756)

---
Here is your homework. Enjoy!
