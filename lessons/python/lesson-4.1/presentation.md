# Lesson 4.1
## String Manipulation 2
---
Welcome to lesson 4.1! We will continue with string manipulation.
This time we'll learn some tricks that'll be more useful to you in
solving string manipulation problems in general.
*****************************************************
## String as a Sequence

```python
a_list = ["a", "b", "c"]
for thing in a_list:
  print(thing)
```
---
Up to this point, we have been using loops to iterate through things
inside of lists.

But did you know that, we can also use them to iterate through strings?
*****************************************************
## String as a Sequence

```python
a_str = "abc"
for thing in a_str:
  print(thing)
```
Prints
```
a
b
c
```
---
Yes! And it looks like this.

Why does this work??? Because in concept, a string is simply a sequence
of characters. The string "abc" is a sequence that contains letters
"a", "b", and "c". If you use the for loop to iterate through them, you
get each letter one by one.
*****************************************************
# Sequence

A sequence is a type of value in Python that has a length, and
supports indexing. For example, given a sequence `seq`, you can
call `len(seq)` to get its length, and you can use the subscript
notation `seq[idx]` to access one of its items as long as `idx`
is an integer less than its length.

---
This is the definition of what a sequence is in Python.
*****************************************************
# Sequence

A sequence is a type of value in Python that has a length, and
supports indexing. For example, given a sequence `seq`, you can
call `len(seq)` to get its length, and you can use the subscript
notation `seq[idx]` to access one of its items as long as `idx`
is an integer less than its length.

---
So far, you've seen two things that are sequences:

1. lists
2. strings

There are more, as we will see later. You can use a for loop to
iterate any type that is a sequence.
*****************************************************
## String as a Sequence

```python
sentence = input("Type a sentence")
result = ""
for char in sentence:
  result = char + result
```

---
This means that if we want to convert a string, let's say, a string taken
from the user, we can use the accumulator pattern on that string directly,
without having to convert it to a list first.
*****************************************************
## String as a Sequence

```python
[[sentence = input("Type a sentence")]][[Ask the user for input]]
result = ""
for char in sentence:
  result = char + result
```

---
This program first asks the user to input a sentence.
*****************************************************
## String as a Sequence

```python
sentence = input("Type a sentence")
[[result = ""
for char in sentence:
  result = char + result]][[Accumulator pattern]]
```

---
Then uses the accumulator pattern to build a result string that has the
entered sentence reversed.

Please try running this program in Python Tutor, then modify it to convert
all letter a's to upper case. Have a try, and then move to the next slide to
see the solution.
*****************************************************
## String as a Sequence

Solution:
```python
sentence = input("Type a sentence")
result = ""
for char in sentence:
  if char == "a":    
    result = char.upper() + result
  else:
    result = char + result
```

---
This is the solution to problem.
*****************************************************
## String as a Sequence

Solution:
```python
sentence = input("Type a sentence")
result = ""
for char in sentence:
  [[if char == "a":]][[Check for a]]
    result = char.upper() + result
  else:
    result = char + result
```

---
We have an if statement that checks for a's.
*****************************************************
## String as a Sequence

Solution:
```python
sentence = input("Type a sentence")
result = ""
for char in sentence:
  if char == "a":    
    result = [[char.upper()]][[Uppercase the a]] + result
  else:
    result = char + result
```

---
Then uppercases the a before concatenating it to the front of the result.
*****************************************************
## String as a Sequence

Solution:
```python
sentence = input("Type a sentence")
result = ""
for char in sentence:
  if char == "a":    
    result = char.upper() + result
  else:
    [[result = char + result]][[concatenate other letters]]
```

---
If it's any other letter than a, we still concatenate it to the result,
just without the uppercasing.
*****************************************************
## The `in` Operator

```python
if thing in seq:
  print(thing, "is in the sequence!")
```

---
Python provides a nifty operator: "in".
*****************************************************
## The `in` Operator

```python
if thing [[in]][[In operator]] seq:
  print(thing, "is in the sequence!")
```

---
The "in" operator,
*****************************************************
## Not to be confused...

```python
[[for thing in seq]][[for-in statement]]:
  print(thing)
```

---
not to be confused the "in" keyword in the for-in statement.
*****************************************************
## The `in` Operator

```python
if [[thing in seq]][[Returns a boolean]]:
  print(thing, "is in the sequence!")
```

---
The "in" operator is a standalone operator, but you can use it within an
if statement like this. It returns a True value if the thing is in the
sequence (string or list), or a False value if it is not.

A value that is either True or False is called a boolean value. So the
"in" operator is called a boolean operator. In fact, you've seen other
boolean operators before, namely: `>`, `==`, `<`, `>=`, and `<=`.

For example, `i < 10` returns a True value if i is less than 10, and returns
a False value if it is 10 or greater.
*****************************************************
## Boolean

A boolean in represents a proposition that can be either true or false.
In Python the two boolean values are `True` and `False.`

---
This is the definition of boolean.
*****************************************************
## Boolean Variables

```python
i = 5
a_boolean = i > 5
another_boolean = "a" in "bananas"
boolean3 = i == 5
```

---
To show that boolean values are values all to themselves, we can use
boolean operators such as `in`, `>`, and `==` outside of the context of
an if statement, and instead assign their result to variables.
*****************************************************
## Boolean Variables

```python
[[i = 5]][[Declares and initializes i]]
a_boolean = i > 5
another_boolean = "a" in "bananas"
boolean3 = i == 5
```

---
The first line here simple assigns 5 to the variable i.
*****************************************************
## Boolean Variables

```python
i = 5
[[a_boolean = i > 5]][[Declares a_boolean]]
another_boolean = "a" in "bananas"
boolean3 = i == 5
```

---
The second line declares a variable `a_boolean`.
*****************************************************
## Boolean Variables

```python
i = 5
a_boolean = [[i > 5]][[A boolean operation]]
another_boolean = "a" in "bananas"
boolean3 = i == 5
```

---
But its right-hand-side is a boolean operation: `i > 5` which,
in this case returns the value False, because i, being 5 is not greater than
5.
*****************************************************
## Boolean Variables

```python
i = 5
a_boolean = i > 5
[[another_boolean = "a" in "bananas"]][[Declares another_boolean]]
boolean3 = i == 5
```

---
The next line declares `another_variable`,
*****************************************************
## Boolean Variables

```python
i = 5
a_boolean = i > 5
another_boolean = [["a" in "bananas"]][[An "in" operation]]
boolean3 = i == 5
```

---
This time the right-hand side is an "in" operation, this in this case
will be True because the letter "a" is indeed in "bananas".
*****************************************************
## Boolean Variables

```python
i = 5
a_boolean = i > 5
another_boolean = "a" in "bananas"
[[boolean3 = i == 5]][[Declaring boolean3]]
```

---
Finally this line declares the variable boolean3,
*****************************************************
## Boolean Variables

```python
i = 5
a_boolean = i > 5
another_boolean = "a" in "bananas"
boolean3 = [[i == 5]][[Equals operation]]
```

---
And its right-hand side is an `==` operation which in this case will return
True, because `i` being 5, is indeed equal to 5.
*****************************************************
## Boolean Variables

```python
i = 5
a_boolean = i > 5
another_boolean = "a" in "bananas"
boolean3 = i == 5
```

---
Run this program in Python Tutor and pay attention to what the Global Frame
looks like.

Next, back to the "in" operator.
*****************************************************
## Easy Vowel Detection with "in"

```python
sentence = input("Type a sentence")
result = ""
for char in sentence:
  if char == "a":    
    result = char.upper() + result
  else:
    result = char + result
```

---
Back to this program, which reverses the user input and converts all a's
to capital A's. Now armed with the `in` operator, please modify this
to convert all vowels to uppercase.

Have a try, then go to the next slide for the solution.
*****************************************************
## Easy Vowel Detection with "in"

Solution:
```python
sentence = input("Type a sentence")
result = ""
for char in sentence:
  if char in "aeiou":    
    result = char.upper() + result
  else:
    result = char + result
```

---
The solution is to use the `in` operation with the string "aeiou" on the right
hand side.
*****************************************************
## Easy Vowel Detection with "in"

```python
sentence = input("Type a sentence")
result = ""
for char in sentence:
  if char in ["a", "e", "i", "o", "u"]:    
    result = char.upper() + result
  else:
    result = char + result
```

---
You could also have used a list containing all the vowels like so, because
it is also a sequence. A string is a bit shorter to write.
*****************************************************
## Splitting Strings

```python
"to be or not to be".split(" ")
```

![Split string](./lessons/python/lesson-4.1/split-string.png)

---
Here's another handy tool you should know about: the string type's split
method.

The split method splits a string into multiple strings. The result is
stored as a list of strings as you see at the bottom.
*****************************************************
## Splitting Strings

```python
[["to be or not to be"]][[String to be split]].split(" ")
```

![Split string](./lessons/python/lesson-4.1/split-string.png)

---
On the left hand side of the dot operator is the string to be split up.
*****************************************************
## Splitting Strings

```python
"to be or not to be".[[split]][[the split method]](" ")
```

![Split string](./lessons/python/lesson-4.1/split-string.png)

---
On the right hand side is the name split to refer to the split method.
*****************************************************
## Splitting Strings

```python
"to be or not to be".split[[(" ")]][[Argument list]]
```

![Split string](./lessons/python/lesson-4.1/split-string.png)

---
Then the argument list.
*****************************************************
## Splitting Strings

```python
"to be or not to be".split([[" "]][[The separator]])
```

![Split string](./lessons/python/lesson-4.1/split-string.png)

---
The split method takes one argument: the separator. The separator is a
string for the split method to look for within the string on the LHS
to split on.
*****************************************************
## Splitting Strings

```python
"to[[[ ]]]be[[[ ]]]or[[[ ]]]not[[[ ]]]to[[[ ]]]be".split(" ")
```

![Split string](./lessons/python/lesson-4.1/split-string.png)

---
The separator in this example is the space character. These are the spaces
in the string on the LHS. So it splits cleanly into a list with each word
in the sentence.

Note that the separators are removed from the result as part of the process.
*****************************************************
## Splitting Strings

```python
"to be or not to be".split([["t"]][[The separator]])
```

---
What if we'd changed the separator to a t? What would the result be?

Write it out by hand, and then go to the next slide for the answer.
*****************************************************
## Splitting Strings

```python
"[[[t]]]o be or no[[[t]]] [[[t]]]o be".split("t")
```

![Split string on t](./lessons/python/lesson-4.1/split-string-t.png)

---
This time, because the t is acting as a separator, we get a list containing
just the substrings that are sandwiched between the t's. This includes an
empty string at the beginning because t happens to be the very first letter.
*****************************************************
## Joining Strings

```python
" ".join(["to", "be", "or", "not", "to", "be"])
```

---
The inverse operation to splitting a string is joining multiple strings
into one string.
*****************************************************
## Joining Strings

```python
[[" "]][[The separator]].join(["to", "be", "or", "not", "to", "be"])
```
Result:
```
"to be or not to be"
```

---
This time, the separator is on the left-hand side, and the array of
strings to be joined is on the right.
*****************************************************
## Joining Strings

```python
result = ".".join(["to", "be", "or", "not", "to", "be"])
print(result)
```

---
What does this program produce? Write it out by hand, and then verify
with Python Tutor.
*****************************************************
## Operating on words

```python
sentence = input("Type a sentence")
words = sentence.split(" ")
result_words = []
for word in words:
  result_words = result_words + [word, word]
result_sentence = " ".join(sentence)
print(result_sentence)
```

---
The availability of split and join allows us to operate on a sentence at the
level of words rather than characters.

This program asks the user to type a sentence, and then prints a sentence
where every word the user typed shows up twice.
*****************************************************
## Operating on words

```python
[[sentence = input("Type a sentence")]][[Enter a sentence "to be or not to be"]]
words = sentence.split(" ")
result_words = []
for word in words:
  result_words = result_words + [word, word]
result_sentence = " ".join(sentence)
print(result_sentence)
```

---
Let's say the user enters: to be or not to be.
*****************************************************
## Operating on words

```python
sentence = input("Type a sentence")
[[words = sentence.split(" ")]][[Splits into words]]
result_words = []
for word in words:
  result_words = result_words + [word, word]
result_sentence = " ".join(sentence)
print(result_sentence)
```

---
The program splits the string into a list of strings:
`["to", "be", "or", "not", "to", "be"]`.
*****************************************************
## Operating on words

```python
sentence = input("Type a sentence")
words = sentence.split(" ")
[[result_words = []]][[Accumulator variable]]
for word in words:
  result_words = result_words + [word, word]
result_sentence = " ".join(sentence)
print(result_sentence)
```

---
We are getting ready to use the accumulator pattern, using a list variable
`result_words` as the accumulator variable.
*****************************************************
## Operating on words

```python
sentence = input("Type a sentence")
words = sentence.split(" ")
result_words = []
[[for word in words:]][[Loop through each word]]
  result_words = result_words + [word, word]
result_sentence = " ".join(sentence)
print(result_sentence)
```

---
Now we loop through each word in the list:
`["to", "be", "or", "not", "to", "be"]`.
*****************************************************
## Operating on words

```python
sentence = input("Type a sentence")
words = sentence.split(" ")
result_words = []
for word in words:
  [[result_words = result_words + [word, word]]][[Accumulate!!]]
result_sentence = " ".join(sentence)
print(result_sentence)
```

---
This is the accumulator statement. For each word, it adds two to the
`result_words` list, this is what doubles every word.
*****************************************************
## Operating on words

```python
sentence = input("Type a sentence")
words = sentence.split(" ")
result_words = []
for word in words:
  result_words = result_words + [word, word]
[[result_sentence = " ".join(sentence)]][[Join back to one string]]
print(result_sentence)
```

---
At this point, `result_words` should have
`["to", "to", "be", "be", "or", "or", "not", "not", "to", "to", "be", "be"]`
within it. We just have to use join to put it back into one string.
*****************************************************
## Operating on words

```python
sentence = input("Type a sentence")
words = sentence.split(" ")
result_words = []
for word in words:
  result_words = result_words + [word, word]
result_sentence = " ".join(sentence)
print(result_sentence)
```

---
Run this in Python Tutor and make sure you understand what's going on.

Next, modify it so that the second time each word appears, it is capitalized.
So the result for "to be or not to be" would be
"to TO be BE or OR not NOT to TO be BE".
******************************************************
## Summary

1. Strings as sequences
2. in operator
3. Booleans
4. split method
5. join method

---
This is what you've learned this time.
******************************************************
## Homework

[Homework](https://gist.github.com/airportyh/6379eaa1c6da701ff936e11e45901bdc)

---
Here is your homework. Enjoy!
