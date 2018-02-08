# Lesson 9.5
## Functions - Part 2

---
Welcome back for more on functions!!! This time
we will use functions as a tool to decompose
problems into smaller problems.
**********************************************
## Problem Decomposition

*Problem decomposition* is the process of taking a
problem into a number of smaller problems.

---

**********************************************
## Problem Decomposition

*Problem decomposition* is the process of taking a
problem into a number of smaller problems.

---
Up until now, we have dealt with relatively small
problems. Even so, we can benefit from breaking up
a problem into smaller problems, and solve those
smaller problems individually as functions,
before tackling the larger problem in question.
**********************************************
## Reverse All Words Example

Problem:
Given a phrase containing one or more words,
return a new version of the phrase where every one
of its words has its letters reversed.

---
Let's take this problem as an example. If we were
to write a recipe (a series steps) for solving this
problem --- in  English --- what would that look like?

Please do this exercise yourself with pencil and paper,
and then move to the next slide to see my solution.
(Note, there are multiple possible solutions, so yours
  is not necessarily wrong if it differs.)
**********************************************
## Reverse All Words Recipe

1. Break phrase into a list of words
2. Iterate through each word
    * Reverse the letter of the word
3. Put the reversed words back together into a
new phrase
4. Return the new version of the phrase

---
This is what I came up with. Now, we could go ahead
and write a program following these steps, but
we could also selectively implement one or
more of these steps as a function, and then have
the code that solves the whole problem --- which will
also be a function --- utilize that function.

Yes! A function can call another function!
**********************************************
## Reverse All Words Recipe

1. Break phrase into a list of words
2. Iterate through each word
    * Reverse the letter of the word
3. Put the reversed words back together into a
new phrase
4. Return the new version of the phrase

---
Now, the way you decide which subproblem to break out
as a separate function is a bit of an art --- you
will get to practice that art later. But, for
now I will make the choice for you...
**********************************************
## Reverse All Words Recipe

1. Break phrase into a list of words
2. Iterate through each word
    * [[Reverse the letter of the word]][[write a function to do this]]
3. Put the reversed words back together into a
new phrase
4. Return the new version of the phrase

---
We will write a function to reverse the letters of
an individual word.
**********************************************
## Function: Reverse a Word

```python
def reverse_word(word):
    result = ""
    for letter in word:
        result = letter + result
    return result
```

---
We shall name this function `reverse_word`.

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
that means we can move on to the next step. [Running this code](http://pythontutor.com/visualize.html#code=def%20reverse_word%28word%29%3A%0A%20%20%20%20result%20%3D%20%22%22%0A%20%20%20%20for%20letter%20in%20word%3A%0A%20%20%20%20%20%20%20%20result%20%3D%20letter%20%2B%20result%0A%20%20%20%20return%20result%0A%20%20%20%20%0Aprint%28reverse_word%28%22bananas%22%29%29&cumulative=false&curInstr=0&heapPrimitives=false&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false) should
print `sananab` in the terminal.
**********************************************
## Testing Functions in Isolation

```python
print(reverse_word("bananas"))
print(reverse_word("blueberry"))
print(reverse_word("a"))
print(reverse_word(""))
```

---
In general, you want to remember to test the special cases --- like if there's
just one character, or even an empty string --- in addition to the the
usual suspects, because things that seem obvious often break on the special
cases.

[This program](http://pythontutor.com/visualize.html#code=def%20reverse_word%28word%29%3A%0A%20%20%20%20result%20%3D%20%22%22%0A%20%20%20%20for%20letter%20in%20word%3A%0A%20%20%20%20%20%20%20%20result%20%3D%20letter%20%2B%20result%0A%20%20%20%20return%20result%0A%20%20%20%20%0Aprint%28reverse_word%28%22bananas%22%29%29%0Aprint%28reverse_word%28%22blueberry%22%29%29%0Aprint%28reverse_word%28%22a%22%29%29%0Aprint%28reverse_word%28%22%22%29%29&cumulative=false&curInstr=0&heapPrimitives=false&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false) prints:

```
sananab
yrrebeulb
a

```
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
Now, given that we have a function to help us reverse a single word.
Let's write a function to take phrase, and reverse all its words.
This function: `reverse_all_words` does that.

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
