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
