# Lesson 3.1
## String Manipulation 1

---
This lesson we'll start doing string manipulation. The good news is
that you'll be using all of the same patterns that you've just learned,
but you'll apply them to strings as well as lists.
***************************************
## String Concatenation

```python
a = "Hello"
b = " "
c = "world"
d = "!"
e = a + b + c + d
print(e)
```

Prints `Hello world!`

---
The first tool to put into your toolbelt is string concatenation. Just as
we can add together number using the `+` sign, we can use the same operator
to *concatenate* strings together --- which just means jam them together into
one combined string.

The above code first declares 4 string variables: a, b, c, and d, and then
finally concatenates them into a combined string e.
***************************************
## Accumulator Pattern with Strings

```python
result = ''
letters = ['b', 'a', 'n', 'a', 'n', 'a', 's']
i = 0
while i < len(letters):
  letter = letters[i]
  result = result + letter
  i = i + 1
```

---
Because you can concatenate strings together in the same way you can add
numbers, you can use the accumulator pattern with a string variable as
the accumulator variable, as this example shows.

This program takes a list of individual characters (of the word bananas),
and concatenates them together one by one to form the word "bananas".
***************************************
## Accumulator Pattern with Strings

```python
result = ''
letters = ['b', 'a', 'n', 'a', 'n', 'a', 's']
[[i = 0]][[accumulator variable]]
while i < len(letters):
  letter = letters[i]
  result = result + letter
  i = i + 1
```

---
Just as with any other piece of code using the accumulator pattern,
this one has an accumulator variable. We initialize this variable to the
empty string at the beginning, and as the code runs, it will add a letter
to this string variable one by one.
***************************************
## Accumulator Pattern with Strings

```python
result = ''
letters = ['b', 'a', 'n', 'a', 'n', 'a', 's']
i = 0
[[while i < len(letters):
  letter = letters[i]
  result = result + letter
  i = i + 1]][[while loop]]
```

---
It has a loop.
***************************************
## Accumulator Pattern with Strings

```python
result = ''
letters = ['b', 'a', 'n', 'a', 'n', 'a', 's']
i = 0
while i < len(letters):
  letter = letters[i]
  [[result = result + letter]][[accumulator statement]]
  i = i + 1
```

---
And it has an accumulator statement which adds to the accumulator variable
for each iteration of the loop. The difference is that this time, it is
concatenating to a string, rather than adding to a number.
***************************************
## Accumulator Pattern with Strings

```python
result = ''
letters = ['b', 'a', 'n', 'a', 'n', 'a', 's']
i = 0
while i < len(letters):
  letter = letters[i]
  result = result + letter
  i = i + 1
```

---
Get acquainted to this code and understand how it works by running it
within Python Tutor now.
***************************************
## Looping short-hand: for loops

```python
fruit_list = ['Apple', 'Orange', 'Banana', 'Kiwi']
for fruit in fruit_list:
  print(fruit)
```
Prints:
```
Apple
Orange
Banana
Kiwi
```
---
Since so many of our problems require loops, it'd be nice if writing loops
were more convenient. Fortunately, there is a way: the for-loop.

This is a for-loop in Python. A for loop is used to iterate through a list of
items.
***************************************
## Looping short-hand: for loops

```python
fruit_list = ['Apple', 'Orange', 'Banana', 'Kiwi']
[[for fruit in fruit_list:]][[for-in statement]]
  print(fruit)
```

---
A for-loop contains a for-in statement.
***************************************
## Looping short-hand: for loops

```python
fruit_list = ['Apple', 'Orange', 'Banana', 'Kiwi']
[[for]][[for keyword]] fruit in fruit_list:
  print(fruit)
```

---
Within this statement, first there is the for keyword.
***************************************
## Looping short-hand: for loops

```python
fruit_list = ['Apple', 'Orange', 'Banana', 'Kiwi']
for [[fruit]][[loop variable]] in fruit_list:
  print(fruit)
```

---
The word that comes after "for" is the *loop variable*.

You may choose the name of this loop variable like a conventional
variable. In our case, we called it "fruit". This `fruit` variable
will contain the value of one of the fruits in `fruit_list` for
each iteration of the for-loop.
***************************************
## Looping short-hand: for loops

```python
fruit_list = ['Apple', 'Orange', 'Banana', 'Kiwi']
for fruit [[in]][[in keyword]] fruit_list:
  print(fruit)
```
---
There there is the "in" keyword.
***************************************
## Looping short-hand: for loops

```python
fruit_list = ['Apple', 'Orange', 'Banana', 'Kiwi']
for fruit in [[fruit_list]][[list or sequence]]:
  print(fruit)
```

---
The word that comes after "in" is a list or sequence --- we'll talk more
about what sequences are later. In this case, our list is `fruit_list`.
***************************************
## Looping short-hand: for loops

```python
fruit_list = ['Apple', 'Orange', 'Banana', 'Kiwi']
for fruit in fruit_list:
[[  print(fruit)]][[loop body]]
```

---
This is the body of the loop. Because there are 4 fruits in this list,
This print statement will execute 4 times, each time printing one of the
fruits.
***************************************
## for loop vs while loop

With for loop:
```python
fruit_list = ['Apple', 'Orange', 'Banana', 'Kiwi']
for fruit in fruit_list:
  print(fruit)
```

With while loop:
```python
fruit_list = ['Apple', 'Orange', 'Banana', 'Kiwi']
i = 0
while i < len(fruit_list):
  fruit = fruit_list[i]
  print(fruit)
  i = i + 1
```

---
You may have noticed that a while loop can do exactly what the for loop
can do, but it just requires more steps.

The top example prints each fruit using a for loop. The bottom version does
the same with a while loop.

In the while loop version you are required to implement the loop
counter pattern, but the for loop does that grunt work for you automatically,
and so there's less code for you to write.

Run both of these examples in PythonTutor to get a feel for how they differ.
Going forward, we'll favor using for loops instead of while loops.
***************************************
## String Accumulator Pattern with for loop???

```python
result = ''
letters = ['b', 'a', 'n', 'a', 'n', 'a', 's']
i = 0
while i < len(letters):
  letter = letters[i]
  result = result + letter
  i = i + 1
```

---
Coming back to this problem now --- where we have a list of characters, and
we want to concatenate them one by one into the `result` variable. We can
do this same problem using a for loop instead of a while loop.

Please try to rewrite this program using a for loop. When you are done,
go to the next slide for the solution.
***************************************
## String Accumulator Pattern with for loop

Solution:
```python
result = ''
letters = ['b', 'a', 'n', 'a', 'n', 'a', 's']
for letter in letters:
  result = result + letter
```

---
In this version of the string accumulator pattern, we still have all
3 parts of the pattern. Namely,
***************************************
## String Accumulator Pattern with for loop

Solution:
```python
[[result = '']][[accumulator variable]]
letters = ['b', 'a', 'n', 'a', 'n', 'a', 's']
for letter in letters:
  result = result + letter
```

---
The accumulator variable,
***************************************
## String Accumulator Pattern with for loop

Solution:
```python
result = ''
letters = ['b', 'a', 'n', 'a', 'n', 'a', 's']
[[for letter in letters:]][[loop]]
  result = result + letter
```

---
The loop,
***************************************
## String Accumulator Pattern with for loop

Solution:
```python
result = ''
letters = ['b', 'a', 'n', 'a', 'n', 'a', 's']
for letter in letters:
  [[result = result + letter]][[accumulator statement]]
```

---
And the accumulator statement.
***************************************
## Challenge: Reverse???

```python
result = ''
letters = ['b', 'a', 'n', 'a', 'n', 'a', 's']
for letter in letters:
  result = result + letter
```

---
How would you modify this program to concatenate these same
letters and in reverse order? Please try it!!! Answer is on
the next slide.
***************************************
## Reverse solution

```python
result = ''
letters = ['b', 'a', 'n', 'a', 'n', 'a', 's']
for letter in letters:
  result = letter + result
```

---
***************************************
## Challenge: Accumulator Pattern with Filtering

```python
result = ''
letters = ['b', 'a', 'n', 'a', 'n', 'a', 's']
for letter in letters:
  result = result + letter
```

---
What about filtering? Modify this program so that the final result
has all the a's removed. Answer is on the next slide.
***************************************
## Accumulator Pattern with Filtering Solution

```python
result = ''
letters = ['b', 'a', 'n', 'a', 'n', 'a', 's']
for letter in letters:
  if letter != 'a':
    result = result + letter
```

---
***************************************
## Accumulator Pattern for Lists

```python
result_list = []
letters = ['b', 'a', 'n', 'a', 'n', 'a', 's']
for letter in letters:
  if letter != 'a':
    result_list.append(letter)
```

---
You've seen that we can use the accumulator pattern with strings.
Now we are going to use it with lists --- as in, a list variable will now
be the accumulator variable.

This example, just like the other accumulator pattern examples,
***************************************
## Accumulator Pattern for Lists

```python
[[result_list = []]][[accumulator variable]]
letters = ['b', 'a', 'n', 'a', 'n', 'a', 's']
for letter in letters:
  if letter != 'a':
    result_list.append(letter)
```

---
Has an accumulator variable. In this case, our accumulator variable
`result_list` has been set to a list.
***************************************
## Accumulator Pattern for Lists

```python
result_list = []
letters = ['b', 'a', 'n', 'a', 'n', 'a', 's']
[[for letter in letters:]][[loop]]
  if letter != 'a':
    result_list.append(letter)
```

---
A loop, just as before...
***************************************
## Accumulator Pattern for Lists

```python
result_list = []
letters = ['b', 'a', 'n', 'a', 'n', 'a', 's']
for letter in letters:
  if letter != 'a':
    [[result_list.append(letter)]][[Accumulator statement]]
```

---
And an accumulator statement. This time, our accumulator statement uses
the list's `append` method, which appends a new item to a list.

Let's go into more detail about the append method.
***************************************
## The append method

```python
a_list = ["a", "b"]
```

![a_list](/lessons/python/lesson-3.1/append-1.png)

---
If you start out with this list.
***************************************
## The append method

```python
a_list.append("c")
```

![a_list](/lessons/python/lesson-3.1/append-1.png)

---
Then you append a new letter "c" to it. You get
***************************************
## The append method

![a_list](/lessons/python/lesson-3.1/append-2.png)

---
c appended to the end of the list.
***************************************
## The append method

```python
a_list.append("c")
```

---
append is the first example of methods that you've come across. So let's
talk a little bit about what methods are.
***************************************
## Method

A method is a function attached to a value - which could be a
string, a number, a list, a dictionary, an object, or any thing else in
Python.

---
***************************************
## Example of a Method Call

```python
a_list.append("c")
```

---
Using append as the example, similarly to how `print("Hello")` is a function
call that executes a function, what we have here is a *method call*.
***************************************
## Example of a Method Call

```python
a_list[[.]][[dot operator]]append("c")
```

---
The period used here is called the *dot operator*.
***************************************
## Example of a Method Call

```python
[[a_list]][[the value where method lives]].append("c")
```

---
The word on the left of the dot is the value where the method lives. In this
case, the value is a list.
***************************************
## Example of a Method Call

```python
a_list.[[append]][[method name]]("c")
```

---
The word on the right of the dot is the name of the method we are calling.
Different types of values have different methods. For example, all lists have
the methods: `append`, `insert`, `index`, `pop`, and more. All strings have
the methods: `split`, `isdigit`, `isalpha`, `join`, and more.

If Python complains that the method you are trying to access doesn't exist
on that value, it might be because you misspelt the name of the method, or it
might be that you expected a different type of value on the left of the dot
than what that value really has.
***************************************
## Example of a Method Call

```python
a_list.append[[("c")]][[argument list]]
```

---
Same as with a function call, a method call also has an argument list. This
argument list has one argument in it, which is the string "c". An argument
list may have 0 or more arguments in it. How many it needs and what the
arguments are used for depends on the method in question. Append takes
exactly one argument, and the value of that argument is used to append to the
end of the list.

That's for an explanation on methods and method calls. Back to accumulators...
***************************************
## Accumulator Pattern for Lists

```python
result_list = []
letters = ['b', 'a', 'n', 'a', 'n', 'a', 's']
for letter in letters:
  if letter != 'a':
    result_list.append(letter)
```

---
Given this program, what will be the final value of the `result_list`?
Please work this out by hand, and then run it in Python Tutor to verify your
answer.
***************************************
## Concatenating Lists

```python
a = ["Hello"]
b = [","]
c = ["world"]
d = ["!"]
e = a + b + c + d
```

![Concatenating Lists](/lessons/python/lesson-3.1/list-concat.png)

---
There is an alternative to using append to add to a list: concatenation.
You can concatenate two lists together to get a new list in the same way
you can concatenate strings.

The code above first declares 4 list variables: a, b, c, and d, and then
concatenates them together to form a 5-th: e. e is now a list containing
each of the members of a, b, c, and d, as shown.

*Note: you can only concatenate lists with other lists, if you try to
concatenate a list with a string or a number, it will not work.*
***************************************
## Concatenating Lists

```python
result_list = []
letters = ['b', 'a', 'n', 'a', 'n', 'a', 's']
for letter in letters:
  if letter != 'a':
    result_list = result_list + [letter]
```

---
We can thus rewrite the previous example using list concatenation instead of
append.
***************************************
## Concatenating Lists

```python
result_list = []
letters = ['b', 'a', 'n', 'a', 'n', 'a', 's']
for letter in letters:
  if letter != 'a':
    result_list = result_list + [[[letter]]][[Wrap letter in list]]
```

---
Here we need to take care to wrap the letter we want to add inside of a new
list (the list only contains the one element) so that we can concatenate
it with the result_list.

Now it is possible to modify this code to reverse the letters ;)
***************************************
## Upper method

```python
a_str.upper()
```

---
To prep you for some of the exercises, you'll need to know how to convert
letters between uppercase and lowercase.

The upper method on the string object takes the original string, converts
all its letters to uppercase if they are not already, and returns the converted
string. Note: it does not modify the original string. So if you want to
used the converted value, you have to save it back to a variable or use it
immediately.
***************************************
## Upper method Example

```python
fruit = 'Bananas'
upper_case_fruit = fruit.upper()
print(fruit)
print(upper_case_fruit)
```
Prints:
```
Bananas
BANANAS
```

---
Here's an example of how you might do that.
**************************************
## Lower method

```python
a_str.lower()
```

---
Conversely, there is a `lower` method on strings as well for converting
letters to lowercase. Now!! I think you are ready.

**************************************
## Summary

* String concatenation
* Accumulator Pattern for strings
* For loops
* Accumulator Pattern for lists
* Append method for lists
* List concatenation
* Upper and lower-casing letters
* Methods and method-calls

---
This is a summary of what you've learned.
**************************************
## Homework

[Homework](https://gist.github.com/airportyh/004c577d36e551b38524b71b00d14c00)

---
Here is your homework. Enjoy!
