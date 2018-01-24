# Lesson 11
## Dictionaries - Part 1

---
Welcome! This lesson you will learn about the dictionary.
The dictionary is a very useful tool to put into your toolbox,
and it will open up many possibilities in terms of the types
of problems you'll be able to solve. Dictionary is a term that
is somewhat specific to Python, although there are other
programming languages that use the same term (Elm is one),
most other programming languages use a different term for
the same concept:

* Ruby folks call them hashes
* Java guys call them hash maps
* C++ people call them hash tables
* JavaScript dudes call them objects (yes, they also called records objects too)
* PHP kin call them associative arrays

So, the programming world is all over the place when it comes to terminology,
but take comfort in the fact that once you know dictionaries well, you
will be able to easily pick up the same corresponding construct in
another programming language in the future.

Let's get started!
******************************************************
# Section 1
## Introduction to Dictionaries
---
******************************************************
## An Analogy

A dictionary is like...

---
When I make these lessons, I really put a lot of thought
into coming up with great analogies. For this one, I
thought long and hard about it, and only after a great
deal of trial and error was I able to come up with the
perfect analogy for what a dictionary is.

A dictionary is like...
******************************************************

![a dictionary](lessons/python/lesson-11/images/dictionary.png)

---
a dictionary.

![Mind blown](lessons/python/lesson-11/images/mindblown.gif)

You know a dictionary? Still remember those? Let me see if I
can jog your memory. If you open a dictionary, it looks like...
******************************************************
![a dictionary](lessons/python/lesson-11/images/dictionary-2.jpg)

---
this...
******************************************************
![an entry](lessons/python/lesson-11/images/entry.png)

---
A dictionary has a lot of *entries* within it, of which "orange" is
one.

In a Python dictionary, this is also called an entry. Nice! No
need to translate.
******************************************************
![a word](lessons/python/lesson-11/images/word-key.png)

---
Within each entry, there is a *word* --- the word for which the definition
is for.

In a Python dictionary, this is called a key. You use a key
to look up a definition.
******************************************************
![a word](lessons/python/lesson-11/images/definition-value.png)

---
Within each entry, there is also the *definition* for the word.
This is the meat of the entry. It is the reason we are looking
up this entry.

In a Python dictionary, this meat part of the dictionary entry
is called the *value*.
******************************************************
![a dictionary](lessons/python/lesson-11/images/dictionary-2.jpg)

---
Thus, a dictionary has a bunch of entries in it, and each entry
is a key-value pair.

To say it even more succinctly: dictionary consists of a number of
key-value pairs.
******************************************************
## Dictionary Terms

| English Term | Python Term |
|--------------|-------------|
| Dictionary   | Dictionary  |
| Entry        | Entry       |
| Word         | Key         |
| Definition   | Value       |

---
Here is a table mapping between the English terms to the equivalent
terms in Python.
******************************************************
## A Dictionary

```python
webster = {
  "apple": "a rounded fruit with firm white flesh and a seedy core",
  "banana": "a tropical plant with thick clusters of yellow finger-shaped fruit",
  "orange": "a juicy citrus fruit with reddish yellow rind"
}
```

---
So, this is what a definition of a dictionary looks like in Python.
******************************************************
## A Dictionary

```python
webster = [[{
  "apple": "a rounded fruit with firm white flesh and a seedy core",
  "banana": "a tropical plant with thick clusters of yellow finger-shaped fruit",
  "orange": "a juicy citrus fruit with reddish yellow rind"
}]][[dictionary expression]]
```

---
The value on the right-hand-side of this variable assignment is a
dictionary expression.
******************************************************
## A Dictionary

```python
webster = [[[{]]]
  "apple": "a rounded fruit with firm white flesh and a seedy core",
  "banana": "a tropical plant with thick clusters of yellow finger-shaped fruit",
  "orange": "a juicy citrus fruit with reddish yellow rind"
[[[}]]]
```

---
A dictionary expression begins and ends with a set of two two curly braces.
These are sometimes also called curly brackets.
******************************************************
## A Dictionary

```python
webster = [[{]][[open curly brace]]
  "apple": "a rounded fruit with firm white flesh and a seedy core",
  "banana": "a tropical plant with thick clusters of yellow finger-shaped fruit",
  "orange": "a juicy citrus fruit with reddish yellow rind"
}
```

---
The first one is the open curly brace, sometimes called the left curly brace.
******************************************************
## A Dictionary

```python
webster = {
  "apple": "a rounded fruit with firm white flesh and a seedy core",
  "banana": "a tropical plant with thick clusters of yellow finger-shaped fruit",
  "orange": "a juicy citrus fruit with reddish yellow rind"
[[}]][[close curly brace]]
```

---
The second one is the close curly brace, sometimes called the right curly
brace.
******************************************************
## A Dictionary

```
webster = {
  [["apple": "a rounded fruit with firm white flesh and a seedy core",
  "banana": "a tropical plant with thick clusters of yellow finger-shaped fruit",
  "orange": "a juicy citrus fruit with reddish yellow rind"]][[dictionary entries]]
}
```

---
In between the two curly braces is a number of dictionary entries.
******************************************************
## A Dictionary

```python
webster = {
  [["apple": "a rounded fruit with firm white flesh and a seedy core"]][[entry 1]],
  "banana": "a tropical plant with thick clusters of yellow finger-shaped fruit",
  "orange": "a juicy citrus fruit with reddish yellow rind"
}
```

---
This is entry 1 --- containing the definition for apple,
******************************************************
## A Dictionary

```python
webster = {
  "apple": "a rounded fruit with firm white flesh and a seedy core",
  [["banana": "a tropical plant with thick clusters of yellow finger-shaped fruit"]][[entry 2]],
  "orange": "a juicy citrus fruit with reddish yellow rind"
}
```

---
this is entry 2 --- the definition for banana,
******************************************************
## A Dictionary

```python
webster = {
  "apple": "a rounded fruit with firm white flesh and a seedy core",
  "banana": "a tropical plant with thick clusters of yellow finger-shaped fruit",
  [["orange": "a juicy citrus fruit with reddish yellow rind"]][[entry 3]]
}
```

---
and this is entry 3 --- the definition for orange.
******************************************************
## A Dictionary

```python
webster = {
  "apple": "a rounded fruit with firm white flesh and a seedy core"[[[,]]]
  "banana": "a tropical plant with thick clusters of yellow finger-shaped fruit"[[[,]]]
  "orange": "a juicy citrus fruit with reddish yellow rind"
}
```

---
These entries are separated by commas
******************************************************
## A Dictionary

```python
webster = {
  [["apple": "a rounded fruit with firm white flesh and a seedy core"]][[a key-value pair]],
  "banana": "a tropical plant with thick clusters of yellow finger-shaped fruit",
  "orange": "a juicy citrus fruit with reddish yellow rind"
}
```

---
Now, drilling down to an individual entry. Remember, we said earlier that
each entry is a key-value pair. Where the key is like a word in the
dictionary and a value is like a definition for the word.
******************************************************
## A Dictionary

```python
webster = {
  "apple"[[:]][[the colon]] "a rounded fruit with firm white flesh and a seedy core",
  "banana": "a tropical plant with thick clusters of yellow finger-shaped fruit",
  "orange": "a juicy citrus fruit with reddish yellow rind"
}
```

---
A colon separates the key from the value.
******************************************************
## A Dictionary

```python
webster = {
  [["apple"]][[key]]: "a rounded fruit with firm white flesh and a seedy core",
  "banana": "a tropical plant with thick clusters of yellow finger-shaped fruit",
  "orange": "a juicy citrus fruit with reddish yellow rind"
}
```

---
on the left-hand side of the colon is the *key* of the entry --- the thing
you use to do a look up,
******************************************************
## A Dictionary

```python
webster = {
  "apple": [["a rounded fruit with firm white flesh and a seedy core"]][[value]],
  "banana": "a tropical plant with thick clusters of yellow finger-shaped fruit",
  "orange": "a juicy citrus fruit with reddish yellow rind"
}
```

---
and on the right-hand side is the *value* --- the thing that you are looking
up.
******************************************************
## A Dictionary

```python
webster = {
  "apple": "a rounded fruit with firm white flesh and a seedy core",
  "banana": "a tropical plant with thick clusters of yellow finger-shaped fruit",
  "orange": "a juicy citrus fruit with reddish yellow rind"
}
```

---
Okay! So, that's a dictionary. How do you use it?
******************************************************
## Accessing a Dictionary

```python
webster["apple"]
```

---
This the syntax you use to look up a dictionary by a particular key ---
in this case the string "apple".
******************************************************
## Accessing a Dictionary

```python
[[webster["apple"]]][[subscript notation]]
```

---
This syntax is the same syntax as looking up a list using an index number:
`a_list[idx]`. This is called subscript notation.

The way to read this code to another individual is "webster subscript apple".
******************************************************
## Accessing a Dictionary

```python
[[webster["apple"]]][[gives the definition of apple]]
```

---
When you perform a dictionary look up using this subscript notation, you get
the value of the entry that is specified by the key --- in this case that
would be the definition of apple.
******************************************************
## Accessing a Dictionary

```python
result = webster["apple"]
print(result)
```

---
Thus, if you ran this program, the text:

a rounded fruit with firm white flesh and a seedy core

would be printed to the screen.

[Run this program in Python Tutor](http://pythontutor.com/visualize.html#code=webster%20%3D%20%7B%0A%20%20%22apple%22%3A%20%22a%20rounded%20fruit%20with%20firm%20white%20flesh%20and%20a%20seedy%20core%22,%0A%20%20%22banana%22%3A%20%22a%20tropical%20plant%20with%20thick%20clusters%20of%20yellow%20finger-shaped%20fruit%22,%0A%20%20%22orange%22%3A%20%22a%20juicy%20citrus%20fruit%20with%20reddish%20yellow%20rind%22%0A%7D%0Aresult%20%3D%20webster%5B%22apple%22%5D%0Aprint%28result%29&cumulative=false&curInstr=0&heapPrimitives=false&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false) and have a look around!
******************************************************
![Dictionary in Python Tutor](lessons/python/lesson-11/images/dict-in-tutor.png)

---

Notice that a dictionary looks like this in Python Tutor.
It is a 2 column table with each row representing an entry.

The left column contains the keys, and the right column contains
the value.

This is almost what a record looks like, only the label
in the top left corner is "dict" instead of "Record".
******************************************************
## Modifying a Dictionary

```python
webster["apple"] = "the fruit of a tree which typically has thin red skin and crisp flesh."
```

---
To modify the definition of an existing entry, you can
simply assign to it a new value.
******************************************************
## Modifying a Dictionary

```python
[[webster["apple"]]][[left-hand side]] = "the fruit of a tree which typically has thin red skin and crisp flesh."
```

---
The left-hand side of the assignment is a look up
of the dictionary --- using subscript notation.
******************************************************
## Modifying a Dictionary

![Dictionary modified](lessons/python/lesson-11/images/dict-in-tutor-modified.png)

---
And it results in the dictionary being updated.

In the case, that the key you are assigning to does not
exist, yet, it will automatically be created, similar to
to an attribute of a record.
******************************************************
## Accessing a Non-Existent Key

```python
print(webster["kiwi"])
```

---
If you try to access (not modify) a non-existent key,
******************************************************
## Accessing a Non-Existent Key

```
KeyError: 'kiwi'
```

---
You will get a `KeyError`, which causes your entire program
to stop.
******************************************************
## Detecting if a Key Exists

```python
key in dictionary
```

---
If you want to detect if a key exists before you try it
--- so that the program doesn't blow up, you can use
the in operator.
******************************************************
## Detecting if a Key Exists

```python
key in dictionary
```

---
If you want to detect if a key exists before you try it
--- so that the program doesn't blow up, you can use
the in operator.

The `in` operator is the operator you used to detect if
a character in a predefined string: `char in "aeiou"`
or if a word is in a list of predefined words:
`word in ["apple", "banana", "orange"]`.
******************************************************
## Detecting if a Key Exists

```python
[[key]][[The key to test]] in dictionary
```
---
In the case of a dictionary, the left-hand side of the `in` operator
is the key to test,
******************************************************
## Detecting if a Key Exists

```python
key in [[dictionary]][[The dictionary]]
```

---
and the right-hand side is the dictionary to test.
******************************************************
## Detecting if a Key Exists

```python
if "kiwi" in webster:
  print("kiwi definition: %s" % webster["kiwi"])
else:
  print("kiwi is not in the dictionary.")
```

---
So you can write this code to cope with the fact that "kiwi"
may or may not be in the `webster` dictionary.
******************************************************
## Detecting if a Key Exists

```python
if "kiwi" in webster:
  print("kiwi definition: %s" % webster["kiwi"])
else:
  print("kiwi is not in the dictionary.")
```

---
That's the basics of dictionaries.

*This concludes section 1. You may wish to do section 1 of the
homework before continuing if you'd like.*
******************************************************
# Section 2:
## The Dictionary Translator Pattern

---
******************************************************
## The Dictionary Translator Pattern

The *dictionary translator pattern* is a pattern that
uses a preset dictionary to translate a value
as needed by the program.

---
Now, you are going to learn a new pattern!
This is the dictionary translator pattern.
******************************************************
## The Dictionary Translator Pattern

```python
text = "I live in GA and my mom lives in NC"
```

---
So, I have a string that mentions a couple of states by their
abbreviations. You'd like to translate the sentence
to use the full names of the states.
******************************************************
## The Dictionary Translator Pattern

```python
state_name_dict = {
  "GA": "Georgia",
  "NC": "North Carolina",
  "TN": "Tennessee",
  "AL": "Alabama"
}
```

---
We create a dictionary to be for the translation. Whenever
we come across an abbreviation, you can simply look up
this dictionary to get the full name.
******************************************************
## The Dictionary Translator Pattern

```python
words = text.split(" ")
result_words = []
for word in words:
  if word in state_name_dict:
    full_name = state_name_dict[word]
    result_words.append(full_name)
  else:
    result_words.append(word)
result = " ".join(result_words)
```

---
Now, we can using this code to go through the words
and replacing the abbreviations as we need to.
******************************************************
## The Dictionary Translator Pattern

```python
[[words = text.split(" ")]][[split to get a list of words]]
result_words = []
for word in words:
  if word in state_name_dict:
    full_name = state_name_dict[word]
    result_words.append(full_name)
  else:
    result_words.append(word)
result = " ".join(result_words)
```

---
The first thing we do is to split the text to get a list of words.
******************************************************
## The Dictionary Translator Pattern

```python
words = text.split(" ")
[[result_words = []]][[accumulator variable]]
for word in words:
  if word in state_name_dict:
    full_name = state_name_dict[word]
    result_words.append(full_name)
  else:
    result_words.append(word)
result = " ".join(result_words)
```

---
This is an accumulator pattern, and we have
an accumulator variable: `result_words`.
******************************************************
## The Dictionary Translator Pattern

```python
words = text.split(" ")
result_words = []
[[for word in words:]][[loop through each word]]
  if word in state_name_dict:
    full_name = state_name_dict[word]
    result_words.append(full_name)
  else:
    result_words.append(word)
result = " ".join(result_words)
```

---
for each word in the sentence...
******************************************************
## The Dictionary Translator Pattern

```python
words = text.split(" ")
result_words = []
for word in words:
  [[if word in state_name_dict:]][[is this a state abbreviation?]]
    full_name = state_name_dict[word]
    result_words.append(full_name)
  else:
    result_words.append(word)
result = " ".join(result_words)
```

---
we check if the word is a known state abbreviation. We can
do this check using the `in` operator on the `state_name_dict`,
because if it's a known state abbreviation, we expect it
to be a key in this dictionary.
******************************************************
## The Dictionary Translator Pattern

```python
words = text.split(" ")
result_words = []
for word in words:
  if word in state_name_dict:
    [[full_name = state_name_dict[word]]][[look up the full name]]
    result_words.append(full_name)
  else:
    result_words.append(word)
result = " ".join(result_words)
```

---
If the word is an abbreviation, we use it to look up the dictionary,
which gets us the full name.
******************************************************
## The Dictionary Translator Pattern

```python
words = text.split(" ")
result_words = []
for word in words:
  if word in state_name_dict:
    full_name = state_name_dict[word]
    [[result_words.append(full_name)]][[append the full name]]
  else:
    result_words.append(word)
result = " ".join(result_words)
```
---
And we append the full name instead of the abbreviation.
******************************************************
## The Dictionary Translator Pattern

```python
words = text.split(" ")
result_words = []
for word in words:
  if word in state_name_dict:
    full_name = state_name_dict[word]
    result_words.append(full_name)
  [[else:]][[not an abbreviation]]
    result_words.append(word)
result = " ".join(result_words)
```

---
If the word is not a state abbreviation,
******************************************************
## The Dictionary Translator Pattern

```python
words = text.split(" ")
result_words = []
for word in words:
  if word in state_name_dict:
    full_name = state_name_dict[word]
    result_words.append(full_name)
  else:
    [[result_words.append(word)]][[append word]]
result = " ".join(result_words)
```

---
then we append the word itself.
******************************************************
## The Dictionary Translator Pattern

```python
words = text.split(" ")
result_words = []
for word in words:
  if word in state_name_dict:
    full_name = state_name_dict[word]
    result_words.append(full_name)
  else:
    result_words.append(word)
[[result = " ".join(result_words)]][[join the list into string]]
```

---
at the end we join the list back to a string to yield the result.

[Run this code in Python Tutor](http://pythontutor.com/visualize.html#code=state_name_dict%20%3D%20%7B%0A%20%20%22GA%22%3A%20%22Georgia%22,%0A%20%20%22NC%22%3A%20%22North%20Carolina%22,%0A%20%20%22TN%22%3A%20%22Tennessee%22,%0A%20%20%22AL%22%3A%20%22Alabama%22%0A%7D%0A%0Atext%20%3D%20%22I%20live%20in%20GA%20and%20my%20mom%20lives%20in%20NC%22%0Awords%20%3D%20text.split%28%22%20%22%29%0Aresult_words%20%3D%20%5B%5D%0Afor%20word%20in%20words%3A%0A%20%20if%20word%20in%20state_name_dict%3A%0A%20%20%20%20full_name%20%3D%20state_name_dict%5Bword%5D%0A%20%20%20%20result_words.append%28full_name%29%0A%20%20else%3A%0A%20%20%20%20result_words.append%28word%29%0Aresult%20%3D%20%22%20%22.join%28result_words%29&cumulative=false&curInstr=0&heapPrimitives=false&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false),
and follow how this code works now.

This concludes section 2. If you'd like to do section 2
of the homework before moving on, you may do so.
***************************************************
# Section 3:
## Dynamically Entering a Dictionary
---
Now, let's look at how to ask a user to dynamically
enter the entries of a dictionary.

***************************************************
## Dynamically Enter a Dictionary

```python
acronyms = {}
while True:
    acronym = input("Enter an acronym: ")
    full_phrase = input("Enter its definition: ")
    acronyms[acronym] = full_phrase
    yn = input("Enter another? (y/n) ")
    if yn == "n":
        break
print(acronyms)
```

---
This is a while loop that asks the user to enter acronyms
and their definitions and store them in a dictionary called
`acronyms` for as many times as they'd like.
***************************************************
## Dynamically Enter a Dictionary

```python
[[acronyms = {}]][[Define empty dictionary]]
while True:
    acronym = input("Enter an acronym: ")
    full_phrase = input("Enter its definition: ")
    acronyms[acronym] = full_phrase
    yn = input("Enter another? (y/n) ")
    if yn == "n":
        break
print(acronyms)
```

---
First, this line defines an empty dictionary.
***************************************************
## Dynamically Enter a Dictionary

```python
acronyms = {}
[[while True:]][[Loop]]
    acronym = input("Enter an acronym: ")
    full_phrase = input("Enter its definition: ")
    acronyms[acronym] = full_phrase
    yn = input("Enter another? (y/n) ")
    if yn == "n":
        break
print(acronyms)
```

---
This while loop will always loop because its conditional is `True`.
A break statement within the loop body will have to causes it to stop.
***************************************************
## Dynamically Enter a Dictionary

```python
acronyms = {}
while True:
    [[acronym = input("Enter an acronym: ")]][[Prompt 1]]
    full_phrase = input("Enter its definition: ")
    acronyms[acronym] = full_phrase
    yn = input("Enter another? (y/n) ")
    if yn == "n":
        break
print(acronyms)
```

---
This line prompts the user to enter an acronym.
***************************************************
## Dynamically Enter a Dictionary

```python
acronyms = {}
while True:
    acronym = input("Enter an acronym: ")
    [[full_phrase = input("Enter its definition: ")]][[Prompt 2]]
    acronyms[acronym] = full_phrase
    yn = input("Enter another? (y/n) ")
    if yn == "n":
        break
print(acronyms)
```

---
This line asks what the acronym stands for.
***************************************************
## Dynamically Enter a Dictionary

```python
acronyms = {}
while True:
    acronym = input("Enter an acronym: ")
    full_phrase = input("Enter its definition: ")
    [[acronyms[acronym] = full_phrase]][[Store in dictionary]]
    yn = input("Enter another? (y/n) ")
    if yn == "n":
        break
print(acronyms)
```

---
And here, we add a new entry to the dictionary,
or potentially overwriting an existing entry if one with the same
acronym already exists.
***************************************************
## Dynamically Enter a Dictionary

```python
acronyms = {}
while True:
    acronym = input("Enter an acronym: ")
    full_phrase = input("Enter its definition: ")
    acronyms[acronym] = full_phrase
    [[yn = input("Enter another? (y/n) ")
    if yn == "n":
        break]][[Choice to enter more]]
print(acronyms)
```

---
This bit of code gives the user the choice to enter more.
***************************************************
## Dynamically Enter a Dictionary

```python
acronyms = {}
while True:
    acronym = input("Enter an acronym: ")
    full_phrase = input("Enter its definition: ")
    acronyms[acronym] = full_phrase
    yn = input("Enter another? (y/n) ")
    if yn == "n":
        break
[[print(acronyms)]][[print the dictionary]]
```

---
When the user is all done, the program prints the dictionary,
which will be formatted to the terminal in a manner just like
a dictionary expression is structured.
***************************************************
## Dynamically Enter a Dictionary

```python
acronyms = {}
while True:
    acronym = input("Enter an acronym: ")
    full_phrase = input("Enter its definition: ")
    acronyms[acronym] = full_phrase
    yn = input("Enter another? (y/n) ")
    if yn == "n":
        break
print(acronyms)
```

---
Try [running this code in Python Tutor](http://pythontutor.com/visualize.html#code=acronyms%20%3D%20%7B%7D%0Awhile%20True%3A%0A%20%20%20%20acronym%20%3D%20input%28%22Enter%20an%20acronym%3A%20%22%29%0A%20%20%20%20full_phrase%20%3D%20input%28%22Enter%20its%20definition%3A%20%22%29%0A%20%20%20%20acronyms%5Bacronym%5D%20%3D%20full_phrase%0A%20%20%20%20yn%20%3D%20input%28%22Enter%20another%3F%20%28y/n%29%20%22%29%0A%20%20%20%20if%20yn%20%3D%3D%20%22n%22%3A%0A%20%20%20%20%20%20%20%20break%0A%0Aprint%28acronyms%29&cumulative=false&curInstr=0&heapPrimitives=false&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%22ABC%22,%22already%20black%20cat%22,%22n%22%5D&textReferences=false).
***************************************************
## Summary

* Dictionary
* Create
* Access
* Modify
* Dictionary Translator Pattern
* Dynamically Entering a Dictionary

---
That is it for this introduction to dictionaries. This is what you've learned.
***************************************************
## Homework

[Homework](https://gist.github.com/airportyh/9d0f0d7af5036796cc98c2ef2485b230)

---
Enjoy your homework!
