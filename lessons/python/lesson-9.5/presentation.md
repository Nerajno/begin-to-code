## Lesson 9.5
# Functions - Part 2

---
Welcome back for more on functions!!! This time
we will use functions as a tool to decompose
problems into smaller problems. This is a *must* if you
want to work on any program that's longer than
a page in length.
**********************************************
## Problem Decomposition

*Problem decomposition* is the process of breaking a
problem into a number of smaller sub-problems.

---

**********************************************
## Problem Decomposition

*Problem decomposition* is the process of breaking a
problem into a number of smaller sub-problems.

---
Up until now, we have dealt with relatively small
problems. Even so, we can benefit from breaking up
a problem into smaller problems and solve those
smaller problems individually as functions,
before tackling the larger problem in question.
**********************************************
## Reverse All Words Example

Problem:
Given a phrase containing one or more words,
return a new version of the phrase where each
of its words has its letters in reverse order.

Examples:

* `super tuesday -> repus yadseut`
* `orange county -> egnaro ytnuoc`

---
Let's take this problem as an example. If we were
to write a recipe (a series steps) for solving this
problem --- in  English --- what would that look like?

Please do this exercise yourself with pencil and paper,
and then move to the next slide to see my solution.

*Note, there are multiple possible solutions, so yours
  is not necessarily wrong if it differs.*
**********************************************
## Reverse All Words Recipe

1. Break phrase into a list of words
2. Create a list to collect the reversed words
2. Iterate through each word
    * Reverse the letters of the word
    * add the reversed word to the list
3. Put the list of reversed words back together into a
  string
4. Return the new version of the phrase

---
This is what I came up with. Now, we could go ahead
and write a program following these steps, but
one of these steps is more involved than the others...
**********************************************
## Reverse All Words Recipe

1. Break phrase into a list of words
2. Create a list to collect the reversed words
2. Iterate through each word
    * [[Reverse the letters of the word]][[Write a function to do this]]
    * add the reversed word to the list
3. Put the list of reversed words back together into a
  string
4. Return the new version of the phrase

---
The step that reverses the letters of a word. The process of
reversing the letters of a word by itself is complicated.

So let's break that out into a sub-problem.
**********************************************
## Reverse Letters of a Word Recipe

Given a word, return a new version of the word with
its letters in reverse order.

Examples:

* `banana -> ananab`
* `orange -> egnaro`
* `kiwi -> iwik`

---
How do you reverse the letters of a word?

Let's write a recipe for it.
Come up with the steps on your own, and then move to the
next slide to see my solution.
**********************************************
## Reverse Letters of a Word Recipe

1. Create an empty string to collect the letters, call it `result`
2. Iterate through each letter of the word
    * append the letter to the left of `result`
3. Return `result`

---
Here are my steps for reversing the letters of a word.

Now, let's write a function for it.
**********************************************
## Function: Reverse a Word

1. Create an empty string to collect the letters, call it `result`
2. Iterate through each letter of the word
    * append the letter to the left of `result`
3. Return `result`

```python
[[[def reverse_word():]]]
```

---
First, we shall name this function `reverse_word`.

A good convention
to follow is to name a function as a phrase that starts with a verb.
Because a function's purpose is to *do* something, naming it a verb just
makes sense.
**********************************************
## Function: Reverse a Word

1. Create an empty string to collect the letters, call it `result`
2. Iterate through each letter of the word
    * append the letter to the left of `result`
3. Return `result`

```python
def reverse_word([[word]][[string parameter]]):
```

---
Next we need to identify the parameters.

This function does something to a word, so it
will take a string parameter `word` --- this is the word it will reverse.

Next, let's go through the recipe step by step, and
write each step in Python.
**********************************************
## Function: Reverse a word

1. [[[Create an empty string to collect the letters, call it `result`]]]
2. Iterate through each letter of the word
    * append the letter to the left of `result`
3. Return `result`

```python
def reverse_word(word):
    [[[result = ""]]]
```

---
The first step is to create a variable --- we'll call it `result` ---
and initialize it to an empty string.
**********************************************
## Function: Reverse a word

1. Create an empty string to collect the letters, call it `result`
2. [[[Iterate through each letter of the word]]]
    * append the letter to the left of `result`
3. Return `result`

```python
def reverse_word(word):
    result = ""
    [[[for letter in word:]]]
```

---
Then we'll iterate through each letter of the word using a
for loop.
**********************************************
## Function: Reverse a word

1. Create an empty string to collect the letters, call it `result`
2. Iterate through each letter of the word
    * [[[append the letter to the left of `result`]]]
3. Return `result`

```python
def reverse_word(word):
    result = ""
    for letter in word:
        [[[result = letter + result]]]
```

---
Then we'll append --- or concatenate --- the letter to the left
of the current value of `result`.
**********************************************
## Function: Reverse a word

1. Create an empty string to collect the letters, call it `result`
2. Iterate through each letter of the word
    * append the letter to the left of `result`
3. [[[Return `result`]]]

```python
def reverse_word(word):
    result = ""
    for letter in word:
        result = letter + result
    [[[return result]]]
```

---
And finally, we return the final version of the result to
the caller of this function.
**********************************************
## Function: Reverse a word

1. Create an empty string to collect the letters, call it `result`
2. Iterate through each letter of the word
    * append the letter to the left of `result`
3. Return `result`

```python
def reverse_word(word):
    result = ""
    for letter in word:
        result = letter + result
    return result
```

---
That's the function! Now we are ready to test it.
**********************************************
## Testing Functions in Isolation

```python
print(reverse_word("bananas"))
```

---
The nice thing about breaking a program up into small pieces is that you can
test each piece in isolation, and thus get feedback faster about whether or
not you are getting it right.

In our case, we can apply the `reverse_word` function to just any word,
like "bananas", to see if it's doing what it's supposed to do. If it works,
that means we can move on to the next step.

[Running this code](http://pythontutor.com/visualize.html#code=def%20reverse_word%28word%29%3A%0A%20%20%20%20result%20%3D%20%22%22%0A%20%20%20%20for%20letter%20in%20word%3A%0A%20%20%20%20%20%20%20%20result%20%3D%20letter%20%2B%20result%0A%20%20%20%20return%20result%0A%20%20%20%20%0Aprint%28reverse_word%28%22bananas%22%29%29&cumulative=false&curInstr=0&heapPrimitives=false&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false) should
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
## Function: Reverse a Word

```python
def reverse_word(word):
    result = ""
    for letter in word:
        result = letter + result
    return result
```

---
So, now that we can reverse a word,
**********************************************
## Reverse the Words

1. Break phrase into a list of words
2. Create a list to collect the reversed words
2. Iterate through each word
    * Reverse the letters of the word
    * add the reversed word to the list
3. Put the list of reversed words back together into a
  string
4. Return the new version of the phrase

---
Back to the original problem!

Let's write *this recipe* in Python, as another function.
**********************************************
### Function: Reverse All The Words

1. Break phrase into a list of words
2. Create a list to collect the reversed words
2. Iterate through each word
    * Reverse the letters of the word
    * add the reversed word to the list
3. Put the list of reversed words back together into a
  string
4. Return the new version of the phrase

```python
[[[def reverse_all_words():]]]
```

---
First, let's define a function. We will continue the tradition
of calling functions by what they do. So this function is called
`reverse_all_words`.
**********************************************
### Function: Reverse All The Words

1. Break phrase into a list of words
2. Create a list to collect the reversed words
2. Iterate through each word
    * Reverse the letters of the word
    * add the reversed word to the list
3. Put the list of reversed words back together into a
  string
4. Return the new version of the phrase

```python
def reverse_all_words([[phrase]][[string parameter]]):
```

---
This function does something to a phrase,
so it will take a string parameter `phrase`.

Next, let's go step by step through the recipe.
**********************************************
### Function: Reverse All The Words

1. [[[Break phrase into a list of words]]]
2. Create a list to collect the reversed words
2. Iterate through each word
    * Reverse the letters of the word
    * add the reversed word to the list
3. Put the list of reversed words back together into a
  string
4. Return the new version of the phrase

```python
def reverse_all_words(phrase):
    [[[words = phrase.split(" ")]]]
```

---
Step 1 --- as the recipe says --- is to break the phrase into a list
of words. We use the `split` method of string to do that conveniently.
**********************************************
### Function: Reverse All The Words

1. Break phrase into a list of words
2. [[[Create a list to collect the reversed words]]]
2. Iterate through each word
    * Reverse the letters of the word
    * add the reversed word to the list
3. Put the list of reversed words back together into a
  string
4. Return the new version of the phrase

```python
def reverse_all_words(phrase):
    words = phrase.split(" ")
    [[[result_words = []]]]
```

---
Next, we create a list variable to be used to collect
the reversed words,
**********************************************
### Function: Reverse All The Words

1. Break phrase into a list of words
2. Create a list to collect the reversed words
2. [[[Iterate through each word]]]
    * Reverse the letters of the word
    * add the reversed word to the list
3. Put the list of reversed words back together into a
  string
4. Return the new version of the phrase

```python
def reverse_all_words(phrase):
    words = phrase.split(" ")
    result_words = []
    [[[for word in words:]]]
```

---
Then, we iterate through each word with a for loop
**********************************************
### Function: Reverse All The Words

1. Break phrase into a list of words
2. Create a list to collect the reversed words
2. Iterate through each word
    * [[[Reverse the letters of the word]]]
    * add the reversed word to the list
3. Put the list of reversed words back together into a
  string
4. Return the new version of the phrase

```python
def reverse_all_words(phrase):
    words = phrase.split(" ")
    result_words = []
    for word in words:
        [[[result_word = reverse_word(word)]]]
```

---
For each word, we want to generate a reversed version
of the word. Good thing we already have a FUNCTION that
does that!!!
**********************************************
### Function: Reverse All The Words

1. Break phrase into a list of words
2. Create a list to collect the reversed words
2. Iterate through each word
    * [[[Reverse the letters of the word]]]
    * add the reversed word to the list
3. Put the list of reversed words back together into a
  string
4. Return the new version of the phrase

```python
def reverse_all_words(phrase):
    words = phrase.split(" ")
    result_words = []
    for word in words:
        result_word = [[reverse_word(word)]][[call that function!]]
```

---
To reverse a word, all we have to do now is to call the
`reverse_word` function that was just made, passing in the current word as the
argument to get the result.
**********************************************
### Function: Reverse All The Words

1. Break phrase into a list of words
2. Create a list to collect the reversed words
2. Iterate through each word
    * [[[Reverse the letters of the word]]]
    * add the reversed word to the list
3. Put the list of reversed words back together into a
  string
4. Return the new version of the phrase

```python
def reverse_all_words(phrase):
    words = phrase.split(" ")
    result_words = []
    for word in words:
        [[result_word]][[store the reversed word here]] = reverse_word(word)
```

---
then we store the reversed word in the `result_word` variable.
**********************************************
### Function: Reverse All The Words

1. Break phrase into a list of words
2. Create a list to collect the reversed words
2. Iterate through each word
    * Reverse the letters of the word
    * [[[add the reversed word to the list]]]
3. Put the list of reversed words back together into a
  string
4. Return the new version of the phrase

```python
def reverse_all_words(phrase):
    words = phrase.split(" ")
    result_words = []
    for word in words:
        result_word = reverse_word(word)
        [[[result_words.append(result_word)]]]
```

---
Once we have the reversed word, we append it to the `result_words`
list.
**********************************************
### Function: Reverse All The Words

1. Break phrase into a list of words
2. Create a list to collect the reversed words
2. Iterate through each word
    * Reverse the letters of the word
    * add the reversed word to the list
3. [[[Put the list of reversed words back together into a
  string]]]
4. Return the new version of the phrase

```python
def reverse_all_words(phrase):
    words = phrase.split(" ")
    result_words = []
    for word in words:
        result_word = reverse_word(word)
        result_words.append(result_word)
    [[[result_phrase = " ".join(result_words)]]]
```

---
When we are done with every word, we join the list of
result words back into one single string separated by spaces,
conveniently using string's join method. We store that
into the `result_phrase` variable.
**********************************************
### Function: Reverse All The Words

1. Break phrase into a list of words
2. Create a list to collect the reversed words
2. Iterate through each word
    * Reverse the letters of the word
    * add the reversed word to the list
3. Put the list of reversed words back together into a
  string
4. [[[Return the new version of the phrase]]]

```python
def reverse_all_words(phrase):
    words = phrase.split(" ")
    result_words = []
    for word in words:
        result_word = reverse_word(word)
        result_words.append(result_word)
    result_phrase = " ".join(result_words)
    [[[return result_phrase]]]
```

---
Finally, we return `result_phrase` --- containing the phrase
where each word has been reversed, back to the caller of
this function.
**********************************************
### Function: Reverse All The Words

1. Break phrase into a list of words
2. Create a list to collect the reversed words
2. Iterate through each word
    * Reverse the letters of the word
    * add the reversed word to the list
3. Put the list of reversed words back together into a
  string
4. Return the new version of the phrase

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
There we have it! This function implements the recipe.
**********************************************
## Function: Reverse All The Words

```python
phrase = input("Type a phrase: ")
result = reverse_all_words(phrase)
print(result)
```

---
Now, with the aid of the `reverse_all_words` function, we can write the main
program in 3 lines, like so.
**********************************************
### Reverse the Words: Full Source

```python
def reverse_word(word):
    result = ""
    for letter in word:
        result = letter + result
    return result

def reverse_all_words(phrase):
    words = phrase.split(" ")
    result_words = []
    for word in words:
        result_word = reverse_word(word)
        result_words.append(result_word)
    result_phrase = " ".join(result_words)
    return result_phrase

phrase = input("Type a phrase: ")
result = reverse_all_words(phrase)
print(result)
```

---
This is the full source code of this example.

Now, let's take a detailed look at what happens when functions
are called within this program.
**********************************************
![Stack Frames 1](lessons/python/lesson-9.5/images/stack-frames-1.png)

---
Here, I've made a simulation of the code. It is like Python Tutor, except
that the code is hierarchical. We start with the top level program and its
global frame --- where the variables are stored.

We are currently on line 17, where a function call to `reverse_all_words` is
about to happen, we will pass the value of `phrase` to it as an argument,
which has the value of `"love it"` --- that's what the user entered.
**********************************************
![Stack Frames 2](lessons/python/lesson-9.5/images/stack-frames-2.png)

---
When that function call is made,
it expands the source code for the called function (`reverse_all_words`)
to the right, and displays the frame for that function underneath it.

The parameter `phrase` here is actually local to the code within this function.
The value `"love it"` came in as an argument from the top level code on line 17.

Note that line 17 is still in the process of executing --- thus the red arrow
is still next to it, but it's progress is now happening within the
`reverse_all_words` call.
**********************************************
![Stack Frames 4](lessons/python/lesson-9.5/images/stack-frames-4.png)

---
We skip a few steps, to line 11, where it makes a nested function call ---
a function is calling another function.

It will call the `reverse_word` function and pass the current value of
`word` into it --- which has the value of the string `"love"`.
**********************************************
![Stack Frames 5](lessons/python/lesson-9.5/images/stack-frames-5.png)

---
When `reverse_word` is called,
yet another frame forms, and we drill down to that function.

As we can see, the `word` parameter on this new frame
has been initialized with the string `"love"`, the value that was passed
in as the argument on line 11.

Again, note that line 11 is still in progress. In fact, line 17 is also
still in progress --- it will be done only when the call to `reverse_all_words`
returns. And line 11 will be done when this call to `reverse_word` returns.
**********************************************
![Stack Frames 14](lessons/python/lesson-9.5/images/stack-frames-14.png)

---
Let's skip to the end of this `reverse_word` function.
At the last line of the function, it is about to
return the string `"evol"` as its return value.
**********************************************
![Stack Frames 15](lessons/python/lesson-9.5/images/stack-frames-15.png)

---
When a function returns, it's stack frame --- along with the variables within
it --- is destroyed. The only thing that remains is the return value `"evol"`,
which substitutes in to the function call expression --- `reverse_word(word)`
--- that was made in the parent frame.
**********************************************
![Stack Frames 18](lessons/python/lesson-9.5/images/stack-frames-18.png)

---
We skip a few steps again to get to the next word. We will call
the `reverse_word` function again, this time to reverse the word `"it"`.
**********************************************
![Stack Frames 19](lessons/python/lesson-9.5/images/stack-frames-19.png)

---
Again, we create a new frame for this function call --- we *don't* reuse
the frame from the last time the function was called.

This time `word` has been initialized to `"it"`.
**********************************************
![Stack Frames 21](lessons/python/lesson-9.5/images/stack-frames-21.png)

---
We skip to the end of this function, and see that it will return the
string `"ti"`.
**********************************************
![Stack Frames 22](lessons/python/lesson-9.5/images/stack-frames-22.png)

---
Again, the frame of the returned function is destroyed, and the only thing
that remains is the returned value: `"ti"`, which is sent back to the
caller.
**********************************************
![Stack Frames 23](lessons/python/lesson-9.5/images/stack-frames-23.png)

---
The caller gets the reversed word in the variable `result_word` at this
point.
**********************************************
![Stack Frames 27](lessons/python/lesson-9.5/images/stack-frames-27.png)

---
Let's skip to the end of this function, where the return value
has been determined --- it is `"evol ti"`.
**********************************************
![Stack Frames 28](lessons/python/lesson-9.5/images/stack-frames-28.png)

---
And again, the function's frame is destroyed, and all that's left is
the return value --- which is sent back to the caller.
**********************************************
![Stack Frames 29](lessons/python/lesson-9.5/images/stack-frames-29.png)

---
Now, the top level program has the resulting phrase ---
`"evol ti"` --- stored in the `result` variable.
**********************************************
## Reverse the Words: Full Source

![3 Frames](./lessons/python/lesson-9.5/images/python-tutor-frames-full.png)

---
In Python Tutor, when we are in the midst of calling a nested function,
the stack frame looks like this.

The global frame is always on top. When a function is called in the top
level, a frame is added underneath the global frame --- here it's the
`reverse_all_words` frame. Then when a nested function call is made,
that's again added to the bottom of the frames --- here the
`reverse_word` frame.
**********************************************
## Reverse the Words: Full Source

![3 Frames](./lessons/python/lesson-9.5/images/python-tutor-frames-full.png)

---
[Step through this program](http://pythontutor.com/visualize.html#code=def%20reverse_word%28word%29%3A%0A%20%20%20%20result%20%3D%20%22%22%0A%20%20%20%20for%20letter%20in%20word%3A%0A%20%20%20%20%20%20%20%20result%20%3D%20letter%20%2B%20result%0A%20%20%20%20return%20result%0A%0Adef%20reverse_all_words%28phrase%29%3A%0A%20%20%20%20words%20%3D%20phrase.split%28%22%20%22%29%0A%20%20%20%20result_words%20%3D%20%5B%5D%0A%20%20%20%20for%20word%20in%20words%3A%0A%20%20%20%20%20%20%20%20result_word%20%3D%20reverse_word%28word%29%0A%20%20%20%20%20%20%20%20result_words.append%28result_word%29%0A%20%20%20%20result_phrase%20%3D%20%22%20%22.join%28result_words%29%0A%20%20%20%20return%20result_phrase%0A%0Aphrase%20%3D%20input%28%22Type%20a%20phrase%3A%20%22%29%0Aresult%20%3D%20reverse_all_words%28phrase%29%0Aprint%28result%29&cumulative=false&curInstr=0&heapPrimitives=false&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%22love%20it%22%5D&textReferences=false) to get a feel for how things work in Python Tutor.
**********************************************
## Summary

* Break a problem into smaller problems
* Solve smaller problems as functions
* Testing functions in isolation
* Solve larger problem as a function
* The Stack Frame

---
In this lesson, you learned how to break a problem into smaller
problems and solve them individually as functions. How to test
each function in isolation, and how a hierarchy of nested function calling
works in terms of the stack frame.

Good going!
************************************************
## Homework

[Homework](https://gist.github.com/airportyh/873e706b39dea0b083eafaec6944c340)

---
Enjoy your homework.
