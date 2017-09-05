# Lesson 3
## Lists, Ranges and the For Loop
---
In this lesson, we'll cover lists, ranges and the for loop.
******************************************
## Lists

```python
[1, 5, 2, 3, 4]
```
---
This is a list of numbers in Python
******************************************

![List Representation](lessons/python/lesson-3/list-repr-python-tutor.png)

---
This is how you would see a list represented inside of Python Tutor. 
First there's the label that says "list", that tells you this is a 
list, to differentiate it from other things that we'll learn later.

Then we have something that looks like like a row of cells, 
and each cell has a little index number -
that's the gray number on the top left corner of each cell. Here
the index numbers are 0, 1, 2, 3, 4 - they always go in order, starting
from 0 - if you hear the term zero-based indexing, that is referring to
lists, or other things whose index number sequence start from zero. 

Then, the numbers in black in each cell are the contents of each cell. A cell
is like a variable that stores something, and a list is like a row of variables.
But a list can grow and shrink, so it could hold any number of cells.
*****************************************
## Lists
```python
a_list = [1, 5, 2, 3, 4]
```
---
You can store a list into a variable like so,
as you can with any other kind of value in Python.
*****************************************

![List Variable](lessons/python/lesson-3/list-variable.png)

---
When you have a list variable, what you would see
in Python Tutor is this - a variable slot inside
the frame in the "Frames" section pointing to a
representation of the list in the "Objects" section
like so.

"What is the Frames section and what is the
Objects section?" - you might be wondering.

The Frames
section is like the short-term memory of the brain, 
whereas the Objects section is like the long-term
memory of the brain - we'll revisit this later
when we get to functions.

At this point, notice
that the value of a list variable is not the contents
of the list, but merely a pointer to a "list object"
in the Objects area. This has profound implications,
which we'll discover later.
*****************************************
## Accessing an item
```python
a_list[1]
```
---
To access an individual item inside a list, tell the
list the index number you want to access by using the subscript notation. 

The way to say this expression is: 

    a_list subscript 1
    
Another way to say this is:

    Access a_list at index 1
*****************************************
## Accessing an item

![List Variable](lessons/python/lesson-3/list-variable.png)

```python
a_list[1]
```
Result:
```
5
```
---
This expression returns the content of cell number 1,
which as you can see in the diagram, is 5.
******************************************
## What will this print?
```python
a_list = [1, 5, 2, 3, 4]
print a_list[1]
print a_list[3]
print a_list[4]
print a_list[2]
print a_list[0]
```
---
It's time for a challenge! What will this program print?
Write out your prediction, on a piece or paper or 
a text editor. Then run this program to verify it.
*****************************************
## Accessing an non-existent cell
```python
a_list = [1, 5, 2, 3, 4]
print a_list[5]
```

```
IndexError: list index out of range
```
---
If you try to access an item by an index number that
does not exist in the list, you will get an error. More
specifically, an IndexError. This our example, there
isn't a cell with the index number of 5.
*****************************************
## Appending to a list

```python
a_list.append(7)
```
Result:

![Append result](lessons/python/lesson-3/append-result.png)

---
You can append a new item to a list using the append
method of the list, like so.
*****************************************
## Deleting from a list

```python
del a_list[1]
```
Result:

![Delete result](lessons/python/lesson-3/delete-result.png)

---
You can also delete an item from a list by the item's
index number.
*****************************************
## A list of strings
```python
parts = ['head', 'shoulders', 'knees', 'toes']
```

---
Lists can contain any data type, not just numbers.
*****************************************
## A mixed list
```python
part1 = ['head', 1]
part2 = ['shoulders', 2]
part3 = ['knees', 2]
part4 = ['toes', 10]
```

---
You can also have different types(kinds) of things
in the same list.
*****************************************
## A list of lists
```python
parts = [
  ['head', 1],
  ['shoulders', 2],
  ['knees', 2],
  ['toes', 10]
]
```


---
You can even have a list of lists!!! 

![Mindblown](lessons/python/lesson-3/mindblown.gif)

What would this
even look like in Python Tutor? I leave this as an
exercise for the reader:

Predict what it would look like, draw it on paper. Then
run this program in Python Tutor to verify.
*****************************************
# For loops
## How to go through lists
---
Now, that you have access to lists, let's talk about
how to go through the items in a list. That's what
for loops do.
*****************************************
## For loop
```
for item in a_list:
  print("Hey! I'm in a loop!")
  print("The item is %s." % item)
```
---
In Python - as opposed
to other programming languages - a for loop is used to
iterate through a list of items.

Intuitively, what we are saying is: we have a list of
things, and for each thing in the list of things, 
we'll perform a set of operations to it.

So this is a for-in loop statement. It consists of ...
*****************************************
## For loop
```
[[for]][[The for keyword]] item in a_list:
  print("Hey! I'm in a loop!")
  print("The item is %s." % item)
```
---
The word "for" - which is a Python keyword.
*****************************************
## For loop
```
for [[item]][[This is a variable name]] in a_list:
  print("Hey! I'm in a loop!")
  print("The item is %s." % item)
```
---
A variable declaration - even though this doesn't look like a normal variable declaration, which normally looks like:

```python
some_variable = "some value"
```

We are in fact declaring a variable called item as
a side effect of this for loop statement. You can
name this variable anything you want, as long as
it is a valid identifier.
*****************************************
## For loop
```
for item [[in]][[The in keyword]] a_list:
  print("Hey! I'm in a loop!")
  print("The item is %s." % item)
```
---
Then we have the word in, which is also a Python keyword.
*****************************************
## For loop
```
for item in [[a_list]][[A list variable]]:
  print("Hey! I'm in a loop!")
  print("The item is %s." % item)
```
---
Then a list variable is specified. We are using the `a_list` variable we declared earlier, as such:

```python
a_list = [1, 5, 2, 3, 4]
```
*****************************************
## For loop
```
for item in a_list:
[[  print("Hey! I'm in a loop!")
  print("The item is %s." % item)]][[The loop body]]
```
---
Finally we have the body of the for loop, which will
execute as many times as there are items in the list we are looping over.
*****************************************
## For loop
```
for item in a_list:
  print("Hey! I'm in a loop!")
  print("The item is %s." % [[item]][[One of the items in a_list]])
```
---
Within the body of the loop, the item variable will contain one of the items in a_list each time through the loop.
*****************************************
## What does this print?
```
a_list = [1, 5, 2, 3, 4]
for item in a_list:
  print("Hey! I'm in a loop!")
  print("The item is %s." % item)
```
---
Challenge time! What does this program print? Write it down on paper, and then run it to verify the result.
*****************************************
## What does this print (2)?
```
the_list = ["Mary", "Lois", "Guillermo", "Manoush"]
for name in the_list:
  print("Hello, %s!" % name)
```
---
Challenge time again! What does this program print? Write it down on paper, and then run it to verify the result.
*****************************************
## Nested For Loops
```
the_list = ["Mary", "Lois", "Guillermo", "Manoush"]
the_fruits = ["apple", "orange", "banana", "kiwi"]
for name in the_list:
  for fruit in the_fruits:
    print("%s eats the %s" % (name, fruit))
```
---
You can put a for loop inside another for loop!!!

![Mind blown](lessons/python/lesson-3/mindblown.gif)

What does this program do? Again, predict the outcome, and then type this program in to Python Tutor, and step through the program line-by-line to see the result.
*****************************************
# Ranges
## Generating lists on the fly
---
Now we'll move on to ranges, whose purpose is to 
generate lists on the fly.
*****************************************
## Ranges

```python
range(1, 5)
```
---
You can use the range function to create a range between
two numbers like so.
*****************************************
## Ranges

```python
[[range]][[The range function]](1, 5)
```
---
This is the range function.
*****************************************
## Ranges

```python
range([[1]][[Beginning number]], 5)
```
---
This is the beginning number.
*****************************************
## Ranges

```python
range(1, [[5]][[Ending number]])
```
---
And this is the ending number.
*****************************************
## Ranges

```python
range(1, 5)
```

Result is equivalent to:

```
[1, 2, 3, 4]
```
---
It will generate the equivalent of a list of numbers
between the two numbers - in this case 1 and 5, including
the start number, but not including the end number.

*I know it's incredibly strange that it includes the
beginning number but not the ending number, that's
just something you'll have to remember.*
*****************************************
## Ranges

```python
range(1, 10, [[2]][[The skip amount]])
```

Result is equivalent to:

```
[1, 3, 5, 7, 9]
```
---
You can provide a third number to the range function,
which will specify the skip amount between each two adjacent numbers in the resulting list.
*****************************************
## Decreasing ranges

```python
range(10, 0, [[-1]][[A negative skip amount? Wah?]])
```

Result is equivalent to:

```
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
```
---
It is also possible to create a decreasing range by
specifying a negative skip amount.
*****************************************
## Range short-hand
```python
range(5)
```
---
The range function has a short-hand form which allows you
to pass in just one number.
*****************************************
## Range short-hand
```python
range([[5]][[The ending number]])
```
---
If you do so, that number specifies the ending number, and the beginning number
is assumed to be zero.
*****************************************
## Range short-hand
```python
range(5)
```
Is equivalent to
```python
range(0, 5)
```
Result:
```
[0, 1, 2, 3, 4]
```
---
So these two ranges are equivalent.
*****************************************
## Using range with for loops
```python
for num in range(5):
  print('I <3 Python')
```
---
It is a common pattern in Python to use range to generate
a list and then use a for loop to iterate through each number in the resulting list.
The above code will print "I <3 Python" 5 times.

In general, if you wish to do some thing a desired number of times,
generate a range with that as the ending number and use a for loop
to iterate through it.
*****************************************
## Summary of what you've learned

* Lists
* For Loops
* Ranges
---
This concludes this lesson. Good job making it this far!

You've learned the basics of lists in Python, how to 
use for loops to iterate over each item of a list, and
then how to use the range function to conveniently generate
lists on the fly.
